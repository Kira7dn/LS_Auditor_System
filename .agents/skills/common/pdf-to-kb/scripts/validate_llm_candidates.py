"""
validate_llm_candidates.py
==========================
Validate staged LLM entity candidates before importing to Neo4j.

Usage:
  uv run C:/Users/kira7/.gemini/config/skills/pdf-to-kb/scripts/validate_llm_candidates.py --candidates Projects/ESG/graph/llm_candidates/llm_candidates.jsonl --kb-dir Projects/ESG/kb/ghg_protocol
"""
import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from import_concept_map import ONTOLOGY_NODES, WHITELIST_EDGES, has_anchor, parse_frontmatter  # noqa: E402


def norm_text(value: str) -> str:
    value = value.replace("\u00ad", "")
    value = value.translate(str.maketrans({"“": '"', "”": '"', "‘": "'", "’": "'"}))
    value = re.sub(r"([A-Za-z])-\s+([A-Za-z])", r"\1\2", value)
    return re.sub(r"\s+", " ", value.strip()).casefold()


def quote_in_text(quote: str, text: str) -> bool:
    quote_norm = norm_text(quote)
    return bool(quote_norm) and quote_norm in norm_text(text)


def valid_id(value: str) -> bool:
    return bool(re.fullmatch(r"[a-z0-9][a-z0-9_]*", value or ""))


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    records = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        record = json.loads(line)
        record["_line_number"] = line_no
        records.append(record)
    return records


def validate_confidence(value: Any, min_confidence: float) -> bool:
    try:
        return float(value) >= min_confidence
    except (TypeError, ValueError):
        return False


def sanitize_record(record: Dict[str, Any], kb_dir: Path, min_confidence: float = 0.5) -> tuple[Dict[str, Any] | None, List[str]]:
    issues: List[str] = []
    line_no = record.get("_line_number")
    file_path = Path(record.get("file", ""))
    if not file_path.exists():
        file_path = kb_dir / file_path.name
    if not file_path.exists():
        return None, [f"line {line_no}: source file not found: {record.get('file')}"]

    content = file_path.read_text(encoding="utf-8")
    metadata = parse_frontmatter(content)
    anchor = record.get("anchor")
    if not anchor or not has_anchor(content, anchor):
        issues.append(f"line {line_no}: anchor not found in source file: {anchor}")
    for field in ("source_pdf", "page_start", "page_end", "content_hash", "section_text_hash"):
        if not record.get(field):
            issues.append(f"line {line_no}: missing candidate metadata: {field}")
    for field in ("source_pdf", "page_start", "page_end", "content_hash"):
        if not metadata.get(field):
            issues.append(f"line {line_no}: source markdown missing metadata: {field}")
    if issues:
        return None, issues

    section_text = record.get("section_text", "")
    kept_nodes = []
    node_ids = set()
    for idx, node in enumerate(record.get("nodes", [])):
        node_issues = []
        node_id = node.get("id")
        label = node.get("label")
        quote = node.get("evidence_quote", "")
        if not valid_id(node_id):
            node_issues.append(f"line {line_no}: node[{idx}] invalid id: {node_id}")
        if label not in ONTOLOGY_NODES:
            node_issues.append(f"line {line_no}: node[{idx}] invalid label: {label}")
        if not node.get("name"):
            node_issues.append(f"line {line_no}: node[{idx}] missing name")
        if not validate_confidence(node.get("confidence"), min_confidence):
            node_issues.append(f"line {line_no}: node[{idx}] confidence below minimum: {node.get('confidence')}")
        if not quote_in_text(quote, section_text):
            node_issues.append(f"line {line_no}: node[{idx}] evidence_quote not found in section text")
        if node_issues:
            issues.extend(node_issues)
        else:
            kept_nodes.append(node)
            node_ids.add(node_id)

    kept_edges = []
    for idx, edge in enumerate(record.get("edges", [])):
        edge_issues = []
        from_id = edge.get("from")
        to_id = edge.get("to")
        rel_type = edge.get("type")
        quote = edge.get("evidence_quote", "")
        if rel_type not in WHITELIST_EDGES:
            edge_issues.append(f"line {line_no}: edge[{idx}] invalid type: {rel_type}")
        if from_id not in node_ids or to_id not in node_ids:
            edge_issues.append(f"line {line_no}: edge[{idx}] endpoints must reference validated nodes in the same section record")
        if not validate_confidence(edge.get("confidence"), min_confidence):
            edge_issues.append(f"line {line_no}: edge[{idx}] confidence below minimum: {edge.get('confidence')}")
        if not quote_in_text(quote, section_text):
            edge_issues.append(f"line {line_no}: edge[{idx}] evidence_quote not found in section text")
        if edge_issues:
            issues.extend(edge_issues)
        else:
            kept_edges.append(edge)

    sanitized = dict(record)
    sanitized["nodes"] = kept_nodes
    sanitized["edges"] = kept_edges
    if not kept_nodes:
        return None, issues + [f"line {line_no}: no validated nodes remain"]
    return sanitized, issues


def validate_record(record: Dict[str, Any], kb_dir: Path, min_confidence: float = 0.5) -> List[str]:
    _, issues = sanitize_record(record, kb_dir, min_confidence)
    return issues


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate LLM entity candidate JSONL before import.")
    parser.add_argument("--candidates", required=True, help="Candidate JSONL path")
    parser.add_argument("--kb-dir", required=True, help="Path to markdown KB directory")
    parser.add_argument("--out", default="", help="Optional validated JSONL output path")
    parser.add_argument("--limit", type=int, default=10, help="Maximum sample issues in compact output")
    parser.add_argument("--min-confidence", type=float, default=0.5, help="Minimum node/edge confidence to accept")
    parser.add_argument("--fail-on-issues", action="store_true", help="Exit non-zero if issues are found")
    return parser.parse_args()


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
        args = parse_args()
        records = load_jsonl(Path(args.candidates))
        issue_items = []
        valid_records = []
        for record in records:
            sanitized, issues = sanitize_record(record, Path(args.kb_dir), args.min_confidence)
            if issues:
                for issue in issues:
                    issue_items.append({"line_number": record.get("_line_number"), "anchor": record.get("anchor"), "issue": issue})
            if sanitized:
                valid_records.append(sanitized)

        if args.out:
            out_path = Path(args.out)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            with out_path.open("w", encoding="utf-8", newline="\n") as f:
                for record in valid_records:
                    record.pop("_line_number", None)
                    f.write(json.dumps(record, ensure_ascii=False) + "\n")

        output = {
            "status": "success" if not issue_items else "issues_found",
            "records": len(records),
            "valid_records": len(valid_records),
            "issue_count": len(issue_items),
            "issues_sample": issue_items[: max(1, args.limit)],
            "validated_output": args.out or None,
        }
        print(json.dumps(output, indent=2, ensure_ascii=False))
        if args.fail_on_issues and issue_items:
            sys.exit(1)
    except Exception as exc:
        print(json.dumps({"status": "error", "error_code": type(exc).__name__, "message": str(exc)}, indent=2, ensure_ascii=False))
        sys.exit(1)


if __name__ == "__main__":
    main()
