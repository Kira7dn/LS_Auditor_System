---
trigger: "always_on"
description: "Quy tắc quản trị dữ liệu Audit và bảo toàn dữ liệu gốc"
---

# Data Governance Rules

## 1. Raw Data Is Immutable
- Agent KHÔNG được ghi đè, format lại, đổi schema hoặc xóa dữ liệu gốc của khách hàng.
- Mọi thao tác chuẩn hóa, join, validate, compute phải tạo artifact dẫn xuất trong `Projects/<case_id>/artifacts/`.
- Nếu cần trích mẫu dữ liệu gốc vào Evidence Pack, chỉ sao chép phần cần thiết và ghi rõ nguồn.

## 2. Data Quality Minimums
Mỗi dataset dẫn xuất phải có log hoặc JSON result gồm:
- source path;
- row count trước và sau xử lý;
- danh sách cột;
- missing required columns;
- null count;
- duplicate row count;
- join rate nếu có join.

## 3. Schema Discipline
- Không suy luận schema âm thầm khi schema đã được cung cấp.
- Nếu schema thiếu hoặc cột không khớp, trả lỗi JSON thay vì tiếp tục kết luận.
- Mọi normalize phải ghi rõ rename map, type cast và field bị mất.

## 4. Unit of Measure Discipline
- Không cộng/trừ số lượng khi chưa kiểm tra đơn vị tính.
- Khi phát hiện nhiều đơn vị tính cho cùng một item, đánh dấu `UOM_MISMATCH` và yêu cầu auditor xác minh.

---
*Status: MANDATORY DATA RULE*
