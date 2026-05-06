import argparse
import json
import sys
from pathlib import Path
from typing import Dict


def calculate_roi(investment: float, annual_savings: float) -> Dict[str, float]:
    """
    Calculates ROI and Payback period.

    Args:
        investment: Total cost of the solution.
        annual_savings: Estimated annual financial recovery.

    Returns:
        A dictionary with roi_percent and payback_months.
    """
    roi = (annual_savings / investment) * 100 if investment > 0 else 0
    payback_months = (investment / (annual_savings / 12)) if annual_savings > 0 else 0
    return {"roi_percent": round(roi, 2), "payback_months": round(payback_months, 1)}


def main():
    parser = argparse.ArgumentParser(description="LS Auditor: ROI & Payback Calculator (Generic)")
    parser.add_argument("--investment", type=float, required=True, help="Total investment cost")
    parser.add_argument("--savings", type=float, required=True, help="Annual savings")
    parser.add_argument("--out", type=str, help="Optional output file path")

    args = parser.parse_args()

    try:
        results = calculate_roi(args.investment, args.savings)
        result_dict = {
            "status": "success", 
            "investment": args.investment, 
            "annual_savings": args.savings, 
            "metrics": results
        }

        output_json = json.dumps(result_dict, indent=2)
        print(output_json)

        if args.out:
            Path(args.out).parent.mkdir(parents=True, exist_ok=True)
            with open(args.out, "w", encoding="utf-8") as f:
                f.write(output_json)

    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}))
        sys.exit(1)


if __name__ == "__main__":
    main()
