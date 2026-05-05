import argparse
import json
import logging
import os
import sys
from pathlib import Path
from typing import Any, Dict

from ls_auditor.evidence import create_evidence_pack

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", stream=sys.stderr)


def create_evidence_dossier(finding_id: str, base_dir: str = "Evidence_Packs") -> Dict[str, Any]:
    """
    Tạo cấu trúc thư mục hồ sơ bằng chứng chuẩn hóa cho một phát hiện sai phạm.
    """
    path = os.path.join(base_dir, finding_id)
    subdirs = ["data", "images", "logs"]

    created_dirs = []
    try:
        os.makedirs(path, exist_ok=True)
        for sd in subdirs:
            subdir_path = os.path.join(path, sd)
            os.makedirs(subdir_path, exist_ok=True)
            created_dirs.append(subdir_path)

        return {"status": "success", "finding_id": finding_id, "dossier_root": path, "subdirectories": created_dirs}
    except Exception as e:
        return {"status": "error", "message": f"Could not create dossier: {str(e)}"}


def main():
    parser = argparse.ArgumentParser(description="LS Auditor: Evidence Packaging Tool")
    parser.add_argument("--id", type=str, required=True, help="ID của phát hiện sai phạm (e.g., FIND-2026-001)")
    parser.add_argument("--base_dir", type=str, default="Evidence_Packs", help="Thư mục gốc chứa các hồ sơ")
    parser.add_argument("--finding", type=str, default=None, help="JSON string hoặc đường dẫn file finding JSON")

    args = parser.parse_args()

    try:
        if args.finding:
            finding_path = Path(args.finding)
            finding = json.loads(finding_path.read_text(encoding="utf-8")) if finding_path.exists() else json.loads(args.finding)
            finding.setdefault("id", args.id)
            result = create_evidence_pack(finding, args.base_dir)
        else:
            result = create_evidence_dossier(args.id, args.base_dir)
        print(json.dumps(result, indent=2, ensure_ascii=False))

    except Exception as e:
        logging.error(f"Packaging failed: {str(e)}")
        print(
            json.dumps(
                {
                    "status": "error",
                    "error_code": "EVIDENCE_PACKAGING_FAILED",
                    "message": str(e),
                    "suggestion": "Check --id, --base_dir and optional --finding JSON.",
                },
                ensure_ascii=False,
            )
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
