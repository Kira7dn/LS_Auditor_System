# NHẬT KÝ QUY TRÌNH ĐI TẮT TẠI XƯỞNG (WORKAROUND LOGS)
Tài liệu ghi nhận các lối đi tắt (Workarounds) do nhân viên tự thực hiện để đối phó với khó khăn vận hành:

## 1. Đi tắt Hệ số Co Rút (Static Shrinkage Override)
*   *Mô tả:* Bỏ qua việc đo co rút của từng cây vải hoàn tất. Sử dụng cố định sơ đồ Marker co rút 5% cho tất cả các lô len Merino.
*   *Lý do:* Tiết kiệm 45 phút thiết lập sơ đồ CAD và tránh ùn ứ khâu cắt vải.
*   *Hệ quả:* Hao hụt vải cắt thực tế tăng thêm **1.5% - 2.2%** vượt định mức BOM.

## 2. Mượn sản lượng liên PO (Cross-PO Yield Borrowing)
*   *Mô tả:* Lấy bán thành phẩm (chi tiết cắt) của PO chưa may gấp để cấn trừ vào PO sắp đến hạn xuất khẩu nhằm che giấu lỗi cắt hỏng của công nhân.
*   *Lý do:* Tránh bị phạt KPI năng suất tổ cắt và kịp hạn giao hàng của Buyer.
*   *Hệ quả:* Số liệu sản lượng may ráp trên hệ thống ERP bị ảo (PO chưa may xong đã báo hoàn thành, PO đang may thì thiếu số liệu).

## 3. Ghi sổ hồi tố cuối tuần (Weekly Retroactive ERP Logging)
*   *Mô tả:* Thay vì quét mã QR xuất kho nguyên liệu tức thời, tổ cắt gom phiếu giấy và nhập lùi ngày (Retroactive) vào chiều thứ Sáu hàng tuần.
*   *Lý do:* Tránh phiền hà do Wi-Fi xưởng yếu và công nhân không biết dùng app ERP.
*   *Hệ quả:* Kế toán hoàn toàn mất kiểm soát tồn kho tức thời (Real-time Inventory), gây ra hiện tượng đọng vốn hoặc cạn kiệt BOM bất ngờ.