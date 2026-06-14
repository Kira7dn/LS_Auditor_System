from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def inspect_registry(registry_path: str | Path) -> dict[str, Any]:
    path = Path(registry_path)
    if not path.exists():
        return {
            "registry_path": str(path),
            "asset_count": 0,
            "missing_count": 0,
            "missing": [],
            "warning": "Registry file not found. This workspace now uses GEMINI.md, global_workflows, and .agents/ as source of truth.",
        }
    registry = json.loads(path.read_text(encoding="utf-8"))
    missing = []
    for asset in registry.get("assets", []):
        asset_path = Path(asset.get("path", ""))
        if not asset_path.exists():
            missing.append({"id": asset.get("id"), "path": str(asset_path)})
    return {
        "registry_path": str(path),
        "asset_count": len(registry.get("assets", [])),
        "missing_count": len(missing),
        "missing": missing,
    }
