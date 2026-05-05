# SOP: Mua hàng PR/PO

## Thuật ngữ & viết tắt
- **PR:** Purchase Request, yêu cầu mua hàng nội bộ.
- **PO:** Purchase Order, đơn đặt hàng gửi nhà cung cấp.
- **GRN:** phiếu ghi nhận hàng đã nhận vào kho.
- **Emergency PO:** PO tạo để xử lý nhu cầu gấp, thường có rủi ro giá cao.
- **Split PO:** chia nhỏ PO để né ngưỡng phê duyệt hoặc làm yếu kiểm soát.
- **Target price:** giá mục tiêu dùng để so sánh với giá mua thực tế.

## 1. Mục đích
Đảm bảo mọi Purchase Order được tạo từ Purchase Request hợp lệ, có đủ phê duyệt và không vượt nhu cầu sản xuất.

## 2. Quy trình chuẩn
1. Purchasing Officer nhận PR từ ERP.
2. Kiểm tra vendor đã được phê duyệt.
3. Kiểm tra giá mua so với last purchase price và target price.
4. Nếu PO trên 50,000 USD, cần Finance Controller duyệt.
5. Nếu PO dưới 50,000 USD, Purchasing Manager có thể duyệt.
6. Emergency PO phải có lý do và người yêu cầu.
7. Không chia PO để né hạn mức phê duyệt.

## 3. Quy định giá
- Chênh lệch giá trên 12% so với target price phải có báo giá phụ.
- Emergency PO được phép cao hơn target price nhưng phải ghi `emergency_reason`.
- Vendor mới phải có Vendor Master approval trước khi tạo PO.

## 4. Điểm kiểm soát
- Mỗi PO phải có `pr_id`.
- PO quantity không được vượt PR quantity nếu không có approval note.
- Nhiều PO cùng vendor, cùng material, cùng ngày, cùng người tạo cần được xem xét split PO.

## 5. Ghi chú thực tế
Purchasing thường xử lý PR urgent qua email trước, sau đó cập nhật ERP cuối ngày. Điều này tạo rủi ro PO có ngày tạo trước khi PR được hoàn thiện trong hệ thống.
