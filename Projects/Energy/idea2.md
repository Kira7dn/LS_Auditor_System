# THIẾT KẾ HỆ THỐNG: TỔ HỢP TRẠM SẠC XE ĐIỆN NGHỈ DƯỠNG & BIOGAS PHÁT ĐIỆN TRỰC TIẾP

Tài liệu đặc tả hệ thống tối ưu hóa hiệu suất và chi phí đầu tư cho lô đất diện tích 500m² tại Khu công nghiệp (KCN) miền Bắc, do đội ngũ nghiên cứu và phát triển (R&D) thực hiện.

------------------------------
## I. SƠ ĐỒ ĐIỀU PHỐI NĂNG LƯỢNG TỔNG THỂ (MICROGRID TỐI ƯU)

Hệ thống vận hành theo chu trình khép kín, tập trung lưu trữ năng lượng trực tiếp vào hệ thống pin BESS hiệu suất cao:

```
                                [ RÁC BẾP ĂN KCN ] (300-400 kg/ngày)
                                        │
                                        ▼
                         [ Hệ 2 Bể Biogas Ủ Khô Ngầm (20m³) ]
                                        │
                                        ▼ (Khí Biogas thô)
                            [ Bộ Lọc H2S Bằng Hạt Fe2O3 ]
                                        │
                                        ▼ (Khí Gas Sạch)
                            [ Máy Phát Điện Chạy Gas ]
                                        │
                                        ▼ (Phát điện bổ trợ)
┌───────────────────────────────────────────────────────────────────────┐
│                          TỦ PIN BESS (40 kWh)                         │ ◄─── [ GIÀN PIN SOLAR ] (20 kWp)
└───────────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼ (Cấp dòng sạc ổn định)
                            [ TRỤ SẠC XE ĐIỆN ] (01 Bốt - 02 Cổng sạc AC 7kW)
```

------------------------------
## II. CẤU TRÚC PHÂN VÙNG MẶT BẰNG LÔ ĐẤT 500m²

Mặt bằng được phân chia thành 3 phân khu chức năng biệt lập để bảo đảm tính thẩm mỹ và an toàn vận hành:

1. **Phân vùng 1 (Khu trải nghiệm - 250m²):**
   * Mái che pin mặt trời (Solar Carport) rộng khoảng 150m², phục vụ 4 vị trí đỗ sạc ô tô điện.
   * Phòng chờ nghỉ dưỡng kiêm Quán Cà phê (70m²): Tích hợp hệ thống điều hòa nhiệt độ, cảnh quan xanh, cổng sạc thiết bị di động và bảng LED hiển thị dữ liệu giảm phát thải CO2 theo thời gian thực.
2. **Phân vùng 2 (Khu kỹ thuật điều phối - 80m²):** Nơi đặt tủ pin BESS công suất 40 kWh, tủ phân phối điện thông minh và máy phát điện chạy gas bọc hộp cách âm tiêu chuẩn.
3. **Phân vùng 3 (Xưởng sinh học khép kín - 170m²):** Đặt ở vị trí cuối khu đất, ngăn cách bằng hàng rào cây xanh dày. Gồm nhà tiếp nhận rác bọc áp suất âm, hệ thống 2 bể ủ biogas khô composite ngầm (tổng dung tích 20m³) và cột lọc hấp phụ H2S bằng hạt Fe2O3 kết hợp màng lọc xơ dừa ẩm.

------------------------------
## III. CẤU TRÚC PHẦN CỨNG SẢN XUẤT NĂNG LƯỢNG LÕI (Trọng tâm R&D)

Hệ thống áp dụng chiến lược tích hợp các mô-đun cốt lõi thương mại hóa sẵn có kết hợp tự thiết kế các cụm lọc phụ trợ để tối ưu hóa chi phí:

1. **Hệ lọc khử khí độc H2S tự chế:**
   * Cột lọc chứa hạt quặng sắt oxit (Fe2O3) xếp tầng, giữ lại khí H2S gây ăn mòn. 
   * Thiết kế cột kép song song hỗ trợ quá trình hoàn nguyên hạt lọc bằng không khí tự nhiên định kỳ, duy trì tuổi thọ hệ thống lâu dài.
2. **Máy phát điện chạy khí sinh học cải tiến:**
   * Thiết kế động cơ đốt trong cải tiến bộ chế hòa khí phù hợp với đặc tính cháy của khí biogas hỗn hợp (CH4 và CO2).
   * Tích hợp bộ khởi động tự động (ATS) điều khiển qua tín hiệu điện từ tủ BESS.
3. **Hệ thống lưu trữ năng lượng BESS dung lượng cao:**
   * Sử dụng hệ pin Lithium-ion LiFePO4 dung lượng 40 kWh tích hợp mạch quản lý pin (BMS) thông minh, đạt hiệu suất sạc xả tối thiểu 88%.

------------------------------
## IV. KIẾN TRÚC PHẦN MỀM & TỰ ĐỘNG HÓA

1. **Thuật toán điều phối năng lượng thông minh (EMS):**
   * Đọc dữ liệu phụ tải sạc xe điện để điều phối ưu tiên nguồn cấp từ Solar Carport.
   * Kích hoạt tự động máy phát điện chạy gas khi dung lượng pin lưu trữ BESS xuống dưới mức 20% hoặc khi phụ tải sạc xe vượt ngưỡng chịu tải của pin.
   * Tự động kết nối mua điện lưới giờ thấp điểm vào ban đêm để nạp đầy pin BESS, tối ưu hóa chi phí vận hành.
2. **Hệ thống IoT theo dõi chỉ số Carbon (Tiêu chuẩn MRV):**
   * Số hóa dữ liệu lưu lượng khí sinh học tiêu thụ và sản lượng điện xanh sinh ra.
   * Mã hóa bảo mật và truyền tải dữ liệu thời gian thực lên hệ thống lưu trữ đám mây phục vụ việc đánh giá phát thải và bán tín chỉ Carbon quốc tế.

------------------------------
## V. BẢNG TỔNG QUAN TÀI CHÍNH (Quy mô 1 Bốt sạc)

* **Tổng vốn đầu tư (CAPEX):** ~495.000.000 VNĐ.
* **Năng lực phục vụ sạc:** 3 – 4 xe ô tô điện mỗi ngày (tương đương khoảng 58.400 kWh/năm).
* **Cơ cấu doanh thu hàng năm (~429 triệu VNĐ/năm):**
  * Doanh thu bán điện sạc (Giá thị trường 3.850đ/kWh): ~224 triệu VNĐ (52%).
  * Phí thu gom và xử lý rác hữu cơ đầu vào (500.000đ/tấn): ~73 triệu VNĐ (17%).
  * Doanh thu bán tín chỉ Carbon (Giá 50 USD/tấn CO2 giảm thiểu): ~63 triệu VNĐ (15%).
  * Doanh thu bán phân hữu cơ vi sinh Letron Organic (~9.2 tấn/năm): ~69 triệu VNĐ (16%).
* **Chi phí vận hành hàng năm (OPEX):** ~45.000.000 VNĐ (Phần lớn dành cho việc nạp điện lưới giờ thấp điểm).
* **Lợi nhuận gộp thu về:** ~384.000.000 VNĐ/năm.
* **Thời gian hoàn vốn thực tế:** Khoảng 1.29 năm (Tối ưu hóa mạnh nhờ tích hợp nguồn thu phân hữu cơ).

------------------------------
## VI. ĐÁNH GIÁ TỰ CHỦ NĂNG LƯỢNG TÁI TẠO (RE100)

Phương án tối giản đạt tỷ lệ tự chủ năng lượng cao nhưng chịu giới hạn thất thoát điện năng dư thừa:

1. **Cân đối cung - cầu điện năng hàng năm:**
   * **Tổng nhu cầu tiêu thụ:** 90 kWh điện/ngày (gồm sạc xe và phụ tải phòng chờ), tương đương **32,850 kWh/năm**.
   * **Nguồn cung Solar tại chỗ (20 kWp):** đạt **25,550 kWh/năm**.
   * **Nguồn cung điện sinh học từ biogas thô (31.5 m3 CH4/ngày):** đi qua máy phát điện gas công suất 5 kW (hiệu suất 30%) sản sinh: 11,497.5 m3 CH4 / 0.33 m3/kWh = **34,840 kWh/năm**.
   * **Tổng nguồn cung tái tạo tự sạc:** 25,550 kWh (Solar) + 34,840 kWh (Biogas thô) = **60,390 kWh/năm**.
2. **Tỷ lệ tự chủ năng lượng tái tạo:**
   * Đạt mức **100% (RE100)** tính trung bình cả năm do tổng nguồn cung xanh vượt phụ tải tiêu thụ.
3. **Mức độ hao phí năng lượng dư thừa:**
   * Hệ thống thừa khoảng **27,540 kWh điện/năm**. Tuy nhiên, do giới hạn dung lượng tủ BESS (40 kWh) và sự vắng bóng của hệ thống điện phân SOEC/tháp Sabatier, toàn bộ lượng điện mặt trời dư thừa ban ngày này bị lãng phí do không có thiết bị thu hồi và lưu trữ dưới dạng khí nén Bio-CNG.
