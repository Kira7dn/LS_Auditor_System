"""
extract_pdf_to_kb.py
====================
Production script: Chuyển đổi PDF → Knowledge Base Markdown.
Tuân thủ nghiêm ngặt bộ tiêu chuẩn SCRIPT_STANDARDS.md (AI-First Scripting).

Usage:
  uv run C:/Users/kira7/.gemini/config/skills/pdf-to-kb/scripts/extract_pdf_to_kb.py --pdf document.pdf --out kb_output/
  uv run C:/Users/kira7/.gemini/config/skills/pdf-to-kb/scripts/extract_pdf_to_kb.py --pdf document.pdf --out kb_output/ --config chapters.json

Output (stdout):
  JSON object with execution details or error state.
All logs/progress are routed to stderr.
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

import fitz  # pymupdf

# ── Default font config (can be overridden by --font-config) ──────────────────
DEFAULT_FONT_CONFIG = {
    "h2_min_size": 12.5,
    "h3_min_size": 10.0,
    "h3_max_len": 100,
    "h3_no_trailing_punct": True,
    "callout_max_size": 9.5,
    "callout_min_len": 8,
    "skip_max_size": 8.5,
    "superscript_max_size": 7.5,
    "diagram_cluster_min": 3,
    "diagram_avg_len_max": 35,
    "bold_flag": 16,
    "italic_flag": 2,
    "box_label_pattern": r"^(BOX|FIGURE|TABLE|APPENDIX)\s*([A-Z][-.]?\s*)?[\d\.]",
    "spaced_label_pattern": r"^([A-Z] ){2,}[A-Z]$",
    "noise_words": ["GUIDANCE", "STANDARD", "GUIDANCESTANDARD", "STANDARD GUIDANCE"],
    "chapter_label_pattern": r"C H A O P T E R\s+\d+",
}

# ── Classifier ────────────────────────────────────────────────────────────────

class LineClassifier:
    def __init__(self, cfg: Dict[str, Any]):
        self.cfg = cfg
        self.FLAG_BOLD = cfg["bold_flag"]
        self.RE_BOX    = re.compile(cfg["box_label_pattern"], re.IGNORECASE)
        self.RE_SPACED = re.compile(cfg["spaced_label_pattern"])
        self.NOISE     = set(cfg["noise_words"])

    def classify(self, size: float, flags: int, text: str) -> str:
        s = text.strip()
        if not s:
            return "skip"
        is_bold = bool(flags & self.FLAG_BOLD)
        cfg = self.cfg

        # ── Skip rules (highest priority) ──
        if size < cfg["superscript_max_size"]:
            return "skip"
        if size <= cfg["skip_max_size"]:
            return "skip"
        if len(s) == 1:
            return "skip"
        if len(s) <= 2 and not s[0].isalpha():
            return "skip"
        if self.RE_SPACED.match(s):
            return "skip"
        if s in self.NOISE:
            return "skip"

        # ── BOX/FIGURE/TABLE (any size) ──
        if self.RE_BOX.match(s):
            return "box_label"

        # ── Bold rules ──
        if is_bold:
            if size >= cfg["h2_min_size"]:
                return "h2"
            if size >= cfg["h3_min_size"]:
                if len(s) <= cfg["h3_max_len"]:
                    if not cfg["h3_no_trailing_punct"] or not re.search(r"[.!?;]\s*$", s):
                        return "h3"
                return "body"
            return "skip"  # small bold = chapter footer

        # ── Non-bold rules ──
        if size <= cfg["callout_max_size"]:
            if len(s) > cfg["callout_min_len"] and not re.fullmatch(r"\d{1,3}", s):
                return "callout"
            return "skip"

        return "body"


def postprocess_items(items: List[tuple], cfg: Dict[str, Any]) -> List[tuple]:
    """Merge split headings; suppress diagram clusters."""
    if not items:
        return items

    # Pass A: merge consecutive same-level headings (split across PDF column)
    merged = []
    i = 0
    while i < len(items):
        cls, text = items[i]
        if cls in ("h2", "h3") and i + 1 < len(items) and items[i + 1][0] == cls:
            merged.append((cls, text + " " + items[i + 1][1]))
            i += 2
        else:
            merged.append((cls, text))
            i += 1
    items = merged

    # Pass B: suppress diagram clusters (3+ short consecutive headings)
    cluster_min = cfg["diagram_cluster_min"]
    avg_max     = cfg["diagram_avg_len_max"]
    result = []
    i = 0
    while i < len(items):
        cls, text = items[i]
        if cls not in ("h2", "h3"):
            result.append((cls, text))
            i += 1
            continue
        # Count run
        run = []
        j = i
        while j < len(items) and items[j][0] in ("h2", "h3"):
            run.append(items[j])
            j += 1
        avg_len = sum(len(r[1]) for r in run) / len(run) if run else 0
        if len(run) >= cluster_min and avg_len < avg_max:
            for _, rtxt in run:
                if len(rtxt.strip()) > 3:
                    result.append(("body", rtxt))
            i = j
        else:
            for r in run:
                result.append(r)
            i = j
    return result


def extract_page(page: fitz.Page, classifier: LineClassifier, cfg: Dict[str, Any]) -> List[tuple]:
    """Extract (cls, text) items from one PDF page."""
    blocks = page.get_text("dict", sort=True)["blocks"]
    raw = []

    for bi, b in enumerate(blocks):
        if b["type"] != 0:
            continue
        for pdf_line in b["lines"]:
            text = ""
            dom_size, dom_flags = 10.0, 0
            for span in pdf_line["spans"]:
                if span["size"] > 6.5:
                    text += span["text"]
                if span["size"] > dom_size or dom_flags == 0:
                    dom_size  = span["size"]
                    dom_flags = span["flags"]
            text = text.strip()
            if not text:
                continue
            cls = classifier.classify(dom_size, dom_flags, text)
            if cls == "skip":
                continue
            raw.append((cls, text, bi))

    # Merge body/callout lines from same block
    items = []
    i = 0
    while i < len(raw):
        cls, text, bi = raw[i]
        if cls in ("h2", "h3", "box_label"):
            items.append((cls, text))
            i += 1
            continue
        parts = [text]
        j = i + 1
        while j < len(raw) and raw[j][0] == cls and raw[j][2] == bi:
            ntext = raw[j][1]
            if parts[-1].endswith("-"):
                parts[-1] = parts[-1][:-1] + ntext
            else:
                parts.append(ntext)
            j += 1
        items.append((cls, " ".join(parts)))
        i = j

    return postprocess_items(items, cfg)


def to_markdown(items: List[tuple]) -> str:
    out = []
    in_callout = False
    for cls, text in items:
        t = text.strip()
        if not t:
            continue
        if cls == "h2":
            in_callout = False
            out += ["", f"## {t}", ""]
        elif cls == "h3":
            in_callout = False
            out += ["", f"### {t}", ""]
        elif cls == "box_label":
            in_callout = False
            out += ["", "> [!NOTE]", f"> **{t}**", "> "]
        elif cls == "callout":
            if not in_callout:
                out.append("")
            out.append(f"> {t}")
            in_callout = True
        elif cls == "body":
            in_callout = False
            out.append(t)
    return "\n".join(out)


def collect_anchor_targets(content: str) -> Dict[str, List[str]]:
    """Map heading text to existing stable anchors placed immediately above it."""
    targets: Dict[str, List[str]] = {}
    anchor_re = re.compile(r"<a\s+[^>]*id\s*=\s*['\"]([^'\"]+)['\"][^>]*>\s*</a>", re.IGNORECASE)
    lines = content.splitlines()
    for idx, line in enumerate(lines):
        match = anchor_re.search(line)
        if not match:
            continue
        anchor = match.group(1)
        for next_line in lines[idx + 1:]:
            stripped = next_line.strip()
            if not stripped:
                continue
            if stripped.startswith("#"):
                heading = re.sub(r"^#+\s*", "", stripped).strip()
                targets.setdefault(heading.casefold(), []).append(anchor)
            break
    return targets


def apply_preserved_anchors(content: str, existing_content: str) -> str:
    """Reinsert existing anchors before matching headings in regenerated Markdown."""
    targets = collect_anchor_targets(existing_content)
    if not targets:
        return content

    used = set()
    output = []
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            heading = re.sub(r"^#+\s*", "", stripped).strip()
            for anchor in targets.get(heading.casefold(), []):
                if anchor not in used:
                    output.append(f'<a id="{anchor}"></a>')
                    used.add(anchor)
        output.append(line)
    return "\n".join(output)


# ── Chapter metadata ──────────────────────────────────────────────────────────

def make_frontmatter(
    chapter_num: int,
    title: str,
    slug: str,
    standard: str,
    source_id: str = "",
    source_pdf: str = "",
    page_start: Optional[int] = None,
    page_end: Optional[int] = None,
    content_hash: str = "",
) -> str:
    tags = [standard.split("(")[0].strip(), title] if standard else [title]
    tags_yaml = json.dumps(tags, ensure_ascii=False)
    metadata = ""
    if source_id:
        metadata += f'source_id: "{source_id}"\n'
    if source_pdf:
        metadata += f'source_pdf: "{source_pdf}"\n'
    if page_start is not None:
        metadata += f"page_start: {page_start}\n"
    if page_end is not None:
        metadata += f"page_end: {page_end}\n"
    if content_hash:
        metadata += f'content_hash: "{content_hash}"\n'
    return (
        f"---\n"
        f"id: {slug}\n"
        f'title: "{title}"\n'
        f"chapter: {chapter_num}\n"
        f'standard: "{standard}"\n'
        f"{metadata}"
        f"tags: {tags_yaml}\n"
        f"---\n\n"
        f"# {title}\n\n"
    )


# ── Chapter processing ────────────────────────────────────────────────────────

def process_chapter(
    doc: fitz.Document,
    chapter: Dict[str, Any],
    out_dir: Path,
    classifier: LineClassifier,
    cfg: Dict[str, Any],
    standard: str,
    source_id: str,
    source_pdf: str,
    emit_source_metadata: bool,
    backup: bool,
    verbose: bool,
) -> Dict[str, Any]:
    """Extract one chapter and write to out_dir. Returns stats dict."""
    n     = chapter["num"]
    slug  = chapter["slug"]
    title = chapter["title"]
    start = chapter["start_page"]
    end   = chapter["end_page"]

    all_items = []
    for pg in range(start - 1, end):
        page_items = extract_page(doc[pg], classifier, cfg)
        all_items.extend(page_items)
        if verbose:
            for cls, txt in page_items:
                print(f"    [{cls:10s}] {txt[:60]}", file=sys.stderr)

    # Cross-page postprocess
    all_items = postprocess_items(all_items, cfg)

    md = to_markdown(all_items)
    md = re.sub(r"\n{3,}", "\n\n", md)

    fname = f"{n:02d}_{slug}.md"
    fpath = out_dir / fname
    existing_content = fpath.read_text(encoding="utf-8") if fpath.exists() else ""
    body = md.strip()
    if existing_content:
        body = apply_preserved_anchors(body, existing_content)
    content_hash = hashlib.sha256(body.strip().encode("utf-8")).hexdigest()

    content = make_frontmatter(
        n,
        title,
        slug,
        standard,
        source_id=source_id if emit_source_metadata else "",
        source_pdf=source_pdf if emit_source_metadata else "",
        page_start=start if emit_source_metadata else None,
        page_end=end if emit_source_metadata else None,
        content_hash=content_hash if emit_source_metadata else "",
    ) + body.strip() + "\n"

    # Backup if requested
    if backup and fpath.exists():
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        bak = fpath.with_suffix(f".{ts}.bak.md")
        shutil.copy2(fpath, bak)

    fpath.write_text(content, encoding="utf-8", newline="\n")

    h2    = content.count("\n## ")
    h3    = content.count("\n### ")
    notes = content.count("[!NOTE]")
    lines = content.count("\n")

    return {"file": fname, "lines": lines, "h2": h2, "h3": h3, "notes": notes}


# ── Chapter detection ─────────────────────────────────────────────────────────

def auto_detect_chapters(doc: fitz.Document, cfg: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Auto-detect chapter start pages using 'C H A P T E R N' pattern.
    Returns list of {num, start_page, end_page} dicts.
    """
    pattern = re.compile(cfg["chapter_label_pattern"])
    found = {}
    for i in range(len(doc)):
        text = doc[i].get_text("text")
        m = pattern.search(text)
        if m:
            # Extract chapter number from match
            num_match = re.search(r"\d+", m.group())
            if num_match:
                ch = int(num_match.group())
                if ch not in found:
                    found[ch] = i + 1  # 1-indexed

    chapters_sorted = sorted(found.items())
    result = []
    for idx, (ch, start) in enumerate(chapters_sorted):
        end = chapters_sorted[idx + 1][1] - 1 if idx + 1 < len(chapters_sorted) else len(doc)
        result.append({"num": ch, "start_page": start, "end_page": end})
    return result


def load_chapters_config(config_path: str) -> List[Dict[str, Any]]:
    """Load chapters.json from scan_chapter_pages.py output."""
    with open(config_path, encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    return data.get("chapters", data)


# ── CLI ───────────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Extract PDF chapters to Knowledge Base Markdown files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--pdf",  required=True, help="Input PDF path")
    p.add_argument("--out",  required=True, help="Output directory")
    p.add_argument("--config",      help="chapters.json from scan_chapter_pages.py")
    p.add_argument("--only",        help="Only extract chapters: '4,5,6'")
    p.add_argument("--skip",        help="Skip chapters: '0,1'")
    p.add_argument("--backup",      action="store_true", help="Backup existing .md files")
    p.add_argument("--font-config", help="Path to font_config.json")
    p.add_argument("--standard",    default="", help="Value for 'standard' YAML field")
    p.add_argument("--source-id",   default="", help="Stable source document ID for citation metadata")
    p.add_argument(
        "--emit-source-metadata",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Emit source_id, source_pdf, page range, and content_hash in YAML frontmatter",
    )
    p.add_argument("--verbose",     action="store_true")
    return p.parse_args()


def main():
    try:
        args = parse_args()

        # Load PDF
        pdf_path = Path(args.pdf)
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")

        doc = fitz.open(str(pdf_path))
        print(f"PDF: {pdf_path.name}  ({len(doc)} pages)", file=sys.stderr)

        # Load font config
        cfg = DEFAULT_FONT_CONFIG.copy()
        font_cfg_path = args.font_config
        if not font_cfg_path:
            default_cfg = Path(__file__).parent.parent / "resources" / "font_config.json"
            if default_cfg.exists():
                font_cfg_path = str(default_cfg)
        if font_cfg_path and Path(font_cfg_path).exists():
            with open(font_cfg_path, encoding="utf-8") as f:
                user_cfg = json.load(f)
            cfg.update({k: v for k, v in user_cfg.items() if not k.startswith("_")})
            print(f"Font config: {font_cfg_path}", file=sys.stderr)

        classifier = LineClassifier(cfg)

        # Load or detect chapter map
        if args.config:
            chapters = load_chapters_config(args.config)
            print(f"Chapters from config: {args.config}", file=sys.stderr)
        else:
            print("Auto-detecting chapter boundaries...", file=sys.stderr)
            chapters = auto_detect_chapters(doc, cfg)
            if not chapters:
                raise ValueError("No chapters detected. Use --config to provide chapters.json")
            print(f"Detected {len(chapters)} chapters.", file=sys.stderr)

        # Filter --only / --skip
        only_set = set(int(x) for x in args.only.split(",")) if args.only else None
        skip_set = set(int(x) for x in args.skip.split(",")) if args.skip else set()
        chapters = [c for c in chapters if
                    (only_set is None or c["num"] in only_set) and c["num"] not in skip_set]

        # Prepare output dir
        out_dir = Path(args.out)
        out_dir.mkdir(parents=True, exist_ok=True)

        standard = args.standard or pdf_path.stem.replace("-", " ").replace("_", " ").title()
        source_id = args.source_id or re.sub(r"[^\w]+", "_", pdf_path.stem.lower()).strip("_")

        # Process
        print(f"\n{'File':<44} {'Lines':>6}  H2  H3  NOTE", file=sys.stderr)
        print("-" * 66, file=sys.stderr)
        stats_list = []
        for chapter in chapters:
            if not chapter.get("title"):
                chapter["title"] = f"Chapter {chapter['num']}"
            if not chapter.get("slug"):
                chapter["slug"] = re.sub(r"[^\w]+", "_", chapter["title"].lower()).strip("_")
            stats = process_chapter(
                doc, chapter, out_dir, classifier, cfg, standard,
                source_id=source_id,
                source_pdf=str(pdf_path),
                emit_source_metadata=args.emit_source_metadata,
                backup=args.backup, verbose=args.verbose,
            )
            print(
                f"[OK] {stats['file']:<42}  {stats['lines']:4d}  "
                f"{stats['h2']:2d}  {stats['h3']:3d}  {stats['notes']:4d}",
                file=sys.stderr
            )
            stats_list.append(stats)

        # Validation summary
        print("\n=== Validation ===", file=sys.stderr)
        issues = []
        for s in stats_list:
            if s["h2"] == 0:
                issues.append(f"  WARN: {s['file']} - H2=0, headings may not be detected")
            if s["lines"] < 20:
                issues.append(f"  WARN: {s['file']} - only {s['lines']} lines, content may be missing")
        if issues:
            for issue in issues:
                print(issue, file=sys.stderr)
        else:
            print("  All files look good.", file=sys.stderr)

        print(f"\nDone. {len(stats_list)} file(s) written to: {out_dir}", file=sys.stderr)

        # Standard output JSON as required by SCRIPT_STANDARDS.md
        result_json = {
            "status": "success",
            "pdf": str(pdf_path),
            "output_directory": str(out_dir),
            "files_written": len(stats_list),
            "chapters": stats_list,
            "validation_issues": issues
        }
        print(json.dumps(result_json, indent=2, ensure_ascii=False))

    except Exception as e:
        error_json = {
            "status": "error",
            "error_code": type(e).__name__,
            "message": str(e),
            "suggestion": "Check input PDF path, chapter config file, or font configuration settings."
        }
        print(json.dumps(error_json, indent=2, ensure_ascii=False))
        sys.exit(1)


if __name__ == "__main__":
    main()
