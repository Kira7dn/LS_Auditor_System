# LS-WORKFLOW-AUDIT-EXECUTION

Workflow này hướng dẫn Agent cách thực hiện phân tích sai lệch, chạy các bài test kiểm soát và đóng gói hồ sơ bằng chứng sai phạm.

## 1. Nạp Ngữ cảnh (Context Loading)
Trước khi bắt đầu, Agent PHẢI nạp các tri thức sau:
- [GEMINI.md](../../../GEMINI.md): Hiến pháp vận hành.
- [asset-index.json](../../../asset-index.json): Bản đồ tài sản tri thức.

## 2. Chuẩn bị (Preparation)

### Bước 2.1: Thiết kế Risk Specification (Configuring the Brain)
Định nghĩa "luật chơi" rủi ro trong file `risk_spec.json`.

### Bước 2.2: Xác định các tham số thực thi
- `[data-path]`: Đường dẫn đến Unified Dataset (Parquet/CSV).
- `[risk-spec-json]`: Đường dẫn đến file Spec.

## 3. Thực thi Chẩn đoán (Forensic Execution)

### Bước 3.1: Nhận diện rủi ro (Risk Detection)
Sử dụng các quy tắc nghiệp vụ (Risk Spec) để quét toàn bộ Unified Dataset.

// turbo
```bash
uv run ls-auditor compute-risks --dataset "[data-path]" --risk-spec "[risk-spec-json]" --out "Projects/[case-id]/artifacts/audit_findings.json"
```

### Bước 3.2: Phân tích Pareto & Ưu tiên (Prioritization)
Áp dụng nguyên lý 80/20 để lọc ra các ngoại lệ trọng yếu.

// turbo
```bash
uv run ls-auditor prioritize --findings "Projects/[case-id]/artifacts/audit_findings.json" --top-pct 0.8 --out "Projects/[case-id]/artifacts/prioritized_findings.json"
```

### Bước 3.3: Lập báo cáo & Tự động đóng gói hồ sơ bằng chứng (Automated Dossier)
Khởi tạo toàn bộ báo cáo và hồ sơ bằng chứng cho danh sách ngoại lệ đã ưu tiên.

// turbo
```bash
uv run ls-auditor report --prioritized-data "Projects/[case-id]/artifacts/prioritized_findings.json" --template-dir ".agents/templates/auditor/" --out-dir "Projects/[case-id]/artifacts/"
uv run ls-auditor trace --finding "Projects/[case-id]/artifacts/prioritized_findings.json" --out-dir "Projects/[case-id]/evidence/"
```
*Ghi chú: Lệnh `trace` hiện đã hỗ trợ Batch Processing, tự động đóng gói hồ sơ cho TOÀN BỘ danh sách ngoại lệ trọng yếu.*

## 4. Xác nhận & Bàn giao (Verification)
- Đảm bảo các chỉ số Leakage đã được tính toán đúng.
- Kiểm tra tính đầy đủ của bộ Dossier (EVIDENCE.md cho từng case).
- Báo cáo trạng thái **READY FOR REVIEW**.

---

## ⚡ CHẾ ĐỘ TỰ ĐỘNG HOÀN TOÀN (FULLY AUTOMATED MODE)
Auditor có thể chạy toàn bộ quy trình chỉ với 1 lệnh duy nhất:

// turbo
```bash
uv run ls-auditor run-all --dataset "[data-path]" --risk-spec "[risk-spec-json]" --out-dir "Results/[case-id]/" --top-pct 0.8
```

---
**Status:** ACTIVE HARDENED WORKFLOW (Antigravity Optimized)
**Target:** AI Agent (Executor)
**Owner:** Auditor Brain
