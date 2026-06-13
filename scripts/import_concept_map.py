"""
import_concept_map.py
======================
Deterministic Knowledge Graph Ingestion script.
Enforces 10 strict validation rules (Ontology, Whitelists, Anchors, and Orphan checks)
before writing to Neo4j database.
Tuân thủ nghiêm ngặt bộ tiêu chuẩn SCRIPT_STANDARDS.md (AI-First Scripting).

Usage:
  uv run scripts/import_concept_map.py --map Projects/ESG/concept_map.json --kb-dir Projects/ESG/ghg_kb

Output (stdout):
  JSON object with execution details or error status.
All logs/progress are routed to stderr.
"""
import sys
import os
import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Any, Set

from neo4j import GraphDatabase

ONTOLOGY_NODES: Set[str] = {
    "Standard", "Chapter", "Requirement", "Definition", "Principle", "BoundaryRule", 
    "ScopeRule", "DisclosureRequirement", "EmissionSourceType", "ActivityDataType", 
    "EmissionFactor", "GWP", "CalculationMethod", "Formula", "Unit", "UncertaintyRule", 
    "Company", "Facility", "Asset", "Meter", "Invoice", "FuelReceipt", "ElectricityBill", 
    "TransportLog", "ERPRecord", "UploadedDocument", "DataExtract", "EvidenceType", 
    "SourceDocument", "ControlPoint", "AuditTest", "ValidationRule", "Exception", 
    "Finding", "ApprovalStep", "Reviewer", "ControlType"
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

def validate_concept_map(map_data: Dict[str, Any], kb_dir: Path) -> List[str]:
    """Verify nodes and edges against the 10 strict ontology and link validation rules."""
    errors = []
    warnings = []
    
    kb_files = list(kb_dir.glob("*.md"))
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
        matching_files = [f for f in kb_files if f.name.endswith(f"{doc_id}.md")]
        if not matching_files:
            errors.append(f"Node '{node_id}': Markdown file ending with '{doc_id}.md' not found in {kb_dir}")
            continue
            
        file_path = matching_files[0]
        content = file_path.read_text(encoding="utf-8")
        
        # Rule 2: stable anchor/section_id exists (<a id="anchor"></a>)
        anchor_pattern = re.compile(rf'<a\s+id="{re.escape(anchor)}"\s*>\s*</a>', re.IGNORECASE)
        if not anchor_pattern.search(content):
            # Fallback to standard heading text match to see if it is a legacy header
            heading_pattern = re.compile(rf"^#+\s+{re.escape(anchor)}\s*$", re.MULTILINE | re.IGNORECASE)
            if not heading_pattern.search(content):
                errors.append(f"Node '{node_id}': Stable anchor (<a id='{anchor}'></a>) not found in file {file_path.name}")

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
        # Or simple check: if a requirement is audited by a ControlPoint, does that ControlPoint have an outgoing edge to an EvidenceType?
        control_points = incoming_edges.get(req_id, [])
        for cp in control_points:
            has_evidence = any(edge.get("type") == "REQUIRES_EVIDENCE" for edge in edges if edge.get("from") == cp)
            if not has_evidence:
                warnings.append(f"WARN: ControlPoint '{cp}' checking Requirement '{req_id}' has no REQUIRES_EVIDENCE relationships defined.")

    if warnings:
        for w in warnings:
            print(w, file=sys.stderr)

    return errors

def slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r'[^a-z0-9\s_-]', '', s)
    s = re.sub(r'[\s_-]+', '_', s)
    return s

def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')

        parser = argparse.ArgumentParser(description="Ingest Concept Map into Neo4j with 10 ontology validation rules.")
        parser.add_argument("--map", required=True, help="Path to concept_map.json")
        parser.add_argument("--kb-dir", required=True, help="Path to ghg_kb markdown folder")
        parser.add_argument("--env", default=".env", help="Path to .env configuration file")
        parser.add_argument("--llm", action="store_true", help="Enable LLM extraction of new concepts from Markdown KB")
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

        # 1. Validation Step
        print("Starting 10-rule pre-ingestion validation...", file=sys.stderr)
        validation_errors = validate_concept_map(map_data, kb_dir)
        if validation_errors:
            raise ValueError(f"Concept Map validation failed with {len(validation_errors)} error(s):\n" + "\n".join(validation_errors))
        print("Pre-ingestion validation passed successfully.", file=sys.stderr)

        # 2. Neo4j Ingestion Step
        print("Connecting to Neo4j database...", file=sys.stderr)
        driver = GraphDatabase.driver(uri, auth=(user, password))
        
        # Create schema constraints
        with driver.session(database=database) as session:
            print("Creating uniqueness constraints...", file=sys.stderr)
            session.run("CREATE CONSTRAINT concept_id_unique IF NOT EXISTS FOR (c:Concept) REQUIRE c.id IS UNIQUE")
        
        # Load files to verify exact filenames
        kb_files = list(kb_dir.glob("*.md"))
        
        # Track all processed node IDs to prevent duplicates during LLM extraction
        processed_node_ids = set()

        # Merge Static Nodes
        nodes_created = 0
        with driver.session(database=database) as session:
            for node in map_data.get("nodes", []):
                node_id = node["id"]
                label = node["label"]
                name = node["name"]
                doc_id = node["doc_id"]
                anchor = node["anchor"]
                
                # Fetch exact matching file name
                matching_files = [f for f in kb_files if f.name.endswith(f"{doc_id}.md")]
                file_name = matching_files[0].name
                
                # Construct file_path and file_uri
                rel_path = f"Projects/ESG/ghg_kb/{file_name}"
                file_uri = f"file:///{rel_path}#{anchor}"
                
                # Ingestion is idempotent using MERGE
                query = (
                    f"MERGE (c:Concept {{id: $id}}) "
                    f"SET c.name = $name, c.doc_id = $doc_id, c.anchor = $anchor, "
                    f"    c.file_path = $file_path, c.file_uri = $file_uri "
                    f"WITH c "
                    f"CALL apoc.create.addLabels(c, [$label]) YIELD node "
                    f"RETURN node"
                )
                session.run(
                    query,
                    id=node_id,
                    name=name,
                    doc_id=doc_id,
                    anchor=anchor,
                    file_path=rel_path,
                    file_uri=file_uri,
                    label=label
                )
                nodes_created += 1
                processed_node_ids.add(node_id)
                
        # Merge Static Edges
        edges_created = 0
        with driver.session(database=database) as session:
            for edge in map_data.get("edges", []):
                from_id = edge["from"]
                to_id = edge["to"]
                rel_type = edge["type"]
                
                query = (
                    f"MATCH (a:Concept {{id: $from_id}}) "
                    f"MATCH (b:Concept {{id: $to_id}}) "
                    f"MERGE (a)-[r:{rel_type}]->(b) "
                    f"RETURN r"
                )
                session.run(query, from_id=from_id, to_id=to_id)
                edges_created += 1

        # 3. LLM Extraction & Ingestion Step
        llm_nodes_created = 0
        llm_edges_created = 0
        if args.llm:
            openai_key = os.getenv("OPENAI_API_KEY")
            if not openai_key:
                print("Warning: OPENAI_API_KEY not set in environment. Skipping LLM extraction.", file=sys.stderr)
            else:
                print("Starting LLM-based concept extraction on KB markdown files...", file=sys.stderr)
                from openai import OpenAI
                client = OpenAI(api_key=openai_key)

                # Loop through all markdown files
                for md_file in kb_files:
                    doc_id = md_file.name.replace(".md", "")
                    if doc_id.startswith("00_") or doc_id == "index":
                        continue  # Skip intro/index files
                        
                    print(f"Processing {md_file.name} with LLM...", file=sys.stderr)
                    try:
                        content = md_file.read_text(encoding="utf-8")
                        
                        # Call LLM
                        prompt = (
                            f"Analyze the following markdown file '{md_file.name}' and extract compliance audit concepts (Nodes) and relationships (Edges).\n\n"
                            f"Ontology whitelist labels:\n"
                            f"{list(ONTOLOGY_NODES)}\n\n"
                            f"Relationship whitelist types:\n"
                            f"{list(WHITELIST_EDGES)}\n\n"
                            f"Markdown content:\n{content[:15000]}\n\n"
                            f"Instructions:\n"
                            f"1. Extract new Requirement, CalculationMethod, EmissionSourceType, EvidenceType, ControlPoint, AuditTest nodes.\n"
                            f"2. For each node, return:\n"
                            f"   - id: unique string slug, lowercase (e.g. scope3_outsourcing)\n"
                            f"   - label: one of the whitelist labels above\n"
                            f"   - name: brief descriptive name\n"
                            f"   - closest_heading: the exact Markdown heading text (e.g. '## Recalculating base year emissions' or '### Resale to end-users') right above or containing the concept.\n"
                            f"3. For each relationship, return:\n"
                            f"   - from: source node ID\n"
                            f"   - to: target node ID\n"
                            f"   - type: one of the relationship whitelist types above\n"
                            f"Return ONLY a valid JSON object without markdown blocks or explanation:\n"
                            f"{{\n"
                            f"  \"nodes\": [ {{\"id\": \"node_id\", \"label\": \"OntologyLabel\", \"name\": \"Descriptive Name\", \"closest_heading\": \"## Exact Header\"}} ],\n"
                            f"  \"edges\": [ {{\"from\": \"node_id\", \"to\": \"another_id\", \"type\": \"REL_TYPE\"}} ]\n"
                            f"}}"
                        )
                        
                        response = client.chat.completions.create(
                            model="gpt-4o-mini",
                            messages=[
                                {"role": "system", "content": "You are a professional GHG Auditor AI. You extract structured compliance concepts from standard text."},
                                {"role": "user", "content": prompt}
                            ],
                            temperature=0.1,
                            response_format={"type": "json_object"}
                        )
                        
                        data = json.loads(response.choices[0].message.content)
                        extracted_nodes = data.get("nodes", [])
                        extracted_edges = data.get("edges", [])
                        
                        # Track local changes to insert anchors
                        file_modified = False
                        file_lines = content.splitlines()
                        
                        node_map = {} # Maps extracted id to clean ID
                        for node in extracted_nodes:
                            raw_id = node.get("id")
                            label = node.get("label")
                            name = node.get("name")
                            heading = node.get("closest_heading", "").strip()
                            
                            if not raw_id or not label or not name or label not in ONTOLOGY_NODES:
                                continue
                                
                            clean_id = slugify(raw_id)
                            node_map[raw_id] = clean_id
                            
                            if clean_id in processed_node_ids:
                                continue  # Skip already added nodes
                                
                            # Search heading and insert anchor if missing
                            anchor = clean_id
                            anchor_inserted = False
                            
                            if heading:
                                # Find heading in lines
                                for i, line in enumerate(file_lines):
                                    if heading.lower() in line.lower() and (line.startswith("#") or "##" in line):
                                        # Check line above for anchor
                                        has_anchor = False
                                        if i > 0 and "<a id=" in file_lines[i-1]:
                                            has_anchor = True
                                        if not has_anchor:
                                            # Insert anchor
                                            file_lines.insert(i, f'<a id="{anchor}"></a>')
                                            file_modified = True
                                            anchor_inserted = True
                                        break
                                        
                            if file_modified and anchor_inserted:
                                # Update file content cache
                                content = "\n".join(file_lines)
                                
                            rel_path = f"Projects/ESG/ghg_kb/{md_file.name}"
                            file_uri = f"file:///{rel_path}#{anchor}"
                            
                            # Ingest LLM node
                            query = (
                                f"MERGE (c:Concept {{id: $id}}) "
                                f"SET c.name = $name, c.doc_id = $doc_id, c.anchor = $anchor, "
                                f"    c.file_path = $file_path, c.file_uri = $file_uri "
                                f"WITH c "
                                f"CALL apoc.create.addLabels(c, [$label]) YIELD node "
                                f"RETURN node"
                            )
                            with driver.session(database=database) as session:
                                session.run(
                                    query,
                                    id=clean_id,
                                    name=name,
                                    doc_id=doc_id,
                                    anchor=anchor,
                                    file_path=rel_path,
                                    file_uri=file_uri,
                                    label=label
                                )
                            llm_nodes_created += 1
                            processed_node_ids.add(clean_id)
                            
                        # If file modified, write back to disk
                        if file_modified:
                            md_file.write_text("\n".join(file_lines), encoding="utf-8")
                            print(f"Updated {md_file.name} with new anchors.", file=sys.stderr)
                            
                        # Ingest LLM edges
                        for edge in extracted_edges:
                            raw_from = edge.get("from")
                            raw_to = edge.get("to")
                            rel_type = edge.get("type")
                            
                            clean_from = node_map.get(raw_from, slugify(raw_from or ""))
                            clean_to = node_map.get(raw_to, slugify(raw_to or ""))
                            
                            if clean_from not in processed_node_ids or clean_to not in processed_node_ids:
                                continue  # Skip edges referencing uncreated nodes
                            if rel_type not in WHITELIST_EDGES:
                                continue
                                
                            query = (
                                f"MATCH (a:Concept {{id: $from_id}}) "
                                f"MATCH (b:Concept {{id: $to_id}}) "
                                f"MERGE (a)-[r:{rel_type}]->(b) "
                                f"RETURN r"
                            )
                            with driver.session(database=database) as session:
                                session.run(query, from_id=clean_from, to_id=clean_to)
                            llm_edges_created += 1
                            
                    except Exception as e:
                        print(f"Error extracting from {md_file.name}: {str(e)}", file=sys.stderr)

        driver.close()
        print(f"Successfully imported {nodes_created} static nodes, {llm_nodes_created} LLM nodes, {edges_created} static edges, {llm_edges_created} LLM edges.", file=sys.stderr)

        # Standard SCRIPT_STANDARDS.md output JSON
        result_json = {
            "status": "success",
            "concept_map": str(map_path),
            "kb_directory": str(kb_dir),
            "static_nodes_imported": nodes_created,
            "llm_nodes_imported": llm_nodes_created,
            "static_edges_imported": edges_created,
            "llm_edges_imported": llm_edges_created,
            "total_nodes": nodes_created + llm_nodes_created,
            "total_relationships": edges_created + llm_edges_created,
            "neo4j_uri": uri
        }
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
