"""
validate_citations.py
=====================
Validate Neo4j Concept citation pointers against local Markdown KB files.

Default output is compact for CLI windows. Use --full-json for every issue.

Usage:
  uv run C:/Users/kira7/.gemini/config/skills/pdf-to-kb/scripts/validate_citations.py --kb-dir Projects/ESG/kb/ghg_protocol
"""
import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from neo4j import GraphDatabase

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from import_concept_map import has_anchor, load_env, parse_frontmatter  # noqa: E402


def resolve_node_file(kb_dir: Path, file_path: Optional[str], doc_id: Optional[str]) -> Optional[Path]:
    candidates: List[Path] = []
    if file_path:
        raw = Path(file_path)
        candidates.append(raw)
        if not raw.is_absolute():
            candidates.append(Path.cwd() / raw)
            candidates.append(kb_dir / raw.name)
    if doc_id:
        candidates.extend(sorted(kb_dir.rglob(f"*{doc_id}.md")))
    for candidate in candidates:
        if candidate.exists():
            return candidate.resolve()
    return None


def validate_node(node: Dict[str, Any], kb_dir: Path, strict_metadata: bool) -> List[str]:
    issues: List[str] = []
    node_id = node.get("id") or "(missing id)"
    labels = node.get("labels") or []
    file_path = resolve_node_file(kb_dir, node.get("file_path"), node.get("doc_id"))
    if not file_path:
        return [f"{node_id}: file not found ({node.get('file_path') or node.get('doc_id')})"]

    content = file_path.read_text(encoding="utf-8")
    anchor = node.get("anchor")
    if not anchor and "Chapter" in labels:
        pass
    elif not anchor:
        issues.append(f"{node_id}: anchor missing on graph node")
    elif not has_anchor(content, anchor):
        issues.append(f"{node_id}: anchor '{anchor}' not found in {file_path.name}")

    metadata = parse_frontmatter(content)
    for field in ("source_pdf", "page_start", "page_end", "content_hash"):
        node_value = node.get(field)
        file_value = metadata.get(field)
        if strict_metadata and not file_value and not node_value:
            issues.append(f"{node_id}: citation metadata missing: {field}")
    return issues


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate graph citations against local Markdown KB files.")
    parser.add_argument("--kb-dir", default="Projects/ESG/kb/ghg_protocol", help="Path to markdown KB directory")
    parser.add_argument("--env", default=".env", help="Path to .env configuration file")
    parser.add_argument("--limit", type=int, default=10, help="Maximum sample issues in compact output")
    parser.add_argument("--strict-metadata", action="store_true", help="Treat missing source/page/hash metadata as issues")
    parser.add_argument("--full-json", action="store_true", help="Include all issue details")
    parser.add_argument("--project-id", default="esg", help="Restrict validation to a project_id; use empty string to disable")
    parser.add_argument("--collection-id", default="", help="Restrict validation to a collection_id")
    parser.add_argument("--source-id", default="", help="Restrict validation to a source_id")
    parser.add_argument("--source-map-hash", default="", help="Restrict validation to a specific imported concept_map hash")
    return parser.parse_args()


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
        args = parse_args()
        args.limit = max(1, min(args.limit, 200))

        load_env(Path(args.env))
        uri = os.getenv("NEO4J_URI")
        user = os.getenv("NEO4J_USERNAME")
        password = os.getenv("NEO4J_PASSWORD")
        database = os.getenv("NEO4J_DATABASE", "neo4j")
        if not uri or not user or not password:
            raise ValueError("Missing Neo4j credentials in environment.")

        kb_dir = Path(args.kb_dir)
        driver = GraphDatabase.driver(uri, auth=(user, password))
        with driver.session(database=database) as session:
            rows = session.run(
                """
                MATCH (n:Concept)
                WHERE ($project_id = '' OR n.project_id = $project_id)
                  AND ($collection_id = '' OR n.collection_id = $collection_id)
                  AND ($source_id = '' OR n.source_id = $source_id)
                  AND ($source_map_hash = '' OR n.source_map_hash = $source_map_hash)
                RETURN n.id AS id, n.name AS name, labels(n) AS labels, n.doc_id AS doc_id, n.anchor AS anchor,
                       n.file_path AS file_path, n.file_uri AS file_uri,
                       properties(n).source_pdf AS source_pdf,
                       properties(n).page_start AS page_start,
                       properties(n).page_end AS page_end,
                       properties(n).content_hash AS content_hash
                ORDER BY n.id
                """,
                project_id=args.project_id,
                collection_id=args.collection_id,
                source_id=args.source_id,
                source_map_hash=args.source_map_hash,
            )
            nodes = [dict(row) for row in rows]
        driver.close()

        issue_items = []
        for node in nodes:
            for issue in validate_node(node, kb_dir, args.strict_metadata):
                issue_items.append({"id": node.get("id"), "name": node.get("name"), "issue": issue})

        output = {
            "status": "success",
            "node_count": len(nodes),
            "issue_count": len(issue_items),
            "strict_metadata": args.strict_metadata,
            "source_map_hash": args.source_map_hash,
            "project_id": args.project_id,
            "collection_id": args.collection_id,
            "source_id": args.source_id,
            "issues_sample": issue_items[: args.limit],
        }
        if args.full_json:
            output["issues"] = issue_items
        print(json.dumps(output, indent=2, ensure_ascii=False))
    except Exception as exc:
        print(
            json.dumps(
                {"status": "error", "error_code": type(exc).__name__, "message": str(exc)},
                indent=2,
                ensure_ascii=False,
            )
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
