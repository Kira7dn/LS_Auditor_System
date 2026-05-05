---
description: "Quy trình thực thi phân tích đối chiếu, kiểm tra rủi ro và đóng gói bằng chứng"
---

# LS-WORKFLOW-AUDIT-EXECUTION

Workflow này hướng dẫn Agent cách thực hiện phân tích sai lệch, chạy các bài test kiểm soát và đóng gói hồ sơ bằng chứng sai phạm.

## 1. Nạp Ngữ cảnh (Context Loading)
Trước khi bắt đầu, Agent PHẢI nạp các tri thức sau:
- [GEMINI.md](../../../GEMINI.md): Hiến pháp vận hành.
- [asset-index.json](../../../asset-index.json): Bản đồ tài sản tri thức.
- `[case-study-path]` (MVP default: `Training/handbook/material-planning/CASE_STUDY.md`): Luận đề và phương pháp chẩn đoán mẫu.

## 2. Chuẩn bị (Preparation)
Xác định các tham số thực thi:
- `[data-path]`: Đường dẫn đến Unified Dataset (Parquet/CSV).
- `[threshold-json]`: Các ngưỡng rủi ro cần kiểm tra.

## 3. Thực thi Chẩn đoán (Forensic Execution)

### Bước 3.1: Phân tích định lượng (Quantitative Analysis)
Tính toán giá trị rò rỉ (Leakage) dựa trên sai lệch Kế hoạch vs Thực tế.

// turbo
```bash
uv run .agents/skills/auditor/variance-analysis/scripts/variance_calculator.py --data "[data-path]" --thresholds "[threshold-json]"
```

### Bước 3.2: Lọc ngoại lệ trọng yếu (Exception Detection)
Lọc ra 20% giao dịch gây ra 80% rủi ro và đóng gói vào `candidate-exceptions.md`.

### Bước 3.3: Đóng gói hồ sơ bằng chứng (Evidence Packaging)
Khởi tạo cấu trúc thư mục bằng chứng cho các phát hiện quan trọng.

// turbo
```bash
uv run .agents/skills/auditor/evidence-packaging/scripts/packager.py --id "[finding-id]"
```

## 4. Xác nhận & Bàn giao (Verification)
- Kiểm tra kết quả JSON trả về từ các script.
- Đảm bảo các file Artifact tại `.agents/templates/auditor/` đã được điền đủ số liệu và bằng chứng.
- Báo cáo trạng thái **READY FOR REVIEW** cho Auditor.

---
**Status:** ACTIVE HARDENED WORKFLOW (Antigravity Optimized)
**Target:** AI Agent (Executor)
**Owner:** Auditor Brain
