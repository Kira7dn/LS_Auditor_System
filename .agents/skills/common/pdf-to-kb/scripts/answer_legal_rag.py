"""
Short preset wrapper for evidence-first legal RAG answers.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ANSWER_QUESTION = Path(__file__).parent / "answer_question.py"

PRESETS = {
    "ghg": {
        "kb_dir": "Projects/ESG/kb/ghg_protocol",
        "env": ".env",
        "project_id": "esg",
        "collection_id": "ghg_protocol",
        "source_id": "ghg_protocol_corporate_standard",
        "citation_index": "Projects/ESG/graph/citation_index/pdf_citation_index.jsonl",
        "highlight_dir": "Projects/ESG/evidence/highlights",
    },
    "cbam": {
        "kb_dir": "Projects/ESG/kb/cbam_guidance_importers",
        "env": ".env",
        "project_id": "esg",
        "collection_id": "cbam_guidance_importers",
        "source_id": "cbam_guidance_importers",
        "citation_index": "Projects/ESG/graph/citation_index/pdf_citation_index.jsonl",
        "highlight_dir": "Projects/ESG/evidence/highlights",
    },
    "nd06": {
        "kb_dir": "Projects/ESG/kb/nd06_2022",
        "env": ".env",
        "project_id": "esg",
        "collection_id": "nd06_2022",
        "source_id": "nd06_2022_ndcp",
        "citation_index": "Projects/ESG/graph/citation_index/pdf_citation_index.jsonl",
        "highlight_dir": "Projects/ESG/evidence/highlights",
    },
    "qd226": {
        "kb_dir": "Projects/ESG/kb/qd226_btnmt",
        "env": ".env",
        "project_id": "esg",
        "collection_id": "qd226_btnmt",
        "source_id": "qd226_2022_btnmt",
        "citation_index": "Projects/ESG/graph/citation_index/pdf_citation_index.jsonl",
        "highlight_dir": "Projects/ESG/evidence/highlights",
    },
    "iso14064_1": {
        "kb_dir": "Projects/ESG/kb/tcvn_iso_14064_1_2025",
        "env": ".env",
        "project_id": "esg",
        "collection_id": "tcvn_iso_14064_1_2025",
        "source_id": "tcvn_iso_14064_1_2025",
        "citation_index": "Projects/ESG/graph/citation_index/pdf_citation_index.jsonl",
        "highlight_dir": "Projects/ESG/evidence/highlights",
    },
    "iso14064_2": {
        "kb_dir": "Projects/ESG/kb/tcvn_iso_14064_2",
        "env": ".env",
        "project_id": "esg",
        "collection_id": "tcvn_iso_14064_2",
        "source_id": "tcvn_iso_14064_2_2025",
        "citation_index": "Projects/ESG/graph/citation_index/pdf_citation_index.jsonl",
        "highlight_dir": "Projects/ESG/evidence/highlights",
    },
    "iso14067": {
        "kb_dir": "Projects/ESG/kb/tcvn_iso_14067",
        "env": ".env",
        "project_id": "esg",
        "collection_id": "tcvn_iso_14067",
        "source_id": "tcvn_iso_14067_2020",
        "citation_index": "Projects/ESG/graph/citation_index/pdf_citation_index.jsonl",
        "highlight_dir": "Projects/ESG/evidence/highlights",
    },
}


def resolve_preset(args: argparse.Namespace) -> str:
    texts = []
    question_val = getattr(args, "question", None)
    if question_val:
        texts.append(question_val)
    
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
    if "ghg" in combined or "scope" in combined:
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
    citation_index = getattr(args, "citation_index", None) or preset["citation_index"]
    highlight_dir = getattr(args, "highlight_dir", None) or preset["highlight_dir"]
    
    command = [
        sys.executable,
        str(ANSWER_QUESTION),
        "--question",
        getattr(args, "question", ""),
        "--kb-dir",
        kb_dir,
        "--env",
        getattr(args, "env", None) or preset["env"],
        "--project-id",
        project_id,
        "--collection-id",
        collection_id,
        "--source-id",
        source_id,
        "--limit",
        str(getattr(args, "limit", 8)),
        "--claim-limit",
        str(getattr(args, "claim_limit", 3)),
    ]
    if not getattr(args, "no_pdf_bbox", False):
        command.append("--with-pdf-bbox")
        command.extend(["--citation-index", citation_index])
    if not getattr(args, "no_render_highlights", False):
        command.append("--render-highlights")
        command.extend(["--highlight-dir", highlight_dir])
    return command


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Preset wrapper around answer_question.py. Supports dynamic presets and CLI overrides."
    )
    parser.add_argument("--preset", choices=sorted(PRESETS), default=None, help="Preset configuration to use (default: auto-detect from keyword/question, fallback to ghg)")
    parser.add_argument("--question", required=True)
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--claim-limit", type=int, default=3)
    parser.add_argument("--no-pdf-bbox", action="store_true", help="Disable PDF bbox citation resolution.")
    parser.add_argument("--no-render-highlights", action="store_true", help="Disable highlight image rendering.")
    
    # Optional CLI overrides
    parser.add_argument("--kb-dir", help="Override preset knowledge base directory")
    parser.add_argument("--env", help="Override preset env file path")
    parser.add_argument("--project-id", help="Override preset project ID")
    parser.add_argument("--collection-id", help="Override preset collection ID")
    parser.add_argument("--source-id", help="Override preset source ID")
    parser.add_argument("--citation-index", help="Override preset citation index path")
    parser.add_argument("--highlight-dir", help="Override preset highlights output directory")
    
    return parser.parse_args()


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    args = parse_args()
    proc = subprocess.run(build_command(args), check=False, text=True)
    raise SystemExit(proc.returncode)


if __name__ == "__main__":
    main()

