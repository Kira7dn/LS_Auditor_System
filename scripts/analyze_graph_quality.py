"""
analyze_graph_quality.py
========================
Read-only Neo4j graph quality report for the PDF-to-KB legal RAG pipeline.

Outputs compact JSON to stdout and writes:
  - Projects/ESG/graph/quality_reports/graph_quality_report.json
  - Projects/ESG/graph/quality_reports/graph_quality_report.md
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

from neo4j import GraphDatabase


GENERIC_TERMS = {
    "activity",
    "activities",
    "approach",
    "boundary",
    "calculation",
    "company",
    "data",
    "emission",
    "emissions",
    "factor",
    "ghg",
    "ghg emission",
    "ghg emissions",
    "information",
    "inventory",
    "method",
    "methodology",
    "process",
    "report",
    "reporting",
    "requirement",
    "requirements",
    "source",
    "sources",
    "standard",
}

SUSPICIOUS_BIDIRECTIONAL_TYPES = {
    "APPLIES_TO",
    "CHECKS_REQUIREMENT",
    "CONTAINS",
    "DEFINES",
    "EVIDENCES",
    "REQUIRES",
    "REQUIRES_ACTIVITY_DATA",
    "REQUIRES_EVIDENCE",
    "SUPPORTS_CLAIM",
    "USES_FACTOR",
    "USES_FORMULA",
}


def load_env(env_path: Path) -> None:
    if not env_path.exists():
        return
    with env_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                os.environ[key] = value.strip("'\"")


def normalize_text(value: str | None) -> str:
    value = value or ""
    value = value.casefold()
    value = value.translate(str.maketrans({"“": '"', "”": '"', "‘": "'", "’": "'"}))
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def token_set(value: str) -> set[str]:
    return {token for token in normalize_text(value).split() if token}


def similarity(a: str, b: str) -> float:
    norm_a = normalize_text(a)
    norm_b = normalize_text(b)
    if not norm_a or not norm_b:
        return 0.0
    seq = SequenceMatcher(None, norm_a, norm_b).ratio()
    tokens_a = set(norm_a.split())
    tokens_b = set(norm_b.split())
    jaccard = len(tokens_a & tokens_b) / len(tokens_a | tokens_b) if tokens_a and tokens_b else 0.0
    return max(seq, jaccard)


def compact(items: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    return items[: max(0, limit)]


def node_label(node: dict[str, Any]) -> str:
    labels = [label for label in node.get("labels", []) if label != "Concept"]
    return labels[0] if labels else "Concept"


def is_llm(node: dict[str, Any]) -> bool:
    return bool(node.get("llm_generated")) or str(node.get("source_map_hash") or "").startswith("llm:")


def has_citation_gap(node: dict[str, Any]) -> bool:
    if node_label(node) == "Chapter" and not node.get("anchor"):
        return False
    required = ("file_uri", "anchor", "source_pdf", "page_start", "page_end", "content_hash")
    return any(node.get(field) in (None, "") for field in required)


def fetch_graph(
    driver: Any,
    database: str,
    project_id: str = "",
    collection_id: str = "",
    source_id: str = "",
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    with driver.session(database=database) as session:
        nodes = session.run(
            """
            MATCH (c:Concept)
            WHERE ($project_id = '' OR c.project_id = $project_id)
              AND ($collection_id = '' OR c.collection_id = $collection_id)
              AND ($source_id = '' OR c.source_id = $source_id)
            RETURN c.id AS id,
                   c.name AS name,
                   labels(c) AS labels,
                   c.doc_id AS doc_id,
                   c.anchor AS anchor,
                   c.file_uri AS file_uri,
                   c.source_pdf AS source_pdf,
                   c.page_start AS page_start,
                   c.page_end AS page_end,
                   c.content_hash AS content_hash,
                   coalesce(c.llm_generated, false) AS llm_generated,
                   coalesce(c.auto_generated, false) AS auto_generated,
                   c.project_id AS project_id,
                   c.collection_id AS collection_id,
                   c.source_id AS source_id,
                   c.source_map_hash AS source_map_hash,
                   c.confidence AS confidence
            ORDER BY c.id
            """,
            project_id=project_id,
            collection_id=collection_id,
            source_id=source_id,
        ).data()
        relationships = session.run(
            """
            MATCH (a:Concept)-[r]->(b:Concept)
            WHERE ($project_id = '' OR r.project_id = $project_id)
              AND ($collection_id = '' OR r.collection_id = $collection_id)
              AND ($source_id = '' OR r.source_id = $source_id)
            RETURN a.id AS from_id,
                   a.name AS from_name,
                   b.id AS to_id,
                   b.name AS to_name,
                   type(r) AS type,
                   coalesce(r.llm_generated, false) AS llm_generated,
                   coalesce(r.auto_generated, false) AS auto_generated,
                   r.project_id AS project_id,
                   r.collection_id AS collection_id,
                   r.source_id AS source_id,
                   r.source_map_hash AS source_map_hash,
                   r.confidence AS confidence,
                   r.evidence_quote AS evidence_quote
            ORDER BY type(r), a.id, b.id
            """,
            project_id=project_id,
            collection_id=collection_id,
            source_id=source_id,
        ).data()
    return nodes, relationships


def analyze(nodes: list[dict[str, Any]], relationships: list[dict[str, Any]], similar_threshold: float) -> dict[str, Any]:
    by_id = {node["id"]: node for node in nodes}
    degree = Counter()
    outgoing = Counter()
    incoming = Counter()
    for rel in relationships:
        degree[rel["from_id"]] += 1
        degree[rel["to_id"]] += 1
        outgoing[rel["from_id"]] += 1
        incoming[rel["to_id"]] += 1

    exact_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for node in nodes:
        key = normalize_text(node.get("name") or node.get("id"))
        if key:
            exact_groups[key].append(node)

    exact_duplicate_names = []
    for key, group in exact_groups.items():
        if len(group) <= 1:
            continue
        exact_duplicate_names.append(
            {
                "normalized_name": key,
                "count": len(group),
                "nodes": [
                    {
                        "id": node["id"],
                        "name": node.get("name"),
                        "label": node_label(node),
                        "llm_generated": is_llm(node),
                        "degree": degree[node["id"]],
                    }
                    for node in sorted(group, key=lambda item: item["id"])
                ],
            }
        )
    exact_duplicate_names.sort(key=lambda item: (-item["count"], item["normalized_name"]))

    similar_name_candidates = []
    sorted_nodes = sorted(nodes, key=lambda node: node["id"])
    for idx, left in enumerate(sorted_nodes):
        for right in sorted_nodes[idx + 1 :]:
            if left["id"] == right["id"]:
                continue
            score = similarity(left.get("name") or left["id"], right.get("name") or right["id"])
            if score >= similar_threshold and normalize_text(left.get("name")) != normalize_text(right.get("name")):
                similar_name_candidates.append(
                    {
                        "score": round(score, 3),
                        "left": {
                            "id": left["id"],
                            "name": left.get("name"),
                            "label": node_label(left),
                            "llm_generated": is_llm(left),
                            "degree": degree[left["id"]],
                        },
                        "right": {
                            "id": right["id"],
                            "name": right.get("name"),
                            "label": node_label(right),
                            "llm_generated": is_llm(right),
                            "degree": degree[right["id"]],
                        },
                    }
                )
    similar_name_candidates.sort(key=lambda item: (-item["score"], item["left"]["id"], item["right"]["id"]))

    generic_llm_nodes = []
    for node in nodes:
        if not is_llm(node):
            continue
        name_norm = normalize_text(node.get("name") or node["id"])
        id_norm = normalize_text(node["id"].replace("_", " "))
        tokens = token_set(node.get("name") or node["id"])
        if name_norm in GENERIC_TERMS or id_norm in GENERIC_TERMS or (len(tokens) <= 2 and degree[node["id"]] >= 2):
            generic_llm_nodes.append(
                {
                    "id": node["id"],
                    "name": node.get("name"),
                    "label": node_label(node),
                    "degree": degree[node["id"]],
                    "incoming": incoming[node["id"]],
                    "outgoing": outgoing[node["id"]],
                    "source_map_hash": node.get("source_map_hash"),
                }
            )
    generic_llm_nodes.sort(key=lambda item: (-item["degree"], item["id"]))

    expert_nodes = [node for node in nodes if not is_llm(node)]
    llm_nodes = [node for node in nodes if is_llm(node)]
    expert_llm_overlaps = []
    for llm_node in llm_nodes:
        best = None
        for expert_node in expert_nodes:
            score = similarity(llm_node.get("name") or llm_node["id"], expert_node.get("name") or expert_node["id"])
            if score >= similar_threshold and (best is None or score > best["score"]):
                best = {
                    "score": round(score, 3),
                    "llm_node": {
                        "id": llm_node["id"],
                        "name": llm_node.get("name"),
                        "label": node_label(llm_node),
                        "degree": degree[llm_node["id"]],
                    },
                    "expert_node": {
                        "id": expert_node["id"],
                        "name": expert_node.get("name"),
                        "label": node_label(expert_node),
                        "degree": degree[expert_node["id"]],
                    },
                }
        if best:
            expert_llm_overlaps.append(best)
    expert_llm_overlaps.sort(key=lambda item: (-item["score"], item["llm_node"]["id"]))

    orphan_requirements = []
    for node in nodes:
        if "Requirement" in node.get("labels", []) and degree[node["id"]] == 0:
            orphan_requirements.append({"id": node["id"], "name": node.get("name"), "llm_generated": is_llm(node)})
    orphan_requirements.sort(key=lambda item: (item["llm_generated"], item["id"]))

    low_confidence_edges = []
    for rel in relationships:
        confidence = rel.get("confidence")
        if rel.get("llm_generated") and confidence is not None and float(confidence) < 0.7:
            low_confidence_edges.append(
                {
                    "from": rel["from_id"],
                    "type": rel["type"],
                    "to": rel["to_id"],
                    "confidence": confidence,
                    "evidence_quote": rel.get("evidence_quote"),
                }
            )
    low_confidence_edges.sort(key=lambda item: (item["confidence"], item["from"], item["type"], item["to"]))

    pair_types = defaultdict(list)
    for rel in relationships:
        pair_types[(rel["from_id"], rel["to_id"], rel["type"])].append(rel)
    bidirectional_edges = []
    seen = set()
    for (from_id, to_id, rel_type), rels in pair_types.items():
        reverse_key = (to_id, from_id, rel_type)
        if reverse_key not in pair_types or rel_type not in SUSPICIOUS_BIDIRECTIONAL_TYPES:
            continue
        pair_key = tuple(sorted([from_id, to_id])) + (rel_type,)
        if pair_key in seen:
            continue
        seen.add(pair_key)
        bidirectional_edges.append(
            {
                "type": rel_type,
                "left": {"id": from_id, "name": by_id.get(from_id, {}).get("name")},
                "right": {"id": to_id, "name": by_id.get(to_id, {}).get("name")},
                "forward_count": len(rels),
                "reverse_count": len(pair_types[reverse_key]),
                "llm_involved": any(rel.get("llm_generated") for rel in rels + pair_types[reverse_key]),
            }
        )
    bidirectional_edges.sort(key=lambda item: (not item["llm_involved"], item["type"], item["left"]["id"]))

    citation_gaps = [
        {
            "id": node["id"],
            "name": node.get("name"),
            "label": node_label(node),
            "missing_fields": [
                field
                for field in ("file_uri", "anchor", "source_pdf", "page_start", "page_end", "content_hash")
                if node.get(field) in (None, "")
            ],
        }
        for node in nodes
        if has_citation_gap(node)
    ]
    citation_gaps.sort(key=lambda item: item["id"])

    top_degree_nodes = [
        {
            "id": node["id"],
            "name": node.get("name"),
            "label": node_label(node),
            "degree": degree[node["id"]],
            "incoming": incoming[node["id"]],
            "outgoing": outgoing[node["id"]],
            "llm_generated": is_llm(node),
        }
        for node in nodes
    ]
    top_degree_nodes.sort(key=lambda item: (-item["degree"], item["id"]))

    labels = Counter(node_label(node) for node in nodes)
    rel_types = Counter(rel["type"] for rel in relationships)

    return {
        "summary": {
            "node_count": len(nodes),
            "relationship_count": len(relationships),
            "llm_node_count": sum(1 for node in nodes if is_llm(node)),
            "auto_node_count": sum(1 for node in nodes if node.get("auto_generated")),
            "llm_relationship_count": sum(1 for rel in relationships if rel.get("llm_generated")),
            "auto_relationship_count": sum(1 for rel in relationships if rel.get("auto_generated")),
            "citation_gap_count": len(citation_gaps),
            "exact_duplicate_name_group_count": len(exact_duplicate_names),
            "similar_name_candidate_count": len(similar_name_candidates),
            "generic_llm_node_count": len(generic_llm_nodes),
            "expert_llm_overlap_count": len(expert_llm_overlaps),
            "orphan_requirement_count": len(orphan_requirements),
            "bidirectional_edge_count": len(bidirectional_edges),
            "low_confidence_edge_count": len(low_confidence_edges),
        },
        "node_label_distribution": dict(sorted(labels.items())),
        "relationship_type_distribution": dict(sorted(rel_types.items())),
        "exact_duplicate_names": exact_duplicate_names,
        "similar_name_candidates": similar_name_candidates,
        "generic_llm_nodes": generic_llm_nodes,
        "expert_llm_overlaps": expert_llm_overlaps,
        "orphan_requirements": orphan_requirements,
        "bidirectional_edges": bidirectional_edges,
        "low_confidence_edges": low_confidence_edges,
        "citation_gaps": citation_gaps,
        "top_degree_nodes": top_degree_nodes,
    }


def render_markdown(report: dict[str, Any], sample_limit: int) -> str:
    summary = report["summary"]
    lines = [
        "# Graph Quality Report",
        "",
        f"Generated at: {report['generated_at']}",
        "",
        "## Summary",
        "",
        "| Metric | Value |",
        "|---|---:|",
    ]
    for key, value in summary.items():
        lines.append(f"| `{key}` | {value} |")

    def add_section(title: str, items: list[dict[str, Any]], formatter: Any) -> None:
        lines.extend(["", f"## {title}", ""])
        if not items:
            lines.append("No issues found.")
            return
        for item in items[:sample_limit]:
            lines.append(formatter(item))

    add_section(
        "Exact Duplicate Names",
        report["exact_duplicate_names"],
        lambda item: f"- `{item['normalized_name']}` ({item['count']} nodes): "
        + ", ".join(f"`{node['id']}`" for node in item["nodes"][:8]),
    )
    add_section(
        "Similar Name Candidates",
        report["similar_name_candidates"],
        lambda item: f"- score `{item['score']}`: `{item['left']['id']}` ({item['left']['name']}) <-> "
        f"`{item['right']['id']}` ({item['right']['name']})",
    )
    add_section(
        "Generic LLM Nodes",
        report["generic_llm_nodes"],
        lambda item: f"- `{item['id']}` ({item['name']}), label `{item['label']}`, degree `{item['degree']}`",
    )
    add_section(
        "Expert vs LLM Overlaps",
        report["expert_llm_overlaps"],
        lambda item: f"- score `{item['score']}`: LLM `{item['llm_node']['id']}` ({item['llm_node']['name']}) -> "
        f"expert `{item['expert_node']['id']}` ({item['expert_node']['name']})",
    )
    add_section(
        "Orphan Requirements",
        report["orphan_requirements"],
        lambda item: f"- `{item['id']}` ({item['name']}), llm_generated=`{item['llm_generated']}`",
    )
    add_section(
        "Suspicious Bidirectional Edges",
        report["bidirectional_edges"],
        lambda item: f"- `{item['type']}` between `{item['left']['id']}` and `{item['right']['id']}`, "
        f"llm_involved=`{item['llm_involved']}`",
    )
    add_section(
        "Citation Gaps",
        report["citation_gaps"],
        lambda item: f"- `{item['id']}` missing: " + ", ".join(f"`{field}`" for field in item["missing_fields"]),
    )
    add_section(
        "Top Degree Nodes",
        report["top_degree_nodes"],
        lambda item: f"- `{item['id']}` ({item['name']}), degree `{item['degree']}`, "
        f"in `{item['incoming']}`, out `{item['outgoing']}`, llm=`{item['llm_generated']}`",
    )
    lines.extend(
        [
            "",
            "## Recommended Next Actions",
            "",
            "1. Review `expert_llm_overlaps` and create `Projects/ESG/graph/canonical_aliases.json` for safe merges.",
            "2. Inspect `generic_llm_nodes` before running more LLM extraction.",
            "3. Resolve suspicious bidirectional edges by edge-type direction rules.",
            "4. Keep `citation_gap_count` at `0` before using the graph for legal-grade answers.",
        ]
    )
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze Neo4j graph quality for legal-grade RAG hardening.")
    parser.add_argument("--env", default=".env", help="Path to .env with Neo4j credentials")
    parser.add_argument("--project-id", default="esg", help="Restrict analysis to project_id; use empty string to disable")
    parser.add_argument("--collection-id", default="", help="Restrict analysis to collection_id")
    parser.add_argument("--source-id", default="", help="Restrict analysis to source_id")
    parser.add_argument("--out-dir", default="Projects/ESG/graph/quality_reports", help="Directory for graph_quality_report.json/.md")
    parser.add_argument("--sample-limit", type=int, default=20, help="Items included in compact stdout/Markdown sections")
    parser.add_argument("--similar-threshold", type=float, default=0.86, help="Name similarity threshold for duplicate candidates")
    parser.add_argument("--full-json", action="store_true", help="Print full report JSON to stdout")
    return parser.parse_args()


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

        with GraphDatabase.driver(uri, auth=(user, password)) as driver:
            driver.verify_connectivity()
            nodes, relationships = fetch_graph(driver, database, args.project_id, args.collection_id, args.source_id)

        report = analyze(nodes, relationships, args.similar_threshold)
        report["status"] = "success"
        report["generated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        report["neo4j_uri"] = uri
        report["database"] = database
        report["scope"] = {
            "project_id": args.project_id,
            "collection_id": args.collection_id,
            "source_id": args.source_id,
        }

        out_dir = Path(args.out_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        json_path = out_dir / "graph_quality_report.json"
        md_path = out_dir / "graph_quality_report.md"
        json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
        md_path.write_text(render_markdown(report, args.sample_limit), encoding="utf-8", newline="\n")

        if args.full_json:
            stdout_report = report
        else:
            stdout_report = {
                "status": "success",
                "summary": report["summary"],
                "report_json": str(json_path),
                "report_markdown": str(md_path),
                "samples": {
                    "generic_llm_nodes": compact(report["generic_llm_nodes"], args.sample_limit),
                    "expert_llm_overlaps": compact(report["expert_llm_overlaps"], args.sample_limit),
                    "bidirectional_edges": compact(report["bidirectional_edges"], args.sample_limit),
                    "citation_gaps": compact(report["citation_gaps"], args.sample_limit),
                },
            }
        print(json.dumps(stdout_report, ensure_ascii=False, indent=2))
    except Exception as exc:
        print(json.dumps({"status": "error", "error_code": type(exc).__name__, "message": str(exc)}, ensure_ascii=False, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
