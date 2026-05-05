---
description: "Quy trình end-to-end cho Production MVP LS Auditor Assistant"
---

# LS-WORKFLOW-FULL-AUDIT-ASSISTANT

Workflow này điều phối toàn bộ assistant từ khởi tạo case đến báo cáo cuối cùng. Template gốc không được ghi đè; mọi artifact case phải nằm trong `Projects/<case_id>/`.

## 1. Required Context
- `GEMINI.md`
- `asset-index.json`
- `.agents/rules/OPERATIONAL_SPEC.md`
- `.agents/rules/DATA_GOVERNANCE.md`
- `.agents/rules/EVIDENCE_STANDARDS.md`
- `.agents/rules/FINDING_STANDARDS.md`
- `[case-study-path]`

## 2. Case Initialization

// turbo
```bash
uv run ls-auditor init-case --case-id "[case-id]" --template "[template-key]"
```

## 3. Data Preparation

// turbo
```bash
uv run ls-auditor validate --input "[raw-file]" --schema "[schema-json-or-path]" --out "Projects/[case-id]/artifacts/validation.json"
```

// turbo
```bash
uv run ls-auditor normalize --input "[raw-file]" --spec "[normalize-spec-json-or-path]" --out "Projects/[case-id]/artifacts/normalized.parquet"
```

// turbo
```bash
uv run ls-auditor join --spec "[join-spec-json-or-path]" --out "Projects/[case-id]/artifacts/unified.parquet"
```

## 4. Audit Execution

// turbo
```bash
uv run ls-auditor compute --dataset "Projects/[case-id]/artifacts/unified.parquet" --metric-spec "[metric-spec-json-or-path]" --out "Projects/[case-id]/artifacts/leakage_analysis.json"
```

// turbo
```bash
uv run ls-auditor rule-test --dataset "Projects/[case-id]/artifacts/unified.parquet" --rules "[rules-json-or-path]" --out "Projects/[case-id]/artifacts/rule_test.json"
```

// turbo
```bash
uv run ls-auditor trace --finding "[finding-json-or-path]" --out-dir "Projects/[case-id]/Evidence_Packs"
```

## 5. Delivery

// turbo
```bash
uv run ls-auditor chart --dataset "Projects/[case-id]/artifacts/unified.parquet" --out "Projects/[case-id]/artifacts/chart.md"
```

// turbo
```bash
uv run ls-auditor assemble-report --case-dir "Projects/[case-id]" --out "Projects/[case-id]/FINAL_AUDIT_REPORT.md"
```

## 6. Acceptance
- `registry inspect` không có missing path.
- Raw input không thay đổi.
- Mọi command trả JSON hợp lệ.
- Evidence Pack tồn tại cho mọi confirmed finding.
- Final report chỉ dùng số liệu có artifact nguồn.

---
**Status:** ACTIVE PRODUCTION MVP WORKFLOW
**Target:** LS Auditor Assistant
