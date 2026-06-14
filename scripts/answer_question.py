"""
answer_question.py
==================
Evidence-first answer prototype for pdf-to-kb Legal RAG.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


QUERY_GRAPH = Path("C:/Users/kira7/.gemini/config/skills/pdf-to-kb/scripts/query_graph.py")
REFUSAL = "Không tìm thấy căn cứ đủ trong KB để trả lời chắc chắn."
STOPWORDS = {"and", "or", "the", "what", "how", "why", "when", "where", "which", "who", "does", "not", "no", "with"}


def citation_complete(citation: dict[str, Any]) -> bool:
    required = ("file_uri", "anchor", "source_pdf", "page_start", "page_end", "content_hash")
    return all(citation.get(field) not in (None, "") for field in required)


def material_text(citation: dict[str, Any]) -> str:
    text = str(citation.get("matched_text") or "").strip()
    if len(text) < 12:
        return ""
    if text.startswith("<a "):
        return ""
    if text.startswith("#"):
        return ""
    return text


def build_claims(citations: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    claims = []
    seen = set()
    for citation in citations:
        text = material_text(citation)
        if not text or text in seen or not citation_complete(citation):
            continue
        seen.add(text)
        claims.append({"claim": text, "citation": citation})
        if len(claims) >= limit:
            break
    return claims


def unsupported_ascii_tokens(question: str, claims: list[dict[str, Any]]) -> list[str]:
    evidence_text = " ".join(claim["claim"].lower() for claim in claims)
    tokens = [token.lower() for token in __import__("re").findall(r"[A-Za-z][A-Za-z0-9_-]{3,}", question)]
    unsupported = []
    for token in tokens:
        parts = [part for part in token.replace("_", "-").split("-") if part and part not in STOPWORDS]
        if not parts:
            continue
        if any(part not in evidence_text for part in parts):
            unsupported.append(token)
    return unsupported


def run_retrieval(question: str, args: argparse.Namespace) -> dict[str, Any]:
    command = [
        sys.executable,
        str(QUERY_GRAPH),
        "--search",
        question,
        "--kb-dir",
        args.kb_dir,
        "--env",
        args.env,
        "--limit",
        str(args.limit),
        "--project-id",
        args.project_id,
        "--collection-id",
        args.collection_id,
        "--source-id",
        args.source_id,
        "--full-json",
    ]
    proc = subprocess.run(command, check=False, capture_output=True, text=True, encoding="utf-8")
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr or proc.stdout)
    return json.loads(proc.stdout)


def answer_from_payload(question: str, payload: dict[str, Any], claim_limit: int = 3) -> dict[str, Any]:
    citations = payload.get("citations", [])
    claims = build_claims(citations, claim_limit)
    if not claims:
        return {
            "status": "success",
            "refused": True,
            "reason": "no_complete_cited_claims",
            "answer": REFUSAL,
            "claims": [],
            "citations": [],
            "query_metadata": payload.get("query_metadata", {}),
        }
    unsupported = unsupported_ascii_tokens(question, claims)
    if unsupported:
        return {
            "status": "success",
            "refused": True,
            "reason": "unsupported_query_tokens",
            "unsupported_tokens": unsupported,
            "answer": REFUSAL,
            "claims": [],
            "citations": [],
            "query_metadata": payload.get("query_metadata", {}),
            "question": question,
        }
    answer_lines = ["Dựa trên KB hiện có:"]
    for idx, claim in enumerate(claims, start=1):
        answer_lines.append(f"{idx}. {claim['claim']}")
    return {
        "status": "success",
        "refused": False,
        "reason": "",
        "answer": "\n".join(answer_lines),
        "claims": claims,
        "citations": [claim["citation"] for claim in claims],
        "query_metadata": payload.get("query_metadata", {}),
        "question": question,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Answer from KB only when complete citations are available.")
    parser.add_argument("--question", required=True)
    parser.add_argument("--kb-dir", default="Projects/ESG/kb/ghg_protocol")
    parser.add_argument("--env", default=".env")
    parser.add_argument("--project-id", default="esg")
    parser.add_argument("--collection-id", default="")
    parser.add_argument("--source-id", default="")
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--claim-limit", type=int, default=3)
    return parser.parse_args()


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
        args = parse_args()
        payload = run_retrieval(args.question, args)
        print(json.dumps(answer_from_payload(args.question, payload, args.claim_limit), ensure_ascii=False, indent=2))
    except Exception as exc:
        print(json.dumps({"status": "error", "error_code": type(exc).__name__, "message": str(exc)}, ensure_ascii=False, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
