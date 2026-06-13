"""
verify_graph.py
===============
Queries the Neo4j database to inspect the loaded concept map, count nodes, edges,
and trace audit paths to verify the integrity of the graph.
Outputs JSON to stdout, debug messages to stderr.
"""
import sys
import os
import json
from pathlib import Path
from neo4j import GraphDatabase

def load_env(env_path: Path) -> None:
    if not env_path.exists():
        return
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ[k] = v.strip("'\"")

def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')

        env_path = Path(".env")
        load_env(env_path)

        uri = os.getenv("NEO4J_URI")
        user = os.getenv("NEO4J_USERNAME")
        password = os.getenv("NEO4J_PASSWORD")
        database = os.getenv("NEO4J_DATABASE", "neo4j")

        if not uri or not user or not password:
            raise ValueError("Missing Neo4j credentials in environment.")

        print(f"Connecting to Neo4j at {uri}...", file=sys.stderr)
        driver = GraphDatabase.driver(uri, auth=(user, password))

        results = {}

        with driver.session(database=database) as session:
            # Summary queries
            total_n = session.run("MATCH (n) RETURN count(n)").single()[0]
            total_r = session.run("MATCH ()-[r]->() RETURN count(r)").single()[0]
            results["total_nodes"] = total_n
            results["total_relationships"] = total_r

            # Query 1: Node labels summary
            print("Querying node count and label distribution...", file=sys.stderr)
            node_res = session.run("MATCH (n:Concept) RETURN labels(n) AS labels, count(n) AS cnt")
            node_counts = []
            for r in node_res:
                # Filter out the generic 'Concept' label to get the specific ontology label
                specific_labels = [l for l in r["labels"] if l != "Concept"]
                label_name = specific_labels[0] if specific_labels else "Concept"
                node_counts.append({"label": label_name, "count": r["cnt"]})
            results["node_distribution"] = node_counts

            # Query 2: Relationship types summary
            print("Querying relationship counts...", file=sys.stderr)
            rel_res = session.run("MATCH ()-[r]->() RETURN type(r) AS rel_type, count(r) AS cnt")
            rel_counts = []
            for r in rel_res:
                rel_counts.append({"relationship": r["rel_type"], "count": r["cnt"]})
            results["relationship_distribution"] = rel_counts

            # Query 3: Trace sample path from ControlPoint to Principle / Standard
            print("Tracing sample audit paths...", file=sys.stderr)
            path_res = session.run(
                "MATCH p = (cp:ControlPoint)-[*1..4]->(target) "
                "RETURN [n in nodes(p) | {id: n.id, label: [l in labels(n) WHERE l <> 'Concept'][0], name: n.name}] AS path "
                "LIMIT 5"
            )
            paths = []
            for r in path_res:
                paths.append(r["path"])
            results["sample_paths"] = paths

            # Query 4: Check if any orphan requirements exist in DB
            print("Checking for orphan requirements in database...", file=sys.stderr)
            orphan_res = session.run(
                "MATCH (r:Requirement) "
                "WHERE not (r)-[]-() "
                "RETURN r.id AS id, r.name AS name"
            )
            orphans = [{"id": r["id"], "name": r["name"]} for r in orphan_res]
            results["orphan_requirements"] = orphans

        driver.close()
        print(json.dumps(results, indent=2, ensure_ascii=False))

    except Exception as e:
        error_json = {
            "status": "error",
            "error_code": type(e).__name__,
            "message": str(e)
        }
        print(json.dumps(error_json, indent=2, ensure_ascii=False))
        sys.exit(1)

if __name__ == "__main__":
    main()
