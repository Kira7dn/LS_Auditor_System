import json
import logging
import argparse
import sys
from typing import List, Dict, Any

# Cấu hình logging ra stderr để không làm bẩn stdout (dành cho JSON)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stderr
)

def calculate_variance(actual: float, plan: float) -> tuple[float, float]:
    """
    Tính toán sai lệch tuyệt đối và tỷ lệ phần trăm.
    """
    abs_var = actual - plan
    pct_var = abs_var / plan if plan != 0 else 0
    return abs_var, pct_var

def calculate_leakage(variance_qty: float, unit_price: float) -> float:
    """
    Tính toán rò rỉ tài chính dựa trên sai lệch số lượng.
    """
    if variance_qty > 0:
        return variance_qty * unit_price
    return 0.0

def run_analysis(data_list: List[Dict[str, Any]], thresholds: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Phân tích danh sách giao dịch và xác định mức độ rủi ro.
    """
    findings = []
    for item in data_list:
        try:
            abs_v, p_var = calculate_variance(item['actual_price'], item['target_price'])
            leakage = calculate_leakage(item['actual_qty'] - item['plan_qty'], item['actual_price'])
            
            status = "NORMAL"
            if p_var > thresholds['price_variance']['high_risk']:
                status = "HIGH_RISK"
            elif p_var > thresholds['price_variance']['medium_risk']:
                status = "MEDIUM_RISK"
                
            findings.append({
                "id": item['id'],
                "p_var": p_var,
                "p_var_pct": f"{p_var:.2%}",
                "leakage": leakage,
                "status": status
            })
        except KeyError as e:
            logging.error(f"Missing key in data item: {e}")
            continue
            
    return findings

def main():
    parser = argparse.ArgumentParser(description="LS Auditor: Variance & Leakage Calculator")
    parser.add_argument("--data", type=str, help="JSON string hoặc đường dẫn file chứa dữ liệu giao dịch")
    parser.add_argument("--thresholds", type=str, help="JSON string chứa các ngưỡng rủi ro")
    
    args = parser.parse_args()
    
    try:
        # Load dữ liệu từ input (Hỗ trợ cả JSON string trực tiếp từ AI)
        data = json.loads(args.data) if args.data else []
        thresholds = json.loads(args.thresholds) if args.thresholds else {
            "price_variance": {"high_risk": 0.2, "medium_risk": 0.1}
        }
        
        if not data:
            logging.warning("No data provided for analysis.")
            print(json.dumps({"status": "success", "data": []}))
            return

        results = run_analysis(data, thresholds)
        
        # Output duy nhất là JSON qua stdout
        print(json.dumps({
            "status": "success",
            "count": len(results),
            "findings": results
        }, indent=2))
        
    except Exception as e:
        logging.error(f"Analysis failed: {str(e)}")
        print(json.dumps({
            "status": "error",
            "message": str(e)
        }))
        sys.exit(1)

if __name__ == "__main__":
    main()
