import argparse
import json
import sys
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
    parser = argparse.ArgumentParser(description="LS Auditor: ROI & Payback Calculator")
    parser.add_argument("--investment", type=float, required=True, help="Total investment cost")
    parser.add_argument("--savings", type=float, required=True, help="Annual savings")

    args = parser.parse_args()

    try:
        results = calculate_roi(args.investment, args.savings)

        # Output strictly JSON to stdout
        print(
            json.dumps(
                {"status": "success", "investment": args.investment, "annual_savings": args.savings, "metrics": results}, indent=2
            )
        )

    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}))
        sys.exit(1)


if __name__ == "__main__":
    main()
