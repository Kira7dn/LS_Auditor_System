"""
apply_canonical_aliases.py
==========================
Dry-run or apply conservative Concept node canonical aliases in Neo4j.

Default behavior is read-only dry-run. Use --apply to migrate relationships and
delete alias source nodes.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

from neo4j import GraphDatabase


REL_TYPE_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")


def load_env(env_path: Path) -> None:
    if not env_path.exists():
        return
    with env_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                os.environ[key] = value.strip("'\"")


def load_aliases(path: Path) -> dict[str, str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    aliases = data.get("aliases", data)
    if not isinstance(aliases, dict):
        raise ValueError("Alias file must contain an object or an 'aliases' object.")
    clean: dict[str, str] = {}
    for source, target in aliases.items():
        if not isinstance(source, str) or not isinstance(target, str) or not source or not target:
            raise ValueError(f"Invalid alias entry: {source!r} -> {target!r}")
        if source != target:
            clean[source] = target
    return clean


def inspect_alias(tx: Any, source: str, target: str, project_id: str) -> dict[str, Any]:
    row = tx.run(
        """
        OPTIONAL MATCH (s:Concept {id: $source})
        WHERE $project_id = '' OR s.project_id = $project_id
        OPTIONAL MATCH (t:Concept {id: $target})
        WHERE $project_id = '' OR t.project_id = $project_id
        WITH s, t
        OPTIONAL MATCH (s)-[out]->()
        WITH s, t, count(out) AS outgoing
        OPTIONAL MATCH ()-[inc]->(s)
        WITH s, t, outgoing, count(inc) AS incoming
        RETURN s.id AS source_id,
               s.name AS source_name,
               labels(s) AS source_labels,
               t.id AS target_id,
               t.name AS target_name,
               labels(t) AS target_labels,
               outgoing,
               incoming
        """,
        source=source,
        target=target,
        project_id=project_id,
    ).single()
    return dict(row) if row else {}


def rel_rows(tx: Any, source: str, project_id: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    outgoing = tx.run(
        """
        MATCH (s:Concept {id: $source})-[r]->(other:Concept)
        WHERE $project_id = '' OR s.project_id = $project_id
        RETURN type(r) AS type, properties(r) AS props, other.id AS other_id
        """,
        source=source,
        project_id=project_id,
    ).data()
    incoming = tx.run(
        """
        MATCH (other:Concept)-[r]->(s:Concept {id: $source})
        WHERE $project_id = '' OR s.project_id = $project_id
        RETURN type(r) AS type, properties(r) AS props, other.id AS other_id
        """,
        source=source,
        project_id=project_id,
    ).data()
    return outgoing, incoming


def merge_relationship(
    tx: Any,
    from_id: str,
    rel_type: str,
    to_id: str,
    props: dict[str, Any],
    source: str,
    project_id: str,
) -> None:
    if not REL_TYPE_RE.fullmatch(rel_type):
        raise ValueError(f"Unsafe relationship type: {rel_type}")
    tx.run(
        f"""
        MATCH (a:Concept {{id: $from_id}})
        MATCH (b:Concept {{id: $to_id}})
        WHERE ($project_id = '' OR a.project_id = $project_id)
          AND ($project_id = '' OR b.project_id = $project_id)
        MERGE (a)-[r:{rel_type}]->(b)
        SET r += $props,
            r.canonicalized = true,
            r.canonical_alias_source = $source
        """,
        from_id=from_id,
        to_id=to_id,
        props=props,
        source=source,
        project_id=project_id,
    ).consume()


def apply_alias(tx: Any, source: str, target: str, project_id: str) -> dict[str, Any]:
    info = inspect_alias(tx, source, target, project_id)
    if not info.get("source_id") or not info.get("target_id"):
        return {"source": source, "target": target, "status": "skipped_missing_node", **info}

    outgoing, incoming = rel_rows(tx, source, project_id)
    migrated_outgoing = 0
    migrated_incoming = 0
    skipped_self_loops = 0

    for rel in outgoing:
        other_id = rel["other_id"]
        if other_id == target:
            skipped_self_loops += 1
            continue
        merge_relationship(tx, target, rel["type"], other_id, rel.get("props") or {}, source, project_id)
        migrated_outgoing += 1

    for rel in incoming:
        other_id = rel["other_id"]
        if other_id == target:
            skipped_self_loops += 1
            continue
        merge_relationship(tx, other_id, rel["type"], target, rel.get("props") or {}, source, project_id)
        migrated_incoming += 1

    tx.run(
        """
        MATCH (target:Concept {id: $target})
        WHERE $project_id = '' OR target.project_id = $project_id
        SET target.alias_ids =
          CASE
            WHEN $source IN coalesce(target.alias_ids, []) THEN target.alias_ids
            ELSE coalesce(target.alias_ids, []) + $source
          END
        WITH target
        MATCH (source:Concept {id: $source})
        WHERE $project_id = '' OR source.project_id = $project_id
        DETACH DELETE source
        """,
        source=source,
        target=target,
        project_id=project_id,
    ).consume()
    return {
        "source": source,
        "target": target,
        "status": "applied",
        "migrated_outgoing": migrated_outgoing,
        "migrated_incoming": migrated_incoming,
        "skipped_self_loops": skipped_self_loops,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Dry-run/apply canonical aliases for Neo4j Concept nodes.")
    parser.add_argument("--aliases", default="Projects/ESG/graph/canonical_aliases.json", help="Canonical aliases JSON path")
    parser.add_argument("--env", default=".env", help="Path to .env with Neo4j credentials")
    parser.add_argument("--project-id", default="esg", help="Restrict alias operation to project_id; use empty string to disable")
    parser.add_argument("--apply", action="store_true", help="Actually migrate relationships and delete alias source nodes")
    parser.add_argument("--out", default="Projects/ESG/graph/import_reports/canonical_aliases_apply_report.json", help="Report JSON path")
    return parser.parse_args()


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
        args = parse_args()
        load_env(Path(args.env))
        aliases = load_aliases(Path(args.aliases))

        uri = os.getenv("NEO4J_URI")
        user = os.getenv("NEO4J_USERNAME")
        password = os.getenv("NEO4J_PASSWORD")
        database = os.getenv("NEO4J_DATABASE", "neo4j")
        if not uri or not user or not password:
            raise ValueError("Missing Neo4j credentials in environment.")

        results = []
        with GraphDatabase.driver(uri, auth=(user, password)) as driver:
            driver.verify_connectivity()
            with driver.session(database=database) as session:
                if args.apply:
                    for source, target in aliases.items():
                        results.append(session.execute_write(apply_alias, source, target, args.project_id))
                else:
                    for source, target in aliases.items():
                        info = session.execute_read(inspect_alias, source, target, args.project_id)
                        results.append({"source": source, "target": target, "status": "dry_run", **info})

        report = {
            "status": "success",
            "mode": "apply" if args.apply else "dry_run",
            "project_id": args.project_id,
            "alias_count": len(aliases),
            "results": results,
        }
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
        print(json.dumps(report, ensure_ascii=False, indent=2))
    except Exception as exc:
        print(json.dumps({"status": "error", "error_code": type(exc).__name__, "message": str(exc)}, ensure_ascii=False, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
