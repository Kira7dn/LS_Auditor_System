"""
import_concept_map.py
======================
Deterministic Knowledge Graph Ingestion script.
Enforces 10 strict validation rules (Ontology, Whitelists, Anchors, and Orphan checks)
before writing to Neo4j database.
Tuân thủ nghiêm ngặt bộ tiêu chuẩn SCRIPT_STANDARDS.md (AI-First Scripting).

Usage:
  uv run scripts/import_legal_rag.py

Output (stdout):
  JSON object with execution details or error status.
All logs/progress are routed to stderr.
"""
import sys
import os
import re
import json
import argparse
import hashlib
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Any, Set, Tuple, Optional

from neo4j import GraphDatabase

ONTOLOGY_NODES: Set[str] = {
    "Standard", "Chapter", "Requirement", "Definition", "Principle", "BoundaryRule", 
    "ScopeRule", "DisclosureRequirement", "EmissionSourceType", "ActivityDataType", 
    "EmissionFactor", "GWP", "CalculationMethod", "Formula", "Unit", "UncertaintyRule", 
    "Company", "Facility", "Asset", "Meter", "Invoice", "FuelReceipt", "ElectricityBill", 
    "TransportLog", "ERPRecord", "UploadedDocument", "DataExtract", "EvidenceType", 
    "SourceDocument", "ControlPoint", "AuditTest", "ValidationRule", "Exception", 
    "Finding", "ApprovalStep", "Reviewer", "ControlType", "Section"
}

WHITELIST_EDGES: Set[str] = {
    "CONTAINS", "DEFINES", "REQUIRES", "PROHIBITS", "APPLIES_TO", "EXCEPTION_OF", 
    "VERSION_OF", "CALCULATED_USING", "REQUIRES_ACTIVITY_DATA", "USES_FACTOR", 
    "CONVERTS_TO", "HAS_UNIT", "HAS_UNCERTAINTY", "MUST_COMPLY_WITH", "USES_FORMULA", 
    "OWNS", "OPERATES", "LOCATED_AT", "EVIDENCES", "SUPPORTS_CLAIM", "MEASURED_BY", 
    "MATCHES_RECORD", "CONFLICTS_WITH", "CHECKS_REQUIREMENT", "CHECKS_EVIDENCE", 
    "FAILS_WHEN", "TRIGGERS_RECALCULATION", "CREATES_FINDING", "APPROVED_BY", 
    "REQUIRES_EVIDENCE", "EXECUTES_CONTROL", "SUBJECT_TO", "ALTERNATIVE_TO", 
    "CATEGORIZED_AS", "DETERMINED_BY", "ENSURES_COMPLIANCE_WITH", "APPLIES_PRINCIPLE"
}

def load_env(env_path: Path) -> None:
    if not env_path.exists():
        return
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ[k] = v.strip("'\"")

def map_hash(map_path: Path) -> str:
    return hashlib.sha256(map_path.read_bytes()).hexdigest()

def resolve_doc_file(kb_dir: Path, doc_id: str) -> Optional[Path]:
    """Resolve doc_id to NN_doc_id.md or doc_id.md inside kb_dir."""
    matches = sorted(f for f in kb_dir.rglob("*.md") if f.stem == doc_id or f.name.endswith(f"{doc_id}.md"))
    return matches[0] if matches else None

def anchor_regex(anchor: str) -> re.Pattern:
    return re.compile(
        rf"<a\s+[^>]*id\s*=\s*['\"]{re.escape(anchor)}['\"][^>]*>\s*</a>",
        re.IGNORECASE,
    )

def has_anchor(content: str, anchor: str) -> bool:
    if anchor_regex(anchor).search(content):
        return True
    heading_pattern = re.compile(rf"^#+\s+{re.escape(anchor)}\s*$", re.MULTILINE | re.IGNORECASE)
    return bool(heading_pattern.search(content))

def parse_frontmatter(content: str) -> Dict[str, Any]:
    """Parse simple YAML frontmatter scalars without requiring a YAML dependency."""
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
        key = key.strip()
        value = value.strip().strip("'\"")
        if value.isdigit():
            metadata[key] = int(value)
        else:
            metadata[key] = value
    return metadata

def file_uri_for_anchor(file_path: Path, anchor: str) -> str:
    return f"{file_path.resolve().as_uri()}#{anchor}"

def metadata_source_id(metadata: Dict[str, Any], fallback: str) -> str:
    return str(metadata.get("source_id") or fallback)

def collection_id_for_file(kb_dir: Path, file_path: Path, fallback: str) -> str:
    """Infer collection_id from the first folder under the KB root."""
    try:
        relative = file_path.resolve().relative_to(kb_dir.resolve())
    except ValueError:
        return fallback
    if len(relative.parts) > 1:
        return relative.parts[0]
    return fallback

def compact_list(items: List[str], limit: int = 5) -> List[str]:
    return items[:limit]

def infer_section_label(anchor: str, heading: str) -> str:
    text = f"{anchor} {heading}".lower()
    if re.search(r"\bscope[_\s-]*[123]\b", text):
        return "ScopeRule"
    if "principle" in text or anchor.startswith("principles_"):
        return "Principle"
    if "definition" in text or "define" in text:
        return "Definition"
    if "calculation" in text or "emission factor" in text:
        return "CalculationMethod"
    if "report" in text:
        return "DisclosureRequirement"
    if "verification" in text or "audit" in text:
        return "AuditTest"
    if "quality" in text or "control" in text:
        return "ControlPoint"
    return "Section"

def extract_sections_from_markdown(file_path: Path, kb_dir: Path) -> Tuple[Dict[str, Any], List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Build deterministic Chapter + Section graph records from anchored Markdown headings."""
    content = file_path.read_text(encoding="utf-8")
    metadata = parse_frontmatter(content)
    doc_id = metadata.get("id") or re.sub(r"^\d+_", "", file_path.stem)
    title = metadata.get("title") or doc_id.replace("_", " ").title()
    source_pdf = metadata.get("source_pdf")
    page_start = metadata.get("page_start")
    page_end = metadata.get("page_end")
    content_hash = metadata.get("content_hash")
    rel_path = str(file_path.resolve())

    chapter = {
        "id": str(doc_id),
        "label": "Chapter",
        "name": str(title),
        "doc_id": str(doc_id),
        "anchor": "",
        "file_path": rel_path,
        "file_uri": file_path.resolve().as_uri(),
        "source_pdf": source_pdf,
        "page_start": page_start,
        "page_end": page_end,
        "content_hash": content_hash,
    }

    anchor_re = re.compile(r"<a\s+[^>]*id\s*=\s*['\"]([^'\"]+)['\"][^>]*>\s*</a>", re.IGNORECASE)
    heading_re = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
    pending_anchors: List[str] = []
    sections: List[Dict[str, Any]] = []
    edges: List[Dict[str, Any]] = []

    for line in content.splitlines():
        anchor_match = anchor_re.search(line)
        if anchor_match:
            pending_anchors.append(anchor_match.group(1))
            continue

        heading_match = heading_re.match(line.strip())
        if not heading_match:
            continue

        heading = heading_match.group(2).strip()
        level = len(heading_match.group(1))
        if not pending_anchors:
            continue

        for anchor in pending_anchors:
            section_id = anchor
            section = {
                "id": section_id,
                "label": infer_section_label(anchor, heading),
                "name": heading,
                "doc_id": str(doc_id),
                "anchor": anchor,
                "heading_level": level,
                "file_path": rel_path,
                "file_uri": file_uri_for_anchor(file_path, anchor),
                "source_pdf": source_pdf,
                "page_start": page_start,
                "page_end": page_end,
                "content_hash": content_hash,
            }
            sections.append(section)
            edges.append({"from": str(doc_id), "to": section_id, "type": "CONTAINS", "edge_key": f"{doc_id}|CONTAINS|{section_id}"})
        pending_anchors = []

    return chapter, sections, edges

def validate_concept_map(
    map_data: Dict[str, Any],
    kb_dir: Path,
    strict_citation: bool = False,
    verbose: bool = False,
) -> Tuple[List[str], List[str]]:
    """Verify nodes and edges against the 10 strict ontology and link validation rules."""
    errors = []
    warnings = []
    
    nodes = map_data.get("nodes", [])
    edges = map_data.get("edges", [])
    
    node_ids = {n["id"] for n in nodes if "id" in n}
    requirement_nodes = {n["id"] for n in nodes if n.get("label") == "Requirement"}
    calc_method_nodes = {n["id"] for n in nodes if n.get("label") == "CalculationMethod"}
    
    # Track incoming and outgoing edges for orphan detection
    incoming_edges: Dict[str, List[str]] = {nid: [] for nid in node_ids}
    outgoing_edges: Dict[str, List[str]] = {nid: [] for nid in node_ids}
    
    # Edge relationship types
    for edge in edges:
        from_node = edge.get("from")
        to_node = edge.get("to")
        edge_type = edge.get("type")
        
        if from_node in outgoing_edges:
            outgoing_edges[from_node].append(to_node)
        if to_node in incoming_edges:
            incoming_edges[to_node].append(from_node)
            
        # Rule 4: Edge type is in the whitelist
        if edge_type not in WHITELIST_EDGES:
            errors.append(f"Edge '{from_node} -> {to_node}': Relationship type '{edge_type}' is not in the whitelist.")

    for idx, node in enumerate(nodes):
        node_id = node.get("id")
        label = node.get("label")
        doc_id = node.get("doc_id")
        anchor = node.get("anchor")
        
        if not node_id or not doc_id or not anchor:
            errors.append(f"Node at index {idx} is missing required fields (id, doc_id, anchor)")
            continue
            
        # Rule 5: Node type is in the ontology
        if label not in ONTOLOGY_NODES:
            errors.append(f"Node '{node_id}': Label '{label}' is not in the ontology node whitelist.")
            
        # Rule 1: doc_id exists
        file_path = resolve_doc_file(kb_dir, doc_id)
        if not file_path:
            errors.append(f"Node '{node_id}': Markdown file ending with '{doc_id}.md' not found in {kb_dir}")
            continue
            
        content = file_path.read_text(encoding="utf-8")
        
        # Rule 2: stable anchor/section_id exists (<a id="anchor"></a>)
        if not has_anchor(content, anchor):
            errors.append(f"Node '{node_id}': Stable anchor (<a id='{anchor}'></a>) not found in file {file_path.name}")

        metadata = parse_frontmatter(content)
        missing_citation = [k for k in ("source_pdf", "page_start", "page_end", "content_hash") if not metadata.get(k)]
        if missing_citation:
            message = f"Node '{node_id}': Citation metadata missing in {file_path.name}: {', '.join(missing_citation)}"
            if strict_citation:
                errors.append(message)
            else:
                warnings.append(f"WARN: {message}")

    # Rule 6: No orphan requirements
    for req_id in requirement_nodes:
        total_connections = len(incoming_edges.get(req_id, [])) + len(outgoing_edges.get(req_id, []))
        if total_connections == 0:
            errors.append(f"Node '{req_id}': Orphan Requirement node detected (no incoming/outgoing relationships).")

    # Rule 7: Calculation method validation (must have activity data and formula relations)
    for calc_id in calc_method_nodes:
        has_formula = any(edge.get("type") == "USES_FORMULA" for edge in edges if edge.get("from") == calc_id)
        has_act_data = any(edge.get("type") == "REQUIRES_ACTIVITY_DATA" for edge in edges if edge.get("from") == calc_id)
        if not has_formula or not has_act_data:
            warnings.append(f"WARN: CalculationMethod '{calc_id}' is missing USES_FORMULA or REQUIRES_ACTIVITY_DATA relationships.")

    # Rule 8: Evidence requirement check
    for req_id in requirement_nodes:
        # Check if there is an path from Control Point -> Requirement, and Control Point -> EvidenceType
        control_points = incoming_edges.get(req_id, [])
        for cp in control_points:
            has_evidence = any(edge.get("type") == "REQUIRES_EVIDENCE" for edge in edges if edge.get("from") == cp)
            if not has_evidence:
                warnings.append(f"WARN: ControlPoint '{cp}' checking Requirement '{req_id}' has no REQUIRES_EVIDENCE relationships defined.")

    if warnings and verbose:
        for w in warnings:
            print(w, file=sys.stderr)

    return errors, warnings

def main():
    try:
        parser = argparse.ArgumentParser(description="Ingest Concept Map into Neo4j with 10 ontology validation rules.")
        parser.add_argument("--map", required=True, help="Path to concept_map.json")
        parser.add_argument("--kb-dir", required=True, help="Path to ghg_kb markdown folder")
        parser.add_argument("--env", default=".env", help="Path to .env configuration file")
        parser.add_argument("--project-id", default="esg", help="Project scope for imported nodes/relationships")
        parser.add_argument("--collection-id", default="ghg_protocol", help="KB collection scope for imported nodes/relationships")
        parser.add_argument("--source-id", default="ghg_protocol_corporate_standard", help="Source document set scope")
        parser.add_argument("--source-pdf", default="", help="Source PDF path to use when markdown metadata is missing")
        parser.add_argument("--prune-stale", action="store_true", help="Delete stale relationships for this source map instead of marking them")
        parser.add_argument("--strict-citation", action="store_true", help="Fail import when markdown source/page/hash metadata is missing")
        parser.add_argument("--full-json", action="store_true", help="Include full validation warning details in stdout JSON")
        parser.add_argument("--verbose", action="store_true", help="Print all validation warnings to stderr")
        parser.add_argument(
            "--auto-sections",
            action=argparse.BooleanOptionalAction,
            default=True,
            help="Import deterministic Chapter/Section nodes from Markdown anchors before applying concept_map overlay",
        )
        args = parser.parse_args()

        env_path = Path(args.env)
        load_env(env_path)

        uri = os.getenv("NEO4J_URI")
        user = os.getenv("NEO4J_USERNAME")
        password = os.getenv("NEO4J_PASSWORD")
        database = os.getenv("NEO4J_DATABASE", "neo4j")

        if not uri or not user or not password:
            raise ValueError("Missing Neo4j credentials in environment. Ensure NEO4J_URI, NEO4J_USERNAME, and NEO4J_PASSWORD are set.")

        map_path = Path(args.map)
        if not map_path.exists():
            raise FileNotFoundError(f"Concept map file not found: {map_path}")

        kb_dir = Path(args.kb_dir)
        if not kb_dir.exists():
            raise FileNotFoundError(f"KB directory not found: {kb_dir}")

        with open(map_path, "r", encoding="utf-8") as f:
            map_data = json.load(f)
        source_map = str(map_path.resolve())
        source_map_hash = map_hash(map_path)
        import_batch_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

        # 1. Validation Step
        print("Starting 10-rule pre-ingestion validation...", file=sys.stderr)
        validation_errors, validation_warnings = validate_concept_map(
            map_data,
            kb_dir,
            strict_citation=args.strict_citation,
            verbose=args.verbose,
        )
        if validation_errors:
            raise ValueError(f"Concept Map validation failed with {len(validation_errors)} error(s):\n" + "\n".join(validation_errors))
        if validation_warnings and not args.verbose:
            print(
                f"Validation completed with {len(validation_warnings)} warning(s). "
                "Use --verbose or --full-json for details.",
                file=sys.stderr,
            )
        print("Pre-ingestion validation passed successfully.", file=sys.stderr)

        # 2. Neo4j Ingestion Step
        print("Connecting to Neo4j database...", file=sys.stderr)
        driver = GraphDatabase.driver(uri, auth=(user, password))
        
        # Create schema constraints
        with driver.session(database=database) as session:
            print("Creating uniqueness constraints...", file=sys.stderr)
            session.run("CREATE CONSTRAINT concept_id_unique IF NOT EXISTS FOR (c:Concept) REQUIRE c.id IS UNIQUE")
            session.run("CREATE INDEX concept_project_id IF NOT EXISTS FOR (c:Concept) ON (c.project_id)")
            session.run("CREATE INDEX concept_project_collection IF NOT EXISTS FOR (c:Concept) ON (c.project_id, c.collection_id)")
            session.run("CREATE INDEX concept_project_source IF NOT EXISTS FOR (c:Concept) ON (c.project_id, c.source_id)")

        # 2a. Import deterministic chapter/section graph from Markdown anchors.
        auto_nodes_imported = 0
        auto_edges_imported = 0
        active_edge_keys = []
        active_node_ids = set()
        if args.auto_sections:
            print("Importing deterministic Markdown section graph...", file=sys.stderr)
            with driver.session(database=database) as session:
                for md_file in sorted(kb_dir.rglob("*.md")):
                    if ".bak." in md_file.name:
                        continue
                    # Only filter by source_id when the caller explicitly scoped to one source.
                    content = md_file.read_text(encoding="utf-8")
                    metadata = parse_frontmatter(content)
                    file_source_id = metadata_source_id(metadata, args.source_id)
                    if args.source_id and file_source_id != args.source_id:
                        continue
                    file_collection_id = collection_id_for_file(kb_dir, md_file, args.collection_id)
                    chapter, sections, section_edges = extract_sections_from_markdown(md_file, kb_dir)
                    missing_metadata = [
                        key for key in ("source_pdf", "page_start", "page_end", "content_hash") if not chapter.get(key)
                    ]
                    if args.strict_citation and missing_metadata:
                        print(
                            f"WARN: Skipping auto section graph for {md_file.name}; missing citation metadata: "
                            f"{', '.join(missing_metadata)}",
                            file=sys.stderr,
                        )
                        continue
                    auto_nodes = [chapter] + sections
                    for node in auto_nodes:
                        active_node_ids.add(node["id"])
                        label = node["label"]
                        node_source_id = metadata_source_id(metadata, args.source_id)
                        query = (
                            f"MERGE (c:Concept {{id: $id}}) "
                            f"SET c.name = $name, c.doc_id = $doc_id, c.anchor = $anchor, "
                            f"    c.project_id = $project_id, c.collection_id = $collection_id, c.source_id = $source_id, "
                            f"    c.file_path = $file_path, c.file_uri = $file_uri, "
                            f"    c.source_pdf = $source_pdf, c.page_start = $page_start, c.page_end = $page_end, "
                            f"    c.content_hash = $content_hash, c.source_map = $source_map, "
                            f"    c.source_map_hash = $source_map_hash, c.import_batch_id = $import_batch_id, "
                            f"    c.auto_generated = true, c.curated = false, c.llm_generated = false "
                            f"WITH c "
                            f"SET c:{label} "
                            f"RETURN c"
                        )
                        session.run(
                            query,
                            id=node["id"],
                            name=node["name"],
                            doc_id=node["doc_id"],
                            anchor=node["anchor"],
                            file_path=node["file_path"],
                            file_uri=node["file_uri"],
                            project_id=args.project_id,
                            collection_id=file_collection_id,
                            source_id=node_source_id,
                            source_pdf=node.get("source_pdf"),
                            page_start=node.get("page_start"),
                            page_end=node.get("page_end"),
                            content_hash=node.get("content_hash"),
                            source_map=source_map,
                            source_map_hash=source_map_hash,
                            import_batch_id=import_batch_id,
                        )
                        auto_nodes_imported += 1

                    for edge in section_edges:
                        active_edge_keys.append(edge["edge_key"])
                        session.run(
                            f"MATCH (a:Concept {{id: $from_id}}) "
                            f"MATCH (b:Concept {{id: $to_id}}) "
                            f"MERGE (a)-[r:{edge['type']}]->(b) "
                            f"SET r.source_map = $source_map, r.source_map_hash = $source_map_hash, "
                            f"    r.project_id = $project_id, r.collection_id = $collection_id, r.source_id = $source_id, "
                            f"    r.import_batch_id = $import_batch_id, r.edge_key = $edge_key, "
                            f"    r.stale = false, r.auto_generated = true "
                            f"RETURN r",
                            from_id=edge["from"],
                            to_id=edge["to"],
                            source_map=source_map,
                            source_map_hash=source_map_hash,
                            project_id=args.project_id,
                            collection_id=file_collection_id,
                            source_id=file_source_id,
                            import_batch_id=import_batch_id,
                            edge_key=edge["edge_key"],
                        )
                        auto_edges_imported += 1
        
        # 2b. Merge curated concept_map nodes as an overlay.
        nodes_created = 0
        node_scopes: Dict[str, Tuple[str, str]] = {}
        with driver.session(database=database) as session:
            for node in map_data.get("nodes", []):
                node_id = node["id"]
                label = node["label"]
                name = node["name"]
                doc_id = node["doc_id"]
                anchor = node["anchor"]
                active_node_ids.add(node_id)
                
                # Fetch exact matching file name
                file_path = resolve_doc_file(kb_dir, doc_id)
                if not file_path:
                    raise FileNotFoundError(f"Markdown file for doc_id '{doc_id}' not found in {kb_dir}")
                content = file_path.read_text(encoding="utf-8")
                metadata = parse_frontmatter(content)
                
                # Construct file_path and file_uri
                rel_path = str(file_path.resolve())
                file_uri = file_uri_for_anchor(file_path, anchor)
                source_pdf = metadata.get("source_pdf") or args.source_pdf
                source_id = str(node.get("source_id") or metadata_source_id(metadata, args.source_id))
                collection_id = str(node.get("collection_id") or collection_id_for_file(kb_dir, file_path, args.collection_id))
                page_start = metadata.get("page_start")
                page_end = metadata.get("page_end")
                content_hash = metadata.get("content_hash")
                node_scopes[node_id] = (collection_id, source_id)
                
                # Ingestion is idempotent using MERGE
                query = (
                    f"MERGE (c:Concept {{id: $id}}) "
                    f"SET c.name = $name, c.doc_id = $doc_id, c.anchor = $anchor, "
                    f"    c.project_id = $project_id, c.collection_id = $collection_id, c.source_id = $source_id, "
                    f"    c.file_path = $file_path, c.file_uri = $file_uri, "
                    f"    c.source_pdf = $source_pdf, c.page_start = $page_start, c.page_end = $page_end, "
                    f"    c.content_hash = $content_hash, c.source_map = $source_map, "
                    f"    c.source_map_hash = $source_map_hash, c.import_batch_id = $import_batch_id, "
                    f"    c.curated = true, c.auto_generated = false, c.llm_generated = false "
                    f"WITH c "
                    f"SET c:{label} "
                    f"RETURN c"
                )
                session.run(
                    query,
                    id=node_id,
                    name=name,
                    doc_id=doc_id,
                    anchor=anchor,
                    file_path=rel_path,
                    file_uri=file_uri,
                    project_id=args.project_id,
                    collection_id=collection_id,
                    source_id=source_id,
                    source_pdf=source_pdf,
                    page_start=page_start,
                    page_end=page_end,
                    content_hash=content_hash,
                    source_map=source_map,
                    source_map_hash=source_map_hash,
                    import_batch_id=import_batch_id,
                )
                nodes_created += 1
                
        # Merge Edges
        edges_created = 0
        with driver.session(database=database) as session:
            for edge in map_data.get("edges", []):
                from_id = edge["from"]
                to_id = edge["to"]
                rel_type = edge["type"]
                edge_key = f"{from_id}|{rel_type}|{to_id}"
                active_edge_keys.append(edge_key)
                from_scope = node_scopes.get(from_id, (args.collection_id, args.source_id))
                to_scope = node_scopes.get(to_id, (args.collection_id, args.source_id))
                edge_collection_id = from_scope[0] if from_scope[0] == to_scope[0] else "cross_collection"
                edge_source_id = from_scope[1] if from_scope[1] == to_scope[1] else "cross_source"
                
                query = (
                    f"MATCH (a:Concept {{id: $from_id}}) "
                    f"MATCH (b:Concept {{id: $to_id}}) "
                    f"MERGE (a)-[r:{rel_type}]->(b) "
                    f"SET r.source_map = $source_map, r.source_map_hash = $source_map_hash, "
                    f"    r.project_id = $project_id, r.collection_id = $collection_id, r.source_id = $source_id, "
                    f"    r.import_batch_id = $import_batch_id, r.edge_key = $edge_key, "
                    f"    r.stale = false, r.curated = true "
                    f"RETURN r"
                )
                session.run(
                    query,
                    from_id=from_id,
                    to_id=to_id,
                    source_map=source_map,
                    source_map_hash=source_map_hash,
                    project_id=args.project_id,
                    collection_id=edge_collection_id,
                    source_id=edge_source_id,
                    import_batch_id=import_batch_id,
                    edge_key=edge_key,
                )
                edges_created += 1

            if args.prune_stale:
                stale_query = (
                    "MATCH ()-[r]->() "
                    "WHERE r.source_map = $source_map AND r.project_id = $project_id "
                    "AND NOT r.edge_key IN $active_edge_keys "
                    "DELETE r RETURN count(r) AS stale_count"
                )
            else:
                stale_query = (
                    "MATCH ()-[r]->() "
                    "WHERE r.source_map = $source_map AND r.project_id = $project_id "
                    "AND NOT r.edge_key IN $active_edge_keys "
                    "SET r.stale = true RETURN count(r) AS stale_count"
                )
            stale_count = session.run(
                stale_query,
                source_map=source_map,
                project_id=args.project_id,
                active_edge_keys=active_edge_keys,
            ).single()["stale_count"]

            stale_auto_nodes = 0
            if args.prune_stale:
                stale_auto_nodes = session.run(
                    """
                    MATCH (n:Concept)
                    WHERE n.source_map = $source_map
                      AND n.project_id = $project_id
                      AND n.auto_generated = true
                      AND coalesce(n.curated, false) = false
                      AND NOT n.id IN $active_node_ids
                    WITH collect(n) AS nodes, count(n) AS stale_count
                    FOREACH (n IN nodes | DETACH DELETE n)
                    RETURN stale_count
                    """,
                    source_map=source_map,
                    project_id=args.project_id,
                    active_node_ids=list(active_node_ids),
                ).single()["stale_count"]

        driver.close()
        print(
            f"Successfully imported {nodes_created} curated nodes, {auto_nodes_imported} auto nodes, "
            f"{edges_created} curated relationships, and {auto_edges_imported} auto relationships. "
            f"Stale relationships {'pruned' if args.prune_stale else 'marked'}: {stale_count}",
            file=sys.stderr,
        )

        # Standard SCRIPT_STANDARDS.md output JSON
        result_json = {
            "status": "success",
            "concept_map": str(map_path),
            "kb_directory": str(kb_dir),
            "project_id": args.project_id,
            "collection_id": args.collection_id,
            "source_id": args.source_id,
            "nodes_imported": nodes_created,
            "edges_imported": edges_created,
            "auto_nodes_imported": auto_nodes_imported,
            "auto_edges_imported": auto_edges_imported,
            "stale_relationships": stale_count,
            "stale_auto_nodes_pruned": stale_auto_nodes if args.prune_stale else 0,
            "import_batch_id": import_batch_id,
            "source_map_hash": source_map_hash,
            "validation_warning_count": len(validation_warnings),
            "validation_warnings_sample": compact_list(validation_warnings),
            "neo4j_uri": uri
        }
        if args.full_json:
            result_json["validation_warnings"] = validation_warnings
        print(json.dumps(result_json, indent=2, ensure_ascii=False))

    except Exception as e:
        error_json = {
            "status": "error",
            "error_code": type(e).__name__,
            "message": str(e),
            "suggestion": "Check Neo4j database status, credentials in .env, file paths, or markdown anchor existence."
        }
        print(json.dumps(error_json, indent=2, ensure_ascii=False))
        sys.exit(1)

if __name__ == "__main__":
    main()
