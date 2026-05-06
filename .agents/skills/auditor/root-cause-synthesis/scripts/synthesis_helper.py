import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", stream=sys.stderr)


def load_json_input(input_val: str) -> Any:
    """Loads JSON from a file path or a raw JSON string."""
    if Path(input_val).exists():
        with open(input_val, "r", encoding="utf-8") as f:
            return json.load(f)
    try:
        return json.loads(input_val)
    except json.JSONDecodeError:
        raise ValueError(f"Input is neither a valid file path nor a valid JSON string: {input_val[:50]}...")


def extract_exception_list(data: Any) -> List[Dict[str, Any]]:
    """Extracts a list of exceptions from various possible JSON structures."""
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        # Common patterns in LS Auditor
        if "metrics" in data and "top_exceptions" in data["metrics"]:
            return data["metrics"]["top_exceptions"]
        if "outputs" in data and "findings" in data["outputs"]:
            return data["outputs"]["findings"]
        if "findings" in data:
            return data["findings"]
    return []


def group_exceptions(exceptions: List[Dict[str, Any]], category_map: Dict[str, str]) -> Dict[str, List[str]]:
    """Gộp các ngoại lệ riêng lẻ thành các nhóm danh mục hệ thống."""
    synthesis = {}
    for exc in exceptions:
        risk_type = exc.get("type") or exc.get("risk_id", "Unclassified")
        category = category_map.get(risk_type, "Unclassified")
        if category not in synthesis:
            synthesis[category] = []
        
        # ID discovery priority
        exc_id = exc.get("id") or exc.get("pr_id") or exc.get("po_id") or "Unknown"
        synthesis[category].append(exc_id)
    return synthesis


def identify_systemic_risk(synthesis: Dict[str, List[str]], threshold: int = 3) -> List[Dict[str, Any]]:
    """Xác định các rủi ro hệ thống dựa trên số lượng ngoại lệ vượt ngưỡng."""
    systemic_risks = []
    for category, ids in synthesis.items():
        unique_ids = list(set(ids))
        if len(ids) >= threshold:
            systemic_risks.append(
                {
                    "category": category,
                    "total_count": len(ids),
                    "unique_count": len(unique_ids),
                    "severity": "CRITICAL" if len(ids) > 10 else "WARNING",
                    "sample_exception_ids": unique_ids[:10],
                }
            )
    return systemic_risks


def main():
    parser = argparse.ArgumentParser(description="LS Auditor: Root Cause Synthesis Helper (Generic)")
    parser.add_argument("--exceptions", type=str, required=True, help="Path to JSON file or JSON string of exceptions")
    parser.add_argument("--category_map", type=str, required=True, help="Path to JSON file or JSON string of category mapping")
    parser.add_argument("--threshold", type=int, default=3, help="Threshold to identify systemic risk")
    parser.add_argument("--out", type=str, help="Optional output file path")

    args = parser.parse_args()

    try:
        raw_exceptions = load_json_input(args.exceptions)
        exceptions = extract_exception_list(raw_exceptions)
        category_map = load_json_input(args.category_map)

        if not exceptions:
            logging.warning("No exceptions found in the input data.")

        grouped = group_exceptions(exceptions, category_map)
        risks = identify_systemic_risk(grouped, args.threshold)

        result = {
            "status": "success", 
            "systemic_risks": risks, 
            "grouped_exceptions_summary": {k: len(v) for k, v in grouped.items()}
        }

        output_json = json.dumps(result, indent=2, ensure_ascii=False)
        print(output_json)

        if args.out:
            Path(args.out).parent.mkdir(parents=True, exist_ok=True)
            with open(args.out, "w", encoding="utf-8") as f:
                f.write(output_json)
            logging.info(f"Results saved to {args.out}")

    except Exception as e:
        logging.error(f"Synthesis failed: {str(e)}")
        print(json.dumps({"status": "error", "message": str(e)}))
        sys.exit(1)


if __name__ == "__main__":
    main()
