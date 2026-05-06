from __future__ import annotations

import argparse
import sys
from pathlib import Path

from ls_auditor.data import (
    compute_risks,
    copy_templates,
    inspect_parquet,
    join_tables,
    normalize_table,
    prioritize_exceptions,
    read_table,
    render_audit_reports,
    run_rule_tests,
    validate_table,
)
from ls_auditor.evidence import create_evidence_pack
from ls_auditor.io import emit, error_result, json_result, load_json_value, write_json
from ls_auditor.registry import inspect_registry
from ls_auditor.reports import assemble_report, create_chart_artifact


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ls-auditor")
    subparsers = parser.add_subparsers(dest="command", required=True)

    registry = subparsers.add_parser("registry")
    registry_sub = registry.add_subparsers(dest="registry_command", required=True)
    inspect = registry_sub.add_parser("inspect")
    inspect.add_argument("--registry", default="asset-index.json")

    init = subparsers.add_parser("init-case")
    init.add_argument("--case-id", required=True)
    init.add_argument("--template", default="material-planning")
    init.add_argument("--out-root", default="Projects")

    validate = subparsers.add_parser("validate")
    validate.add_argument("--input", required=True)
    validate.add_argument("--schema", required=True)
    validate.add_argument("--out")

    normalize = subparsers.add_parser("normalize")
    normalize.add_argument("--input", required=True)
    normalize.add_argument("--spec", required=True)
    normalize.add_argument("--out", required=True)

    join = subparsers.add_parser("join")
    join.add_argument("--spec", required=True)
    join.add_argument("--out", required=True)

    compute_risks = subparsers.add_parser("compute-risks")
    compute_risks.add_argument("--dataset", required=True)
    compute_risks.add_argument("--risk-spec", required=True)
    compute_risks.add_argument("--out")

    prioritize = subparsers.add_parser("prioritize")
    prioritize.add_argument("--findings", required=True)
    prioritize.add_argument("--top-pct", type=float, default=0.8)
    prioritize.add_argument("--out")

    report = subparsers.add_parser("report")
    report.add_argument("--prioritized-data", required=True)
    report.add_argument("--template-dir", required=True)
    report.add_argument("--out-dir", required=True)

    run_all = subparsers.add_parser("run-all")
    run_all.add_argument("--dataset", required=True)
    run_all.add_argument("--risk-spec", required=True)
    run_all.add_argument("--out-dir", required=True)
    run_all.add_argument("--top-pct", type=float, default=0.8)

    rule_test = subparsers.add_parser("rule-test")
    rule_test.add_argument("--dataset", required=True)
    rule_test.add_argument("--rules", required=True)
    rule_test.add_argument("--out")

    trace = subparsers.add_parser("trace")
    trace.add_argument("--finding", required=True)
    trace.add_argument("--out-dir", required=True)

    inspect_pq = subparsers.add_parser("inspect-parquet")
    inspect_pq.add_argument("--input", required=True)
    inspect_pq.add_argument("--out")

    chart = subparsers.add_parser("chart")
    chart.add_argument("--dataset", required=True)
    chart.add_argument("--out", required=True)

    report = subparsers.add_parser("assemble-report")
    report.add_argument("--case-dir", required=True)
    report.add_argument("--out", required=True)
    return parser


def run(args: argparse.Namespace) -> dict:
    if args.command == "registry":
        metrics = inspect_registry(args.registry)
        return json_result("success", inputs={"registry": args.registry}, metrics=metrics)

    if args.command == "init-case":
        case_root = Path(args.out_root) / args.case_id
        raw = case_root / "raw"
        artifacts = case_root / "artifacts"
        evidence = case_root / "Evidence_Packs"
        working = case_root / "working"
        for directory in [raw, artifacts, evidence, working]:
            directory.mkdir(parents=True, exist_ok=True)
        copied = copy_templates(".agents/templates/auditor", working / "templates")
        return json_result(
            "success",
            inputs={"case_id": args.case_id, "template": args.template},
            outputs={
                "case_dir": str(case_root),
                "raw_dir": str(raw),
                "artifacts_dir": str(artifacts),
                "evidence_dir": str(evidence),
                "copied_templates": copied,
            },
        )

    if args.command == "validate":
        schema = load_json_value(args.schema, default={})
        metrics = validate_table(args.input, schema)
        result = json_result(
            "success" if metrics["valid"] else "error",
            inputs={"input": args.input, "schema": args.schema},
            metrics=metrics,
            errors=[] if metrics["valid"] else [{"error_code": "SCHEMA_MISMATCH", "missing_columns": metrics["missing_columns"]}],
        )
        if args.out:
            write_json(args.out, result)
            result["outputs"]["result_path"] = args.out
        return result

    if args.command == "normalize":
        spec = load_json_value(args.spec, default={})
        metrics = normalize_table(args.input, spec, args.out)
        return json_result(
            "success", inputs={"input": args.input, "spec": args.spec}, outputs={"dataset": args.out}, metrics=metrics
        )

    if args.command == "join":
        spec = load_json_value(args.spec, default={})
        metrics = join_tables(spec, args.out)
        return json_result("success", inputs={"spec": args.spec}, outputs={"dataset": args.out}, metrics=metrics)

    if args.command == "compute-risks":
        spec = load_json_value(args.risk_spec, default={})
        findings = compute_risks(args.dataset, spec)
        result = json_result("success", inputs={"dataset": args.dataset, "risk_spec": args.risk_spec}, metrics={"count": len(findings)}, outputs={"findings": findings})
        if args.out:
            write_json(args.out, result)
        return result

    if args.command == "prioritize":
        findings_data = load_json_value(args.findings, default={})
        # If findings_data is the full json_result from compute-risks
        actual_findings = findings_data.get("outputs", {}).get("findings", []) if isinstance(findings_data, dict) else findings_data
        metrics = prioritize_exceptions(actual_findings, args.top_pct)
        result = json_result("success", inputs={"findings": args.findings, "top_pct": args.top_pct}, metrics=metrics)
        if args.out:
            write_json(args.out, result)
        return result

    if args.command == "report":
        data = load_json_value(args.prioritized_data, default={})
        # Handle the structure returned by prioritize command
        actual_data = data.get("metrics", {}) if "metrics" in data else data
        files = render_audit_reports(actual_data, args.template_dir, args.out_dir)
        return json_result("success", inputs={"prioritized_data": args.prioritized_data, "template_dir": args.template_dir}, outputs={"generated_files": files})

    if args.command == "run-all":
        out_dir = Path(args.out_dir)
        artifacts_dir = out_dir / "artifacts"
        evidence_dir = out_dir / "evidence"
        artifacts_dir.mkdir(parents=True, exist_ok=True)
        
        # 1. Compute Risks
        risk_spec = load_json_value(args.risk_spec, default={})
        findings = compute_risks(args.dataset, risk_spec)
        write_json(artifacts_dir / "audit_findings.json", json_result("success", outputs={"findings": findings}))
        
        # 2. Prioritize
        prioritized_metrics = prioritize_exceptions(findings, args.top_pct)
        prioritized_result = json_result("success", metrics=prioritized_metrics)
        write_json(artifacts_dir / "prioritized_findings.json", prioritized_result)
        
        # 3. Report
        template_dir = Path(".agents/templates/auditor/")
        report_files = render_audit_reports(prioritized_metrics, template_dir, artifacts_dir)
        
        # 4. Trace (Top Findings)
        evidence_files = []
        for finding in prioritized_metrics.get("top_exceptions", [])[:10]: # Trace top 10
            trace_result = create_evidence_pack(finding, evidence_dir)
            evidence_files.extend(trace_result["files"])
            
        return json_result(
            "success", 
            inputs={"dataset": args.dataset, "risk_spec": args.risk_spec},
            outputs={
                "reports": report_files,
                "evidence_count": len(prioritized_metrics.get("top_exceptions", [])[:10]),
                "dossier_root": str(out_dir)
            }
        )

    if args.command == "rule-test":
        rules = load_json_value(args.rules, default={})
        metrics = run_rule_tests(args.dataset, rules)
        result = json_result(
            "success" if metrics["passed"] else "error", inputs={"dataset": args.dataset, "rules": args.rules}, metrics=metrics
        )
        if args.out:
            write_json(args.out, result)
            result["outputs"]["result_path"] = args.out
        return result

    if args.command == "trace":
        data = load_json_value(args.finding, default={})
        
        # Determine if it's a single finding or a list (from prioritized_findings.json)
        findings = []
        if isinstance(data, list):
            findings = data
        elif isinstance(data, dict):
            if "metrics" in data and "top_exceptions" in data["metrics"]:
                findings = data["metrics"]["top_exceptions"]
            elif "outputs" in data and "findings" in data["outputs"]:
                findings = data["outputs"]["findings"]
            else:
                findings = [data]
        
        results = []
        for f in findings:
            results.append(create_evidence_pack(f, args.out_dir))
            
        return json_result(
            "success", 
            inputs={"finding_source": args.finding}, 
            outputs={"evidence_count": len(results), "out_dir": str(args.out_dir)},
            metrics={"count": len(results)}
        )

    if args.command == "inspect-parquet":
        metrics = inspect_parquet(args.input)
        result = json_result("success", inputs={"input": args.input}, metrics=metrics)
        if args.out:
            write_json(args.out, result)
            result["outputs"]["result_path"] = args.out
        return result

    if args.command == "chart":
        frame = read_table(args.dataset)
        summary = {"row_count": int(len(frame)), "columns": list(frame.columns)}
        metrics = create_chart_artifact(summary, args.out)
        return json_result("success", inputs={"dataset": args.dataset}, outputs=metrics, metrics=summary)

    if args.command == "assemble-report":
        metrics = assemble_report(args.case_dir, args.out)
        return json_result("success", inputs={"case_dir": args.case_dir}, outputs={"report": args.out}, metrics=metrics)

    raise ValueError(f"Unsupported command: {args.command}")


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        emit(run(args))
        return 0
    except Exception as exc:
        emit(error_result("COMMAND_FAILED", str(exc), "Check command arguments and input file schema."))
        return 1


if __name__ == "__main__":
    sys.exit(main())
