from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


def json_result(
    status: str,
    *,
    inputs: dict[str, Any] | None = None,
    outputs: dict[str, Any] | None = None,
    metrics: dict[str, Any] | None = None,
    warnings: list[str] | None = None,
    errors: list[str] | None = None,
    **extra: Any,
) -> dict[str, Any]:
    result: dict[str, Any] = {
        "status": status,
        "inputs": inputs or {},
        "outputs": outputs or {},
        "metrics": metrics or {},
        "warnings": warnings or [],
        "errors": errors or [],
    }
    result.update(extra)
    return result


def error_result(error_code: str, message: str, suggestion: str = "") -> dict[str, Any]:
    return {
        "status": "error",
        "error_code": error_code,
        "message": message,
        "suggestion": suggestion,
    }


def emit(result: dict[str, Any]) -> None:
    sys.stdout.buffer.write(json.dumps(result, ensure_ascii=False, indent=2).encode("utf-8"))
    sys.stdout.buffer.write(b"\n")


def load_json_value(value: str | None, *, default: Any = None) -> Any:
    if value is None:
        return default
    candidate = Path(value)
    if candidate.exists():
        return json.loads(candidate.read_text(encoding="utf-8"))
    return json.loads(value)


def write_json(path: str | Path, value: Any) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")
    return target


def stderr(message: str) -> None:
    print(message, file=sys.stderr)
