---
description: "Quy trình chuẩn bị, làm sạch và hợp nhất dữ liệu Audit"
---

# LS-WORKFLOW-DATA-PREPARATION

Workflow này hướng dẫn Agent cách làm sạch, chuẩn hóa và tạo bộ dữ liệu hợp nhất (Unified Dataset) từ các nguồn rời rạc.

## 1. Nạp Ngữ cảnh (Context Loading)
Agent PHẢI nạp các tri thức sau:
- [asset-index.json](../../../asset-index.json)
- [SCRIPT_STANDARDS.md](../../rules/SCRIPT_STANDARDS.md)

## 2. Thực thi Chuẩn bị (Data Execution)

### Bước 2.1: Thiết kế kiến trúc dữ liệu (Data Strategy)
Xác định cách Join các bảng dữ liệu dựa trên thư viện Schema.

// turbo
```bash
uv run .agents/skills/auditor/data-strategy/scripts/data_architect.py --cycle "[cycle-key]"
```

### Bước 2.2: Chuẩn hóa & Hợp nhất (Normalize & Join)
Thực thi các lệnh CLI để tạo file Parquet cuối cùng. Đảm bảo mọi lỗi dữ liệu được ghi lại.

// turbo
```bash
uv run .agents/skills/auditor/variance-analysis/scripts/variance_calculator.py --data "[raw-data-path]"
```

## 3. Xác nhận Chất lượng (Verification)
- Kiểm tra file `.agents/templates/auditor/data-quality-log.md`.
- Đảm bảo tỷ lệ khớp (Join rate) đạt ngưỡng yêu cầu (> 80%).

---
**Status:** ACTIVE HARDENED WORKFLOW (Antigravity Optimized)
**Target:** AI Agent (Executor)
**Owner:** Auditor Brain
