"""
build_pdf_citation_index.py
===========================
Build a reverse PDF bbox citation index from existing Markdown KB anchors.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

import fitz

from pdf_bbox_citations import normalize_text, text_hash


ANCHOR_RE = re.compile(r"<a\s+[^>]*id\s*=\s*['\"]([^'\"]+)['\"][^>]*>\s*</a>", re.IGNORECASE)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def parse_frontmatter(content: str) -> dict[str, Any]:
    if not content.startswith("---\n"):
        return {}
    end = content.find("\n---", 4)
    if end == -1:
        return {}
    metadata: dict[str, Any] = {}
    for raw_line in content[4:end].splitlines():
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        value = value.strip().strip("'\"")
        metadata[key.strip()] = int(value) if value.isdigit() else value
    return metadata


def resolve_path(value: str, base_dir: Path) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    cwd_candidate = Path.cwd() / path
    if cwd_candidate.exists():
        return cwd_candidate.resolve()
    return (base_dir / path).resolve()


def material_line(line: str) -> bool:
    stripped = line.strip()
    if len(stripped) < 16:
        return False
    if stripped.startswith("<a "):
        return False
    if stripped.startswith("---"):
        return False
    if stripped.startswith("|"):
        return False
    return True


def iter_anchor_sections(md_file: Path) -> list[dict[str, Any]]:
    content = md_file.read_text(encoding="utf-8-sig")
    metadata = parse_frontmatter(content)
    lines = content.splitlines()
    sections: list[dict[str, Any]] = []
    current_anchor: str | None = None
    current: dict[str, Any] | None = None

    for line in lines:
        anchor_match = ANCHOR_RE.search(line)
        if anchor_match:
            if current:
                sections.append(current)
            current_anchor = anchor_match.group(1)
            current = {
                "anchor": current_anchor,
                "heading": "",
                "paragraph": "",
                "metadata": metadata,
                "markdown_file": str(md_file.resolve()),
            }
            continue

        if not current_anchor or current is None:
            continue

        heading_match = HEADING_RE.match(line.strip())
        if heading_match and not current["heading"]:
            current["heading"] = heading_match.group(2).strip()
            continue

        if not current["paragraph"] and material_line(line) and not HEADING_RE.match(line.strip()):
            current["paragraph"] = line.strip()

    if current:
        sections.append(current)
    return sections


def search_variants(text: str) -> list[str]:
    text = text.strip()
    variants = [text]
    normalized = normalize_text(text)
    if normalized and normalized != text:
        variants.append(normalized)
    words = normalized.split()
    if len(words) > 10:
        variants.append(" ".join(words[:10]))
    if len(words) > 6:
        variants.append(" ".join(words[:6]))
    deduped: list[str] = []
    for item in variants:
        if item and item not in deduped:
            deduped.append(item)
    return deduped


def rect_payload(rects: list[Any]) -> tuple[list[float], list[list[float]]]:
    bboxes = [[round(rect.x0, 2), round(rect.y0, 2), round(rect.x1, 2), round(rect.y1, 2)] for rect in rects]
    x0 = min(bbox[0] for bbox in bboxes)
    y0 = min(bbox[1] for bbox in bboxes)
    x1 = max(bbox[2] for bbox in bboxes)
    y1 = max(bbox[3] for bbox in bboxes)
    return [round(x0, 2), round(y0, 2), round(x1, 2), round(y1, 2)], bboxes


def candidate_texts(section: dict[str, Any]) -> list[tuple[str, str, float]]:
    candidates: list[tuple[str, str, float]] = []
    heading = section.get("heading") or ""
    paragraph = section.get("paragraph") or ""
    if paragraph:
        candidates.append(("paragraph", paragraph, 0.95))
    if heading:
        candidates.append(("heading", heading, 0.85))
    return candidates



def search_pdf(
    pdf_path: Path,
    page_start: int,
    page_end: int,
    section: dict[str, Any],
) -> dict[str, Any] | None:
    with fitz.open(str(pdf_path)) as doc:
        first = max(1, int(page_start or 1))
        last = min(int(page_end or len(doc)), len(doc))
        best: dict[str, Any] | None = None
        for match_type, text, base_confidence in candidate_texts(section):
            for variant in search_variants(text):
                if len(normalize_text(variant)) < 6:
                    continue
                for page_number in range(first, last + 1):
                    page = doc[page_number - 1]
                    rects = page.search_for(variant)
                    if not rects:
                        continue
                    confidence = base_confidence
                    if len(rects) > 1:
                        confidence -= 0.1
                    if variant != text:
                        confidence -= 0.08
                    bbox, bboxes = rect_payload(rects)
                    record = {
                        "page_number": page_number,
                        "bbox": bbox,
                        "bboxes": bboxes,
                        "matched_pdf_text": text,
                        "searched_text": variant,
                        "match_type": match_type,
                        "confidence": round(max(0.0, confidence), 3),
                        "ambiguous": len(rects) > 1,
                        "match_count_on_page": len(rects),
                    }
                    if best is None or record["confidence"] > best["confidence"]:
                        best = record
        return best


def build_records(args: argparse.Namespace) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    kb_dir = Path(args.kb_dir)
    records: list[dict[str, Any]] = []
    unresolved: list[dict[str, Any]] = []
    anchor_count = 0

    for md_file in sorted(kb_dir.glob("*.md")):
        if ".bak." in md_file.name:
            continue
        sections = iter_anchor_sections(md_file)
        heading_counts: dict[str, int] = {}
        for section in sections:
            heading = normalize_text(section.get("heading") or "")
            if heading:
                heading_counts[heading] = heading_counts.get(heading, 0) + 1
        for section in sections:
            heading = normalize_text(section.get("heading") or "")
            section["duplicate_heading"] = bool(heading and heading_counts.get(heading, 0) > 1)
            anchor_count += 1
            metadata = section["metadata"]
            source_pdf = metadata.get("source_pdf")
            page_start = metadata.get("page_start")
            page_end = metadata.get("page_end")
            if not source_pdf or not page_start or not page_end:
                unresolved.append({"anchor": section["anchor"], "markdown_file": str(md_file), "reason": "missing_metadata"})
                continue
            pdf_path = resolve_path(str(source_pdf), Path.cwd())
            if not pdf_path.exists():
                unresolved.append({"anchor": section["anchor"], "markdown_file": str(md_file), "reason": "pdf_not_found", "source_pdf": source_pdf})
                continue
            match = search_pdf(pdf_path, int(page_start), int(page_end), section)
            if not match:
                unresolved.append({"anchor": section["anchor"], "markdown_file": str(md_file), "reason": "no_pdf_match"})
                continue
            records.append(
                {
                    "project_id": args.project_id,
                    "collection_id": args.collection_id,
                    "source_id": args.source_id or metadata.get("source_id") or "",
                    "anchor": section["anchor"],
                    "markdown_file": str(md_file.resolve()),
                    "source_pdf": str(pdf_path),
                    "source_pdf_declared": source_pdf,
                    "page_start": page_start,
                    "page_end": page_end,
                    "text_hash": text_hash(match["matched_pdf_text"]),
                    **match,
                }
            )

    summary = {
        "status": "success",
        "anchor_count": anchor_count,
        "resolved_count": len(records),
        "unresolved_count": len(unresolved),
        "bbox_resolve_rate": round(len(records) / max(1, anchor_count), 3),
        "ambiguous_count": sum(1 for item in records if item.get("ambiguous")),
        "unresolved_sample": unresolved[:20],
    }
    return records, summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build reverse PDF bbox citation index from Markdown KB anchors.")
    parser.add_argument("--kb-dir", default="Projects/ESG/kb/ghg_protocol")
    parser.add_argument("--project-id", default="esg")
    parser.add_argument("--collection-id", default="ghg_protocol")
    parser.add_argument("--source-id", default="ghg_protocol_corporate_standard")
    parser.add_argument("--out", default="Projects/ESG/graph/citation_index/pdf_citation_index.jsonl")
    parser.add_argument("--report", default="Projects/ESG/graph/citation_index/pdf_citation_index_report.json")
    return parser.parse_args()


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
        args = parse_args()
        records, summary = build_records(args)
        out_path = Path(args.out)
        report_path = Path(args.report)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text("\n".join(json.dumps(record, ensure_ascii=False) for record in records) + ("\n" if records else ""), encoding="utf-8", newline="\n")
        report_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
        print(json.dumps({**summary, "index": str(out_path), "report": str(report_path)}, ensure_ascii=False, indent=2))
    except Exception as exc:
        print(json.dumps({"status": "error", "error_code": type(exc).__name__, "message": str(exc)}, ensure_ascii=False, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
