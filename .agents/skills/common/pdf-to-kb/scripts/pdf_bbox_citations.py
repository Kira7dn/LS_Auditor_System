from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any


def normalize_text(value: str | None) -> str:
    value = value or ""
    value = value.casefold()
    value = value.translate(str.maketrans({"“": '"', "”": '"', "‘": "'", "’": "'", "\u00a0": " "}))
    value = re.sub(r"(\w)-\s+(\w)", r"\1\2", value)
    value = re.sub(r"[^0-9a-zà-ỹđ]+", " ", value, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", value).strip()


def text_hash(value: str | None) -> str:
    return hashlib.sha256(normalize_text(value).encode("utf-8")).hexdigest()


def bbox_hash(bbox: list[Any]) -> str:
    if bbox and isinstance(bbox[0], list):
        rounded = [[round(float(item), 2) for item in rect] for rect in bbox]
    else:
        rounded = [round(float(item), 2) for item in bbox]
    return hashlib.sha256(json.dumps(rounded, separators=(",", ":")).encode("utf-8")).hexdigest()[:10]


def citation_key(record: dict[str, Any]) -> tuple[str, str, str, str]:
    return (
        str(record.get("project_id") or ""),
        str(record.get("collection_id") or ""),
        str(record.get("source_id") or ""),
        str(record.get("anchor") or ""),
    )


def load_pdf_citation_index(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    records: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            records.append(json.loads(line))
    return records


def index_by_scope_anchor(records: list[dict[str, Any]]) -> dict[tuple[str, str, str, str], list[dict[str, Any]]]:
    grouped: dict[tuple[str, str, str, str], list[dict[str, Any]]] = {}
    for record in records:
        grouped.setdefault(citation_key(record), []).append(record)
    for group in grouped.values():
        group.sort(key=lambda item: float(item.get("confidence") or 0.0), reverse=True)
    return grouped


def similarity(a: str | None, b: str | None) -> float:
    norm_a = normalize_text(a)
    norm_b = normalize_text(b)
    if not norm_a or not norm_b:
        return 0.0
    if norm_a == norm_b:
        return 1.0
    tokens_a = set(norm_a.split())
    tokens_b = set(norm_b.split())
    if not tokens_a or not tokens_b:
        return 0.0
    return len(tokens_a & tokens_b) / len(tokens_a | tokens_b)


def highlight_file_name(record: dict[str, Any], suffix: str = "png") -> str:
    source_id = str(record.get("source_id") or "source")
    anchor = str(record.get("anchor") or "anchor")
    page_number = int(record.get("page_number") or 0)
    bbox = record.get("bboxes") or record.get("bbox") or [0, 0, 0, 0]
    safe_source = re.sub(r"[^A-Za-z0-9_.-]+", "_", source_id).strip("_")
    safe_anchor = re.sub(r"[^A-Za-z0-9_.-]+", "_", anchor).strip("_")
    return f"{safe_source}__{safe_anchor}__p{page_number}__{bbox_hash(bbox)}.{suffix}"


def dynamic_search_pdf(
    pdf_path: Path,
    page_start: int,
    page_end: int,
    text: str,
) -> dict[str, Any] | None:
    import fitz
    if not pdf_path.exists():
        return None
    
    # Strip leading markdown symbols (headers, blockquotes, list markers)
    cleaned = text.strip()
    cleaned = re.sub(r'^[#*_\->•\s\d.]+\s+', '', cleaned)
    cleaned = cleaned.strip('*_ ')
    
    normalized = normalize_text(cleaned)
    if not normalized or len(normalized) < 6:
        return None
        
    variants = [cleaned]
    if normalized != cleaned:
        variants.append(normalized)
    words = normalized.split()
    if len(words) > 10:
        variants.append(" ".join(words[:10]))
    if len(words) > 6:
        variants.append(" ".join(words[:6]))
        
    deduped = []
    for item in variants:
        if item and item not in deduped:
            deduped.append(item)
            
    with fitz.open(str(pdf_path)) as doc:
        first = max(1, int(page_start or 1))
        last = min(int(page_end or len(doc)), len(doc))
        for variant in deduped:
            if len(normalize_text(variant)) < 6:
                continue
            for page_number in range(first, last + 1):
                page = doc[page_number - 1]
                rects = page.search_for(variant)
                if not rects:
                    continue
                
                bboxes = [[round(rect.x0, 2), round(rect.y0, 2), round(rect.x1, 2), round(rect.y1, 2)] for rect in rects]
                x0 = min(bbox[0] for bbox in bboxes)
                y0 = min(bbox[1] for bbox in bboxes)
                x1 = max(bbox[2] for bbox in bboxes)
                y1 = max(bbox[3] for bbox in bboxes)
                bbox = [round(x0, 2), round(y0, 2), round(x1, 2), round(y1, 2)]
                
                return {
                    "page_number": page_number,
                    "bbox": bbox,
                    "bboxes": bboxes,
                    "matched_pdf_text": cleaned,
                    "searched_text": variant,
                    "match_type": "paragraph",
                    "confidence": 0.95,
                    "ambiguous": len(rects) > 1,
                    "match_count_on_page": len(rects),
                }
    return None


def resolve_pdf_citations(
    citations: list[dict[str, Any]],
    index_records: list[dict[str, Any]],
    *,
    min_confidence: float = 0.55,
    limit: int | None = None,
) -> list[dict[str, Any]]:
    grouped = index_by_scope_anchor(index_records)
    resolved: list[dict[str, Any]] = []
    seen: set[tuple[str, str, int, str]] = set()
    for citation in citations:
        anchor = citation.get("anchor")
        if not anchor:
            continue
        key = citation_key(citation)
        candidates = grouped.get(key)
        if not candidates:
            loose_key = ("", "", "", str(anchor))
            candidates = grouped.get(loose_key, [])

        matched_text = citation.get("matched_text") or citation.get("name") or ""
        best = None
        resolution_similarity = 0.0

        if candidates:
            ranked = sorted(
                candidates,
                key=lambda item: (
                    similarity(matched_text, item.get("matched_pdf_text")),
                    float(item.get("confidence") or 0.0),
                ),
                reverse=True,
            )
            best = dict(ranked[0])
            resolution_similarity = similarity(matched_text, best.get("matched_pdf_text"))

        is_unresolved = not candidates or (len(normalize_text(matched_text)) >= 12 and resolution_similarity == 0.0)
        if is_unresolved:
            # Try dynamic search!
            source_pdf_val = citation.get("source_pdf")
            page_start_val = citation.get("page_start")
            page_end_val = citation.get("page_end")
            resolved_dynamic = False
            if source_pdf_val and page_start_val is not None and page_end_val is not None:
                pdf_path = Path(source_pdf_val)
                if not pdf_path.is_absolute():
                    pdf_path = (Path.cwd() / pdf_path).resolve()
                dynamic_match = dynamic_search_pdf(pdf_path, int(page_start_val), int(page_end_val), matched_text)
                if dynamic_match:
                    best = {
                        "project_id": citation.get("project_id") or "",
                        "collection_id": citation.get("collection_id") or "",
                        "source_id": citation.get("source_id") or "",
                        "anchor": anchor,
                        "markdown_file": citation.get("file_path") or "",
                        "source_pdf": str(pdf_path),
                        "source_pdf_declared": source_pdf_val,
                        "page_start": page_start_val,
                        "page_end": page_end_val,
                        "text_hash": text_hash(matched_text),
                        **dynamic_match,
                    }
                    resolution_similarity = 1.0
                    resolved_dynamic = True
            if not resolved_dynamic:
                if not candidates or (len(normalize_text(matched_text)) >= 12 and resolution_similarity == 0.0):
                    continue

        if float(best.get("confidence") or 0.0) < min_confidence:
            best["pdf_bbox_missing_reason"] = "low_confidence"
            continue
        dedupe_key = (
            str(best.get("source_pdf") or ""),
            str(best.get("anchor") or ""),
            int(best.get("page_number") or 0),
            bbox_hash(best.get("bbox") or [0, 0, 0, 0]),
        )
        if dedupe_key in seen:
            continue
        seen.add(dedupe_key)
        best["citation_anchor"] = anchor
        best["citation_matched_text"] = matched_text
        best["resolution_similarity"] = resolution_similarity
        resolved.append(best)
        if limit is not None and len(resolved) >= limit:
            break
    return resolved
