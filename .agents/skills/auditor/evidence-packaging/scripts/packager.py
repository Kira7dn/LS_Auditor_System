import os
import json
import argparse
import sys
import logging
from typing import Dict, Any

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', stream=sys.stderr)

def create_evidence_dossier(finding_id: str, base_dir: str = "Evidence_Packs") -> Dict[str, Any]:
    """
    Tạo cấu trúc thư mục hồ sơ bằng chứng chuẩn hóa cho một phát hiện sai phạm.
    """
    path = os.path.join(base_dir, finding_id)
    subdirs = ['data', 'images', 'logs']
    
    created_dirs = []
    try:
        os.makedirs(path, exist_ok=True)
        for sd in subdirs:
            subdir_path = os.path.join(path, sd)
            os.makedirs(subdir_path, exist_ok=True)
            created_dirs.append(subdir_path)
        
        return {
            "status": "success",
            "finding_id": finding_id,
            "dossier_root": path,
            "subdirectories": created_dirs
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Could not create dossier: {str(e)}"
        }

def main():
    parser = argparse.ArgumentParser(description="LS Auditor: Evidence Packaging Tool")
    parser.add_argument("--id", type=str, required=True, help="ID của phát hiện sai phạm (e.g., FIND-2026-001)")
    parser.add_argument("--base_dir", type=str, default="Evidence_Packs", help="Thư mục gốc chứa các hồ sơ")
    
    args = parser.parse_args()
    
    try:
        result = create_evidence_dossier(args.id, args.base_dir)
        print(json.dumps(result, indent=2))
        
    except Exception as e:
        logging.error(f"Packaging failed: {str(e)}")
        print(json.dumps({"status": "error", "message": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
