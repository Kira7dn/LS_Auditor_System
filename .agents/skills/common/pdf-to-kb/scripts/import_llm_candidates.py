"""
import_llm_candidates.py
========================
Import validated LLM candidate entities/relations into Neo4j.

This script assumes candidates were already checked with validate_llm_candidates.py.
It keeps provenance on every node/edge: extractor, model, source anchor, page range,
content hash, section text hash, and evidence quote.

Usage:
  uv run C:/Users/kira7/.gemini/config/skills/pdf-to-kb/scripts/import_llm_candidates.py --candidates Projects/ESG/llm_candidates.valid.jsonl
"""
import argparse
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List

from neo4j import GraphDatabase

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from import_concept_map import WHITELIST_EDGES, load_env  # noqa: E402


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def candidates_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_aliases(path_value: str) -> Dict[str, str]:
    if not path_value:
        return {}
    path = Path(path_value)
    if not path.exists():
        raise FileNotFoundError(f"Alias file not found: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    aliases = data.get("aliases", data)
    if not isinstance(aliases, dict):
        raise ValueError("Alias file must contain an object or an 'aliases' object.")
    clean_aliases: Dict[str, str] = {}
    for source, target in aliases.items():
        if not isinstance(source, str) or not isinstance(target, str) or not source or not target:
            raise ValueError(f"Invalid alias entry: {source!r} -> {target!r}")
        if source == target:
            continue
        clean_aliases[source] = target
    return clean_aliases


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Import validated LLM candidates into Neo4j.")
    parser.add_argument("--candidates", required=True, help="Validated candidate JSONL path")
    parser.add_argument("--env", default=".env", help="Path to .env configuration file")
    parser.add_argument("--project-id", default="esg", help="Project scope for imported LLM graph")
    parser.add_argument("--collection-id", default="ghg_protocol", help="Collection scope for imported LLM graph")
    parser.add_argument("--source-id", default="ghg_protocol_corporate_standard", help="Source scope for imported LLM graph")
    parser.add_argument("--approved-only", action="store_true", help="Import only records/nodes/edges marked approved")
    parser.add_argument("--source-map-hash", default="", help="Optional source_map_hash to attach to imported LLM graph")
    parser.add_argument("--aliases", default="", help="Optional canonical alias JSON mapping LLM node ids to canonical Concept ids")
    parser.add_argument("--dry-run", action="store_true", help="Count import effects without writing to Neo4j")
    return parser.parse_args()


def is_approved(item: Dict[str, Any], approved_only: bool) -> bool:
    if not approved_only:
        return True
    return item.get("status") == "approved" or item.get("approved") is True


def summarize_records(records: List[Dict[str, Any]], aliases: Dict[str, str], approved_only: bool) -> Dict[str, int]:
    nodes_imported = 0
    nodes_aliased = 0
    edges_imported = 0
    skipped_records = 0
    for record in records:
        if approved_only and record.get("status") != "approved":
            skipped_records += 1
            continue
        imported_node_ids = set()
        for node in record.get("nodes", []):
            if not is_approved(node, approved_only):
                continue
            node_id = node["id"]
            canonical_id = aliases.get(node_id, node_id)
            imported_node_ids.add(canonical_id)
            if canonical_id != node_id:
                nodes_aliased += 1
            else:
                nodes_imported += 1
        for edge in record.get("edges", []):
            if not is_approved(edge, approved_only):
                continue
            if edge.get("type") not in WHITELIST_EDGES:
                continue
            from_id = aliases.get(edge.get("from"), edge.get("from"))
            to_id = aliases.get(edge.get("to"), edge.get("to"))
            if from_id in imported_node_ids and to_id in imported_node_ids:
                edges_imported += 1
    return {
        "skipped_records": skipped_records,
        "nodes_imported": nodes_imported,
        "nodes_aliased": nodes_aliased,
        "edges_imported": edges_imported,
    }


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
        args = parse_args()
        load_env(Path(args.env))

        uri = os.getenv("NEO4J_URI")
        user = os.getenv("NEO4J_USERNAME")
        password = os.getenv("NEO4J_PASSWORD")
        database = os.getenv("NEO4J_DATABASE", "neo4j")
        if not uri or not user or not password:
            raise ValueError("Missing Neo4j credentials in environment.")

        candidate_path = Path(args.candidates)
        records = load_jsonl(candidate_path)
        aliases = load_aliases(args.aliases)
        import_hash = candidates_hash(candidate_path)
        source_map_hash = args.source_map_hash or f"llm:{import_hash}"
        if args.dry_run:
            summary = summarize_records(records, aliases, args.approved_only)
            print(
                json.dumps(
                    {
                        "status": "success",
                        "dry_run": True,
                        "records": len(records),
                        **summary,
                        "project_id": args.project_id,
                        "collection_id": args.collection_id,
                        "source_id": args.source_id,
                        "source_map_hash": source_map_hash,
                        "alias_count": len(aliases),
                    },
                    indent=2,
                    ensure_ascii=False,
                )
            )
            return

        driver = GraphDatabase.driver(uri, auth=(user, password))
        nodes_imported = 0
        nodes_aliased = 0
        edges_imported = 0
        skipped_records = 0
        alias_warnings = []

        with driver.session(database=database) as session:
            session.run("CREATE CONSTRAINT concept_id_unique IF NOT EXISTS FOR (c:Concept) REQUIRE c.id IS UNIQUE")
            session.run("CREATE INDEX concept_project_id IF NOT EXISTS FOR (c:Concept) ON (c.project_id)")
            session.run("CREATE INDEX concept_project_collection IF NOT EXISTS FOR (c:Concept) ON (c.project_id, c.collection_id)")
            session.run("CREATE INDEX concept_project_source IF NOT EXISTS FOR (c:Concept) ON (c.project_id, c.source_id)")

            for record in records:
                if args.approved_only and record.get("status") != "approved":
                    skipped_records += 1
                    continue

                doc_id = record["doc_id"]
                anchor = record["anchor"]
                file_path = str(Path(record["file"]).resolve())
                file_uri = f"{Path(record['file']).resolve().as_uri()}#{anchor}"
                common = {
                    "doc_id": doc_id,
                    "anchor": anchor,
                    "file_path": file_path,
                    "file_uri": file_uri,
                    "project_id": args.project_id,
                    "collection_id": args.collection_id,
                    "source_id": record.get("source_id") or args.source_id,
                    "source_pdf": record.get("source_pdf"),
                    "page_start": record.get("page_start"),
                    "page_end": record.get("page_end"),
                    "content_hash": record.get("content_hash"),
                    "section_text_hash": record.get("section_text_hash"),
                    "extractor": record.get("extractor", "openai"),
                    "model": record.get("model", ""),
                    "source_map_hash": source_map_hash,
                }

                imported_node_ids = set()
                for node in record.get("nodes", []):
                    if not is_approved(node, args.approved_only):
                        continue
                    node_id = node["id"]
                    canonical_id = aliases.get(node_id, node_id)
                    if canonical_id != node_id:
                        exists = session.run(
                            """
                            MATCH (c:Concept {id: $id})
                            WHERE ($project_id = '' OR c.project_id = $project_id)
                            RETURN count(c) AS count
                            """,
                            id=canonical_id,
                            project_id=args.project_id,
                        ).single()["count"]
                        if not exists:
                            alias_warnings.append(f"Alias target not found, skipped node {node_id} -> {canonical_id}")
                            continue
                        imported_node_ids.add(canonical_id)
                        nodes_aliased += 1
                        continue
                    label = node["label"]
                    session.run(
                        f"MERGE (c:Concept {{id: $id}}) "
                        f"SET c.name = $name, c.doc_id = $doc_id, c.anchor = $anchor, "
                        f"    c.project_id = $project_id, c.collection_id = $collection_id, c.source_id = $source_id, "
                        f"    c.file_path = $file_path, c.file_uri = $file_uri, "
                        f"    c.source_pdf = $source_pdf, c.page_start = $page_start, c.page_end = $page_end, "
                        f"    c.content_hash = $content_hash, c.section_text_hash = $section_text_hash, "
                        f"    c.extractor = $extractor, c.model = $model, c.source_map_hash = $source_map_hash, "
                        f"    c.llm_generated = true, c.evidence_quote = $evidence_quote, "
                        f"    c.confidence = $confidence, c.rationale_short = $rationale_short "
                        f"WITH c SET c:{label} RETURN c",
                        id=node_id,
                        name=node.get("name"),
                        evidence_quote=node.get("evidence_quote"),
                        confidence=node.get("confidence"),
                        rationale_short=node.get("rationale_short"),
                        **common,
                    )
                    imported_node_ids.add(node_id)
                    nodes_imported += 1

                for edge in record.get("edges", []):
                    if not is_approved(edge, args.approved_only):
                        continue
                    rel_type = edge.get("type")
                    if rel_type not in WHITELIST_EDGES:
                        continue
                    from_id = aliases.get(edge.get("from"), edge.get("from"))
                    to_id = aliases.get(edge.get("to"), edge.get("to"))
                    if from_id not in imported_node_ids or to_id not in imported_node_ids:
                        continue
                    session.run(
                        f"MATCH (a:Concept {{id: $from_id}}) "
                        f"MATCH (b:Concept {{id: $to_id}}) "
                        f"MERGE (a)-[r:{rel_type}]->(b) "
                        f"SET r.project_id = $project_id, r.collection_id = $collection_id, r.source_id = $source_id, "
                        f"    r.source_map_hash = $source_map_hash, r.llm_generated = true, "
                        f"    r.extractor = $extractor, r.model = $model, "
                        f"    r.evidence_quote = $evidence_quote, r.confidence = $confidence, "
                        f"    r.rationale_short = $rationale_short "
                        f"RETURN r",
                        from_id=from_id,
                        to_id=to_id,
                        project_id=args.project_id,
                        collection_id=args.collection_id,
                        source_id=record.get("source_id") or args.source_id,
                        source_map_hash=source_map_hash,
                        extractor=record.get("extractor", "openai"),
                        model=record.get("model", ""),
                        evidence_quote=edge.get("evidence_quote"),
                        confidence=edge.get("confidence"),
                        rationale_short=edge.get("rationale_short"),
                    )
                    edges_imported += 1

        driver.close()
        print(
            json.dumps(
                {
                    "status": "success",
                    "records": len(records),
                    "skipped_records": skipped_records,
                    "nodes_imported": nodes_imported,
                    "nodes_aliased": nodes_aliased,
                    "edges_imported": edges_imported,
                    "project_id": args.project_id,
                    "collection_id": args.collection_id,
                    "source_id": args.source_id,
                    "source_map_hash": source_map_hash,
                    "alias_count": len(aliases),
                    "alias_warnings_sample": alias_warnings[:10],
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
