---
trigger: model_decision
description: "Vòng đời artifact từ Discovery đến Final Report"
---

# Artifact Lifecycle

## 1. Template vs Output
- `.agents/templates/auditor/` chỉ chứa template gốc.
- Artifact của từng case phải nằm trong `Projects/<case_id>/working/` hoặc `Projects/<case_id>/artifacts/`.
- Không ghi đè template gốc khi chạy audit.

## 2. Case Workspace
Mỗi case dùng cấu trúc:

```text
Projects/<case_id>/
├── raw/
├── working/
│   └── templates/
├── artifacts/
├── Evidence_Packs/
└── FINAL_AUDIT_REPORT.md
```

## 3. Workflow Outputs
- Discovery tạo account thesis, process map, control point table.
- Data Preparation tạo data quality log và unified dataset.
- Audit Execution tạo business analysis report, candidate exceptions, risk register, evidence packs.
- Solution Packaging tạo problem classification, intervention thesis, solution proposal.
- Final Report tổng hợp artifact đã xác minh.

---
*Status: MANDATORY ARTIFACT RULE*