# TÀI LIỆU THIẾT KẾ KỸ THUẬT & TÍNH TOÁN CÔNG SUẤT HỆ THỐNG BIOGAS Ủ KHÔ NGẦM HÓA
**Dự án:** Trạm Sạc Xe Điện Tuần Hoàn Năng Lượng Flagship (Quy mô KCN)  
**Tác giả:** Đội ngũ Nghiên cứu & Phát triển (R&D) Letron  

---

## I. TỔNG QUAN CÔNG NGHỆ LỰA CHỌN (DRY ANAEROBIC DIGESTION)

Hệ thống biogas của trạm sạc Flagship áp dụng công nghệ **Ủ khô kỵ khí (Dry Anaerobic Digestion)** nhằm tối ưu hóa diện tích chiếm dụng mặt đất và loại bỏ nhu cầu xử lý lượng nước thải pha loãng khổng lồ từ công nghệ ủ ướt truyền thống:
* **Hàm lượng chất rắn khô cao (Total Solids - TS):** Duy trì từ 20% đến 30% trong suốt chu kỳ phân hủy.
* **Ngầm hóa chịu lực:** Toàn bộ bể phân hủy sinh học và thiết bị xử lý phụ trợ được lắp đặt dưới lòng đất, bên dưới nền bê tông chịu tải của bãi đỗ xe điện.
* **Hệ thống bể đôi song song:** Chia nhỏ quy trình thành hai bể hoạt động luân phiên, bảo đảm sự liên tục của dòng khí methane đầu ra.

---

## II. THÔNG SỐ ĐẦU VÀO THIẾT KẾ (DESIGN INPUTS)

Dưới đây là các thông số đặc tính của chất thải hữu cơ đầu vào được sử dụng làm cơ sở thiết kế hệ thống:

| Thông số đầu vào | Ký hiệu | Giá trị định mức | Đơn vị | Nhận xét |
| :--- | :--- | :--- | :--- | :--- |
| **Khối lượng rác nạp hàng ngày** | M_in | 350 | kg/ngày | Rác thải thực phẩm nhà ăn KCN băm nhỏ |
| **Khối lượng riêng của rác băm** | rho_in | 750 | kg/m³ | Trạng thái xốp sau khi băm |
| **Độ ẩm của chất thải** | MC | 75 | % | Hàm lượng nước tự nhiên trong rác thực phẩm |
| **Hàm lượng chất rắn khô** | TS | 25 | % | Tương đương 87.5 kg chất khô/ngày |
| **Hàm lượng chất rắn bay hơi** | VS | 85 | % của TS | Tương đương 74.4 kg chất hữu cơ phân hủy/ngày |

---

## III. TÍNH TOÁN KÍCH THƯỚC BỂ PHÂN HỦY (DIGESTER SIZING)

Quy trình tính toán dung tích bể ủ khô kỵ khí được thực hiện theo các bước kỹ thuật sau:

1. **Thể tích rác nạp hàng ngày (V_in):**
   * V_in = M_in / rho_in = 350 kg / 750 kg/m³ = **0.47 m³/ngày**.
2. **Thời gian lưu giữ chất thải kỵ khí (Hydraulic Retention Time - HRT):**
   * Lựa chọn thời gian lưu giữ đạt **25 ngày** để bảo đảm vi sinh vật phân hủy triệt để xenlulozo và protein ở điều kiện nhiệt độ ổn định 38 độ C.
3. **Thể tích chất nền hoạt động (V_active):**
   * V_active = V_in x HRT = 0.47 m³/ngày x 25 ngày = **11.75 m³**.
4. **Thể tích bùn hoạt tính tuần hoàn để mồi vi sinh (V_inoculum):**
   * Thiết kế yêu cầu phối trộn 25% thể tích bùn vi sinh hoạt tính tuần hoàn để duy trì mật độ vi khuẩn methanogen và chống axit hóa nhanh bể ủ.
   * V_mix = V_active x 1.25 = 11.75 m³ x 1.25 = **14.7 m³**.
5. **Khoảng trống an toàn chứa khí phía trên (Freeboard - 20%):**
   * Tổng dung tích yêu cầu của hệ thống: V_total = V_mix / 0.8 = 14.7 m³ / 0.8 = **18.375 m³**.
   * Quy tròn dung tích thiết kế lên **20 m³**.

### Cấu hình thiết bị lựa chọn:
* Lắp đặt **02 bể composite ngầm song song, mỗi bể có dung tích 10 m³** (Đường kính trong: 2.0m, Chiều dài: 3.2m).
* Việc chia đôi bể giúp thuận tiện cho công tác bảo trì, nạp liệu luân phiên theo mẻ 25 ngày mà dòng khí sinh học đầu ra luôn duy trì ổn định.

---

## IV. TÍNH TOÁN SẢN LƯỢNG KHÍ VÀ ĐIỆN NĂNG THU HỒI

1. **Sản lượng Biogas hàng ngày:**
   * Hiệu suất sinh khí từ rác thực phẩm phân hủy khô đạt trung bình 128.5 m³ Biogas trên mỗi tấn rác thô.
   * Tổng thể tích Biogas thu về hàng ngày: 0.35 tấn x 128.5 m³/tấn = **45.0 m³ Biogas/ngày**.
2. **Thành phần khí sinh học sau lọc sạch (Membrane Upgrading):**
   * Khí Methane (CH4 - 60%): **27.0 m³/ngày**.
   * Khí Carbon Dioxide (CO2 - 40%): **18.0 m³/ngày**.
3. **Hiệu suất phát điện từ khí sinh học tại chỗ:**
   * Lượng khí CH4 sạch sau lọc màng (27.0 m³/ngày) được cấp cho máy phát điện chạy gas công suất 15 kW (hiệu suất chuyển hóa 35%).
   * Chỉ số tiêu hao của động cơ gas: ~0.285 m³ CH4 để phát ra 1 kWh điện.
   * Tổng điện năng sinh ra: 27.0 m³ / 0.285 m³/kWh = **94.7 kWh điện/ngày** (đáp ứng phần lớn nhu cầu điện cơ bản của trạm sạc nghỉ dưỡng).

---

## V. CẤU TẠO CHI TIẾT & HỆ THỐNG PHỤ TRỢ BỂ Ủ NGẦM

Toàn bộ hệ thống 2 bể 10 m³ được thiết kế cơ khí đồng bộ để bảo đảm độ bền cơ học và hiệu suất nhiệt động học:

```mermaid
flowchart TD
    %% Định nghĩa các khối thiết bị chính
    Cabin[Cabin Tiếp Nhận Rác Trên Mặt Đất] -->|Trục vít tải kín| Digester[Hệ Thống 2 Bể Composite Ngầm: 20m3]
    
    %% Phân khu ngầm hóa cách nhiệt và gia nhiệt
    subgraph Digester_System["Hệ Thống Bể Ngầm Cách Nhiệt & Gia Nhiệt"]
        Digester
        PU[Lớp bảo ôn PU Foam dày 100mm] -.->|Bọc thân bể| Digester
        CHP_Heating[Cuộn ống đồng dẫn nhiệt CHP] -.->|Sưởi ấm ổn định 38°C| Digester
    end
    
    %% Đường thu hồi và lọc khí Biogas chính
    Digester -->|Thu hồi Biogas thô từ đỉnh bể| Gas_Buffer[Bình Đệm Chứa Biogas Áp Suất Thấp]
    Gas_Buffer -->|Lọc ẩm & bụi| Filter[Cột Khử H2S Fe2O3]
    Filter -->|Biogas sạch sau lọc H2S| Membrane[Hệ Màng Lọc Upgrading Membrane]
    
    %% Phân tách dòng từ Membrane
    Membrane -->|CH4 sạch 60%| Gen[Máy Phát Điện Chạy Gas]
    Membrane -->|CO2 giàu 40%| CO2_Buffer[Bình Đệm Chứa CO2]
    
    %% Kết nối năng lượng điện & khí thải
    Gen -->|Dòng điện phát ra| BESS[Tủ Pin Lưu Trữ BESS]
    Gen -->|Khí thải chứa CO2 (Mùa đông/Zero-emission)| Mineral["Bể Khoáng Hóa CO2 bằng Ca(OH)2"]
    CO2_Buffer -->|Mùa đông / Thiếu điện| Mineral
    
    %% Đường xả thải và lọc khí âm rò rỉ
    Digester -->|Bơm bùn trục vít| Press[Máy Ép Trục Vít Tách Nước]
    Digester -->|Quạt hút khí áp suất âm| Biofilter[Tháp Lọc Sinh Học Khử Mùi Ngầm]
    
    %% Sản phẩm đầu ra phụ
    Press -->|Nhiệt sấy dư CHP| Fertilizer[Sản Xuất Phân Bón Hữu Cơ Đóng Bao]
    Biofilter -->|Lọc giá thể xơ dừa ẩm| Vent[Xả Khí Sạch Ra Khí Quyển]
```

1. **Kết cấu vỏ bể composite cách nhiệt:**
   * FRP composite dày 12mm chịu được áp lực đất và tải trọng xe đỗ trên bề mặt.
   * Toàn bộ thân bể được phun phủ lớp bọt cách nhiệt polyurethane (PU foam) dày 100mm, bảo vệ bằng lớp màng PE chống thấm nước ngầm bên ngoài.
2. **Hệ thống sưởi ấm CHP chủ động:**
   * Chạy các cuộn ống đồng tuần hoàn dầu truyền nhiệt bao quanh thân vỏ composite trước khi phun phủ PU foam.
   * Nhiệt lượng nóng (80 - 90 độ C) dẫn từ bộ thu hồi nhiệt dư CHP (lò Sabatier và khí thải động cơ) liên tục chạy qua ống đồng, giữ ấm hỗn hợp ủ ổn định ở 38 độ C bất kể thời tiết giá lạnh của mùa đông miền Bắc.
3. **Cơ cấu nạp liệu áp suất âm:**
   * Trạm tiếp nhận rác băm đặt trên mặt đất có cửa lùa gioăng kín. Rác được băm nhỏ tự động đưa xuống bể ngầm thông qua trục vít tải (screw conveyor) khép kín chịu áp lực, ngăn ngừa hoàn toàn mùi hôi thoát ra.
4. **Cơ cấu xử lý bã thải & sản xuất phân bón vi sinh thương mại:**
   * **Đầu ra bùn thải kỵ khí (Digestate):** Với 350 kg rác thực phẩm nạp vào mỗi ngày, sau khi phân hủy kỵ khí và tiêu hao chất rắn bay hơi (VS), lượng bùn sinh học thải ra định kỳ khoảng **120 kg/ngày** (độ ẩm tự nhiên khoảng 85%, tương đương 18 kg chất khô/ngày).
   * **Bơm bùn chuyên dụng:** Sử dụng bơm trục vít xoắn chịu mài mòn cao (công suất 0.75 kW) để bơm bùn từ đáy bể ngầm lên hệ xử lý mặt đất.
   * **Hệ thống ép tách nước (Screw Press):** Bùn thải đi qua máy ép trục vít công suất 1.5 kW, sử dụng lưới lọc hình trụ bằng Inox 304 có khe hở 0.5mm.
     * Hiệu quả tách nước: Ép độ ẩm bùn giảm từ 85% xuống **60% (độ ẩm bánh bùn)**.
     * Khối lượng bánh bùn sau ép: Giảm xuống còn xấp xỉ **45 kg/ngày** (tiết giảm 62.5% tổng khối lượng cần vận chuyển). Lượng nước ép (moisture water) được dẫn tuần hoàn ngược lại bể ủ để cấp ẩm hoặc đưa vào hệ thống xử lý nước thải.
   * **Buồng sấy khô cưỡng bức bằng nhiệt dư CHP (Thermal Cascade Tier 4):**
     * Bánh bùn sau ép (45 kg, độ ẩm 60%) được chuyển vào buồng sấy khay tĩnh hoặc tang trống quay nhỏ.
     * Nguồn nhiệt sấy: Sử dụng quạt hút nhiệt (0.37 kW) tuần hoàn dòng khí nóng 65 - 75 độ C đi qua bộ trao đổi nhiệt khí-dầu (dẫn dầu truyền nhiệt silicone từ lò Sabatier và nước giải nhiệt máy phát điện).
     * Yêu cầu bốc hơi nước: Cần bay hơi từ 60% xuống độ ẩm mục tiêu **25% (độ ẩm chuẩn của phân hữu cơ vi sinh)**, tương đương bốc hơi **21 kg nước/ngày**.
     * Năng lượng nhiệt tiêu hao: Khoảng 14.7 kWh nhiệt/ngày (hoàn toàn tự cung cấp từ cụm CHP).
     * Khối lượng phân khô thô thu hồi: **~24 kg/ngày**.
   * **Phối trộn chế phẩm vi sinh hữu ích & Khoáng hóa CO2:**
     * Phân khô sau sấy (~24 kg/ngày) được đưa vào máy trộn bột trục ngang.
     * Bổ sung 5% chế phẩm vi sinh dạng bột chứa các bào tử vi sinh vật đối kháng và phân giải xenlulozo mạnh mẽ (*Trichoderma harzianum*, *Bacillus subtilis*, *Azotobacter*) và chất mang dinh dưỡng khoáng (Humic).
     * **Tích hợp khoáng hóa CO2 mùa đông:** Vào mùa đông hoặc khi thiếu điện mặt trời, lượng khí $CO_2$ thu hồi từ biogas (~35.3 kg $CO_2$/ngày) được sục qua dung dịch vôi tôi để tạo ra **~80.3 kg Canxi Cacbonat ($CaCO_3$) rắn**. Lượng bột Canxi này được trộn trực tiếp vào mẻ phân bón để tạo ra dòng sản phẩm phân bón hữu cơ vi sinh giàu Canxi giúp khử chua đất nông nghiệp hiệu quả.
     * **Sản lượng phân hữu cơ vi sinh thành phẩm:** Đạt **~25.2 kg/ngày** (Mùa hè - không trộn vôi) và tăng lên **~105.5 kg/ngày** (Mùa đông - có tích hợp khoáng hóa $CaCO_3$). Được đóng vào bao thương hiệu Letron Organic phục vụ chăm sóc cảnh quan resort hoặc bán thương mại cho các hộ nông nghiệp lân cận KCN.
   * **Mạch tuần hoàn không xả thải lỏng (Zero Liquid Discharge - ZLD) cho dịch ép:**
     * Với 75 lít nước dịch ép tách ra từ máy ép trục vít hàng ngày, hệ thống được thiết kế khép kín hoàn toàn, triệt tiêu 100% nước thải công nghiệp ra ngoài:
     * **Phần 1 - Tưới cảnh quan resort (15 lít/ngày):** 
       * Đáp ứng nhu cầu tưới dinh dưỡng định kỳ cho cây xanh xung quanh trạm sạc.
       * Dịch ép thô qua bể sục khí hiếu khí nhỏ (Aerobic Stabilization Tank, 500 lít) trong 24 - 48 giờ để khử sạch mùi hôi và chuyển hóa đạm amoni thành dạng nitrat dễ tiêu, sau đó pha loãng với nước sạch để tưới trực tiếp.
     * **Phần 2 - Lọc sạch tinh khiết cấp cho bộ điện phân PEM (60 lít/ngày):**
       * Phần dịch ép dư thừa còn lại (60 lít/ngày) được đưa qua cụm lọc màng RO tích hợp lọc than hoạt tính mini (RO Purification Module).
       * Hiệu suất thu hồi nước sạch đạt 80% (tương đương **~48.0 lít nước tinh khiết/ngày**). Nước sạch này đạt tiêu chuẩn dẫn thẳng vào bồn chứa nước cấp cho bộ điện phân màng PEM, kết hợp với dòng nước ngưng tụ thu hồi từ lò Sabatier (~28.8 lít/ngày) tạo thành vòng tuần hoàn kín **vượt nhu cầu nước cấp** của PEM (57.6 lít/ngày), giúp trạm sạc tự chủ 100% tài nguyên nước cấp điện phân.
     * **Phần 3 - Tuần hoàn bùn thải cô đặc (12.0 lít/ngày):**
       * 20% lượng dịch ép đậm đặc sau lọc RO (khoảng 12.0 lít/ngày chứa toàn bộ muối khoáng và chất dinh dưỡng dư) được bơm tuần hoàn ngược lại buồng sấy phân bón vi sinh. Nhiệt dư CHP sẽ sấy khô lượng bùn này thành thể rắn, trộn vào phân bón vi sinh đóng bao.

---

## VI. AN TOÀN VẬN HÀNH & KIỂM SOÁT MÙI HÔI TRONG KCN

Để bảo đảm tiêu chuẩn vệ sinh môi trường nghiêm ngặt của khu công nghiệp và duy trì cảnh quan phòng chờ quán cà phê sang trọng bên cạnh, hệ thống áp dụng 3 lớp bảo vệ:
* **Lớp 1 - Kiểm soát áp suất âm bể ủ ngầm:** Quạt hút liên tục hút biogas thô từ đỉnh hầm ủ về bình chứa đệm, duy trì trạng thái áp suất âm nhẹ bên trong bể ngầm để ngăn chặn hoàn toàn khí tự thoát qua các khớp nối.
* **Lớp 2 - Tháp lọc mùi sinh học xơ dừa ẩm (Biofilter):** Khí thải thoát ra tại khu vực cabin băm rác được gom qua quạt hút cưỡng bức đưa qua tháp lọc sinh học ẩm đặt ngầm dưới đất (chứa giá thể xơ dừa, than hoạt tính và vi sinh vật chuyên dụng để khử sạch H2S và hợp chất hữu cơ bay hơi VOCs trước khi thải ra khí quyển).
* **Lớp 3 - Hệ van bảo vệ quá áp (PVRV):** Mỗi bể composite được trang bị van thở an toàn chống quá áp và chân không (Pressure Vacuum Relief Valve) dẫn ống xả cao lên cột thu lôi của trạm sạc để bảo đảm an toàn cháy nổ tuyệt đối.

---

## VII. BẢNG SO SÁNH CHI PHÍ ĐẦU TƯ (CAPEX) CÁC PHƯƠNG ÁN HỆ THỐNG BIOGAS

Dưới đây là bảng tổng hợp so sánh chi phí đầu tư (CAPEX) chi tiết giữa hai tùy chọn quy mô triển khai, giúp doanh nghiệp dễ dàng đánh giá và lựa chọn phương án phân bổ nguồn vốn. Cả hai tùy chọn đều tích hợp đầy đủ công nghệ tuần hoàn khép kín (điện phân PEM, tháp Sabatier, màng lọc Upgrading Membrane, đóng bình Bio-CNG và sấy phân bón), chỉ khác nhau về quy mô công suất thiết bị:
* **Tùy chọn A (Đơn vị Tối thiểu - Minimum Unit cho 01 Bốt sạc súng đôi - 02 súng sạc):** Thiết kế ở quy mô siêu nhỏ (micro-scale) để xử lý trung bình 175 kg rác/ngày, phục vụ phát điện bổ trợ 5 kW và đóng bình Bio-CNG quy mô nhỏ để cấp nguồn độc lập cho 01 bốt sạc súng đôi.
* **Tùy chọn B (Quy mô Trạm Flagship 500m² KCN - Trang bị 04 Bốt sạc kép - 08 súng sạc):** Thiết kế ở quy mô thương mại hoàn chỉnh (commercial-scale) để xử lý triệt để 350 kg rác/ngày, phục vụ phát điện 15 kW cách âm, đóng bình Bio-CNG công suất lớn và cấp nguồn cho hệ thống 04 bốt sạc kép (tổng cộng 08 súng sạc AC/DC) đặt dưới mái che Solar Carport rộng 250m².

| STT | Hạng mục thiết bị / Chi phí | Tùy chọn A (Minimum Unit) | Tùy chọn B (Trạm Flagship 500m²) |
| :--- | :--- | :--- | :--- |
| 1 | **Hệ thống bể phân hủy ngầm** | 65,000,000 *(01 bể FRP 10m³)* | 150,000,000 *(02 bể FRP 10m³ + CHP)* |
| 2 | **Cabin & Hệ thống nạp liệu** | 25,000,000 *(Trục vít bán tự động)* | 45,000,000 *(Cabin kín áp suất âm + Trục vít)* |
| 3 | **Hệ lọc khử độc H2S** | 15,000,000 *(Cột lọc đơn Fe2O3)* | 35,000,000 *(Cột lọc kép song song)* |
| 4 | **Máy phát điện chạy gas** | 25,000,000 *(Động cơ gas cải tiến 5 kW)* | 75,000,000 *(Máy phát gas 15 kW cách âm)* |
| 5 | **Màng lọc nâng cấp Biogas Membrane** | 25,000,000 *(Tháp lọc màng thô)* | 75,000,000 *(Tháp lọc màng sợi rỗng cao cấp)* |
| 6 | **Hệ nén đóng bình Bio-CNG** | 50,000,000 *(Máy nén mini + bình chứa)* | 120,000,000 *(Máy nén piston 200 bar + bình chứa)* |
| 7 | **Ép bùn & Sấy phân bón** | 25,000,000 *(Khay sấy nhiệt + ép mini)* | 60,000,000 *(Máy ép trục vít + buồng sấy)* |
| 8 | **Tháp khử mùi Biofilter** | 15,000,000 *(Tháp xơ dừa đặt nổi)* | 30,000,000 *(Tháp lọc sinh học ngầm)* |
| 9 | **Tủ điều khiển & Tự động hóa** | 20,000,000 *(PLC mini giám sát áp/nhiệt)* | 55,000,000 *(PLC Siemens + cảm biến + SCADA)* |
| 10 | **Xây dựng & Lắp đặt ngầm** | 30,000,000 *(Đào móng định vị bể 10m³)* | 120,000,000 *(Gia cố móng bê tông chịu tải bãi đỗ)* |
| | **TỔNG CỘNG CAPEX** | **295,000,000 VNĐ** | **765,000,000 VNĐ** |
