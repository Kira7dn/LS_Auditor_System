---
description: "Quy trình tổng hợp nguyên nhân gốc rễ và thiết kế giải pháp can thiệp"
---

# LS-WORKFLOW-SOLUTION-PACKAGING

Workflow này hướng dẫn Agent cách đóng gói các phát hiện Audit thành một bộ giải pháp có tính thuyết phục và giá trị kinh tế cao.

## 1. Nạp Ngữ cảnh (Context Loading)
Agent PHẢI nạp các tri thức sau:
- [GEMINI.md](../../../GEMINI.md)
- `[case-study-path]` (MVP default: `Training/handbook/material-planning/CASE_STUDY.md`)

## 2. Thực thi Giải pháp (Solution Execution)

### Bước 2.1: Tổng hợp nguyên nhân gốc rễ (Synthesis)
Gộp các ngoại lệ riêng lẻ thành các nhóm rủi ro hệ thống.

// turbo
```bash
uv run .agents/skills/auditor/root-cause-synthesis/scripts/synthesis_helper.py --exceptions "[exception-json]" --category_map "[map-json]"
```

### Bước 2.2: Thiết kế giải pháp & Tính toán ROI (ROI Analysis)
Thiết kế lộ trình can thiệp và tính toán hiệu quả kinh tế.

// turbo
```bash
uv run .agents/skills/auditor/solution-design/scripts/roi_calculator.py --investment "[cost]" --savings "[savings]"
```

## 3. Xác nhận Artifacts (Verification)
Đảm bảo các file sau đã được hoàn thiện:
- `.agents/templates/auditor/problem-classification.md`
- `.agents/templates/auditor/intervention-thesis.md`
- `.agents/templates/auditor/solution-proposal.md`

---
**Status:** ACTIVE HARDENED WORKFLOW (Antigravity Optimized)
**Target:** AI Agent (Executor)
**Owner:** Auditor Brain
