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


def compute_risks(dataset: str | Path, risk_spec: dict[str, Any]) -> list[dict[str, Any]]:
    frame = read_table(dataset)
    findings = []
    
    for risk in risk_spec.get("risks", []):
        risk_id = risk["id"]
        condition = risk["condition"]
        leakage_expr = risk.get("leakage_expr")
        severity = risk.get("severity", "Medium")
        
        try:
            # Query the dataframe for rows matching the condition
            bad_rows = frame.query(condition).copy()
            
            if not bad_rows.empty:
                # Calculate leakage if expression is provided
                if leakage_expr:
                    # Using eval to calculate leakage based on the expression
                    bad_rows["leakage"] = bad_rows.eval(leakage_expr)
                else:
                    bad_rows["leakage"] = 0.0
                
                for index, row in bad_rows.iterrows():
                    finding = {
                        "risk_id": risk_id,
                        "type": risk["name"],
                        "leakage": float(row["leakage"]),
                        "severity": severity,
                        "evidence": f"Condition met: {condition}",
                        "row_index": int(index)
                    }
                    # Include metadata if provided
                    if "metadata" in risk:
                        finding.update(risk["metadata"])
                        
                    # Include some context IDs if they exist
                    for id_col in ["pr_id", "po_id", "material_id", "plan_id"]:
                        if id_col in row:
                            finding[id_col] = str(row[id_col])
                            
                    findings.append(finding)
        except Exception as e:
            # Skip risks with invalid expressions/missing columns
            continue
            
    return findings


def prioritize_exceptions(findings: list[dict[str, Any]], top_pct: float = 0.8) -> dict[str, Any]:
    if not findings:
        return {"top_exceptions": [], "risk_summary": {}, "total_leakage": 0}
        
    df = pd.DataFrame(findings)
    # Deduplicate by key IDs if possible, but for generic we use index + risk_id
    
    total_leakage = df["leakage"].sum()
    df = df.sort_values(by="leakage", ascending=False)
    df["cum_leakage"] = df["leakage"].cumsum()
    df["cum_pct"] = df["cum_leakage"] / total_leakage if total_leakage > 0 else 0
    
    top_findings = df[df["cum_pct"] <= top_pct].to_dict(orient="records")
    risk_summary_df = df.groupby("type").agg({"leakage": ["sum", "mean", "count"]})
    risk_summary_df.columns = ["total_leakage", "avg_leakage", "count"]
    risk_summary = risk_summary_df.to_dict(orient="index")
    
    return {
        "total_leakage": float(total_leakage),
        "top_exceptions": top_findings,
        "risk_summary": risk_summary,
        "critical_count": len(top_findings)
    }


def render_audit_reports(prioritized_data: dict[str, Any], template_dir: str | Path, output_dir: str | Path) -> list[str]:
    template_dir = Path(template_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    generated_files = []
    
    # 1. Candidate Exceptions Report
    exc_template_path = template_dir / "candidate-exceptions.md"
    if exc_template_path.exists():
        content = exc_template_path.read_text(encoding="utf-8")
        content = content.replace("[total_leakage]", f"{prioritized_data['total_leakage']:,.2f}")
        content = content.replace("[critical_count]", str(prioritized_data['critical_count']))
        
        # Build table rows
        rows = []
        for find in prioritized_data.get("top_exceptions", [])[:20]:
            fid = f"{find.get('risk_id')[:3]}-{find.get('pr_id', 'N/A')}-{find.get('material_id', 'N/A')}"
            action = "Confirm" if find.get('severity') == "High" else "Investigate"
            row = f"| {fid} | {find['type']} | ${find['leakage']:,.2f} | {find['evidence']} | {action} | {find['severity']} |"
            rows.append(row)
        
        content = content.replace("| [Finding ID] | [Risk Type] | $[Amount] | [Evidence Snippet] | [Investigate/Trace/Confirm] | [High/Medium/Low] |", "\n".join(rows))
        
        out_path = output_dir / "candidate-exceptions.md"
        out_path.write_text(content, encoding="utf-8")
        generated_files.append(str(out_path))

    # 2. Risk Register Report
    reg_template_path = template_dir / "risk-register.md"
    if reg_template_path.exists():
        content = reg_template_path.read_text(encoding="utf-8")
        
        rows = []
        for rtype, rdata in prioritized_data.get("risk_summary", {}).items():
            priority = "🔴 High" if rdata['total_leakage'] > 50000 else "🟡 Medium"
            hypothesis = "Phân tích thêm nguyên nhân gốc rễ"
            row = f"| {rtype} | {rdata['count']} | ${rdata['total_leakage']:,.2f} | ${rdata['avg_leakage']:,.2f} | {priority} | {hypothesis} |"
            rows.append(row)
            
        content = content.replace("| [Risk Type] | [Count] | $[Total] | $[Avg] | [Priority] | [Hypothesis] |", "\n".join(rows))
        
        out_path = output_dir / "risk-register.md"
        out_path.write_text(content, encoding="utf-8")
        generated_files.append(str(out_path))
        
    return generated_files


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
    columns_info = []
    stats = {}
    
    for name, dtype in frame.dtypes.items():
        col_name = str(name)
        columns_info.append({"name": col_name, "dtype": str(dtype)})
        
        # Thống kê nghiệp vụ cơ bản
        col_stats = {"null_count": int(frame[name].isna().sum())}
        
        # Nếu là ID hoặc Object, đếm giá trị duy nhất
        if col_name.endswith("_id") or str(dtype) == "object":
            col_stats["unique_count"] = int(frame[name].nunique())
            
        # Nếu là số, tính sum/mean/min/max
        if pd.api.types.is_numeric_dtype(dtype):
            col_stats.update({
                "sum": float(frame[name].sum()) if not frame[name].isna().all() else 0,
                "mean": float(frame[name].mean()) if not frame[name].isna().all() else 0,
                "min": float(frame[name].min()) if not frame[name].isna().all() else 0,
                "max": float(frame[name].max()) if not frame[name].isna().all() else 0
            })
        
        stats[col_name] = col_stats

    return {
        "row_count": int(len(frame)),
        "column_count": int(len(frame.columns)),
        "columns": columns_info,
        "statistics": stats,
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
