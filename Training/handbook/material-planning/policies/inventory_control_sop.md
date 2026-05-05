# SOP: Kiểm soát tồn kho vật tư

## Thuật ngữ & viết tắt
- **DIOH:** số ngày tồn kho đủ dùng theo tốc độ tiêu thụ hiện tại.
- **QC Hold:** vật tư bị giữ lại để kiểm tra chất lượng, chưa được dùng cho sản xuất.
- **Stock watch:** trạng thái cảnh báo vật tư tồn cao hoặc chậm luân chuyển.
- **Open PO:** PO đã đặt nhưng chưa nhận đủ hàng.
- **Dead stock:** vật tư tồn lâu, ít hoặc không còn nhu cầu sử dụng.
- **Available stock:** tồn kho có thể sử dụng sau khi trừ QC hold và các hạn chế khác.

## 1. Mục đích
Giảm vốn bị khóa trong tồn kho và ngăn việc mua thêm vật tư đang dư.

## 2. Quy trình chuẩn
1. Warehouse cập nhật nhập/xuất kho trong ERP cuối mỗi ca.
2. Slow-moving material được review mỗi tuần.
3. Material có Days of Inventory on Hand trên 90 ngày phải được đánh dấu `stock_watch`.
4. Planner không được request thêm material đang `stock_watch` nếu không có approved exception.
5. Warehouse gửi báo cáo tồn kho cuối tuần cho Planner và Finance.

## 3. Ngưỡng kiểm soát
- `DIOH > 90`: cảnh báo tồn kho cao.
- `DIOH > 120`: yêu cầu freeze PR mới trừ khi có đơn hàng đã xác nhận.
- `DIOH > 180`: dead stock candidate.

## 4. Điểm kiểm soát
- Tồn kho khả dụng phải trừ hàng bị QC hold.
- Tồn kho phải tính cả PO đang về trong 14 ngày.
- Material consumption thấp hơn kế hoạch ba tuần liên tiếp phải được review.

## 5. Ghi chú thực tế
Warehouse cho biết ERP và tồn thực tế lệch nhiều ở nhóm casing và packaging do xuất kho cuối ca cập nhật muộn.
