# SOP: Lập kế hoạch sản xuất và nhu cầu vật tư

**Công ty mô phỏng:** Aurora Electronics Manufacturing JSC  
**Nhà máy:** AUR-01, Khu công nghiệp Sao Bắc  
**Phạm vi:** PCB assembly, sensor module, power adapter, casing và packaging.

## Thuật ngữ & viết tắt
- **BOM:** định mức vật tư cho một thành phẩm.
- **MRP:** quy trình tính nhu cầu vật tư từ kế hoạch sản xuất, BOM, tồn kho và PO đang về.
- **PR:** yêu cầu mua hàng nội bộ.
- **Open PO:** PO đã đặt nhưng chưa nhận đủ hàng.
- **Defensive Ordering:** đặt dư để tránh thiếu vật tư hoặc dừng line.
- **Buffer:** phần đặt thêm so với nhu cầu chuẩn.

## 1. Mục đích
Quy định cách Production Planning chuyển forecast và đơn hàng đã xác nhận thành kế hoạch sản xuất tuần/tháng, sau đó tạo nhu cầu vật tư cho MRP và Purchase Request.

## 2. Vai trò
- **Sales Operations:** cung cấp confirmed order và forecast thay đổi.
- **Production Planner:** lập kế hoạch sản xuất, chạy MRP, tạo material requirement.
- **Warehouse:** xác nhận tồn kho khả dụng.
- **Purchasing:** nhận PR đã duyệt và tạo PO.
- **Finance Controller:** kiểm tra ngân sách và giới hạn phê duyệt.

## 3. Quy trình chuẩn
1. Production Planner nhận forecast vào ngày 25 hàng tháng.
2. Planner khóa master production schedule trước ngày 28.
3. Planner chạy MRP theo BOM chuẩn trong ERP.
4. ERP tự động trừ tồn kho khả dụng và PO đang về.
5. Planner chỉ được tạo PR cho phần thiếu hụt sau khi trừ tồn kho và open PO.
6. Mọi PR vượt BOM requirement trên 5% phải ghi lý do.
7. PR urgent chỉ dùng khi có thay đổi confirmed order hoặc lỗi chất lượng đã được QC xác nhận.

## 4. Ngoại lệ được phép
- Khách hàng tăng đơn trong vòng 7 ngày trước ngày giao.
- Nhà cung cấp báo trì hoãn giao hàng có email xác nhận.
- QC hold làm một lô vật tư không thể sử dụng.

## 5. Điểm kiểm soát
- MRP phải có `plan_id`.
- PR phải tham chiếu `plan_id` và `material_id`.
- Planner không được tạo PR thủ công nếu không có lý do ngoại lệ.

## 6. Ghi chú thực tế
ERP tồn kho thường cập nhật chậm sau ca đêm. Planner đôi khi gọi Warehouse để hỏi tồn thực tế trước khi tạo PR. Việc này được chấp nhận tạm thời nhưng phải ghi chú trong PR.
