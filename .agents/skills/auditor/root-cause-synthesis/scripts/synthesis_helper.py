import json
import argparse
import sys
import logging
from typing import List, Dict, Any

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', stream=sys.stderr)

def group_exceptions(exceptions: List[Dict[str, Any]], category_map: Dict[str, str]) -> Dict[str, List[str]]:
    """Gộp các ngoại lệ riêng lẻ thành các nhóm danh mục hệ thống."""
    synthesis = {}
    for exc in exceptions:
        category = category_map.get(exc['type'], "Unclassified")
        if category not in synthesis:
            synthesis[category] = []
        synthesis[category].append(exc['id'])
    return synthesis

def identify_systemic_risk(synthesis: Dict[str, List[str]], threshold: int = 3) -> List[Dict[str, Any]]:
    """Xác định các rủi ro hệ thống dựa trên số lượng ngoại lệ vượt ngưỡng."""
    systemic_risks = []
    for category, ids in synthesis.items():
        if len(ids) >= threshold:
            systemic_risks.append({
                "category": category,
                "count": len(ids),
                "severity": "CRITICAL" if len(ids) > 5 else "WARNING",
                "exception_ids": ids
            })
    return systemic_risks

def main():
    parser = argparse.ArgumentParser(description="LS Auditor: Root Cause Synthesis Helper")
    parser.add_argument("--exceptions", type=str, required=True, help="JSON string danh sách ngoại lệ")
    parser.add_argument("--category_map", type=str, required=True, help="JSON string bản đồ phân loại rủi ro")
    parser.add_argument("--threshold", type=int, default=3, help="Ngưỡng để xác định rủi ro hệ thống")
    
    args = parser.parse_args()
    
    try:
        exceptions = json.loads(args.exceptions)
        category_map = json.loads(args.category_map)
        
        grouped = group_exceptions(exceptions, category_map)
        risks = identify_systemic_risk(grouped, args.threshold)
        
        print(json.dumps({
            "status": "success",
            "systemic_risks": risks,
            "grouped_exceptions": grouped
        }, indent=2))
        
    except Exception as e:
        logging.error(f"Synthesis failed: {str(e)}")
        print(json.dumps({"status": "error", "message": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
