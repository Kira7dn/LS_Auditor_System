---
name: root-cause-synthesis
description: Kỹ năng tổng hợp từ các ngoại lệ (Exceptions) riêng lẻ thành các lỗi hệ thống (Systemic Failures) và xác định nguyên nhân gốc rễ.
---

# Root Cause Synthesis Skill

Kỹ năng này hướng dẫn Agent cách kết nối các "chấm" dữ liệu rời rạc để vẽ nên bức tranh toàn cảnh về những hỏng hóc trong bộ máy vận hành của khách hàng.

## When to Use This Skill

- Khi đã hoàn thành việc thực thi Audit và có danh sách các Findings/Risks.
- Trước khi thiết kế giải pháp can thiệp (Intervention).
- Khi chuẩn bị nội dung cho file `risk-register.md` và `final-audit-report.md`.

## Core Capabilities

### 1. Phân nhóm rủi ro (Risk Clustering)
- Gom nhóm các lỗi lẻ tẻ theo danh mục: Nhân sự, Quy trình, Công nghệ, hoặc Chính sách.
- Nhận diện các "Điểm nóng" (Hotspots) - nơi tập trung nhiều sai phạm nhất.

### 2. Truy tìm nguyên nhân gốc rễ (Root Cause Tracing)
- Áp dụng kỹ thuật **5 Whys** để đào sâu từ hiện tượng (Ví dụ: Đặt hàng dư) đến nguyên nhân thực sự (Ví dụ: Hệ thống dự báo không chính xác).
- Phân tích sự tương quan giữa các rủi ro (Ví dụ: Quy trình lỏng lẻo dẫn đến nhân viên cố tình bypass).

### 3. Đánh giá tính hệ thống (Systemic Assessment)
- Phân biệt giữa "Lỗi ngẫu nhiên" (Human Error) và "Lỗi thiết kế" (Design Failure).
- Đánh giá tác động cộng hưởng của nhiều lỗi nhỏ đối với sức khỏe tài chính doanh nghiệp.

## Key Patterns

### Pattern 1: The "5 Whys" Loop for Audit
Agent phải thực hiện truy vấn ngược:
1. Hiện tượng: Đặt mua vật tư A vượt định mức 50%.
2. Tại sao 1: Vì nhân viên sản xuất yêu cầu thêm.
3. Tại sao 2: Vì họ sợ thiếu hàng làm dừng máy.
4. Tại sao 3: Vì kế hoạch sản xuất thường xuyên thay đổi phút chót.
5. Tại sao 4: Vì kinh doanh nhận đơn hàng không kiểm tra năng lực sản xuất.
-> **Root Cause**: Thiếu sự kết nối thông tin giữa Sales và Production.

### Pattern 2: The Fishbone (Ishikawa) Synthesis
Phân tích nguyên nhân qua 4M:
- **Man**: Kỹ năng, ý thức, sự thiếu hụt nhân sự.
- **Method**: Quy trình lạc hậu, thiếu bước kiểm tra.
- **Machine**: Hệ thống ERP cũ, dữ liệu không real-time.
- **Material**: Đặc thù vật tư khó kiểm soát, định mức BOM sai.

## Quick Start (Synthesis Structure)

```markdown
### Systemic Failure: Đứt gãy niềm tin vào hệ thống Planning
- **Biểu hiện**: Tỷ lệ đặt dư 20%, Tồn kho chậm luân chuyển tăng 15% mỗi quý.
- **Root Cause**: Dữ liệu tồn kho thực tế lệch với ERP khiến nhân viên luôn phải đặt dư "cho chắc".
- **Hệ quả**: Kẹt vốn lưu động 2 triệu USD/năm.
```

## Best Practices
- **Look for Patterns**: Một lỗi lặp lại ở 3 bộ phận khác nhau chắc chắn là lỗi hệ thống.
- **Focus on the "Big Why"**: Đừng chỉ dừng lại ở việc đổ lỗi cho cá nhân, hãy tìm lỗi ở cơ chế.
- **Quantify the Impact**: Luôn gắn nguyên nhân gốc rễ với một con số thiệt hại tổng thể.

## Common Pitfalls
- **Kết luận vội vàng**: Đưa ra nguyên nhân mà không có đủ số lượng Findings để chứng minh tính hệ thống.
- **Lỗi ngụy biện**: Nhầm lẫn giữa sự tương quan (Correlation) và nguyên nhân kết quả (Causation).
- **Giải pháp hời hợt**: Đưa ra nguyên nhân là "Do ý thức nhân viên kém" (đây thường không phải nguyên nhân gốc rễ mà hệ thống có thể sửa được).

## Assistant Contract
- **Trigger**: Khi đã có candidate exceptions hoặc confirmed findings.
- **Input**: exception list, category map, threshold.
- **Output**: systemic risk groups and root cause candidates.
- **Artifacts**: `Projects/<case_id>/working/problem-classification.md`.
- **Failure Modes**: nhóm quá rộng, thiếu control gap, nhầm triệu chứng thành nguyên nhân.
- **Acceptance Checklist**: mỗi systemic risk có exception IDs, control gap và intervention direction.
