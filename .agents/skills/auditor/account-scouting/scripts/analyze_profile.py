import argparse
import json
import logging
import os
import sys
from pathlib import Path
from typing import Any, Dict, List

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", stream=sys.stderr)


class ProfileAnalyzer:
    """Hỗ trợ Agent phân tích hồ sơ khách hàng để nhận diện rủi ro."""

    def __init__(self, industry_risk_path: str):
        if not os.path.exists(industry_risk_path):
            raise FileNotFoundError(f"Industry risk file not found: {industry_risk_path}")
        with open(industry_risk_path, "r", encoding="utf-8") as f:
            self.industry_data = json.load(f)

    def scan_for_keywords(self, text: str, industry_key: str) -> List[Dict[str, Any]]:
        """Tìm kiếm các từ khóa rủi ro đặc thù của ngành trong văn bản."""
        risks_found = []
        if industry_key not in self.industry_data["industries"]:
            logging.warning(f"Industry key '{industry_key}' not found in database.")
            return risks_found

        industry = self.industry_data["industries"][industry_key]
        for hotspot in industry.get("risk_hotspots", []):
            if hotspot["area"].lower() in text.lower():
                risks_found.append(hotspot)

        return risks_found


def main():
    parser = argparse.ArgumentParser(description="LS Auditor: Account Profile Analyzer")
    parser.add_argument("--client", type=str, required=True, help="Tên khách hàng")
    parser.add_argument("--industry", type=str, required=True, help="Mã ngành (e.g., garment_and_textile)")
    parser.add_argument("--text", type=str, required=True, help="Văn bản hồ sơ khách hàng")
    parser.add_argument("--db_path", type=str, default=None, help="Đường dẫn file industry_risks.json")

    args = parser.parse_args()

    # Xác định đường dẫn DB mặc định
    db_path = args.db_path or os.path.join(os.path.dirname(__file__), "../resources/industry_risks.json")

    try:
        profile_text = Path(args.text).read_text(encoding="utf-8") if Path(args.text).exists() else args.text
        analyzer = ProfileAnalyzer(db_path)
        risks = analyzer.scan_for_keywords(profile_text, args.industry)

        print(
            json.dumps(
                {
                    "status": "success",
                    "client": args.client,
                    "industry": args.industry,
                    "findings_count": len(risks),
                    "risks": risks,
                    "warnings": [],
                    "errors": [],
                },
                indent=2,
                ensure_ascii=False,
            )
        )

    except Exception as e:
        logging.error(f"Analysis failed: {str(e)}")
        print(
            json.dumps(
                {
                    "status": "error",
                    "error_code": "PROFILE_ANALYSIS_FAILED",
                    "message": str(e),
                    "suggestion": "Check --industry, --text and --db_path inputs.",
                },
                ensure_ascii=False,
            )
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
