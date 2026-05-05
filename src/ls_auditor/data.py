from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any

import pandas as pd


def read_table(path: str | Path) -> pd.DataFrame:
    source = Path(path)
    suffix = source.suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(source)
    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(source)
    if suffix == ".json":
        return pd.read_json(source)
    if suffix == ".parquet":
        return pd.read_parquet(source)
    raise ValueError(f"Unsupported tabular input type: {source.suffix}")


def write_table(frame: pd.DataFrame, path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    suffix = target.suffix.lower()
    if suffix == ".csv":
        frame.to_csv(target, index=False)
    elif suffix == ".json":
        frame.to_json(target, orient="records", force_ascii=False, indent=2)
    elif suffix == ".parquet":
        frame.to_parquet(target, index=False)
    else:
        raise ValueError(f"Unsupported tabular output type: {target.suffix}")
    return target


def validate_table(input_path: str | Path, schema: dict[str, Any]) -> dict[str, Any]:
    frame = read_table(input_path)
    required = schema.get("required_columns", [])
    missing = [column for column in required if column not in frame.columns]
    null_counts = frame.isna().sum().to_dict()
    duplicate_rows = int(frame.duplicated().sum())
    return {
        "valid": not missing,
        "row_count": int(len(frame)),
        "column_count": int(len(frame.columns)),
        "columns": list(frame.columns),
        "missing_columns": missing,
        "null_counts": {str(k): int(v) for k, v in null_counts.items()},
        "duplicate_rows": duplicate_rows,
    }


def normalize_table(input_path: str | Path, spec: dict[str, Any], out_path: str | Path) -> dict[str, Any]:
    frame = read_table(input_path)
    original_columns = list(frame.columns)
    if "rename" in spec:
        frame = frame.rename(columns=spec["rename"])
    for column, dtype in spec.get("dtypes", {}).items():
        if column in frame.columns:
            if dtype in {"datetime", "date"}:
                frame[column] = pd.to_datetime(frame[column], errors="coerce")
            else:
                frame[column] = frame[column].astype(dtype)
    if spec.get("trim_strings", True):
        for column in frame.select_dtypes(include=["object", "string"]).columns:
            frame[column] = frame[column].astype(str).str.strip()
    target = write_table(frame, out_path)
    return {
        "output_path": str(target),
        "row_count": int(len(frame)),
        "original_columns": original_columns,
        "normalized_columns": list(frame.columns),
    }


def join_tables(spec: dict[str, Any], out_path: str | Path) -> dict[str, Any]:
    inputs = {item["name"]: read_table(item["path"]) for item in spec.get("inputs", [])}
    if not inputs:
        raise ValueError("Join spec must include at least one input table.")
    joins = spec.get("joins", [])
    if not joins:
        first_name = next(iter(inputs))
        result = inputs[first_name]
    else:
        first_join = joins[0]
        result = inputs[first_join["left"]]
        for join in joins:
            right = inputs[join["right"]]
            result = result.merge(right, how=join.get("how", "left"), on=join["on"])
    target = write_table(result, out_path)
    return {
        "output_path": str(target),
        "row_count": int(len(result)),
        "column_count": int(len(result.columns)),
        "columns": list(result.columns),
    }


def compute_variance(dataset: str | Path, metric_spec: dict[str, Any]) -> dict[str, Any]:
    frame = read_table(dataset)
    price_actual = metric_spec.get("actual_price", "actual_price")
    price_target = metric_spec.get("target_price", "target_price")
    qty_actual = metric_spec.get("actual_qty", "actual_qty")
    qty_plan = metric_spec.get("plan_qty", "plan_qty")
    id_column = metric_spec.get("id", "id")
    threshold = float(metric_spec.get("high_risk_price_variance", 0.2))
    required = [price_actual, price_target, qty_actual, qty_plan]
    missing = [column for column in required if column not in frame.columns]
    if missing:
        raise ValueError(f"Dataset missing required metric columns: {missing}")
    target = frame[price_target].replace(0, pd.NA)
    frame = frame.copy()
    frame["price_variance"] = frame[price_actual] - frame[price_target]
    frame["price_variance_pct"] = (frame["price_variance"] / target).fillna(0)
    frame["quantity_variance"] = frame[qty_actual] - frame[qty_plan]
    frame["leakage"] = frame["quantity_variance"].clip(lower=0) * frame[price_actual]
    frame["risk_status"] = frame["price_variance_pct"].apply(lambda value: "HIGH_RISK" if value > threshold else "NORMAL")
    findings = frame[frame["risk_status"] == "HIGH_RISK"]
    return {
        "row_count": int(len(frame)),
        "finding_count": int(len(findings)),
        "total_leakage": float(frame["leakage"].sum()),
        "findings": [
            {
                "id": str(row.get(id_column, index)),
                "price_variance_pct": float(row["price_variance_pct"]),
                "quantity_variance": float(row["quantity_variance"]),
                "leakage": float(row["leakage"]),
                "risk_status": row["risk_status"],
            }
            for index, row in findings.iterrows()
        ],
    }


def run_rule_tests(dataset: str | Path, rules: dict[str, Any]) -> dict[str, Any]:
    frame = read_table(dataset)
    failures: list[dict[str, Any]] = []
    for rule in rules.get("rules", []):
        column = rule["column"]
        if column not in frame.columns:
            failures.append({"rule_id": rule["id"], "error": f"Missing column {column}"})
            continue
        if rule["type"] == "max":
            bad = frame[frame[column] > rule["value"]]
        elif rule["type"] == "min":
            bad = frame[frame[column] < rule["value"]]
        elif rule["type"] == "not_null":
            bad = frame[frame[column].isna()]
        else:
            failures.append({"rule_id": rule["id"], "error": f"Unsupported rule type {rule['type']}"})
            continue
        if not bad.empty:
            failures.append({"rule_id": rule["id"], "failed_rows": int(len(bad))})
    return {"passed": not failures, "failure_count": len(failures), "failures": failures}


def inspect_parquet(path: str | Path) -> dict[str, Any]:
    frame = pd.read_parquet(path)
    return {
        "row_count": int(len(frame)),
        "column_count": int(len(frame.columns)),
        "columns": [{"name": str(name), "dtype": str(dtype)} for name, dtype in frame.dtypes.items()],
        "preview": json.loads(frame.head(5).to_json(orient="records", force_ascii=False)),
    }


def copy_templates(template_dir: str | Path, target_dir: str | Path) -> list[str]:
    source = Path(template_dir)
    target = Path(target_dir)
    target.mkdir(parents=True, exist_ok=True)
    copied: list[str] = []
    for template in source.glob("*.md"):
        destination = target / template.name
        shutil.copyfile(template, destination)
        copied.append(str(destination))
    return copied
