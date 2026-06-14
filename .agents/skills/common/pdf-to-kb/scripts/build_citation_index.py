"""
Preset wrapper for building PDF citation indexes.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


BUILD_INDEX = Path(__file__).parent / "build_pdf_citation_index.py"

PRESETS = {
    "ghg": {
        "kb_dir": "Projects/ESG/kb/ghg_protocol",
        "project_id": "esg",
        "collection_id": "ghg_protocol",
        "source_id": "ghg_protocol_corporate_standard",
        "out": "Projects/ESG/graph/citation_index/pdf_citation_index.jsonl",
        "report": "Projects/ESG/graph/citation_index/pdf_citation_index_report.json",
    },
    "cbam": {
        "kb_dir": "Projects/ESG/kb/cbam_guidance_importers",
        "project_id": "esg",
        "collection_id": "cbam_guidance_importers",
        "source_id": "cbam_guidance_importers",
        "out": "Projects/ESG/graph/citation_index/pdf_citation_index.jsonl",
        "report": "Projects/ESG/graph/citation_index/pdf_citation_index_report.json",
    },
    "nd06": {
        "kb_dir": "Projects/ESG/kb/nd06_2022",
        "project_id": "esg",
        "collection_id": "nd06_2022",
        "source_id": "nd06_2022_ndcp",
        "out": "Projects/ESG/graph/citation_index/pdf_citation_index.jsonl",
        "report": "Projects/ESG/graph/citation_index/pdf_citation_index_report.json",
    },
    "qd226": {
        "kb_dir": "Projects/ESG/kb/qd226_btnmt",
        "project_id": "esg",
        "collection_id": "qd226_btnmt",
        "source_id": "qd226_2022_btnmt",
        "out": "Projects/ESG/graph/citation_index/pdf_citation_index.jsonl",
        "report": "Projects/ESG/graph/citation_index/pdf_citation_index_report.json",
    },
    "iso14064_1": {
        "kb_dir": "Projects/ESG/kb/tcvn_iso_14064_1_2025",
        "project_id": "esg",
        "collection_id": "tcvn_iso_14064_1_2025",
        "source_id": "tcvn_iso_14064_1_2025",
        "out": "Projects/ESG/graph/citation_index/pdf_citation_index.jsonl",
        "report": "Projects/ESG/graph/citation_index/pdf_citation_index_report.json",
    },
    "iso14064_2": {
        "kb_dir": "Projects/ESG/kb/tcvn_iso_14064_2",
        "project_id": "esg",
        "collection_id": "tcvn_iso_14064_2",
        "source_id": "tcvn_iso_14064_2_2025",
        "out": "Projects/ESG/graph/citation_index/pdf_citation_index.jsonl",
        "report": "Projects/ESG/graph/citation_index/pdf_citation_index_report.json",
    },
    "iso14067": {
        "kb_dir": "Projects/ESG/kb/tcvn_iso_14067",
        "project_id": "esg",
        "collection_id": "tcvn_iso_14067",
        "source_id": "tcvn_iso_14067_2020",
        "out": "Projects/ESG/graph/citation_index/pdf_citation_index.jsonl",
        "report": "Projects/ESG/graph/citation_index/pdf_citation_index_report.json",
    },
}


def resolve_preset(args: argparse.Namespace) -> str:
    texts = []
    kb_dir_val = getattr(args, "kb_dir", None)
    if kb_dir_val:
        texts.append(str(kb_dir_val))
    collection_val = getattr(args, "collection_id", None)
    if collection_val:
        texts.append(collection_val)
    source_val = getattr(args, "source_id", None)
    if source_val:
        texts.append(source_val)
        
    combined = " ".join(texts).lower()
    
    if "cbam" in combined:
        return "cbam"
    if "nd06" in combined:
        return "nd06"
    if "qd226" in combined:
        return "qd226"
    if "14064_1" in combined or "14064-1" in combined:
        return "iso14064_1"
    if "14064_2" in combined or "14064-2" in combined:
        return "iso14064_2"
    if "14067" in combined:
        return "iso14067"
    if "ghg" in combined:
        return "ghg"
        
    return "ghg"


def build_command(args: argparse.Namespace) -> list[str]:
    preset_name = getattr(args, "preset", None) or resolve_preset(args)
    preset = PRESETS.get(preset_name, PRESETS["ghg"])
    
    kb_dir = getattr(args, "kb_dir", None) or preset["kb_dir"]
    project_id = getattr(args, "project_id", None) or preset["project_id"]
    collection_id = getattr(args, "collection_id", None)
    if collection_id is None:
        collection_id = preset["collection_id"]
    source_id = getattr(args, "source_id", None)
    if source_id is None:
        source_id = preset["source_id"]
    out = getattr(args, "out", None) or preset["out"]
    report = getattr(args, "report", None) or preset["report"]
    
    return [
        sys.executable,
        str(BUILD_INDEX),
        "--kb-dir",
        kb_dir,
        "--project-id",
        project_id,
        "--collection-id",
        collection_id,
        "--source-id",
        source_id,
        "--out",
        out,
        "--report",
        report,
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build PDF citation index using a safe preset. Supports dynamic presets and CLI overrides."
    )
    parser.add_argument("--preset", choices=sorted(PRESETS), default=None, help="Preset configuration to use (default: auto-detect from keyword/argument, fallback to ghg)")
    
    # Optional CLI overrides
    parser.add_argument("--kb-dir", help="Override preset knowledge base directory")
    parser.add_argument("--project-id", help="Override preset project ID")
    parser.add_argument("--collection-id", help="Override preset collection ID")
    parser.add_argument("--source-id", help="Override preset source ID")
    parser.add_argument("--out", help="Override preset output jsonl path")
    parser.add_argument("--report", help="Override preset output report json path")
    
    return parser.parse_args()


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    args = parse_args()
    proc = subprocess.run(build_command(args), check=False, text=True)
    raise SystemExit(proc.returncode)


if __name__ == "__main__":
    main()

