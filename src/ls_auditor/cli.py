from __future__ import annotations

import argparse
import sys
from pathlib import Path

from ls_auditor.data import (
    compute_variance,
    copy_templates,
    inspect_parquet,
    join_tables,
    normalize_table,
    read_table,
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

    compute = subparsers.add_parser("compute")
    compute.add_argument("--dataset", required=True)
    compute.add_argument("--metric-spec", required=True)
    compute.add_argument("--out")

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

    if args.command == "compute":
        spec = load_json_value(args.metric_spec, default={})
        metrics = compute_variance(args.dataset, spec)
        result = json_result("success", inputs={"dataset": args.dataset, "metric_spec": args.metric_spec}, metrics=metrics)
        if args.out:
            write_json(args.out, result)
            result["outputs"]["result_path"] = args.out
        return result

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
        finding = load_json_value(args.finding, default={})
        metrics = create_evidence_pack(finding, args.out_dir)
        return json_result(
            "success", inputs={"finding": args.finding}, outputs={"evidence_root": metrics["evidence_root"]}, metrics=metrics
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
