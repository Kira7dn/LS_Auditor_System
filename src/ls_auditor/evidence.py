from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any
import datetime


def create_evidence_pack(finding: dict[str, Any], out_dir: str | Path) -> dict[str, Any]:
    # Determine the best ID for the finding
    finding_id = str(finding.get("id") or finding.get("finding_id") or "FIND-UNSPECIFIED")
    if finding_id == "FIND-UNSPECIFIED" and "risk_id" in finding and "pr_id" in finding:
        finding_id = f"{finding['risk_id'][:3]}-{finding['pr_id']}-{finding.get('material_id', 'N/A')}"
        
    root = Path(out_dir) / finding_id
    artifacts = root / "artifacts"
    artifacts.mkdir(parents=True, exist_ok=True)
    
    # Try to use standard template if available
    template_path = Path(".agents/templates/auditor/evidence-pack.md")
    if template_path.exists():
        content = render_from_template(template_path, finding, finding_id)
    else:
        content = render_finding(finding)
        
    (root / "EVIDENCE.md").write_text(content, encoding="utf-8")
    (root / "FINDING.md").write_text(content, encoding="utf-8")
    (artifacts / "finding.json").write_text(json.dumps(finding, ensure_ascii=False, indent=2), encoding="utf-8")
    
    return {
        "finding_id": finding_id,
        "evidence_root": str(root),
        "files": [str(root / "EVIDENCE.md"), str(root / "FINDING.md"), str(artifacts / "finding.json")],
    }


def render_from_template(template_path: Path, finding: dict[str, Any], finding_id: str) -> str:
    """
    Truly generic template renderer. 
    Replaces any [key] in the template with finding.get(key).
    """
    content = template_path.read_text(encoding="utf-8")
    
    # Prepare context
    context = finding.copy()
    context.update({
        "finding_id": finding_id,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "agent_name": "LS Auditor AI"
    })
    
    # Add some formatted versions
    if "leakage" in context:
        context["leakage_formatted"] = f"${float(context['leakage']):,.2f}"

    # Generic replacement using regex for [key] patterns
    # This allows the template to drive the mapping, not the code.
    def replace_match(match):
        key = match.group(1)
        # Try finding the key in context (case-insensitive for convenience)
        val = context.get(key)
        if val is None:
            # Try some common descriptive placeholders from templates
            if "Mô tả logic" in key: return context.get("evidence", context.get("type", "[TBD]"))
            if "ID của Control Point" in key: return context.get("control_point_id", "[TBD]")
            if "Tại sao lỗi này xảy ra" in key: return context.get("cause", "[TBD]")
            if "Ai đã phê duyệt" in key: return context.get("approver", "[TBD]")
            return match.group(0) # Keep placeholder if not found
        return str(val)

    # Replace both [key] and {{key}} for flexibility
    content = re.sub(r"\[(.*?)\]", replace_match, content)
    content = re.sub(r"\{\{(.*?)\}\}", replace_match, content)
        
    return content


def render_finding(finding: dict[str, Any]) -> str:
    # Fallback to simple listing if no template exists
    lines = [f"# Finding {finding.get('id', 'N/A')}"]
    for k, v in finding.items():
        if k not in ["row_index"]:
            lines.append(f"- **{k.replace('_', ' ').title()}:** {v}")
    return "\n".join(lines)
