# NHẬT KÝ QUY TRÌNH ĐI TẮT KHÂU CẮT VẢI (CUTTING WORKAROUND NOTES)

Tài liệu này tổng hợp các cách làm tạm thời thực tế đang diễn ra tại phân xưởng Cắt của LPTex:

## 1. Sử dụng hệ số co rút tĩnh (Static Shrinkage Override)
* **Thực trạng:** Công nhân bỏ qua việc đo co rút của từng cây vải hoàn tất từ xưởng nhuộm. Họ sử dụng cố định một sơ đồ Marker với hệ số co rút mặc định là **5%** cho tất cả các lô len Merino.
* **Lý do:** Tránh mất 30 - 45 phút thiết lập lại sơ đồ CAD trên máy dệt và tránh ùn ứ khâu cắt khi chuyền may thúc giục sản lượng.
* **Hậu quả:** Hao hụt vải thực tế vượt định mức lý thuyết từ **1.5% - 2.2%**. Lô co rút thực tế thấp hơn 5% gây lãng phí vải dư; lô co rút cao hơn 5% khiến chi tiết cắt bị hụt kích thước (hỏng sản phẩm).

## 2. Mượn sản lượng liên PO (Cross-PO Yield Borrowing)
* **Thực trạng:** Khi công nhân cắt hỏng chi tiết của PO đang cần giao gấp, Tổ trưởng bàn cắt tự ý lấy các chi tiết cắt của PO chưa may gấp để đắp qua, che giấu tỷ lệ lỗi.
* **Lý do:** Tránh bị trừ điểm thi đua năng suất của tổ cắt và kịp tiến độ may ráp xuất khẩu. PO bị mượn sẽ được làm phiếu đề xuất cấp bù nguyên liệu sau dưới dạng "hao hụt bất thường".
* **Hậu quả:** Số liệu sản lượng may và cắt bị bóp méo chéo giữa các PO, gây mất kiểm soát định mức BOM đầu vào.

## 3. Ghi sổ ERP hồi tố muộn (Weekly Retroactive ERP Logging)
* **Thực trạng:** Thay vì quét mã QR và ghi sổ nguyên liệu xuất kho tức thời (trong 1 giờ) theo SOP, tổ cắt ghi nhận thủ công trên giấy và gom lại nhập ERP vào chiều thứ Sáu hàng tuần.
* **Lý do:** Wi-Fi nhà xưởng chập chờn, công nhân tay chân dính dầu mỡ khó sử dụng máy tính bảng.
* **Hậu quả:** Kế toán bị mù thông tin kho thời gian thực, không phát hiện kịp thời biến động tồn kho và hao hụt để cấn trừ.
