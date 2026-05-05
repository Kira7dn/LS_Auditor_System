---
name: evidence-packaging
description: Kỹ năng thu thập, liên kết và đóng gói hồ sơ bằng chứng cho các phát hiện sai phạm (Findings).
---

# Evidence Packaging Skill

Kỹ năng này giúp Agent xây dựng một bộ hồ sơ bằng chứng (Evidence Pack) chặt chẽ, đủ sức thuyết phục khách hàng và các bên liên quan về sự tồn tại của rủi ro.

## When to Use This Skill

- Khi đã phát hiện ra một giao dịch ngoại lệ (Exception) trọng yếu.
- Khi cần chuẩn bị dữ liệu cho buổi thảo luận đối chất với khách hàng.
- Khi chuẩn bị nội dung cho file `evidence-pack.md`.

## Core Capabilities

### 1. Thu thập dấu vết (Audit Trail Gathering)
- Truy xuất toàn bộ lịch sử của một Case ID (Ví dụ: Từ số PO, truy ngược ra PR, phê duyệt PR, và phiếu nhập kho GRN).
- Thu thập metadata (Người phê duyệt, thời gian, địa điểm IP nếu có) để xác định tính chính xác của giao dịch.

### 2. Liên kết đa nguồn (Cross-referencing)
- Đối chiếu dữ liệu giữa các hệ thống khác nhau (Ví dụ: Dữ liệu mua hàng vs Dữ liệu kế toán thanh toán).
- Tìm kiếm các mâu thuẫn giữa các bằng chứng (Ví dụ: Ngày ký duyệt PO sau ngày nhận hàng).

### 3. Trực quan hóa bằng chứng (Evidence Visualization)
- Trích xuất các đoạn log quan trọng.
- Hướng dẫn Auditor chụp ảnh hoặc lấy mẫu chứng từ tại các điểm rủi ro.

## Key Patterns

### Pattern 1: The "Golden Thread" of Evidence
Một hồ sơ bằng chứng hoàn chỉnh phải bao gồm 3 lớp:
1. **Dữ liệu hệ thống**: Export từ ERP/Database (Sử dụng `trace_cli`).
2. **Chứng từ số**: File PDF, ảnh chụp phiếu giao hàng, email phê duyệt.
3. **Phát biểu xác nhận**: Ghi chú từ các buổi phỏng vấn hoặc giải trình của nhân viên liên quan.

### Pattern 2: Exception Contextualization
Đừng chỉ đưa ra con số, hãy đưa ra ngữ cảnh:
- "Giao dịch này được thực hiện vào 11h đêm ngày Chủ nhật bởi một tài khoản có quyền admin thay vì nhân viên mua hàng."

## Quick Start (Evidence Structure)

```markdown
### Case ID: EX-2024-001
- **Finding**: Mua hàng không qua phê duyệt PR.
- **Evidence 1**: PO #12345 tạo ngày 10/01.
- **Evidence 2**: Không tìm thấy PR tương ứng trong hệ thống.
- **Evidence 3**: Phiếu nhập kho đã được ký nhận ngày 12/01.
```

## Best Practices
- **Chain of Custody**: Đảm bảo nguồn gốc dữ liệu rõ ràng, không bị chỉnh sửa.
- **Privacy First**: Che mờ các thông tin cá nhân không liên quan trực tiếp đến sai phạm.
- **Objectivity**: Chỉ mô tả sự thật khách quan (Fact), không đưa ý kiến chủ quan vào hồ sơ bằng chứng.

## Common Pitfalls
- **Bằng chứng rời rạc**: Chỉ đưa ra PO lỗi mà không chỉ ra được các bước liên quan bị bypass.
- **Thiếu ID tham chiếu**: Không gắn mã ID khiến khách hàng không thể tìm lại giao dịch đó trong hệ thống của họ.
- **Quá nhiều dữ liệu rác**: Đưa vào quá nhiều chứng từ không liên quan làm loãng hồ sơ bằng chứng.

## Assistant Contract
- **Trigger**: Khi nâng candidate exception thành confirmed finding.
- **Input**: finding JSON, source artifact paths, evidence output directory.
- **Output**: Evidence Pack folder with `FINDING.md` and source artifacts.
- **Artifacts**: `Projects/<case_id>/Evidence_Packs/<finding_id>/`.
- **Failure Modes**: thiếu transaction ID, thiếu calculation trail, không ghi limitation.
- **Acceptance Checklist**: Evidence Pack có source, timestamp/kỳ dữ liệu, leakage logic và confidence level.
