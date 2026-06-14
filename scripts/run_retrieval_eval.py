"""
run_retrieval_eval.py
=====================
Run a compact retrieval evaluation set against pdf-to-kb query_graph.py.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


QUERY_GRAPH = Path("C:/Users/kira7/.gemini/config/skills/pdf-to-kb/scripts/query_graph.py")


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def citation_complete(citation: dict[str, Any]) -> bool:
    required = ("file_uri", "anchor", "source_pdf", "page_start", "page_end", "content_hash")
    return all(citation.get(field) not in (None, "") for field in required)


def score_result(payload: dict[str, Any], expected_concepts: list[str], expected_anchors: list[str]) -> dict[str, Any]:
    results = payload.get("results", [])
    citations = payload.get("citations", [])
    graph_ids = [item.get("id") for item in results if item.get("id")]
    anchors = [item.get("anchor") for item in citations if item.get("anchor")]
    top1_pool = []
    if graph_ids:
        top1_pool.append(graph_ids[0])
    if anchors:
        top1_pool.append(anchors[0])
    top5_pool = set(graph_ids[:5]) | set(anchors[:5])
    complete_citations = [citation for citation in citations if citation_complete(citation)]
    return {
        "top_1_hit": bool(set(top1_pool) & (set(expected_concepts) | set(expected_anchors))),
        "top_5_hit": bool(top5_pool & (set(expected_concepts) | set(expected_anchors))),
        "anchor_hit": bool(set(anchors) & set(expected_anchors)),
        "concept_hit": bool(set(graph_ids) & set(expected_concepts)),
        "citation_complete": bool(complete_citations),
        "graph_ids": graph_ids[:5],
        "anchors": anchors[:5],
        "complete_citation_count": len(complete_citations),
    }


def run_query(question: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    query = question.get("query") or question["question"]
    command = [
        sys.executable,
        str(QUERY_GRAPH),
        "--search",
        query,
        "--kb-dir",
        args.kb_dir,
        "--env",
        args.env,
        "--limit",
        str(args.top_k),
        "--project-id",
        args.project_id,
        "--collection-id",
        args.collection_id,
        "--source-id",
        args.source_id,
    ]
    if args.full_query_json:
        command.append("--full-json")
    proc = subprocess.run(command, check=False, capture_output=True, text=True, encoding="utf-8")
    if proc.returncode != 0:
        return {"status": "error", "query": query, "stderr": proc.stderr, "stdout": proc.stdout}
    payload = json.loads(proc.stdout)
    return {"status": "success", "query": query, "payload": payload}


def render_markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines = [
        "# Retrieval Eval Report",
        "",
        "| Metric | Value |",
        "|---|---:|",
    ]
    for key, value in summary.items():
        lines.append(f"| `{key}` | {value} |")
    lines.extend(["", "## Cases", ""])
    for item in report["cases"]:
        marker = "PASS" if item["top_5_hit"] and item["citation_complete"] else "FAIL"
        lines.append(
            f"- `{marker}` `{item['id']}`: top5=`{item['top_5_hit']}`, "
            f"anchor=`{item['anchor_hit']}`, concept=`{item['concept_hit']}`, "
            f"citations=`{item['complete_citation_count']}`"
        )
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run retrieval eval for pdf-to-kb Legal RAG.")
    parser.add_argument("--questions", default="Projects/ESG/eval/retrieval_questions.jsonl")
    parser.add_argument("--kb-dir", default="Projects/ESG/kb/ghg_protocol")
    parser.add_argument("--env", default=".env")
    parser.add_argument("--project-id", default="esg")
    parser.add_argument("--collection-id", default="")
    parser.add_argument("--source-id", default="")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--out-json", default="Projects/ESG/eval/retrieval_eval_report.json")
    parser.add_argument("--out-md", default="Projects/ESG/eval/retrieval_eval_report.md")
    parser.add_argument("--full-query-json", action="store_true")
    return parser.parse_args()


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
        args = parse_args()
        questions = load_jsonl(Path(args.questions))
        cases = []
        for question in questions:
            result = run_query(question, args)
            if result["status"] != "success":
                cases.append({"id": question["id"], "status": "error", "query": result["query"], "error": result})
                continue
            score = score_result(
                result["payload"],
                question.get("expected_concepts", []),
                question.get("expected_anchors", []),
            )
            cases.append(
                {
                    "id": question["id"],
                    "question": question["question"],
                    "query": result["query"],
                    "status": "success",
                    **score,
                }
            )
        total = len(cases)
        successful = [case for case in cases if case.get("status") == "success"]
        summary = {
            "question_count": total,
            "successful_query_count": len(successful),
            "top_1_hit_rate": round(sum(1 for case in successful if case["top_1_hit"]) / max(1, total), 3),
            "top_5_hit_rate": round(sum(1 for case in successful if case["top_5_hit"]) / max(1, total), 3),
            "anchor_hit_rate": round(sum(1 for case in successful if case["anchor_hit"]) / max(1, total), 3),
            "concept_hit_rate": round(sum(1 for case in successful if case["concept_hit"]) / max(1, total), 3),
            "citation_complete_rate": round(sum(1 for case in successful if case["citation_complete"]) / max(1, total), 3),
        }
        report = {
            "status": "success",
            "scope": {
                "project_id": args.project_id,
                "collection_id": args.collection_id,
                "source_id": args.source_id,
            },
            "summary": summary,
            "cases": cases,
        }
        out_json = Path(args.out_json)
        out_md = Path(args.out_md)
        out_json.parent.mkdir(parents=True, exist_ok=True)
        out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
        out_md.write_text(render_markdown(report), encoding="utf-8", newline="\n")
        print(json.dumps({"status": "success", "summary": summary, "report_json": str(out_json), "report_markdown": str(out_md)}, ensure_ascii=False, indent=2))
    except Exception as exc:
        print(json.dumps({"status": "error", "error_code": type(exc).__name__, "message": str(exc)}, ensure_ascii=False, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
