from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from ls_auditor.cli import main


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_registry_inspect_has_no_missing_paths(capsys) -> None:
    assert main(["registry", "inspect", "--registry", "non-existent-registry.json"]) == 0
    result = json.loads(capsys.readouterr().out)
    assert result["status"] == "success"
    assert result["metrics"]["missing"] == []


def test_material_planning_golden_path(tmp_path: Path, capsys) -> None:
    project_root = tmp_path / "Projects"
    assert main(["init-case", "--case-id", "material-planning", "--out-root", str(project_root)]) == 0
    init_result = json.loads(capsys.readouterr().out)
    case_dir = Path(init_result["outputs"]["case_dir"])
    assert (case_dir / "raw").exists()
    assert (case_dir / "working" / "templates" / "final-audit-report.md").exists()

    raw_file = case_dir / "raw" / "purchase.csv"
    raw_file.write_text(
        "\n".join(
            [
                "id,actual_price,target_price,actual_qty,plan_qty,item",
                "PO-1,130,100,12,10,A",
                "PO-2,95,100,8,8,B",
            ]
        ),
        encoding="utf-8",
    )
    raw_before = raw_file.read_text(encoding="utf-8")

    schema = case_dir / "artifacts" / "schema.json"
    schema.write_text(
        json.dumps(
            {"required_columns": ["id", "actual_price", "target_price", "actual_qty", "plan_qty"]},
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    validation_out = case_dir / "artifacts" / "validation.json"
    assert main(["validate", "--input", str(raw_file), "--schema", str(schema), "--out", str(validation_out)]) == 0
    validation = json.loads(capsys.readouterr().out)
    assert validation["status"] == "success"

    normalize_spec = case_dir / "artifacts" / "normalize.json"
    normalize_spec.write_text(json.dumps({"trim_strings": True}), encoding="utf-8")
    unified = case_dir / "artifacts" / "unified.parquet"
    assert main(["normalize", "--input", str(raw_file), "--spec", str(normalize_spec), "--out", str(unified)]) == 0
    assert unified.exists()
    assert raw_file.read_text(encoding="utf-8") == raw_before
    capsys.readouterr()

    metric_spec = case_dir / "artifacts" / "metric.json"
    metric_spec.write_text(json.dumps({"high_risk_price_variance": 0.2}), encoding="utf-8")
    leakage_out = case_dir / "artifacts" / "leakage_analysis.json"
    assert main(["compute", "--dataset", str(unified), "--metric-spec", str(metric_spec), "--out", str(leakage_out)]) == 0
    compute_result = json.loads(capsys.readouterr().out)
    assert compute_result["status"] == "success"
    assert compute_result["metrics"]["finding_count"] == 1
    assert read_json(leakage_out)["metrics"]["total_leakage"] == 260.0

    rules = case_dir / "artifacts" / "rules.json"
    rules.write_text(
        json.dumps({"rules": [{"id": "PRICE_MAX", "type": "max", "column": "actual_price", "value": 200}]}),
        encoding="utf-8",
    )
    assert main(["rule-test", "--dataset", str(unified), "--rules", str(rules)]) == 0
    rule_result = json.loads(capsys.readouterr().out)
    assert rule_result["status"] == "success"

    finding = case_dir / "artifacts" / "finding.json"
    finding.write_text(
        json.dumps(
            {
                "id": "FIND-001",
                "condition": "Actual price exceeds target price.",
                "criteria": "Price variance should stay within threshold.",
                "leakage": 260,
                "evidence": str(leakage_out),
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    assert main(["trace", "--finding", str(finding), "--out-dir", str(case_dir / "Evidence_Packs")]) == 0
    trace_result = json.loads(capsys.readouterr().out)
    assert Path(trace_result["outputs"]["evidence_root"], "FINDING.md").exists()

    chart = case_dir / "artifacts" / "chart.md"
    assert main(["chart", "--dataset", str(unified), "--out", str(chart)]) == 0
    assert chart.exists()

    report = case_dir / "FINAL_AUDIT_REPORT.md"
    assert main(["assemble-report", "--case-dir", str(case_dir), "--out", str(report)]) == 0
    assert report.exists()


def test_join_and_inspect_parquet(tmp_path: Path, capsys) -> None:
    left = tmp_path / "left.csv"
    right = tmp_path / "right.csv"
    pd.DataFrame([{"id": "A", "qty": 1}]).to_csv(left, index=False)
    pd.DataFrame([{"id": "A", "price": 10}]).to_csv(right, index=False)
    spec = tmp_path / "join.json"
    spec.write_text(
        json.dumps(
            {
                "inputs": [{"name": "left", "path": str(left)}, {"name": "right", "path": str(right)}],
                "joins": [{"left": "left", "right": "right", "on": "id", "how": "left"}],
            }
        ),
        encoding="utf-8",
    )
    out = tmp_path / "joined.parquet"
    assert main(["join", "--spec", str(spec), "--out", str(out)]) == 0
    assert out.exists()
    capsys.readouterr()
    assert main(["inspect-parquet", "--input", str(out)]) == 0
    result = json.loads(capsys.readouterr().out)
    assert result["status"] == "success"
    assert result["metrics"]["row_count"] == 1
