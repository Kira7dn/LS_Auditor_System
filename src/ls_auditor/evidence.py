from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def create_evidence_pack(finding: dict[str, Any], out_dir: str | Path) -> dict[str, Any]:
    finding_id = str(finding.get("id") or finding.get("finding_id") or "FIND-UNSPECIFIED")
    root = Path(out_dir) / finding_id
    artifacts = root / "artifacts"
    artifacts.mkdir(parents=True, exist_ok=True)
    (root / "FINDING.md").write_text(render_finding(finding), encoding="utf-8")
    (artifacts / "finding.json").write_text(json.dumps(finding, ensure_ascii=False, indent=2), encoding="utf-8")
    return {
        "finding_id": finding_id,
        "evidence_root": str(root),
        "files": [str(root / "FINDING.md"), str(artifacts / "finding.json")],
    }


def render_finding(finding: dict[str, Any]) -> str:
    return "\n".join(
        [
            f"# Finding {finding.get('id', finding.get('finding_id', 'FIND-UNSPECIFIED'))}",
            "",
            f"- **Condition:** {finding.get('condition', 'TBD')}",
            f"- **Criteria:** {finding.get('criteria', 'TBD')}",
            f"- **Cause:** {finding.get('cause', 'TBD')}",
            f"- **Effect / Leakage:** {finding.get('effect', finding.get('leakage', 'TBD'))}",
            f"- **Evidence:** {finding.get('evidence', 'TBD')}",
            f"- **Recommendation:** {finding.get('recommendation', 'TBD')}",
            "",
        ]
    )
