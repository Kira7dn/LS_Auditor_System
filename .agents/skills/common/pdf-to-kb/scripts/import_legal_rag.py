"""
Preset wrapper for legal RAG graph import.

This is the operational entrypoint. The low-level import_concept_map.py flags
remain available for debugging, but agents should use this wrapper.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


IMPORT_CONCEPT_MAP = Path(__file__).parent / "import_concept_map.py"

PRESETS = {
    "esg": {
        "map": "Projects/ESG/graph/concept_map.json",
        "kb_dir": "Projects/ESG/kb",
        "env": ".env",
        "project_id": "esg",
    }
}


def build_command(args: argparse.Namespace) -> list[str]:
    preset = PRESETS[args.preset]
    command = [
        sys.executable,
        str(IMPORT_CONCEPT_MAP),
        "--map",
        preset["map"],
        "--kb-dir",
        preset["kb_dir"],
        "--env",
        preset["env"],
        "--project-id",
        preset["project_id"],
        "--collection-id",
        "",
        "--source-id",
        "",
        "--strict-citation",
    ]
    if args.prune_stale:
        command.append("--prune-stale")
    if args.no_auto_sections:
        command.append("--no-auto-sections")
    if args.full_json:
        command.append("--full-json")
    return command


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Import legal RAG graph using a safe project preset.")
    parser.add_argument("--preset", choices=sorted(PRESETS), default="esg")
    parser.add_argument("--prune-stale", action="store_true")
    parser.add_argument("--no-auto-sections", action="store_true")
    parser.add_argument("--full-json", action="store_true")
    return parser.parse_args()


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    args = parse_args()
    proc = subprocess.run(build_command(args), check=False, text=True)
    raise SystemExit(proc.returncode)


if __name__ == "__main__":
    main()
