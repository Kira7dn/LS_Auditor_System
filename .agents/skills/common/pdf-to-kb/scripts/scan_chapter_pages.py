"""
scan_chapter_pages.py
=====================
Phát hiện chapter boundaries trong PDF và xuất ra chapters.json.
Tuân thủ nghiêm ngặt bộ tiêu chuẩn SCRIPT_STANDARDS.md (AI-First Scripting).

Usage:
  uv run C:/Users/kira7/.gemini/config/skills/pdf-to-kb/scripts/scan_chapter_pages.py --pdf document.pdf
  uv run C:/Users/kira7/.gemini/config/skills/pdf-to-kb/scripts/scan_chapter_pages.py --pdf document.pdf --out chapters.json

Output (stdout):
  JSON object with chapter page boundaries or error state.
All logs/progress are routed to stderr.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Any

import fitz


# Common chapter label patterns
PATTERNS = {
    "spaced": r"C\s+H\s+A\s+P\s+T\s+E\s+R\s+(\d+)",   # "C H A P T E R  4"
    "solid":  r"^CHAPTER\s+(\d+)\b",                     # "CHAPTER 4"
    "roman":  r"^Chapter\s+(\d+)\b",                     # "Chapter 4"
}


def scan_pdf(doc: fitz.Document, pattern_key: str = "spaced") -> List[Dict[str, Any]]:
    """
    Scan all pages for chapter start markers.
    Returns list of {num, start_page, end_page}.
    """
    pat = re.compile(PATTERNS.get(pattern_key, pattern_key), re.MULTILINE)
    found = {}
    for i in range(len(doc)):
        text = doc[i].get_text("text")
        for m in pat.finditer(text):
            ch = int(m.group(1))
            if ch not in found:
                found[ch] = i + 1  # 1-indexed

    sorted_ch = sorted(found.items())
    result = []
    for idx, (ch, start) in enumerate(sorted_ch):
        end = sorted_ch[idx + 1][1] - 1 if idx + 1 < len(sorted_ch) else len(doc)
        result.append({
            "num": ch,
            "slug": "",
            "title": "",
            "start_page": start,
            "end_page": end,
        })
    return result


def try_bookmarks(doc: fitz.Document) -> List[Dict[str, Any]]:
    """Try to extract chapters from PDF bookmarks/outline."""
    try:
        toc = doc.get_toc()  # [[level, title, page], ...]
        if not toc:
            return []
        # Only top-level entries (level=1)
        top = [(t, p) for level, t, p in toc if level == 1]
        if not top:
            return []
        result = []
        for idx, (title, page) in enumerate(top):
            end = top[idx + 1][1] - 1 if idx + 1 < len(top) else doc.page_count
            slug = re.sub(r"[^\w]+", "_", title.lower()).strip("_")
            result.append({
                "num": idx,
                "slug": slug,
                "title": title,
                "start_page": page,
                "end_page": end,
            })
        return result
    except Exception:
        return []


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Scan PDF for chapter boundaries.")
    p.add_argument("--pdf",     required=True, help="Input PDF path")
    p.add_argument("--out",     default="",    help="Output JSON path (default: <pdf>.chapters.json)")
    p.add_argument("--pattern", default="spaced",
                   help="Pattern: 'spaced' (C H A P T E R N), 'solid' (CHAPTER N), "
                        "'roman' (Chapter N), or a raw regex with group(1)=chapter_num")
    p.add_argument("--no-bookmarks", action="store_true",
                   help="Skip checking PDF bookmarks")
    return p.parse_args()


def main():
    try:
        args = parse_args()
        pdf_path = Path(args.pdf)
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")

        doc = fitz.open(str(pdf_path))
        print(f"PDF: {pdf_path.name}  ({doc.page_count} pages)", file=sys.stderr)

        chapters = []

        # Try bookmarks first (most accurate)
        if not args.no_bookmarks:
            chapters = try_bookmarks(doc)
            if chapters:
                print(f"Found {len(chapters)} chapters from PDF bookmarks/outline.", file=sys.stderr)

        # Fall back to text pattern scan
        if not chapters:
            chapters = scan_pdf(doc, args.pattern)
            if chapters:
                print(f"Found {len(chapters)} chapters via pattern '{args.pattern}'.", file=sys.stderr)
            else:
                print("WARNING: No chapters detected. Check --pattern or provide chapters.json manually.", file=sys.stderr)

        # Print result table to stderr
        print(f"\n{'Num':>4}  {'Start':>6}  {'End':>6}  Title", file=sys.stderr)
        print("-" * 50, file=sys.stderr)
        for c in chapters:
            print(f"  {c['num']:>2}  p{c['start_page']:>5}  p{c['end_page']:>5}  {c['title'] or '(no title)'}", file=sys.stderr)

        # Save JSON
        out_path = args.out or str(pdf_path.with_suffix(".chapters.json"))
        output = {
            "status": "success",
            "pdf": str(pdf_path),
            "total_pages": doc.page_count,
            "chapters": chapters,
        }
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        print(f"\nSaved: {out_path}", file=sys.stderr)

        # Output to stdout
        print(json.dumps(output, indent=2, ensure_ascii=False))

    except Exception as e:
        error_json = {
            "status": "error",
            "error_code": type(e).__name__,
            "message": str(e),
            "suggestion": "Check input PDF path, layout patterns or bookmarks flag."
        }
        print(json.dumps(error_json, indent=2, ensure_ascii=False))
        sys.exit(1)


if __name__ == "__main__":
    main()
