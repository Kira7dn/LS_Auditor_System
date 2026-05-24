# USE CASE 01: KIỂM SOÁT HAO HỤT VẢI CẮT (FABRIC CUTTING WASTE CONTROL)

## I. MỤC TIÊU & PHẠM VI (OBJECTIVES & SCOPE)
* **Khâu vận hành:** Phòng cắt & Trải vải (Xưởng may Thủ Đức).
* **Mục tiêu kiểm toán:** Đối chiếu chênh lệch định mức thiết kế lý thuyết (CAD marker) so với lượng vải xuất kho may thực tế nhằm phát hiện hao hụt, lãng phí trải vải, lỗi cắt phạm và nguy cơ cạn kiệt định mức cấp phát của Buyer (BOM depletion).
* **Cam kết tài chính:** Ước tính hao hụt thực tế từ 1.5% - 2.0% (khoảng 7 - 10 tỷ đồng/năm). Mục tiêu thu hồi 50% lượng thất thoát này.

---

## II. THÀNH PHẦN HỒ SƠ CẦN THU THẬP (REQUIRED DOSSIER FILES)

### 1. Hồ sơ Quy trình Thô (Governance Dossier)
* [ ] **`cutting_sop.md`**: Quy định về định mức co rút vải, ma trận phê duyệt định mức hao hụt bù đầu tấm và quy trình trải cắt chính thức.
* [ ] **`cutting_transcript.md`**: Biên bản phỏng vấn Tổ trưởng bàn cắt, Giám đốc sản xuất (COO) và Thủ kho vải về thực tế trải vải và xử lý lỗi hao hụt.
* [ ] **`workaround_notes.md`**: Nhật ký các lối đi tắt (Ví dụ: tự ý lấy vải PO này bù PO khác mà không ghi sổ, hoặc tự điều chỉnh tỷ lệ co rút khi trải vải).
* [ ] **`contradiction_notes.md`**: Bản đối chiếu chỉ ra sự lệch pha giữa SOP chính thức và thực tế vận hành.

### 2. Dữ liệu Kỹ thuật & Giao dịch (Technical Dossier)
* [ ] **`master_bom_fabric.csv`**: Định mức tiêu hao vải lý thuyết cho từng mã hàng/PO theo hợp đồng với Buyer.
* [ ] **`cad_marker_layout.csv` (hoặc `.xml` / `.dxf`)**: Sơ đồ cắt tối ưu xuất từ phần mềm CAD (diện tích chi tiết, tỷ lệ hao hụt định mức kỹ thuật).
* [ ] **`fabric_issuance_transactions.csv`**: Nhật ký xuất kho vải (mã cây vải, chiều dài thực tế, mã PO nhận vải).
* [ ] **`cutting_production_logs.csv`**: Nhật ký bàn cắt (số lớp trải, chiều dài bàn trải thực tế, số lượng chi tiết đã cắt thành công).

---

## III. CÁC RỦI RO VẬN HÀNH & THIỆT HẠI KINH TẾ (OPERATIONAL & ECONOMIC RISKS)

Quy trình cắt là "cổ chai vật chất" trong chuỗi giá trị dệt may len Merino cao cấp. Mọi sai hỏng tại đây đều biến nguyên liệu đắt đỏ thành phế phẩm công nghiệp. Dưới đây là 6 rủi ro vật lý cốt lõi gây tổn thất tài chính trực tiếp:

### 1. Rủi ro Co rút vật lý sau cắt (Post-Cut Shrinkage / Relaxation Failure)
* **Mô tả:** Vải len Merino có tính đàn hồi cao. Nếu không để nghỉ đủ 24 - 48 giờ để giải phóng ứng suất kéo căng trước khi trải (do áp lực tiến độ), vải sẽ tiếp tục co rút tự do *sau khi cắt*.
* **Tác hại kinh tế:** Chi tiết sau cắt bị hụt kích thước so với thiết kế. Khi ráp lên thành phẩm, bộ veston bị lệch size (tay ngắn, chật ngực) và bị QC loại bỏ 100% ở khâu đóng gói (COPQ), lãng phí toàn bộ vải, trims và nhân công may ráp.

### 2. Lãng phí do hao hụt đầu tấm khi trải vải (Excess Spreading End-Loss)
* **Mô tả:** Khi trải nhiều lớp vải chồng lên nhau trên bàn cắt dài, công nhân phải cắt đứt hai đầu bàn trải. Công nhân thao tác ẩu chừa dư mỗi đầu tấm một khoảng dài (15 - 20 cm thay vì 5 - 10 cm tiêu chuẩn).
* **Tác hại kinh tế:** Phần vải thừa đầu tấm hoàn toàn biến thành vải vụn. Với bàn cắt 100 lớp, việc chừa dư thêm 10cm mỗi đầu tấm gây lãng phí vô ích **20 mét vải** đắt tiền cho một lần lên bàn cắt.

### 3. Lệch biên và Trải vải bị căng (Edge Alignment & Tension Defect)
* **Mô tả:** 
    * *Lệch biên:* Các cây vải dệt ra có biên vải không đều. Trải vải lệch biên khiến sơ đồ CAD Marker bị chườm ra ngoài mép vải thực tế.
    * *Trải căng:* Công nhân kéo vải quá mạnh khi trải làm vải bị giãn cơ học tạm thời.
* **Tác hại kinh tế:** Cắt ra chi tiết bị thiếu hụt góc, sứt mẻ không thể may ráp, buộc phải hủy bỏ để cắt bù. Trải căng làm vải co lại sau cắt gây méo mó chi tiết và lệch form áo vest.

### 4. Rủi ro Lệch sọc/Carô (Pattern Pattern-Matching Failure)
* **Mô tả:** Đối với veston cao cấp kẻ sọc/carô, các đường kẻ ở ve áo, nắp túi và cầu vai phải khớp đối xứng tuyệt đối với thân áo. Rủi ro xảy ra khi công nhân đặt sơ đồ CAD lệch tọa độ sọc hoặc các lớp vải trải chồng lên nhau không được ghim định vị sọc thẳng hàng.
* **Tác hại kinh tế:** Sản phẩm may lên bị lệch sọc (Critical Defect) sẽ bị các Buyer khó tính (Ted Baker, Next) trả lại toàn bộ lô hàng hoặc phạt khấu trừ (Chargeback) cực nặng, gây mất trắng chi phí sản xuất.

### 5. Nhầm lẫn mã màu giữa các cây vải (Dye-lot / Shade Band Mixing)
* **Mô tả:** Các cây vải thuộc hai mẻ nhuộm (Dye-lot) khác nhau luôn có độ lệch màu ngoại quan cực nhỏ. Rủi ro xảy ra khi tổ cắt dồn các chi tiết cắt của cây vải mẻ A và mẻ B vào cùng một bó bán thành phẩm giao sang chuyền may.
* **Tác hại kinh tế:** May ráp lộn xộn thân áo mẻ A với tay áo mẻ B. Khi thành phẩm đi ra phòng ủi dưới ánh sáng chuẩn sẽ lộ rõ lỗi lệch màu giữa các bộ phận, làm hỏng hoàn toàn bộ veston cao cấp.

### 6. Thất lạc chi tiết nhỏ gây dừng chuyền may (Lost Cut Piece / Line Downtime)
* **Mô tả:** Một bộ veston gồm 30 - 40 chi tiết cắt lớn nhỏ. Trong quá trình bó hàng (bundling) và đánh số thứ tự lớp vải, công nhân làm rơi mất hoặc đánh sai số thứ tự kiện.
* **Tác hại kinh tế:** Chuyền may đang chạy ráp với tốc độ cao buộc phải dừng hoạt động toàn bộ (30 - 40 công nhân ngồi chờ) để chờ phòng cắt tìm kiếm hoặc thiết lập máy CAD để cắt bù một miếng vải nhỏ lẻ. Chi phí thời gian dừng chuyền (Line downtime) gây lãng phí OpEx rất lớn.

---

## IV. ĐIỂM KIỂM SOÁT KIỂM TOÁN (AUDIT CONTROL POINTS)
* **CP-02 (Vòng lặp co rút động):** Tỷ lệ co rút thực tế đo từ khâu hoàn tất nhuộm phải được cập nhật ngược về phần mềm sơ đồ cắt CAD của cây vải tương ứng trước khi cắt.
    * *Rủi ro nếu thiếu (`R-02`):* Cắt sai kích cỡ veston do co rút vải không đồng đều, bị Buyer phạt đền BOM hoặc chargeback hàng lỗi.
* **CP-04 (Đối chéo sản lượng Cắt - May):** Đối chiếu chéo số lượng chi tiết cắt hoàn tất với số lượng quét QR ráp chuyền may thời gian thực.
    * *Rủi ro nếu thiếu (`R-04`):* Khai khống sản lượng bàn cắt, mượn sản lượng chéo PO để lấy thưởng năng suất.
* **CP-06 (Kiểm toán độ trễ ghi sổ):** Gắn cờ giao dịch xuất kho bù hoặc điều chỉnh số dư lùi ngày trên ERP trễ hơn 24 giờ.
    * *Rủi ro nếu thiếu (`R-06`):* Công nhân ghi sổ lùi ngày để hợp thức hóa lượng vải cắt hỏng.
