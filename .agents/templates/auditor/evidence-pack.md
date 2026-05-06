# EVIDENCE PACK: [finding_id]

Hồ sơ bằng chứng chi tiết cho ngoại lệ được phát hiện.

## 1. Thông tin giao dịch (Transaction Details)
- **Case ID:** [case_id]
- **Vật tư:** [material_id]
- **ID Giao dịch:** [pr_id] / [po_id]
- **Thời gian:** [timestamp]

## 2. Bằng chứng định lượng (Quantitative Evidence)
- **Logic phát hiện:** [evidence]
- **Số liệu nguồn:** Xem chi tiết trong file artifacts/finding.json
- **Cách tính Leakage:** Evaluated by ls-auditor logic engine
- **Giá trị thiệt hại:** [leakage_formatted]

## 3. Lỗ hổng kiểm soát (Control Failure)
- **Control Point:** [control_point_id]
- **Mô tả lỗi:** [cause]
- **Cấp phê duyệt liên quan:** [approver]

## 4. Giới hạn & Giả định (Limitations & Assumptions)
- Giả định dữ liệu từ hệ thống nguồn là chính xác tại thời điểm trích xuất.
- Bằng chứng dựa trên phân tích sai lệch định lượng (Variance Analysis).

---
**Auditor Signature:** [agent_name]
**Status:** EVIDENCE SEALED
