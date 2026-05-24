# USE CASE 03: VẬN HÀNH LÒ HƠI & GIÁM SÁT KHÍ THẢI (BOILER OPERATIONS & ESG CARBON LEDGER)

## I. MỤC TIÊU & PHẠM VI (OBJECTIVES & SCOPE)
* **Khâu vận hành:** Vận hành lò hơi đốt than cám tại nhà máy Thủ Đức (cấp nhiệt cho bể nhuộm) & Giám sát điện năng tiêu thụ dệt/may (Scope 2).
* **Mục tiêu kiểm toán:** 
    1. Giám sát thông số buồng đốt thời gian thực để tối ưu tỷ lệ gió/than, ngăn khói đen và bụi mịn phát sinh gây ô nhiễm.
    2. Đối chéo hóa đơn than mua vào trên sổ kế toán với lượng than tiêu thụ thực tế qua hệ thống IoT cấp than lò hơi.
    3. Thiết lập Sổ cái Carbon bất biến (Immutable Carbon Ledger Scope 1 & 2) đạt chuẩn CBAM để thông quan hàng hóa đi EU.
* **Tầm quan trọng chiến lược:** Triệt tiêu rủi ro bị đình chỉ sản xuất do khiếu nại của cư dân chung cư **9View Apartment** và Sở TN&MT TP.HCM (phạt hành chính 430 triệu năm 2022). Đáp ứng quy định phát thải của Buyer (Ted Baker, Next).

---

## II. THÀNH PHẦN HỒ SƠ CẦN THU THẬP (REQUIRED DOSSIER FILES)

### 1. Hồ sơ Quy trình Thô (Governance Dossier)
* [ ] **`boiler_sop.md`**: Quy trình vận hành lò hơi, định mức kỹ thuật than cám tiêu hao trên mỗi tấn hơi nước, quy chuẩn an toàn môi trường nội bộ.
* [ ] **`environmental_complaints_log.md`**: Nhật ký khiếu nại của cư dân chung cư 9View, các biên bản làm việc với Sở Tài nguyên & Môi trường TP.HCM.
* [ ] **`boiler_interview_transcript.md`**: Biên bản phỏng vấn kỹ sư lò hơi, quản lý xưởng nhuộm và trưởng bộ phận ESG của LPTex.
* [ ] **`energy_compliance_criteria.md`**: Bảng tiêu chuẩn chất lượng khí thải (PM2.5, CO, SO2) theo luật định Việt Nam và yêu cầu của Buyer châu Âu (CBAM).

### 2. Dữ liệu Kỹ thuật & Giao dịch (Technical Dossier)
* [ ] **`boiler_iot_emissions.csv`**: Dữ liệu cảm biến ống khói lò hơi (Nồng độ O2, CO, nhiệt độ khói thải, bụi mịn PM2.5).
* [ ] **`coal_purchase_invoices.csv`**: Danh sách hóa đơn VAT và phiếu cân mua than cám đầu vào từ kế toán.
* [ ] **`boiler_coal_consumption.csv`**: Nhật ký cơ học ghi nhận lượng than nạp vào lò (hoặc số liệu từ bộ nạp than tự động).
* [ ] **`factory_power_consumption.csv`**: Dữ liệu chỉ số điện năng tiêu thụ đo từ các đồng hồ thông minh tại xưởng sợi, dệt, may thời gian thực.

---

## III. CÁC RỦI RO VẬN HÀNH & THIỆT HẠI KINH TẾ (OPERATIONAL & ECONOMIC RISKS)

Lò hơi cung cấp toàn bộ nhiệt năng cho phân xưởng Nhuộm Dệt, nhưng đồng thời cũng là nguồn rủi ro pháp lý sinh tồn của cả nhà máy LPTex Thủ Đức. Dưới đây là các rủi ro vận hành và môi trường có tác động tài chính trực tiếp:

### 1. Rủi ro Sử dụng nhiên liệu kém chất lượng (Substandard/Low-Grade Fuel Usage)
* **Mô tả:** Phòng thu mua chọn các nhà cung cấp than cám giá rẻ không rõ nguồn gốc (hàm lượng bùn tro dơ $> 25\%$, lưu huỳnh cao, độ ẩm lớn) để chạy theo chỉ tiêu tiết kiệm chi phí ngắn hạn của kế toán.
* **Tác hại kinh tế:** Than dơ làm giảm hiệu suất nhiệt của lò (hiệu suất sinh hơi giảm dưới $7\text{ m}^3\text{ hơi / tấn than}$), làm bám tro xỉ buồng đốt, tăng chi phí bảo dưỡng đột xuất. Đốt than dơ gây phát thải khói đen kịt và khí SO2 nồng nặc vượt chuẩn.

### 2. Rủi ro Đình chỉ sản xuất do vi phạm Môi trường (DNRE Shutdown / Legal Suspension Risk)
* **Mô tả:** Lò hơi phát thải khói bụi và khí độc vượt giới hạn cho phép do đốt than kém chất lượng hoặc hệ thống dập bụi bị hỏng, dẫn đến khiếu nại liên tục từ cư dân chung cư 9View Apartment đối diện.
* **Tác hại kinh tế:** LPTex đã bị phạt 430 triệu VND năm 2022. Rủi ro cao nhất là Sở TN&MT từ chối cấp/gia hạn Giấy phép Môi trường, đình chỉ hoạt động phân xưởng Nhuộm. Việc phân xưởng Nhuộm dừng hoạt động sẽ làm tê liệt toàn bộ chuỗi sản xuất khép kín (Sợi -> Dệt -> Nhuộm -> May), gây thiệt hại hàng chục tỷ đồng mỗi tuần dừng hoạt động và làm sụp đổ tiến trình thoái vốn nhà nước.

### 3. Rủi ro Mất kiểm soát hao hụt Than cám vật lý (Coal Theft / Inventory Discrepancy Risk)
* **Mô tả:** Than cám để ngoài bãi kho bị hao hụt tự nhiên do mưa bão rửa trôi hoặc bị gian lận, thất thoát trong quá trình vận chuyển nạp lò do quy trình cân đo nạp liệu chỉ được ghi chép thủ công (theo số xe rùa).
* **Tác hại kinh tế:** Sự chênh lệch giữa lượng than mua vào trên hóa đơn VAT và lượng than thực tế đốt lò (hao hụt âm thầm từ 5% - 10%) khiến doanh nghiệp mất hàng trăm triệu đồng mỗi tháng mua than bù đắp lượng hao hụt không rõ nguyên nhân.

### 4. Rủi ro Bị Buyer châu Âu hủy đơn hàng do vi phạm CBAM (CBAM Compliance Failure)
* **Mô tả:** LPTex không xây dựng được báo cáo phát thải Carbon Scope 1 & 2 đáng tin cậy dựa trên dữ liệu gốc (IoT/Hóa đơn) cho từng mã PO xuất khẩu sang EU theo cơ chế điều chỉnh biên giới carbon (CBAM).
* **Tác hại kinh tế:** Các Buyer lớn như Ted Baker, Next sẽ hủy đơn hàng hoặc chuyển dịch sang các đối thủ cạnh tranh tại Bangladesh/Indonesia để tránh thuế phạt carbon. LPTex mất hoàn toàn thị trường EU có biên lợi nhuận cao, sụt giảm doanh thu gộp nghiêm trọng.

### 5. Rủi ro Hỏng hóc lò hơi gây dừng chuyền Nhuộm (Boiler Failure / Operational Downtime)
* **Mô tả:** Công nhân vận hành lò sai kỹ thuật (điều chỉnh tỷ lệ gió/than không chuẩn, nồng độ O2 dư ngoài tầm 3.5% - 5.5%) dẫn đến nhiệt độ buồng đốt quá tải, áp suất hơi không ổn định gây nứt vỡ ống nước lò hơi.
* **Tác hại kinh tế:** Sự cố dừng lò hơi đột xuất làm ngừng cấp nhiệt toàn xưởng nhuộm, gây hỏng hóc hàng loạt mẻ vải đang nhuộm dở dang (COPQ nhuộm tăng vọt) và làm trễ kế hoạch giao hàng may ráp của cả nhà máy.

---

## IV. ĐIỂM KIỂM SOÁT KIỂM TOÁN (AUDIT CONTROL POINTS)
* **CP-05 (Đối chéo Carbon & Lò hơi):** Tự động đối chiếu chênh lệch giữa lượng than nhập kho trên hóa đơn VAT và lượng than thực tế nạp lò đo bằng IoT/Cân cơ học.
    * *Rủi ro nếu thiếu (`R-05`):* Thất thoát than cám (hao hụt tự do hoặc gian lận), báo cáo sai lượng phát thải carbon làm trượt Compliance Audit của Buyer.
* **Inline Combustion Control (Cảnh báo khói đen sớm):** Phát cảnh báo đỏ lên hệ thống SCADA/Mobile điều hành nếu nồng độ oxy giảm dưới ngưỡng tối ưu hoặc bụi mịn tăng cao trước khi khói đen thoát ra ống khói.
    * *Rủi ro nếu thiếu:* Bị cư dân khiếu nại, bị phạt hành chính lớn hoặc đình chỉ sản xuất khâu nhuộm.
* **Carbon Ledger (Sổ cái Carbon bất biến):** Lưu trữ số liệu phát thải Scope 1 & Scope 2 bất biến trên Cloud SaaS để xuất báo cáo kiểm định SGS/Bureau Veritas trong 1 giờ.
    * *Rủi ro nếu thiếu:* Không kịp xuất trình bằng chứng phát thải khi thông quan thuế quan CBAM tại cảng EU, dừng dòng hàng xuất khẩu.
