from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def inspect_registry(registry_path: str | Path = "asset-index.json") -> dict[str, Any]:
    path = Path(registry_path)
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
