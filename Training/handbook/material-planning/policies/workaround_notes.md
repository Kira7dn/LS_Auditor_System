# Workaround Notes

Tài liệu này tổng hợp các cách làm tạm thời đang tồn tại tại Aurora Electronics. Đây là input mô phỏng, không phải kết luận audit.

## Known Workarounds
- Planner gọi Warehouse qua Zalo để hỏi tồn kho trước khi chạy MRP.
- Purchasing tạo PO urgent qua email rồi cập nhật ERP sau.
- Warehouse nhập GRN cuối ngày, đôi khi sau khi vật tư đã được đưa vào line.
- Một số open PO đã có lịch giao nhưng Planner không thấy trên màn hình MRP do GRN hoặc trạng thái nhận hàng cập nhật trễ.
- Casing và packaging được request dư vì planner sợ trầy xước hoặc thiếu carton khi đóng hàng.
- Sensor module có lead time dài nên planner thường đặt buffer 20-30%.

## Known Data Issues
- Một số PR không có `exception_reason` dù quantity vượt BOM.
- Một số PO có ngày tạo gần nhau, cùng vendor, cùng material và dưới 50,000 USD.
- ERP tồn kho không phản ánh vật tư bị QC hold trong ngày.
- `open_po_grn.csv` có các dòng `erp_visible_to_planner = N`, dùng để kiểm tra đứt gãy thông tin giữa mua hàng, kho và planning.
