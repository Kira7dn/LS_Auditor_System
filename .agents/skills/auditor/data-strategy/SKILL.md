---
name: data-strategy
description: Kỹ năng thiết kế kiến trúc dữ liệu Audit, định nghĩa logic hợp nhất (Join) và chuẩn hóa dữ liệu từ nhiều nguồn khác nhau.
---

# Data Strategy Skill

Kỹ năng này hướng dẫn Agent cách xây dựng một "Single Source of Truth" cho mục đích Audit bằng cách kết nối các bảng dữ liệu rời rạc (Silos).

## When to Use This Skill

- Khi đã có danh sách các bảng dữ liệu thô (PR, PO, GRN, Inventory...).
- Trước khi thực hiện các lệnh `normalize_cli` hoặc `join_cli`.
- Khi cần xử lý các mâu thuẫn về mã vật tư hoặc đơn vị tính giữa các bộ phận.

## Core Capabilities

### 1. Phân tích thực thể (Entity Analysis)
- Xác định thực thể trung tâm (Transaction Anchor) - ví dụ: PO Line Item.
- Nhận diện các thuộc tính khóa (Key attributes) phục vụ việc liên kết.

### 2. Thiết kế ma trận liên kết (Join Matrix Design)
- Định nghĩa logic Join giữa các giai đoạn (Ví dụ: PR -> PO: Nhiều PR có thể gom vào 1 PO; 1 PO có thể có nhiều đợt GRN).
- Xử lý Fuzzy Mapping cho các trường hợp không có ID chung (Ví dụ: Khớp theo Tên nhà cung cấp hoặc Mã vật tư + Thời gian).

### 3. Chuẩn hóa dữ liệu (Data Normalization)
- Thống nhất Đơn vị tính (UoM Conversion) - cực kỳ quan trọng trong sản xuất.
- Chuẩn hóa định dạng Ngày tháng và Tiền tệ (Currency harmonization).

## Key Patterns

### Pattern 1: The Transactional Thread
Agent phải nối được một "sợi chỉ" xuyên suốt vòng đời của một vật tư/giao dịch:
- [Request] -> [Approval] -> [Purchase] -> [Delivery] -> [Payment] -> [Consumption].

### Pattern 2: Schema Enforcement
Mọi Unified Dataset phải có tối thiểu các cột chuẩn:
- `event_timestamp`: Thời điểm xảy ra.
- `entity_id`: ID của đối tượng (Vật tư, Nhân viên).
- `transaction_id`: ID giao dịch (PO No, PR No).
- `quantity`: Số lượng (sau chuẩn hóa UoM).
- `amount`: Giá trị tài chính.
- `actor`: Người thực hiện.

## Quick Start (Data Spec Example)

```json
{
  "join_logic": {
    "left_table": "purchase_orders",
    "right_table": "goods_receipts",
    "join_on": ["po_number", "item_code"],
    "type": "left_join"
  }
}
```

## Best Practices
- **Never Assume Keys**: Đừng giả định rằng PO Number trong bảng Mua hàng khớp hoàn toàn với PO Number trong bảng Kho. Luôn kiểm tra tính duy nhất.
- **Log the Cleaning**: Mọi dòng dữ liệu bị loại bỏ (Dropped) trong quá trình làm sạch đều phải được thống kê lý do.
- **Date Consistency**: Luôn kiểm tra xem ngày nhận hàng (GRN) có trước ngày đặt hàng (PO) không - đây là dấu hiệu của việc "làm chứng từ sau khi đã nhận hàng".

## Common Pitfalls
- **Mất dữ liệu do Inner Join**: Sử dụng Inner Join quá mức làm mất các giao dịch mồ côi (orphaned records) - vốn là nơi chứa nhiều rủi ro Audit nhất.
- **Sai lệch đơn vị tính**: Không quy đổi UoM dẫn đến các phép tính toán sai lệch hàng nghìn lần (Ví dụ: Cái vs Thùng).
- **Thiếu kiểm tra trùng lặp**: Coi các bản ghi trùng lặp là giao dịch thật, làm thổi phồng giá trị rò rỉ.

## Assistant Contract
- **Trigger**: Khi chuẩn bị normalize/join dữ liệu audit.
- **Input**: raw data dictionary, sample files, schema library hoặc case data spec.
- **Output**: schema map, join spec, validation spec.
- **Artifacts**: `Projects/<case_id>/artifacts/data_quality_log.json`, `working/data-spec.md`.
- **Failure Modes**: grain không rõ, join key yếu, mất dòng sau join nhưng không cảnh báo.
- **Acceptance Checklist**: có required columns, grain, join keys, expected join rate và data quality thresholds.
