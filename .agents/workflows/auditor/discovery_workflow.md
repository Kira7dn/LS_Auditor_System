---
description: "Quy trình tiếp cận khách hàng, thiết lập giả thuyết và lập bản đồ quy trình"
---

# LS-WORKFLOW-DISCOVERY

Workflow này hướng dẫn Agent thực hiện các bước tìm hiểu ban đầu, thiết lập giả thuyết rủi ro và lập bản đồ quy trình vận hành (SOP).

## 1. Nạp Ngữ cảnh (Context Loading)
Agent PHẢI nạp các tri thức sau:
- [GEMINI.md](../../../GEMINI.md)
- [asset-index.json](../../../asset-index.json)
- [CASE_STUDY.md](../../../Training/handbook/cases/material-planning/CASE_STUDY.md)

## 2. Thực thi Khám phá (Operational Execution)

### Bước 2.1: Phân tích bối cảnh & Giả thuyết (Scouting)
Sử dụng AI để quét hồ sơ khách hàng và tìm các "điểm nóng" rủi ro đặc thù ngành.

// turbo
```bash
uv run .agents/skills/auditor/account-scouting/scripts/analyze_profile.py --client "[client-name]" --industry "[industry-key]" --text "[profile-text]"
```

### Bước 2.2: Lập bản đồ quy trình (Process Mapping)
Đọc tài liệu SOP và vẽ sơ đồ Mermaid.

// turbo
```bash
uv run .agents/skills/auditor/auditor-mermaid-expert/scripts/mermaid_expert_helper.py --type "flowchart" --nodes "[node-json]" --connections "[conn-json]"
```

## 3. Xác nhận Artifacts (Verification)
Đảm bảo các file sau đã được khởi tạo chuẩn xác:
- `.agents/templates/auditor/account-thesis.md`
- `.agents/templates/auditor/process-map.md`
- `.agents/templates/auditor/control-point-table.md`

---
**Status:** ACTIVE HARDENED WORKFLOW (Antigravity Optimized)
**Target:** AI Agent (Executor)
**Owner:** Auditor Brain
