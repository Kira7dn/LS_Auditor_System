# DATA DICTIONARY: USE CASE 01 (FABRIC CUTTING CONTROL)

Định nghĩa cấu trúc dữ liệu mô phỏng phục vụ thuật toán đối soát khâu Cắt & Trải vải LPTex:

## 1. Bảng `yield_borrowing` (Đối chéo sản lượng Cắt - May)
* **po_number** (VARCHAR): Mã PO sản xuất veston.
* **cutting_qty** (INT): Số lượng chi tiết thân áo đã cắt thành công (quét QR bàn cắt).
* **sewing_qty** (INT): Số lượng áo veston hoàn thành may ráp thực tế (quét QR nhập kho thành phẩm).
* **timestamp_cut** (TIMESTAMP): Thời điểm thực tế cắt vải.
* **timestamp_sew** (TIMESTAMP): Thời điểm hoàn thành may ráp.

## 2. Bảng `fabric_issuance_transactions` (Nhật ký xuất kho & Ghi sổ ERP)
* **po_number** (VARCHAR): Mã PO sản xuất.
* **fabric_roll_id** (VARCHAR): Mã định danh cây vải.
* **actual_length_m** (FLOAT): Chiều dài cây vải thực tế sử dụng (mét).
* **issued_timestamp** (TIMESTAMP): Thời điểm thực tế cây vải được xuất và trải cắt.
* **posted_timestamp** (TIMESTAMP): Thời điểm kế toán ghi nhận giao dịch xuất kho lên hệ thống ERP.

## 3. Bảng `cad_marker_layout` (Định mức co rút CAD vs Tiêu thụ thực tế)
* **po_number** (VARCHAR): Mã PO sản xuất.
* **cad_shrinkage_pct** (FLOAT): Hệ số co rút thiết lập trên sơ đồ CAD Marker (%).
* **actual_shrinkage_pct** (FLOAT): Tỷ lệ co rút đo thực tế của lô vải sau khâu hoàn tất (%).
* **design_length_m** (FLOAT): Chiều dài thiết kế tối ưu lý thuyết của sơ đồ cắt (mét).
* **actual_cut_length_m** (FLOAT): Chiều dài vải thực tế cắt tại bàn trải (mét).
