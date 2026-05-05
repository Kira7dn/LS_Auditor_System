---
description: "Quy trình tổng hợp báo cáo Audit cuối cùng và bàn giao hồ sơ"
---

# LS-WORKFLOW-FINAL-REPORT

Workflow này hướng dẫn Agent cách tổng hợp toàn bộ các kết quả từ Discovery đến Solution để tạo ra bản báo cáo cuối cùng chuyên nghiệp.

## 1. Nạp Ngữ cảnh (Context Loading)
Agent PHẢI nạp toàn bộ các Artifact đã sinh ra:
- `.agents/templates/auditor/business-analysis-report.md`
- `.agents/templates/auditor/risk-register.md`
- `.agents/templates/auditor/intervention-thesis.md`

## 2. Thực thi Tổng hợp (Report Execution)

### Bước 2.1: Đối soát tính nhất quán (Consistency Check)
Đảm bảo số liệu rò rỉ trong báo cáo định lượng khớp 100% với giá trị rủi ro và ROI.

### Bước 2.2: Lắp ghép báo cáo (Assembly)
Sử dụng template chuẩn để tạo file báo cáo tổng hợp.

// turbo
```bash
uv run .agents/skills/auditor/auditor-mermaid-expert/scripts/mermaid_expert_helper.py --type "flowchart" --nodes "[summary-nodes]" --connections "[summary-conns]"
```

## 3. Bàn giao (Handover)
- Kiểm tra file `.agents/templates/auditor/final-audit-report.md`.
- Đóng gói thư mục `Evidence_Packs` và các bộ dữ liệu Parquet.
- Báo cáo trạng thái **MISSION COMPLETED** cho Auditor.

---
**Status:** ACTIVE HARDENED WORKFLOW (Antigravity Optimized)
**Target:** AI Agent (Executor)
**Owner:** Auditor Brain
