# Data Dictionary: Material Planning Mock Input

**Case:** Aurora Electronics Manufacturing JSC  
**Mục đích:** Dữ liệu mô phỏng cho audit Material Planning, defensive ordering và inventory governance.  
**Lưu ý:** Tất cả tên người, vendor, mã vật tư và số liệu đều là fake.

## Thuật ngữ & viết tắt

- **BOM (Bill of Materials):** định mức vật tư cần để sản xuất một thành phẩm.
- **MRP (Material Requirements Planning):** cách tính nhu cầu vật tư dựa trên kế hoạch sản xuất, BOM, tồn kho và PO đang về.
- **PR (Purchase Request):** yêu cầu mua hàng nội bộ.
- **PO (Purchase Order):** đơn đặt hàng gửi nhà cung cấp.
- **GRN (Goods Receipt Note):** phiếu ghi nhận hàng đã nhận vào kho.
- **DIOH (Days of Inventory on Hand):** số ngày tồn kho đủ dùng theo tốc độ tiêu thụ hiện tại.
- **QC Hold:** vật tư bị giữ lại để kiểm tra chất lượng, chưa được dùng cho sản xuất.
- **Open PO:** PO đã đặt nhưng chưa nhận đủ hàng.
- **Defensive Ordering:** đặt dư để tránh thiếu hàng hoặc dừng line.
- **Buffer:** phần số lượng đặt thêm so với nhu cầu chuẩn.
- **Split PO:** chia nhỏ PO để né ngưỡng phê duyệt.
- **Leakage:** giá trị rò rỉ tài chính hoặc rủi ro kinh tế do lỗi quy trình/dữ liệu.

## 1. `production_plan.csv`

**Grain:** một dòng cho một product trong một tuần kế hoạch.

| Column | Meaning |
| --- | --- |
| `plan_id` | Mã kế hoạch tuần, dùng để join với PR/PO/Consumption. |
| `week_start` | Ngày bắt đầu tuần sản xuất. |
| `product_id` | Finished good được sản xuất. |
| `planned_units` | Số lượng thành phẩm dự kiến. |
| `customer_priority` | `normal` hoặc `rush`. |
| `planner` | Người lập kế hoạch. |

## 2. `bom.csv`

**Grain:** một dòng cho một vật tư trong BOM của một product.

| Column | Meaning |
| --- | --- |
| `product_id` | Finished good. |
| `material_id` | Mã vật tư. |
| `qty_per_unit` | Định mức vật tư cho một thành phẩm. |
| `scrap_allowance_pct` | Tỷ lệ hao hụt cho phép. |
| `bom_version` | Phiên bản BOM. |

## 3. `purchase_requests.csv`

**Grain:** một dòng cho một PR line.

| Column | Meaning |
| --- | --- |
| `pr_id` | Mã Purchase Request. |
| `plan_id` | Kế hoạch liên quan. |
| `request_date` | Ngày tạo PR. |
| `material_id` | Vật tư được request. |
| `requested_qty` | Số lượng request. |
| `required_qty_by_bom` | Nhu cầu tính theo kế hoạch và BOM. |
| `requester` | Người tạo request. |
| `urgent_flag` | PR urgent hay không. |
| `exception_reason` | Lý do vượt chuẩn hoặc urgent. |
| `approval_status` | Trạng thái duyệt. |
| `approved_by` | Người duyệt. |

## 4. `purchase_orders.csv`

**Grain:** một dòng cho một PO line.

| Column | Meaning |
| --- | --- |
| `po_id` | Mã Purchase Order. |
| `pr_id` | PR nguồn. |
| `plan_id` | Kế hoạch liên quan. |
| `po_date` | Ngày tạo PO. |
| `material_id` | Vật tư mua. |
| `vendor_id` | Vendor fake. |
| `po_qty` | Số lượng đặt mua. |
| `unit_price` | Giá mua thực tế. |
| `target_price` | Giá mục tiêu. |
| `emergency_flag` | PO urgent hay không. |
| `approved_by` | Người duyệt PO. |
| `approval_note` | Ghi chú phê duyệt. |

## 5. `inventory_balance.csv`

**Grain:** một dòng cho tồn kho của một material tại warehouse.

| Column | Meaning |
| --- | --- |
| `material_id` | Mã vật tư. |
| `warehouse` | Kho. |
| `on_hand_qty` | Tồn kho hiện tại. |
| `qc_hold_qty` | Số lượng bị QC hold. |
| `avg_monthly_consumption` | Tiêu thụ trung bình tháng. |
| `dioh` | Days of Inventory on Hand. |
| `stock_watch` | `Y` nếu vượt ngưỡng tồn kho cao. |
| `last_count_date` | Ngày kiểm kê gần nhất. |

## 6. `material_consumption.csv`

**Grain:** một dòng cho lượng tiêu thụ material theo plan và tuần.

| Column | Meaning |
| --- | --- |
| `consumption_id` | Mã dòng tiêu thụ. |
| `plan_id` | Kế hoạch liên quan. |
| `week_start` | Tuần tiêu thụ. |
| `material_id` | Vật tư tiêu thụ. |
| `consumed_qty` | Số lượng đã xuất dùng. |
| `issue_source` | Nguồn ghi nhận. |
| `line` | Line sản xuất. |

## 7. `open_po_grn.csv`

**Grain:** một dòng cho trạng thái nhận hàng của một PO line.

| Column | Meaning |
| --- | --- |
| `grn_id` | Mã phiếu nhận hàng mô phỏng. |
| `po_id` | PO liên quan. |
| `pr_id` | PR nguồn. |
| `plan_id` | Kế hoạch liên quan. |
| `material_id` | Vật tư trên PO. |
| `vendor_id` | Vendor fake. |
| `po_qty` | Số lượng đặt mua. |
| `received_qty` | Số lượng đã nhận vào kho. |
| `open_qty` | Số lượng chưa nhận. |
| `expected_receipt_date` | Ngày dự kiến nhận hàng. |
| `actual_grn_date` | Ngày GRN được ghi nhận; để trống nếu chưa ghi nhận. |
| `erp_visible_to_planner` | Planner có thấy trạng thái này trong ERP khi chạy MRP hay không. |
| `visibility_issue_reason` | Lý do thông tin không hiển thị kịp. |

## Suggested Joins
- `production_plan.plan_id` -> `purchase_requests.plan_id`
- `purchase_requests.pr_id` -> `purchase_orders.pr_id`
- `purchase_orders.po_id` -> `open_po_grn.po_id`
- `purchase_requests.material_id` -> `inventory_balance.material_id`
- `purchase_requests.plan_id + material_id` -> `material_consumption.plan_id + material_id`
- `production_plan.product_id` -> `bom.product_id`

## Risk Patterns Embedded
- `requested_qty > required_qty_by_bom` ở nhóm casing, packaging, sensor.
- `po_qty > requested_qty` ở một số PR.
- `dioh > 90` nhưng vẫn có PR/PO mới.
- Open PO/GRN không hiển thị kịp cho Planner khi chạy MRP.
- `unit_price > target_price` cho emergency PO.
- PO có `approval_note = split delivery slot` để kiểm tra split PO.
- `consumed_qty < required_qty_by_bom` ở casing và packaging.
