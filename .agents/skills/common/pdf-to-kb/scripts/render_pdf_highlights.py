"""
render_pdf_highlights.py
========================
Render cached PDF bbox highlights for citation evidence.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import fitz

from pdf_bbox_citations import highlight_file_name, load_pdf_citation_index


def render_record(record: dict[str, Any], highlight_dir: Path, output_format: str = "png", zoom: float = 2.0) -> dict[str, Any]:
    source_pdf = Path(record["source_pdf"])
    page_number = int(record["page_number"])
    bboxes = record.get("bboxes") or [record["bbox"]]
    highlight_dir.mkdir(parents=True, exist_ok=True)
    output_path = highlight_dir / highlight_file_name(record, output_format)
    if output_path.exists():
        rendered = False
    else:
        with fitz.open(str(source_pdf)) as doc:
            page = doc[page_number - 1]
            
            # Find text blocks on the page to expand narrow highlights to full paragraphs
            blocks = page.get_text("blocks")
            rects_to_highlight = []
            for bbox in bboxes:
                rect = fitz.Rect(*bbox)
                matched = False
                for b in blocks:
                    bx0, by0, bx1, by1, btext, block_no, block_type = b
                    block_rect = fitz.Rect(bx0, by0, bx1, by1)
                    if block_rect.intersects(rect) or rect.intersects(block_rect):
                        rects_to_highlight.append(block_rect)
                        matched = True
                if not matched:
                    rects_to_highlight.append(rect)
            
            # Deduplicate rectangles
            unique_rects = []
            for r in rects_to_highlight:
                if r not in unique_rects:
                    unique_rects.append(r)
            
            # Add highlight annotations
            for r in unique_rects:
                annot = page.add_highlight_annot(r)
                if annot:
                    annot.update()
            
            # Add footer text and link to source markdown
            md_path = record.get("markdown_file")
            anchor = record.get("anchor")
            if md_path:
                try:
                    rel_path = Path(md_path).relative_to(Path.cwd())
                except ValueError:
                    rel_path = Path(md_path).name
                footer_text = f"Source: {rel_path}#{anchor}"
                footer_uri = Path(md_path).resolve().as_uri() + (f"#{anchor}" if anchor else "")
            else:
                footer_text = None
                footer_uri = None

            if output_format == "png":
                # Compute bounding area for cropping
                if unique_rects:
                    union_rect = fitz.Rect(unique_rects[0])
                    for r in unique_rects[1:]:
                        union_rect.include_rect(r)
                    y0 = max(0.0, union_rect.y0 - 120.0)
                    y1 = min(float(page.rect.height), union_rect.y1 + 120.0)
                else:
                    y0 = 0.0
                    y1 = float(page.rect.height)
                
                if footer_text and footer_uri:
                    footer_rect = fitz.Rect(50, y1 - 22, float(page.rect.width) - 50, y1 - 2)
                    page.draw_rect(footer_rect, color=(1, 1, 1), fill=(1, 1, 1))
                    page.insert_textbox(
                        footer_rect,
                        footer_text,
                        fontsize=8,
                        fontname="helv",
                        color=(0, 0.4, 0.8),
                        align=0 # LEFT
                    )
                    page.insert_link({
                        "kind": fitz.LINK_URI,
                        "from": footer_rect,
                        "uri": footer_uri
                    })
                
                # Use full width of the page to avoid cutting off sentences horizontally
                clip_rect = fitz.Rect(0.0, y0, float(page.rect.width), y1)
                
                pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=clip_rect, alpha=False)
                pix.save(str(output_path))
            elif output_format == "pdf":
                if footer_text and footer_uri:
                    y_bottom = float(page.rect.height)
                    footer_rect = fitz.Rect(50, y_bottom - 30, float(page.rect.width) - 50, y_bottom - 10)
                    page.draw_rect(footer_rect, color=(1, 1, 1), fill=(1, 1, 1))
                    page.insert_textbox(
                        footer_rect,
                        footer_text,
                        fontsize=8,
                        fontname="helv",
                        color=(0, 0.4, 0.8),
                        align=0 # LEFT
                    )
                    page.insert_link({
                        "kind": fitz.LINK_URI,
                        "from": footer_rect,
                        "uri": footer_uri
                    })
                doc.save(str(output_path))
            else:
                raise ValueError(f"Unsupported output format: {output_format}")
        rendered = True
    result = dict(record)
    result["highlight_path"] = str(output_path.resolve())
    result["highlight_uri"] = output_path.resolve().as_uri()
    result["highlight_rendered"] = rendered
    return result


def load_records(args: argparse.Namespace) -> list[dict[str, Any]]:
    if args.record_json:
        return [json.loads(args.record_json)]
    records = load_pdf_citation_index(Path(args.citation_index))
    if args.anchor:
        records = [record for record in records if record.get("anchor") == args.anchor]
    return records[: args.limit]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render PDF bbox highlights with cache.")
    parser.add_argument("--citation-index", default="Projects/ESG/graph/citation_index/pdf_citation_index.jsonl")
    parser.add_argument("--record-json", default="", help="Single PDF citation record JSON")
    parser.add_argument("--anchor", default="", help="Optional anchor filter when rendering from an index")
    parser.add_argument("--highlight-dir", default="Projects/ESG/evidence/highlights")
    parser.add_argument("--format", choices=("png", "pdf"), default="png")
    parser.add_argument("--limit", type=int, default=20)
    return parser.parse_args()


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
        args = parse_args()
        rendered = [render_record(record, Path(args.highlight_dir), args.format) for record in load_records(args)]
        print(
            json.dumps(
                {
                    "status": "success",
                    "highlight_count": len(rendered),
                    "rendered_count": sum(1 for item in rendered if item.get("highlight_rendered")),
                    "highlights": rendered,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    except Exception as exc:
        print(json.dumps({"status": "error", "error_code": type(exc).__name__, "message": str(exc)}, ensure_ascii=False, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
