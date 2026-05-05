import argparse
import json
import logging
import os
import sys
from typing import Any, Dict

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", stream=sys.stderr)


class DataArchitect:
    """Hỗ trợ thiết kế kiến trúc dữ liệu Audit."""

    def __init__(self, schema_lib_path: str):
        if not os.path.exists(schema_lib_path):
            raise FileNotFoundError(f"Schema library not found: {schema_lib_path}")
        with open(schema_lib_path, "r", encoding="utf-8") as f:
            self.library = json.load(f)

    def get_join_flow(self, cycle_key: str) -> Dict[str, Any]:
        """Đề xuất luồng Join dữ liệu dựa trên thư viện Schema."""
        if cycle_key not in self.library["schemas"]:
            return {"status": "error", "message": f"Cycle '{cycle_key}' không tồn tại trong thư viện."}

        cycle = self.library["schemas"][cycle_key]
        return {"status": "success", "cycle": cycle_key, "join_logic": cycle["join_logic"], "tables": cycle["tables"]}


def main():
    parser = argparse.ArgumentParser(description="LS Auditor: Data Architecture Suggester")
    parser.add_argument("--cycle", type=str, required=True, help="Mã chu kỳ nghiệp vụ (e.g., procurement_cycle)")
    parser.add_argument("--lib_path", type=str, default=None, help="Đường dẫn file audit_schema_library.json")

    args = parser.parse_args()

    lib_path = args.lib_path or os.path.join(os.path.dirname(__file__), "../resources/audit_schema_library.json")

    try:
        architect = DataArchitect(lib_path)
        result = architect.get_join_flow(args.cycle)

        print(json.dumps(result, indent=2, ensure_ascii=False))

    except Exception as e:
        logging.error(f"Failed to suggest architecture: {str(e)}")
        print(
            json.dumps(
                {
                    "status": "error",
                    "error_code": "DATA_ARCHITECT_FAILED",
                    "message": str(e),
                    "suggestion": "Check --cycle and --lib_path.",
                },
                ensure_ascii=False,
            )
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
