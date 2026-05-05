from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def assemble_report(case_dir: str | Path, out_path: str | Path) -> dict[str, Any]:
    case_root = Path(case_dir)
    target = Path(out_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    metrics_files = sorted((case_root / "artifacts").glob("*.json"))
    evidence_dirs = sorted((case_root / "Evidence_Packs").glob("*")) if (case_root / "Evidence_Packs").exists() else []
    sections = [
        "# LS Auditor Final Report",
        "",
        "## 1. Executive Summary",
        f"- Case directory: `{case_root}`",
        f"- Artifact JSON files: {len(metrics_files)}",
        f"- Evidence packs: {len(evidence_dirs)}",
        "",
        "## 2. Artifact Index",
    ]
    for artifact in metrics_files:
        sections.append(f"- `{artifact}`")
    sections.extend(["", "## 3. Evidence Packs"])
    for dossier in evidence_dirs:
        sections.append(f"- `{dossier}`")
    sections.extend(["", "## 4. Metrics Snapshot"])
    for artifact in metrics_files:
        try:
            data: Any = json.loads(artifact.read_text(encoding="utf-8"))
            sections.append(f"### {artifact.name}")
            sections.append("```json")
            sections.append(json.dumps(data.get("metrics", data), ensure_ascii=False, indent=2))
            sections.append("```")
        except Exception:
            sections.append(f"- `{artifact}` could not be parsed as JSON.")
    target.write_text("\n".join(sections) + "\n", encoding="utf-8")
    return {"report_path": str(target), "artifact_count": len(metrics_files), "evidence_pack_count": len(evidence_dirs)}


def create_chart_artifact(dataset_summary: dict[str, Any], out_path: str | Path) -> dict[str, Any]:
    target = Path(out_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# LS Auditor Chart Artifact", "", "```json", json.dumps(dataset_summary, ensure_ascii=False, indent=2), "```"]
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"chart_path": str(target)}
