"""
write_run_manifest.py
=====================
Write a compact audit manifest for the current pdf-to-kb hardening run.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_env(env_path: Path) -> None:
    if not env_path.exists():
        return
    with env_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                os.environ[key] = value.strip("'\"")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else ""


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8-sig"))


def mask_uri(uri: str) -> str:
    if "://" not in uri:
        return "***"
    scheme, rest = uri.split("://", 1)
    host = rest.split("/", 1)[0]
    parts = host.split(".")
    if not parts:
        return f"{scheme}://***"
    visible = parts[0][:4]
    return f"{scheme}://{visible}***"


def git_status_short() -> list[str]:
    proc = subprocess.run(["git", "status", "--short"], capture_output=True, text=True, encoding="utf-8", check=False)
    return proc.stdout.splitlines() if proc.returncode == 0 else []


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Write pdf-to-kb hardening run manifest.")
    parser.add_argument("--env", default=".env")
    parser.add_argument("--project-id", default="esg")
    parser.add_argument("--collection-id", default="ghg_protocol")
    parser.add_argument("--source-id", default="ghg_protocol_corporate_standard")
    parser.add_argument("--kb-dir", default="Projects/ESG/kb/ghg_protocol")
    parser.add_argument("--concept-map", default="Projects/ESG/graph/concept_map.json")
    parser.add_argument("--aliases", default="Projects/ESG/graph/canonical_aliases.json")
    parser.add_argument("--graph-quality", default="Projects/ESG/graph/quality_reports/graph_quality_report.json")
    parser.add_argument("--citation-validation", default="")
    parser.add_argument("--retrieval-eval", default="Projects/ESG/eval/retrieval_eval_report.json")
    parser.add_argument("--alias-apply-report", default="Projects/ESG/graph/import_reports/canonical_aliases_apply_report.json")
    parser.add_argument("--out", default="Projects/ESG/manifests/run_manifest.latest.json")
    return parser.parse_args()


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
        args = parse_args()
        load_env(Path(args.env))
        graph_quality = load_json(Path(args.graph_quality))
        retrieval_eval = load_json(Path(args.retrieval_eval))
        alias_apply = load_json(Path(args.alias_apply_report))
        citation_validation = load_json(Path(args.citation_validation)) if args.citation_validation else {}
        manifest = {
            "status": "success",
            "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "kb_dir": args.kb_dir,
            "scope": {
                "project_id": args.project_id,
                "collection_id": args.collection_id,
                "source_id": args.source_id,
            },
            "neo4j_uri_masked": mask_uri(os.getenv("NEO4J_URI", "")),
            "files": {
                "concept_map": {"path": args.concept_map, "sha256": sha256_file(Path(args.concept_map))},
                "canonical_aliases": {"path": args.aliases, "sha256": sha256_file(Path(args.aliases))},
                "graph_quality_report": {"path": args.graph_quality, "sha256": sha256_file(Path(args.graph_quality))},
                "retrieval_eval_report": {"path": args.retrieval_eval, "sha256": sha256_file(Path(args.retrieval_eval))},
                "alias_apply_report": {"path": args.alias_apply_report, "sha256": sha256_file(Path(args.alias_apply_report))},
            },
            "graph_quality_summary": graph_quality.get("summary", {}),
            "retrieval_eval_summary": retrieval_eval.get("summary", {}),
            "alias_apply_summary": {
                "mode": alias_apply.get("mode"),
                "alias_count": alias_apply.get("alias_count"),
                "applied_count": sum(1 for item in alias_apply.get("results", []) if item.get("status") == "applied"),
            },
            "citation_validation_summary": citation_validation,
            "script_paths": [
                "scripts/analyze_graph_quality.py",
                "scripts/apply_canonical_aliases.py",
                "scripts/run_retrieval_eval.py",
                "scripts/answer_question.py",
                "scripts/write_run_manifest.py",
            ],
            "git_status_short": git_status_short(),
        }
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
        print(json.dumps({"status": "success", "manifest": str(out_path), "summary": manifest["retrieval_eval_summary"]}, ensure_ascii=False, indent=2))
    except Exception as exc:
        print(json.dumps({"status": "error", "error_code": type(exc).__name__, "message": str(exc)}, ensure_ascii=False, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
