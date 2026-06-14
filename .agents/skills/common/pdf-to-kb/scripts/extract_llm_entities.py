"""
extract_llm_entities.py
=======================
Extract candidate legal/compliance entities from anchored Markdown sections
using the OpenAI API. This script does not write to Neo4j.

Output is JSONL, one record per processed section. Each record keeps source
anchor/page/hash metadata so later validation can reject unsupported claims.

Usage:
  uv run C:/Users/kira7/.gemini/config/skills/pdf-to-kb/scripts/extract_llm_entities.py --kb-dir Projects/ESG/kb/ghg_protocol --out Projects/ESG/graph/llm_candidates/llm_candidates.jsonl
"""
import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from import_concept_map import ONTOLOGY_NODES, WHITELIST_EDGES, load_env, parse_frontmatter  # noqa: E402


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_")


def section_text_hash(text: str) -> str:
    return hashlib.sha256(text.strip().encode("utf-8")).hexdigest()


def iter_anchored_sections(kb_dir: Path, max_chars: int) -> List[Dict[str, Any]]:
    anchor_re = re.compile(r"<a\s+[^>]*id\s*=\s*['\"]([^'\"]+)['\"][^>]*>\s*</a>", re.IGNORECASE)
    heading_re = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
    sections: List[Dict[str, Any]] = []

    for md_file in sorted(kb_dir.glob("*.md")):
        if ".bak." in md_file.name:
            continue
        content = md_file.read_text(encoding="utf-8")
        metadata = parse_frontmatter(content)
        if not all(metadata.get(k) for k in ("id", "source_pdf", "page_start", "page_end", "content_hash")):
            continue

        lines = content.splitlines()
        pending_anchor = ""
        current: Dict[str, Any] | None = None
        for line in lines:
            anchor_match = anchor_re.search(line)
            if anchor_match:
                pending_anchor = anchor_match.group(1)
                continue

            heading_match = heading_re.match(line.strip())
            if heading_match and pending_anchor:
                if current:
                    current["text"] = "\n".join(current["lines"]).strip()[:max_chars]
                    current["section_text_hash"] = section_text_hash(current["text"])
                    sections.append(current)
                current = {
                    "doc_id": metadata["id"],
                    "file": str(md_file),
                    "anchor": pending_anchor,
                    "heading": heading_match.group(2).strip(),
                    "heading_level": len(heading_match.group(1)),
                    "source_pdf": metadata.get("source_pdf"),
                    "source_id": metadata.get("source_id"),
                    "page_start": metadata.get("page_start"),
                    "page_end": metadata.get("page_end"),
                    "content_hash": metadata.get("content_hash"),
                    "lines": [line],
                }
                pending_anchor = ""
                continue

            if current:
                current["lines"].append(line)

        if current:
            current["text"] = "\n".join(current["lines"]).strip()[:max_chars]
            current["section_text_hash"] = section_text_hash(current["text"])
            sections.append(current)

    for section in sections:
        section.pop("lines", None)
    return sections


def build_prompt(section: Dict[str, Any]) -> str:
    return (
        "Extract compliance/audit graph candidates from this single cited Markdown section.\n"
        "Return only JSON with keys nodes and edges.\n\n"
        f"Allowed node labels: {sorted(ONTOLOGY_NODES)}\n"
        f"Allowed edge types: {sorted(WHITELIST_EDGES)}\n\n"
        "Rules:\n"
        "- Extract only concepts explicitly supported by this section text.\n"
        "- Every node and edge must include evidence_quote copied exactly from the section text.\n"
        "- Use confidence 0.9 for direct explicit evidence and 0.7 only for a directly evidenced relation.\n"
        "- Do not emit nodes or edges below confidence 0.5.\n"
        "- Prefer stable lowercase snake_case IDs.\n"
        "- Do not invent page numbers, anchors, or relationships not evidenced here.\n"
        "- Keep output compact: at most 8 nodes and 10 edges.\n\n"
        f"Section metadata:\n"
        f"doc_id={section['doc_id']}\n"
        f"anchor={section['anchor']}\n"
        f"heading={section['heading']}\n\n"
        "JSON schema:\n"
        "{\n"
        '  "nodes": [\n'
        '    {"id": "node_id", "label": "Requirement", "name": "Short name", '
        '"evidence_quote": "exact text copied from section", "confidence": 0.9, "rationale_short": "why"}\n'
        "  ],\n"
        '  "edges": [\n'
        '    {"from": "node_id", "to": "other_node_id", "type": "REL_TYPE", '
        '"evidence_quote": "exact text copied from section", "confidence": 0.7, "rationale_short": "why"}\n'
        "  ]\n"
        "}\n\n"
        f"Section text:\n{section['text']}"
    )


def call_openai(section: Dict[str, Any], model: str) -> Dict[str, Any]:
    from openai import OpenAI

    client = OpenAI()
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "You extract strictly evidenced legal/compliance graph candidates from cited text.",
            },
            {"role": "user", "content": build_prompt(section)},
        ],
        temperature=0,
        response_format={"type": "json_object"},
    )
    return json.loads(response.choices[0].message.content or "{}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract LLM entity candidates from anchored Markdown sections.")
    parser.add_argument("--kb-dir", required=True, help="Path to markdown KB directory")
    parser.add_argument("--out", required=True, help="Output JSONL candidates path")
    parser.add_argument("--env", default=".env", help="Path to .env configuration file")
    parser.add_argument("--model", default=os.getenv("OPENAI_MODEL", "gpt-4o-mini"), help="OpenAI model")
    parser.add_argument("--limit-sections", type=int, default=0, help="Process only first N sections; 0 means all")
    parser.add_argument("--max-section-chars", type=int, default=8000, help="Maximum section text sent to LLM")
    parser.add_argument("--dry-run", action="store_true", help="Build section records without calling OpenAI")
    return parser.parse_args()


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
        args = parse_args()
        load_env(Path(args.env))

        if not args.dry_run and not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY is not set. Use --dry-run to inspect sections without API calls.")

        sections = iter_anchored_sections(Path(args.kb_dir), args.max_section_chars)
        if args.limit_sections:
            sections = sections[: args.limit_sections]

        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        records_written = 0
        with out_path.open("w", encoding="utf-8", newline="\n") as f:
            for section in sections:
                if args.dry_run:
                    extraction = {"nodes": [], "edges": []}
                else:
                    print(f"LLM extracting {Path(section['file']).name}#{section['anchor']}", file=sys.stderr)
                    extraction = call_openai(section, args.model)

                record = {
                    "status": "candidate",
                    "extractor": "openai",
                    "model": args.model if not args.dry_run else "dry-run",
                    "doc_id": section["doc_id"],
                    "file": section["file"],
                    "anchor": section["anchor"],
                    "heading": section["heading"],
                    "source_pdf": section["source_pdf"],
                    "source_id": section.get("source_id"),
                    "page_start": section["page_start"],
                    "page_end": section["page_end"],
                    "content_hash": section["content_hash"],
                    "section_text_hash": section["section_text_hash"],
                    "section_text": section["text"],
                    "nodes": extraction.get("nodes", []),
                    "edges": extraction.get("edges", []),
                }
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
                records_written += 1

        print(
            json.dumps(
                {
                    "status": "success",
                    "sections_found": len(sections),
                    "records_written": records_written,
                    "output": str(out_path),
                    "dry_run": args.dry_run,
                },
                indent=2,
                ensure_ascii=False,
            )
        )
    except Exception as exc:
        print(json.dumps({"status": "error", "error_code": type(exc).__name__, "message": str(exc)}, indent=2, ensure_ascii=False))
        sys.exit(1)


if __name__ == "__main__":
    main()
