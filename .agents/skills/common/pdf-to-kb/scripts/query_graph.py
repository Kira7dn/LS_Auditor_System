"""
query_graph.py
==============
Deterministic graph and local-text retrieval tool for pdf-to-kb.

The tool keeps the legacy --id / --search interface, adds bounded multi-hop
graph traversal, and uses an in-memory SQLite FTS index for local Markdown
retrieval. It returns JSON with explicit citations for legal-grade RAG use.

Usage:
  uv run C:/Users/kira7/.gemini/config/skills/pdf-to-kb/scripts/query_graph.py --id scope_3
  uv run C:/Users/kira7/.gemini/config/skills/pdf-to-kb/scripts/query_graph.py --search "scope 3" --mode search
  uv run C:/Users/kira7/.gemini/config/skills/pdf-to-kb/scripts/query_graph.py --id scope_3 --depth 2 --mode paths
"""
import argparse
import json
import os
import re
import sqlite3
import sys
from pathlib import Path
from typing import Any, Dict, List

from neo4j import GraphDatabase

REPO_SCRIPTS = Path(__file__).parent
if REPO_SCRIPTS.exists() and str(REPO_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(REPO_SCRIPTS))


def load_env(env_path: Path) -> None:
    if not env_path.exists():
        return
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ[k] = v.strip("'\"")


def clamp_depth(depth: int) -> int:
    return max(1, min(depth, 4))


def node_payload(node: Any) -> Dict[str, Any]:
    labels = [label for label in node.labels if label != "Concept"]
    return {
        "id": node.get("id"),
        "name": node.get("name"),
        "labels": labels,
        "file_path": node.get("file_path"),
        "file_uri": node.get("file_uri"),
        "anchor": node.get("anchor"),
        "source_pdf": node.get("source_pdf"),
        "project_id": node.get("project_id"),
        "collection_id": node.get("collection_id"),
        "source_id": node.get("source_id"),
        "page_start": node.get("page_start"),
        "page_end": node.get("page_end"),
        "content_hash": node.get("content_hash"),
    }


def citation_from_node(node: Any, matched_text: str = "") -> Dict[str, Any]:
    citation = {
        "id": node.get("id"),
        "name": node.get("name"),
        "file_path": node.get("file_path"),
        "file_uri": node.get("file_uri"),
        "anchor": node.get("anchor"),
        "source_pdf": node.get("source_pdf"),
        "project_id": node.get("project_id"),
        "collection_id": node.get("collection_id"),
        "source_id": node.get("source_id"),
        "page_start": node.get("page_start"),
        "page_end": node.get("page_end"),
        "content_hash": node.get("content_hash"),
        "matched_text": matched_text,
    }
    citation["missing_fields"] = citation_missing_fields(citation)
    return citation


def citation_missing_fields(citation: Dict[str, Any]) -> List[str]:
    required = ("file_uri", "anchor", "source_pdf", "page_start", "page_end", "content_hash")
    return [field for field in required if citation.get(field) in (None, "")]


def nearest_anchor_by_line(lines: List[str]) -> Dict[int, str]:
    anchors: Dict[int, str] = {}
    current_anchor = ""
    anchor_re = re.compile(r"<a\s+[^>]*id\s*=\s*['\"]([^'\"]+)['\"][^>]*>\s*</a>", re.IGNORECASE)
    for idx, line in enumerate(lines, start=1):
        match = anchor_re.search(line)
        if match:
            current_anchor = match.group(1)
        anchors[idx] = current_anchor
    return anchors


def parse_frontmatter(content: str) -> Dict[str, Any]:
    if not content.startswith("---\n"):
        return {}
    end = content.find("\n---", 4)
    if end == -1:
        return {}
    metadata: Dict[str, Any] = {}
    for raw_line in content[4:end].splitlines():
        if ":" not in raw_line:
            continue
        key, value = raw_line.split(":", 1)
        value = value.strip().strip("'\"")
        metadata[key.strip()] = int(value) if value.isdigit() else value
    return metadata


def compact_graph_results(results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    compacted = []
    for result in results:
        citation = citation_from_node(result)
        stale_relationship_count = sum(
            1 for rel in result.get("relationships", []) if any(rel.get("stale_path", []))
        )
        compacted.append(
            {
                "id": result.get("id"),
                "name": result.get("name"),
                "labels": result.get("labels", []),
                "file_uri": result.get("file_uri"),
                "anchor": result.get("anchor"),
                "project_id": result.get("project_id"),
                "collection_id": result.get("collection_id"),
                "source_id": result.get("source_id"),
                "relationship_count": len(result.get("relationships", [])),
                "path_count": len(result.get("paths", [])),
                "stale_relationship_count": stale_relationship_count,
                "citation_missing_fields": citation["missing_fields"],
            }
        )
    return compacted


def compact_local_matches(matches: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return [
        {
            "file": match.get("file"),
            "line_number": match.get("line_number"),
            "content": match.get("content"),
            "score": match.get("score"),
            "anchor": match.get("citation", {}).get("anchor"),
        }
        for match in matches
    ]


def compact_citations(citations: List[Dict[str, Any]], limit: int) -> List[Dict[str, Any]]:
    keys = (
        "id",
        "name",
        "file_uri",
        "anchor",
        "source_pdf",
        "project_id",
        "collection_id",
        "source_id",
        "page_start",
        "page_end",
        "content_hash",
        "matched_text",
        "missing_fields",
    )
    return [{key: citation.get(key) for key in keys if citation.get(key) not in (None, "")} for citation in citations[:limit]]


def compact_pdf_citations(pdf_citations: List[Dict[str, Any]], limit: int) -> List[Dict[str, Any]]:
    keys = (
        "anchor",
        "source_pdf",
        "page_number",
        "bbox",
        "matched_pdf_text",
        "match_type",
        "confidence",
        "ambiguous",
        "highlight_uri",
        "highlight_path",
    )
    return [{key: citation.get(key) for key in keys if citation.get(key) not in (None, "")} for citation in pdf_citations[:limit]]


def evidence_markdown(citations: List[Dict[str, Any]], pdf_citations: List[Dict[str, Any]], limit: int) -> List[Dict[str, Any]]:
    pdf_by_anchor: Dict[str, Dict[str, Any]] = {}
    for pdf_citation in pdf_citations:
        anchor = pdf_citation.get("anchor") or pdf_citation.get("citation_anchor")
        if anchor and anchor not in pdf_by_anchor:
            pdf_by_anchor[str(anchor)] = pdf_citation

    evidence: List[Dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for citation in citations:
        anchor = str(citation.get("anchor") or "")
        file_uri = str(citation.get("file_uri") or "")
        matched_text = str(citation.get("matched_text") or citation.get("name") or "").strip()
        if not anchor or not file_uri or not matched_text:
            continue
        if matched_text.startswith("<a "):
            continue
        key = (anchor, matched_text)
        if key in seen:
            continue
        seen.add(key)
        pdf_citation = pdf_by_anchor.get(anchor, {})
        highlight_uri = str(pdf_citation.get("highlight_uri") or "")
        page_number = pdf_citation.get("page_number")
        bbox = pdf_citation.get("bbox")
        if len(matched_text) < 16 and pdf_citation.get("matched_pdf_text"):
            matched_text = str(pdf_citation.get("matched_pdf_text") or "").strip()
        if len(matched_text) < 16:
            continue
        quote = matched_text if len(matched_text) <= 650 else matched_text[:647].rstrip() + "..."
        item = {
            "anchor": anchor,
            "quote": quote,
            "markdown_link": file_uri,
            "pdf_page": page_number,
            "pdf_bbox": bbox,
            "pdf_highlight_uri": highlight_uri,
            "pdf_highlight_markdown": f"![PDF highlight]({highlight_uri})" if highlight_uri else "",
            "pdf_bbox_missing": not bool(highlight_uri),
            "pdf_ambiguous": bool(pdf_citation.get("ambiguous")) if pdf_citation else None,
        }
        item["markdown"] = "\n".join(
            part
            for part in [
                f"> {quote}",
                f"Markdown: {file_uri}",
                (
                    f"PDF: page {page_number}, bbox {bbox}, highlight {highlight_uri}"
                    if highlight_uri
                    else "PDF: bbox/highlight chưa resolve"
                ),
                item["pdf_highlight_markdown"],
            ]
            if part
        )
        evidence.append(item)
        if len(evidence) >= limit:
            break
    return evidence


def with_default_scope(citations: List[Dict[str, Any]], args: argparse.Namespace) -> List[Dict[str, Any]]:
    scoped = []
    for citation in citations:
        item = dict(citation)
        item["project_id"] = item.get("project_id") or args.project_id
        item["collection_id"] = item.get("collection_id") or args.collection_id
        item["source_id"] = item.get("source_id") or args.source_id
        scoped.append(item)
    return scoped


def resolve_pdf_bbox_citations(citations: List[Dict[str, Any]], args: argparse.Namespace) -> List[Dict[str, Any]]:
    if not args.with_pdf_bbox:
        return []
    try:
        from pdf_bbox_citations import load_pdf_citation_index, resolve_pdf_citations
    except Exception as exc:
        print(f"WARN: PDF bbox resolver unavailable: {exc}", file=sys.stderr)
        return []
    records = load_pdf_citation_index(Path(args.citation_index))
    resolved = resolve_pdf_citations(
        with_default_scope(citations, args),
        records,
        min_confidence=args.pdf_bbox_min_confidence,
        limit=args.limit,
    )
    if args.render_highlights and resolved:
        try:
            from render_pdf_highlights import render_record
            resolved = [render_record(record, Path(args.highlight_dir), "png") for record in resolved]
        except Exception as exc:
            print(f"WARN: Failed rendering PDF highlights: {exc}", file=sys.stderr)
    return resolved


def build_local_fts(kb_dir: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE VIRTUAL TABLE kb_lines USING fts5(file, line_number UNINDEXED, anchor UNINDEXED, content)")
    rows = []
    if kb_dir.exists():
        for md_file in sorted(kb_dir.glob("*.md")):
            if ".bak." in md_file.name:
                continue
            try:
                lines = md_file.read_text(encoding="utf-8").splitlines()
                anchors = nearest_anchor_by_line(lines)
                for idx, line in enumerate(lines, start=1):
                    text = line.strip()
                    if text:
                        rows.append((md_file.name, idx, anchors.get(idx, ""), text))
            except Exception as exc:
                print(f"WARN: Failed reading {md_file}: {exc}", file=sys.stderr)
    conn.executemany("INSERT INTO kb_lines(file, line_number, anchor, content) VALUES (?, ?, ?, ?)", rows)
    return conn


def fts_query(term: str) -> str:
    # Quote user text so legal terms with spaces/punctuation are treated as a phrase.
    escaped = term.replace('"', '""')
    return f'"{escaped}"'


def token_fts_query(term: str) -> str:
    tokens = re.findall(r"[A-Za-z0-9_]+", term)
    stopwords = {"and", "or", "the", "a", "an", "of", "to", "in", "by", "for", "with", "as", "is", "are"}
    useful = [token for token in tokens if len(token) > 2 and token.lower() not in stopwords]
    if not useful:
        return fts_query(term)
    return " OR ".join(f'"{token.replace(chr(34), chr(34) * 2)}"' for token in useful[:8])


def local_rank_score(content: str, bm25_score: float, term: str, anchor: str = "") -> float:
    text = content.strip()
    lower = text.lower()
    term_lower = term.lower()
    normalized_term = re.sub(r"[^\w]+", "_", term_lower).strip("_")
    score = float(bm25_score)
    scope_numbers = set(re.findall(r"\bscope\s+([123])\b", lower))
    if text.startswith("#"):
        score -= 2.0
    if term_lower in lower:
        score -= 1.0
    if anchor and anchor.lower() == normalized_term:
        score -= 3.0
    if lower.count(term_lower) > 1:
        score += 5.0
    if text.startswith("#") and len(scope_numbers) >= 3:
        score += 8.0
    if re.search(r"\b(scope\s+[123])(?:\s+\1\b)+", lower):
        score += 6.0
    if len(text) < max(12, len(term) + 4):
        score += 4.0
    if text.lower().startswith("<a "):
        score += 3.0
    if len(set(lower.split())) <= 2:
        score += 2.0
    return score


def local_search(kb_dir: Path, term: str, limit: int) -> List[Dict[str, Any]]:
    if not term:
        return []
    conn = build_local_fts(kb_dir)
    try:
        query = (
            "SELECT file, line_number, anchor, content, bm25(kb_lines) AS score "
            "FROM kb_lines WHERE kb_lines MATCH ? ORDER BY score LIMIT ?"
        )
        rows = conn.execute(query, (fts_query(term), max(limit * 5, limit))).fetchall()
        if not rows:
            rows = conn.execute(query, (token_fts_query(term), max(limit * 8, limit))).fetchall()
    except sqlite3.OperationalError:
        like_term = f"%{term.lower()}%"
        rows = conn.execute(
            "SELECT file, line_number, anchor, content, 0.0 AS score "
            "FROM kb_lines WHERE lower(content) LIKE ? LIMIT ?",
            (like_term, max(limit * 5, limit)),
        ).fetchall()
    finally:
        conn.close()

    matches = []
    metadata_cache: Dict[str, Dict[str, Any]] = {}
    for file_name, line_number, anchor, content, score in rows:
        file_path = (kb_dir / file_name).resolve()
        if file_name not in metadata_cache:
            metadata_cache[file_name] = parse_frontmatter(file_path.read_text(encoding="utf-8"))
        metadata = metadata_cache[file_name]
        ranked_score = local_rank_score(content, score, term, anchor)
        source_pdf = metadata.get("source_pdf")
        page_start = metadata.get("page_start")
        page_end = metadata.get("page_end")
        content_hash = metadata.get("content_hash")
        citation = {
            "file_path": str(file_path),
            "file_uri": f"{file_path.as_uri()}#{anchor}" if anchor else file_path.as_uri(),
            "anchor": anchor or None,
            "source_pdf": source_pdf,
            "project_id": metadata.get("project_id"),
            "collection_id": metadata.get("collection_id"),
            "source_id": metadata.get("source_id"),
            "page_start": page_start,
            "page_end": page_end,
            "content_hash": content_hash,
            "matched_text": content,
        }
        citation["missing_fields"] = citation_missing_fields(citation)
        matches.append(
            {
                "file": file_name,
                "line_number": line_number,
                "content": content,
                "score": ranked_score,
                "raw_bm25_score": score,
                "citation": citation,
            }
        )
    return sorted(matches, key=lambda item: item["score"])[:limit]


def run_graph_query(session: Any, args: argparse.Namespace) -> List[Dict[str, Any]]:
    depth = clamp_depth(args.depth)
    scope_filter = """
      AND ($project_id = '' OR n.project_id = $project_id)
      AND ($collection_id = '' OR n.collection_id = $collection_id)
      AND ($source_id = '' OR n.source_id = $source_id)
      AND ($source_map_hash = '' OR n.source_map_hash = $source_map_hash)
    """
    path_scope_filter = """
      ($project_id = '' OR all(node IN nodes(p) WHERE node.project_id = $project_id)) AND
      ($collection_id = '' OR all(node IN nodes(p) WHERE node.collection_id = $collection_id)) AND
      ($source_id = '' OR all(node IN nodes(p) WHERE node.source_id = $source_id)) AND
      ($source_map_hash = '' OR all(node IN nodes(p) WHERE node.source_map_hash = $source_map_hash))
    """
    neighbor_scope_filter = """
      ($project_id = '' OR m.project_id = $project_id) AND
      ($collection_id = '' OR m.collection_id = $collection_id) AND
      ($source_id = '' OR m.source_id = $source_id) AND
      ($source_map_hash = '' OR m.source_map_hash = $source_map_hash)
    """
    params = {
        "limit": args.limit,
        "source_map_hash": args.source_map_hash,
        "project_id": args.project_id,
        "collection_id": args.collection_id,
        "source_id": args.source_id,
    }
    if args.id:
        if args.mode == "paths":
            cypher = f"""
            MATCH (n:Concept {{id: $concept_id}})
            WHERE true {scope_filter}
            OPTIONAL MATCH p = (n)-[*1..{depth}]-(m:Concept)
            WHERE {path_scope_filter}
            RETURN n, collect(DISTINCT [
                node IN nodes(p) | {{
                    id: node.id,
                    name: node.name,
                    label: [l in labels(node) WHERE l <> 'Concept'][0],
                    file_path: node.file_path,
                    file_uri: node.file_uri,
                    anchor: node.anchor,
                    source_pdf: properties(node).source_pdf,
                    project_id: properties(node).project_id,
                    collection_id: properties(node).collection_id,
                    source_id: properties(node).source_id,
                    page_start: properties(node).page_start,
                    page_end: properties(node).page_end
                }}
            ])[..$limit] AS paths
            """
            res = session.run(cypher, concept_id=args.id, **params)
        else:
            cypher = f"""
            MATCH (n:Concept {{id: $concept_id}})
            WHERE true {scope_filter}
            OPTIONAL MATCH (n)-[r*1..{depth}]-(m:Concept)
            WHERE {neighbor_scope_filter}
            RETURN n, collect(DISTINCT {{
                depth: size(r),
                id: m.id,
                name: m.name,
                label: [l in labels(m) WHERE l <> 'Concept'][0],
                file_path: m.file_path,
                file_uri: m.file_uri,
                anchor: m.anchor,
                source_pdf: properties(m).source_pdf,
                project_id: properties(m).project_id,
                collection_id: properties(m).collection_id,
                source_id: properties(m).source_id,
                page_start: properties(m).page_start,
                page_end: properties(m).page_end,
                stale_path: [rel IN r | coalesce(rel.stale, false)],
                rel_path: [rel IN r | type(rel)]
            }})[..$limit] AS rels
            """
            res = session.run(cypher, concept_id=args.id, **params)
    elif args.search:
        cypher = f"""
        MATCH (n:Concept)
        WHERE toLower(n.name) CONTAINS toLower($term) OR toLower(n.id) CONTAINS toLower($term)
        WITH n
        WHERE true {scope_filter}
        OPTIONAL MATCH (n)-[r*1..{depth}]-(m:Concept)
        WHERE {neighbor_scope_filter}
        RETURN n, collect(DISTINCT {{
            depth: size(r),
            id: m.id,
            name: m.name,
            label: [l in labels(m) WHERE l <> 'Concept'][0],
            file_path: m.file_path,
            file_uri: m.file_uri,
            anchor: m.anchor,
            source_pdf: properties(m).source_pdf,
            project_id: properties(m).project_id,
            collection_id: properties(m).collection_id,
            source_id: properties(m).source_id,
            page_start: properties(m).page_start,
            page_end: properties(m).page_end,
            stale_path: [rel IN r | coalesce(rel.stale, false)],
            rel_path: [rel IN r | type(rel)]
        }})[..$limit] AS rels
        LIMIT $limit
        """
        res = session.run(cypher, term=args.search, **params)
    else:
        raise ValueError("Must provide either --id or --search parameter.")

    results = []
    for record in res:
        node = record["n"]
        item = node_payload(node)
        rels = record["rels"] if "rels" in record.keys() else []
        paths = record["paths"] if "paths" in record.keys() else []
        item["relationships"] = [rel for rel in rels if rel and rel.get("id") is not None]
        item["paths"] = [path for path in paths if path]
        results.append(item)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Query graph and local KB for PDF-to-KB Skill.")
    parser.add_argument("--id", help="Concept ID to look up specifically (e.g. scope_3)")
    parser.add_argument("--search", help="Search term/keyword across concept names, IDs, and local KB")
    parser.add_argument("--kb-dir", default="Projects/ESG/kb/ghg_protocol", help="Path to markdown KB directory")
    parser.add_argument("--env", default=".env", help="Path to .env configuration file")
    parser.add_argument("--depth", type=int, default=3, help="Graph traversal depth, clamped to 1..4")
    parser.add_argument(
        "--mode",
        choices=("neighbors", "paths", "search"),
        default="neighbors",
        help="neighbors returns related concepts, paths returns bounded paths, search emphasizes local fulltext retrieval",
    )
    parser.add_argument("--limit", type=int, default=10, help="Maximum graph/local results")
    parser.add_argument("--full-json", action="store_true", help="Include full graph/local/citation payloads")
    parser.add_argument("--project-id", default="esg", help="Restrict graph results to a project_id; use empty string to disable")
    parser.add_argument("--collection-id", default="", help="Restrict graph results to a collection_id")
    parser.add_argument("--source-id", default="", help="Restrict graph results to a source_id")
    parser.add_argument("--source-map-hash", default="", help="Restrict graph results to a specific imported concept_map hash")
    parser.add_argument("--with-pdf-bbox", action=argparse.BooleanOptionalAction, default=True, help="Resolve citations to PDF page/bbox using a citation index")
    parser.add_argument("--citation-index", default="Projects/ESG/graph/citation_index/pdf_citation_index.jsonl")
    parser.add_argument("--render-highlights", action=argparse.BooleanOptionalAction, default=True, help="Render cached PNG highlights for resolved PDF bbox citations")
    parser.add_argument("--highlight-dir", default="Projects/ESG/evidence/highlights")
    parser.add_argument("--pdf-bbox-min-confidence", type=float, default=0.55)
    return parser.parse_args()


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
        args = parse_args()
        args.depth = clamp_depth(args.depth)
        args.limit = max(1, min(args.limit, 100))

        load_env(Path(args.env))

        uri = os.getenv("NEO4J_URI")
        user = os.getenv("NEO4J_USERNAME")
        password = os.getenv("NEO4J_PASSWORD")
        database = os.getenv("NEO4J_DATABASE", "neo4j")

        if not uri or not user or not password:
            raise ValueError(
                "Missing Neo4j credentials in environment. Ensure NEO4J_URI, NEO4J_USERNAME, and NEO4J_PASSWORD are set."
            )

        kb_dir = Path(args.kb_dir)
        query_term = args.search or args.id or ""

        driver = GraphDatabase.driver(uri, auth=(user, password))
        with driver.session(database=database) as session:
            graph_results = run_graph_query(session, args)
        driver.close()

        local_matches = local_search(kb_dir, query_term, args.limit)
        citations = [citation_from_node(result, query_term) for result in graph_results]
        citations.extend(match["citation"] for match in local_matches)
        pdf_citations = resolve_pdf_bbox_citations(citations, args)

        output_data = {
            "status": "success",
            "query_metadata": {
                "mode": args.mode,
                "depth": args.depth,
                "limit": args.limit,
                "kb_dir": str(kb_dir),
                "retrieval": "neo4j_graph + sqlite_fts5_local_text",
                "full_json": args.full_json,
                "source_map_hash": args.source_map_hash,
                "project_id": args.project_id,
                "collection_id": args.collection_id,
                "source_id": args.source_id,
                "with_pdf_bbox": args.with_pdf_bbox,
                "citation_index": args.citation_index if args.with_pdf_bbox else "",
                "render_highlights": args.render_highlights,
            },
            "result_count": len(graph_results),
            "local_match_count": len(local_matches),
            "citation_count": len(citations),
            "pdf_citation_count": len(pdf_citations),
            "evidence_markdown": evidence_markdown(citations, pdf_citations, args.limit),
            "results": graph_results if args.full_json else compact_graph_results(graph_results),
            "local_text_matches": local_matches if args.full_json else compact_local_matches(local_matches),
            "citations": citations if args.full_json else compact_citations(citations, args.limit),
            "pdf_citations": pdf_citations if args.full_json else compact_pdf_citations(pdf_citations, args.limit),
        }

        print(json.dumps(output_data, indent=2, ensure_ascii=False))

    except Exception as e:
        error_json = {
            "status": "error",
            "error_code": type(e).__name__,
            "message": str(e),
        }
        print(json.dumps(error_json, indent=2, ensure_ascii=False))
        sys.exit(1)


if __name__ == "__main__":
    main()
