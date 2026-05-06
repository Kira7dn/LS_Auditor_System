import argparse
import json
import logging
import sys
from pathlib import Path
from typing import List

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", stream=sys.stderr)


class MermaidExpertHelper:
    """Hệ thống hỗ trợ tạo sơ đồ Mermaid chuẩn Enterprise cho Auditor."""

    # Bảng màu chuyên nghiệp cho Audit
    THEME = {
        "actor": {"fill": "#E3F2FD", "stroke": "#0D47A1", "text": "Khối thực thi"},
        "control": {"fill": "#FFFDE7", "stroke": "#FBC02D", "text": "Điểm kiểm soát"},
        "risk": {"fill": "#FFEBEE", "stroke": "#B71C1C", "text": "Điểm rủi ro cao"},
        "data": {"fill": "#E8F5E9", "stroke": "#2E7D32", "text": "Dữ liệu/Hệ thống"},
        "system": {"fill": "#F3E5F5", "stroke": "#4A148C", "text": "Hệ thống tự động"},
    }

    @staticmethod
    def get_style_header() -> str:
        """Định nghĩa các Class chuyên dụng cho sơ đồ Audit."""
        return (
            "    %% Định nghĩa Style chuẩn Expert\n"
            "    classDef actor fill:#E3F2FD,stroke:#0D47A1,stroke-width:2px,color:#0D47A1;\n"
            "    classDef control fill:#FFFDE7,stroke:#FBC02D,stroke-width:2px,color:#827717,stroke-dasharray: 5 5;\n"
            "    classDef risk fill:#FFEBEE,stroke:#B71C1C,stroke-width:2px,color:#B71C1C;\n"
            "    classDef data fill:#E8F5E9,stroke:#2E7D32,stroke-width:2px,color:#1B5E20;\n"
            "    classDef system fill:#F3E5F5,stroke:#4A148C,stroke-width:2px,color:#4A148C;\n"
        )

    def create_flowchart(self, nodes: List[str], connections: List[str], direction: str = "TB") -> str:
        """Tạo Flowchart quy trình với cấu hình hiện đại."""
        header = f"graph {direction}\n"
        styles = self.get_style_header()
        body = "\n".join([f"    {conn}" for conn in connections])

        # Tự động gán class dựa trên ID node
        class_assignments = []
        for node in nodes:
            if "CP_" in node:
                class_assignments.append(f"    class {node} control;")
            elif "RISK_" in node:
                class_assignments.append(f"    class {node} risk;")
            elif "SYS_" in node:
                class_assignments.append(f"    class {node} system;")
            elif "DB_" in node:
                class_assignments.append(f"    class {node} data;")
            else:
                class_assignments.append(f"    class {node} actor;")

        return f"{header}{styles}{body}\n\n" + "\n".join(class_assignments)


def main():
    parser = argparse.ArgumentParser(description="LS Auditor: Mermaid Diagram Generator (Generic)")
    parser.add_argument("--type", choices=["flowchart", "erd"], default="flowchart", help="Diagram type")
    parser.add_argument("--nodes", type=str, help="JSON list of nodes")
    parser.add_argument("--connections", type=str, help="JSON list of connections")
    parser.add_argument("--direction", type=str, default="TB", help="Direction (TB or LR)")
    parser.add_argument("--out", type=str, help="Optional output file path (Markdown)")

    args = parser.parse_args()

    try:
        expert = MermaidExpertHelper()
        if args.type == "flowchart":
            nodes = json.loads(args.nodes) if args.nodes else []
            connections = json.loads(args.connections) if args.connections else []
            mermaid_code = expert.create_flowchart(nodes, connections, args.direction)

            result = {"status": "success", "type": "flowchart", "mermaid_code": mermaid_code}
            
            print(json.dumps(result, indent=2, ensure_ascii=False))

            if args.out:
                Path(args.out).parent.mkdir(parents=True, exist_ok=True)
                md_content = f"```mermaid\n{mermaid_code}\n```"
                with open(args.out, "w", encoding="utf-8") as f:
                    f.write(md_content)
                logging.info(f"Diagram saved to {args.out}")
        else:
            print(json.dumps({"status": "error", "message": "ERD type not yet fully implemented in CLI."}))

    except Exception as e:
        logging.error(f"Mermaid generation failed: {str(e)}")
        print(json.dumps({"status": "error", "message": str(e)}))
        sys.exit(1)


if __name__ == "__main__":
    main()
