# LeTRON Green Logistics Project Design Document (PDD)

## 1. Executive Summary

### 1.1 Project Overview

Dự án thí điểm vận tải xanh kết nối các KCN trọng điểm bằng xe điện nặng, sạc Megawatt và nguồn năng lượng tái tạo tại Service Hub; đồng thời thiết lập hệ thống dữ liệu chuẩn hóa sẵn sàng đáp ứng các tiêu chuẩn carbon quốc tế tự nguyện cao nhất (như Verra VCS / Gold Standard).

### 1.2 Business Objectives

* Thử nghiệm thực địa độ ổn định, hiệu suất năng lượng của hạm đội xe điện nặng (xe đầu kéo CAMC, xe tải Farizon) và trạm sạc nhanh công suất Megawatt dưới các điều kiện tải trọng thực tế.
* Kiểm chứng và hoàn thiện hệ điều hành LeOS, bộ não số LeDB cùng hệ thống tự động hóa cấp chứng thư Le-GCP.
* Đạt phê duyệt phương pháp luận đo lường tự động (MRV Methodology) từ đơn vị kiểm toán độc lập để sẵn sàng thương mại hóa giải pháp giảm phát thải Scope 3 cho các đối tác FDI vào Quý 4/2026.

### 1.3 Sustainability Objectives

* Đạt tỷ lệ năng lượng tái tạo tự cung cấp (Solar, Gió, RMFC) tại Hub dịch vụ tối thiểu là **60%** hàng năm, tận dụng tối đa dung lượng bể pin dòng chảy Vanadium VFB để dịch chuyển phụ tải.
* Đạt mục tiêu cắt giảm phát thải ròng tối thiểu **200 tấn CO2/năm** cho toàn bộ hạm đội pilot 5 xe so với kịch bản đường cơ sở sử dụng xe tải diesel truyền thống.
* Thiết lập hệ thống minh chứng số (Digital MRV) đạt chuẩn kiểm toán để sẵn sàng hỗ trợ khách hàng FDI báo cáo tuân thủ cơ chế CBAM và ESG.

### 1.4 Expected Deliverables

* **LeTRON Green Cargo Passport (Le-GCP):** Chứng thư số giảm phát thải cấp tự động kèm chữ ký số và mã băm Blockchain.
* **Carbon Ledger & Energy Ledger:** Sổ cái phân tán theo dõi dòng chảy năng lượng sạch và phát thải carbon tích lũy.
* **Green Logistics Dashboard:** Giao diện trực quan hóa lượng giảm phát thải và cường độ carbon theo thời gian thực.
* **Auditor Gateway:** Cổng API truy cập độc lập dành riêng cho đơn vị kiểm toán để đối soát dữ liệu thô.

### 1.5 Intended Verification Scope

* **ISO 14064-2:** Định lượng lượng giảm phát thải khí nhà kính cấp độ dự án vận tải xanh.
* **ISO 14067:** Đánh giá dấu chân carbon tích lũy gán cho từng tấn sản phẩm vận chuyển (Scope 3 của FDI).
* **Audit Trail:** Thiết lập chuỗi bằng chứng số liên tục từ thiết bị biên phục vụ hoạt động kiểm toán độc lập.
* **CBAM Support:** Chuẩn hóa dữ liệu phát thải đáp ứng báo cáo biên giới carbon của EU.
* **ISO/IEC 27001 & TISAX:** Bảo chứng an ninh thông tin và an toàn dữ liệu chuỗi cung ứng công nghệ cao.
* **Verra & Gold Standard Readiness:** Định hình dữ liệu chuẩn hóa phục vụ việc đóng gói chứng chỉ carbon theo cơ chế quốc tế tự nguyện (VCS/GS) trong tương lai.

## 2. Project Scope & Boundary

### 2.1 Physical Boundary (Ranh giới vật lý)

Ranh giới vật lý của dự án được xác định rõ ràng qua 3 nhóm tài sản phục vụ vận hành:

* **Energy Assets (Tài sản năng lượng tại Hub):**
  * Hệ thống điện mặt trời áp mái và bãi đỗ xe: [Điền công suất] MWp.
  * Hệ thống tuabin gió trục đứng: [Điền công suất] kW.
  * Máy phát điện Pin nhiên liệu RMFC sử dụng Bio-Methanol: [Điền công suất] kW.
  * Trạm biến áp đấu nối điện lưới quốc gia (dự phòng bù tải đỉnh).
  * Hệ thống lưu trữ năng lượng tích hợp: Bể pin dòng chảy Vanadium VFB [Điền dung lượng] MWh và Lithium-ion BESS [Điền dung lượng] MWh.
* **Mobility Assets (Tài sản di động):**
  * Hạm đội xe điện nặng: 5 xe đầu kéo CAMC [Điền mã và công suất].
  * Phạm vi di chuyển thực địa: Các tuyến đường vận chuyển kết nối giữa các Khu công nghiệp (KCN) trọng điểm, với điểm bắt đầu và kết thúc tại các Hub sạc của LeTRON.
* **Facility Assets (Tài sản hạ tầng):**
  * Service Hub: Trạm dịch vụ trung tâm tích hợp hệ thống sạc Megawatt công suất lớn và khu vực quản lý kỹ thuật.
  * Maintenance Hub: Trung tâm bảo trì kỹ thuật phương tiện và kiểm định cảm biến IoT.

### 2.2 Digital Boundary (Ranh giới số)

Ranh giới số xác định phạm vi thu thập dữ liệu và luồng xử lý thông tin được kiểm toán:

* **Hệ thống thiết bị biên (Edge IoT Systems):**
  * Le-NodeMobile: Thiết bị phần cứng IoT gắn trực tiếp trên cabin xe để đọc dữ liệu CAN Bus và cảm biến tải trọng trục.
  * Le-NodeHub: Thiết bị Gateway biên đặt tại tủ phân phối trạm sạc để kết xuất dữ liệu công tơ điện và SCADA nguồn phát sạch.
* **Nền tảng xử lý dữ liệu trung tâm (Platform Systems):**
  * Hệ điều hành LeOS: Thực thi các thuật toán tính toán lượng điện sạc hiệu dụng, phân bổ nguồn và tính toán phát thải tức thời.
  * Hệ thống Sổ cái (Ledgers): Energy Ledger (sổ cái năng lượng) và Carbon Ledger (sổ cái phát thải).
  * Bộ não số LeDB (Blockchain Layer): Lưu trữ bất biến dấu vết mật mã (mã băm Hash) của mọi giao dịch dữ liệu gốc để phục vụ kiểm toán.
* *Lưu ý:* Các dữ liệu nằm ngoài ranh giới số bao gồm dữ liệu kế toán tài chính nội bộ, lịch trình lái xe chi tiết và thông tin cá nhân của tài xế (được lọc bỏ để bảo mật thông tin).

### 2.3 Organizational Boundary (Ranh giới tổ chức)

* **Mô hình kiểm kê khí nhà kính:** Áp dụng phương pháp kiểm soát vận hành trực tiếp (Direct Operational Control) theo hướng dẫn của GHG Protocol và ISO 14064-1.
* **Ranh giới báo cáo trách nhiệm phát thải:**
  * Toàn bộ lượng điện năng tiêu thụ và phát thải trực tiếp (Scope 1) từ hạm đội xe điện và máy phát RMFC sinh học thuộc quyền sở hữu của LeTRON.
  * Lượng phát thải gián tiếp (Scope 2) từ điện lưới quốc gia nhập vào trạm sạc thuộc quyền kiểm soát vận hành trực tiếp của LeTRON.
  * Dữ liệu sau khi thẩm định được xuất dưới dạng chứng thư Le-GCP để cung cấp cho đối tác FDI, cho phép họ sử dụng hợp pháp làm dữ liệu giảm phát thải Scope 3 (dịch vụ vận tải đầu vào/đầu ra) của doanh nghiệp họ mà không bị tính trùng lặp (double counting).

## 3. Stakeholder Definition

### 3.1 Internal Stakeholders (Nội bộ LeTRON)

* **LeTRON Holding (Board of Directors / Ban quản trị):** Chỉ đạo chiến lược, phê duyệt kế hoạch phân bổ tài chính cho dự án Logistics Xanh.
* **LeSM (Operations Team / Khối Vận hành):** Trực tiếp quản lý lịch trình chạy hạm đội xe tải, phân bổ hàng hóa cho các FDI và quản lý trạm sạc.
* **LeDB (Engineering & Tech Team / Khối Công nghệ & Kỹ thuật):** Vận hành hệ thống LeOS, giám sát viễn trắc Le-NodeMobile/Hub, bảo trì phần cứng và bảo mật Blockchain LeDB.
* **LeSE (Energy Team / Khối Năng lượng):** Giám sát hiệu suất nguồn phát sạch (Solar, Wind, RMFC) và hệ thống lưu trữ pin VFB.

### 3.2 External Stakeholders (Bên ngoài)

* **FDI Customers (Khách hàng FDI sản xuất):** Các doanh nghiệp thụ hưởng dịch vụ vận tải xanh, nhận chứng thư Le-GCP để chứng minh giảm phát thải Scope 3 của họ.
* **Independent Auditors (Kiểm toán viên độc lập):** Đơn vị truy cập Auditor Access Gateway để thẩm duyệt phương pháp luận đo lường tự động và kiểm toán dữ liệu độc lập.

## 4. Asset Register (Danh mục Tài sản dự án)

Để quản lý dòng chảy dữ liệu và năng lượng, toàn bộ tài sản vật lý, nguồn phát, hệ thống pin lưu trữ và thiết bị đo lường được theo dõi tập trung trong bảng danh mục tài sản dưới đây:

| Nhóm tài sản          | Tên / Định danh tài sản  | Dòng xe / Model thiết bị   | Thông số / Công suất thiết kế                         | Thiết bị đo lường & IoT tích hợp                      | Vai trò vận hành                           |
| :----------------------- | :---------------------------- | :---------------------------- | :---------------------------------------------------------- | :----------------------------------------------------------- | :-------------------------------------------- |
| **Phương tiện** | Le-Truck-01 (Xe tải nặng)   | [Điền dòng xe]             | [Điền dung lượng] kWh                                   | Le-NodeMobile, Cảm biến tải trục                         | Vận chuyển nguyên liệu nặng              |
| **Phương tiện** | Le-Truck-02 (Xe tải nặng)   | [Điền dòng xe]             | [Điền dung lượng] kWh                                   | Le-NodeMobile, Cảm biến tải trục                         | Vận chuyển nguyên liệu nặng              |
| **Phương tiện** | Le-Truck-03 (Xe tải nặng)   | [Điền dòng xe]             | [Điền dung lượng] kWh                                   | Le-NodeMobile, Cảm biến tải trục                         | Vận chuyển nguyên liệu nặng              |
| **Phương tiện** | Le-Truck-04 (Xe tải trung)   | [Điền dòng xe]             | [Điền dung lượng] kWh                                   | Le-NodeMobile, Cảm biến tải trục                         | Vận chuyển thành phẩm FDI                 |
| **Phương tiện** | Le-Truck-05 (Xe tải trung)   | [Điền dòng xe]             | [Điền dung lượng] kWh                                   | Le-NodeMobile, Cảm biến tải trục                         | Vận chuyển thành phẩm FDI                 |
| **Trạm sạc**     | Hạ tầng sạc nhanh Megawatt | Súng sạc Megawatt (MCS)     | [Điền số lượng] x [Điền công suất] kW (OCPP 2.0.1) | Công tơ thông minh 3 pha (Class 0.5S), Gateway Le-NodeHub | Sạc nhanh công suất lớn cho hạm đội xe |
| **Nguồn phát**   | Hệ thống Điện mặt trời  | Solar áp mái & bãi đỗ xe | [Điền công suất] MWp                                    | Cảm biến bức xạ (Pyranometer), SCADA kết nối LeOS      | Nguồn phát sạch tự dùng chính           |
| **Nguồn phát**   | Hệ thống Điện gió        | Tua-bin gió trục đứng     | [Điền công suất] kW                                     | Cảm biến tốc độ gió, SCADA kết nối LeOS              | Nguồn phát sạch bổ trợ                   |
| **Nguồn phát**   | Pin nhiên liệu RMFC         | RMFC chạy Bio-Methanol       | [Điền số lượng] x [Điền công suất] kW              | SCADA giám sát nhiên liệu kết nối LeOS                 | Nguồn phát sạch bù tải nền              |
| **Pin lưu trữ**  | Bể pin dòng chảy Vanadium  | Vanadium Flow (VFB)           | [Điền dung lượng] MWh                                   | Hệ thống quản lý pin BMS & SCADA                         | Lưu trữ năng lượng sạch dài hạn       |
| **Pin lưu trữ**  | Hệ thống pin Lithium BESS   | Lithium-ion BESS              | [Điền dung lượng] MWh                                   | Hệ thống quản lý pin BMS & SCADA                         | Điều hòa công suất đỉnh trạm sạc     |

## 5. System Architecture

### 5.1 Energy Architecture

* **Nguồn phát (Generation):** Hệ thống Solar áp mái hoạt động ban ngày, tua-bin gió hoạt động liên tục khi có sức gió, RMFC sinh học tự động kích hoạt bù tải nền khi hệ thống sạc đạt đỉnh hoặc không đủ nguồn tái tạo thiên nhiên.
* **Lưu trữ (Storage):** Pin dòng chảy Vanadium VFB sạc trực tiếp từ nguồn phát dư thừa ban ngày. Lithium-ion BESS tham gia điều hòa tần số và phóng điện tốc độ cao hỗ trợ sạc Megawatt.
* **Tiêu thụ (Consumption):** Hệ thống súng sạc Megawatt truyền tải năng lượng trực tiếp vào hạm đội xe điện 5 chiếc thông qua sự kiểm soát công suất của LeOS để tránh sụt áp lưới điện.

### 5.2 Digital Architecture (Kiến trúc Dữ liệu số)

Hệ thống sử dụng luồng xử lý và truyền dữ liệu thời gian thực được bảo mật qua ba tầng để đảm bảo tính minh bạch:

<img src="./ref/image/digital_architecture_diagram.png" alt="Sơ đồ Kiến trúc Dữ liệu số (Digital Architecture Diagram)" height="360px" style="display:block; margin:15px auto;" />

* **Telemetry (Viễn trắc):** Dữ liệu từ xe và súng sạc được đẩy về gateway biên theo tần suất 5 giây/lần.
* **Ký số bảo mật:** Mọi gói tin trước khi gửi lên đám mây đều được ký số bằng khóa riêng (Private Key) được lưu trữ an toàn trong chip bảo mật phần cứng tại thiết bị biên.
* **Lưu trữ bất biến:** Các chỉ số năng lượng và phát thải được tổng hợp và đúc mã băm (Hash) lên Blockchain của LeDB nhằm ngăn chặn mọi hành vi chỉnh sửa số liệu hồi tố.

## 6. Energy Ledger Design

### 6.1 Energy Source Classification & Coding

Hệ thống năng lượng được phân loại nguồn rõ ràng để theo dõi dòng chảy năng lượng xanh:

* **Solar (Mã nguồn: ENG-PV):** Điện mặt trời tự sản tự tiêu.
* **Wind (Mã nguồn: ENG-WD):** Điện gió tự sản tự tiêu.
* **Bio-Methanol (Mã nguồn: ENG-BM):** Điện từ pin nhiên liệu RMFC sinh học.
* **Grid (Mã nguồn: ENG-GR):** Điện lưới quốc gia bù tải.

### 6.2 Energy Balance & Flow Model

Quy trình cân bằng năng lượng thời gian thực thực thi trên hệ điều hành LeOS tại Hub dịch vụ tuân thủ nguyên tắc:

Tổng năng lượng cung cấp đầu vào:

$$
E_{Supply}(t) = E_{Solar}(t) + E_{Wind}(t) + E_{RMFC}(t) + E_{Grid}(t)
$$

Sự thay đổi dung lượng pin lưu trữ tại thời điểm *t*:

$$
SOC_{Storage}(t) = SOC_{Storage}(t-1) + \eta_{in} \cdot E_{Surplus}(t) - \frac{E_{Deficit}(t)}{\eta_{out}}
$$

Cân bằng tại đầu súng sạc:

$$
\sum E_{Charger\_Output} \cdot \eta_{charge} = \sum \Delta P_{kWh} + L_{Transmission}
$$

### 6.3 Energy Balance Reconciliation Example (Ví dụ đối soát cân bằng năng lượng thực tế)

Để tăng tính minh bạch và xác thực tính nguyên vẹn của dòng điện sạc, LeOS thực thi quy trình đối soát tự động hàng ngày. Dưới đây là ví dụ minh họa dữ liệu đối soát trong 1 ngày vận hành tại Hub dịch vụ:

* **Tổng năng lượng phát ra đầu vào trong ngày:**
  * Điện mặt trời tự phát (ENG-PV): **2,000 kWh**
  * Điện gió tự phát (ENG-WD): **800 kWh**
  * Điện RMFC Bio-Methanol (ENG-BM): **1,200 kWh**
  * Điện lưới quốc gia bù tải (ENG-GR): **1,000 kWh**
  * *Tổng năng lượng cung cấp đầu vào:* **5,000 kWh**
* **Chuyển dịch năng lượng qua bể lưu trữ (Pin VFB & BESS):**
  * Điện năng nạp vào pin: **1,500 kWh** (Với hiệu suất nạp 85%, năng lượng tích lũy thực tế trong pin là **1,275 kWh**).
  * Điện năng xả từ pin cấp cho súng sạc: **1,275 kWh** (Với hiệu suất xả 90%, năng lượng cấp ra thực tế là **1,147.5 kWh**).
* **Điện năng tiêu thụ sạc thực tế:**
  * Tổng điện năng sạc đo được tại công tơ súng sạc đầu ra (Class 0.5S): **4,500 kWh**
* **Hao hụt truyền tải vật lý nội bộ Hub (Losses):**
  * Hao hụt truyền dẫn: **147.5 kWh** (Nằm trong sai số hiệu suất sạc cho phép $\approx 94\%$).

**Quy tắc đối soát khớp sổ cái năng lượng (Energy Ledger Reconciliation Rule):**

$$
\text{Năng lượng phát ra} + \text{Năng lượng xả} = \text{Năng lượng sạc xe} + \text{Năng lượng nạp pin} + \text{Hao hụt}
$$

$$
5,000 \text{ kWh (Phát)} + 1,147.5 \text{ kWh (Xả)} = 4,500 \text{ kWh (Sạc)} + 1,500 \text{ kWh (Nạp)} + 147.5 \text{ kWh (Hao hụt)}
$$

*Kết quả đối soát:* Cân bằng hai vế khớp **100% (6,147.5 kWh = 6,147.5 kWh)**. Giao dịch hợp lệ và hệ thống LeOS tự động ký số đóng gói dữ liệu nạp lên Blockchain LeDB.

## 7. Carbon Accounting & Baseline Methodology

### 7.1 Baseline vs. Project Comparison Table (Bảng đối chiếu Trước và Sau dự án)

Dưới đây là bảng đối chiếu chi tiết giữa kịch bản vận tải truyền thống (Before) và hệ sinh thái Logistics xanh thông minh Le-GCP (After) để kiểm toán viên dễ dàng theo dõi sự chuyển dịch công nghệ:

| Khía cạnh so sánh                            | Kịch bản Trước dự án (Before - Baseline)                                                                                   | Kịch bản Sau dự án (After - Project Le-GCP)                                                                                                                               |
| :---------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nguồn năng lượng**                  | Sử dụng 100% dầu Diesel hóa thạch hoặc sạc xe điện từ nguồn điện lưới thông thường.                            | Sử dụng 100% điện sạch (Green Electrons) từ Solar, Gió tại Hub và máy phát RMFC sử dụng Bio-Methanol hữu cơ.                                                   |
| **Phát thải Scope 1 & Scope 3**         | Phát thải trực tiếp từ đốt dầu Diesel và phát thải gián tiếp từ nguồn lưới điện carbon cao.                   | Triệt tiêu phát thải trực tiếp và giảm thiểu tối đa phát thải gián tiếp tùy theo tỷ lệ sạc điện sạch thực tế.                                         |
| **Hệ thống lưu trữ & điều phối**   | Không có hệ thống lưu trữ hoặc sử dụng ắc quy chì/Li-ion thông thường có tuổi thọ ngắn (3-5 năm).             | Sử dụng hệ thống pin dòng chảy Vanadium (VFB) bền bỉ (>25 năm) kết hợp BESS và được điều phối thông minh qua LeOS.                                         |
| **Thiết bị & Phương pháp đo (MRV)** | Đo lường thủ công dựa trên hóa đơn dầu giấy, công tơ mét cơ học hoặc log sạc ghi tay.                         | Tự động đo lường thời gian thực bằng thiết bị viễn trắc Le-NodeMobile/Hub (trọng lượng xe W_cargo, quãng đường D_km, điện năng tiêu hao Delta_P_kWh). |
| **Tính liêm chính dữ liệu**          | Dữ liệu dễ bị chỉnh sửa thủ công để làm đẹp báo cáo (Greenwashing). Không có cơ chế xác thực nguồn điện. | Giao thức Zero Trust ký số dữ liệu từ chip bảo mật phần cứng biên, lưu trữ bất biến trên Sổ cái Blockchain LeDB.                                            |
| **Quy trình thẩm định**               | Đơn vị kiểm toán phải xuống thực địa kiểm tra hồ sơ chứng từ giấy thủ công, tốn kém nhân sự và chi phí.  | Kiểm toán từ xa qua cổng API**Auditor Access Gateway**, tự động đối soát mã Hash Blockchain để cấp chứng thư tức thời.                                |
| **Mức độ rủi ro kiểm toán**         | **CAUTION** (Cực kỳ cao) - Dễ bị các tổ chức và quỹ đầu tư quốc tế từ chối cấp chứng chỉ carbon.        | **SAFE** (Tiêu chuẩn vàng) - Đảm bảo tính minh bạch tuyệt đối phục vụ cấp chứng chỉ carbon tự động.                                                  |

### 7.2 Phát thải Đường cơ sở của xe dầu tương đương (Baseline Emissions)

Với mỗi chuyến xe chạy bằng dầu diesel, lượng phát thải được tính theo công thức:

$$
GHG_{Baseline, i} = D_i \times FE_{Diesel, i} \times EF_{Diesel}
$$

Trong đó, định mức tiêu hao dầu thực tế $FE_{Diesel, i}$ (lít/km) phụ thuộc vào tải trọng chở hàng của chuyến xe $i$:

$$
FE_{Diesel, i} = FE_{Base} + \alpha \times W_i
$$

Các thông số và con số áp dụng:

* $D_i$ (km): Quãng đường thực tế của chuyến xe $i$ đo bằng GPS từ thiết bị Le-NodeMobile.
* $FE_{Base}$ (lít/km): Tiêu thụ dầu Diesel cơ bản khi xe chạy rỗng. Áp dụng **0.25 lít/km** cho xe đầu kéo CAMC và **0.18 lít/km** cho xe tải trung Farizon.
* $\alpha$: Hệ số tăng tiêu thụ dầu theo tải trọng. Áp dụng **0.005 lít / (km · tấn)**.
* $W_i$ (tấn): Số tấn hàng thực tế chở trên chuyến xe $i$.
* $EF_{Diesel}$: Hệ số phát thải carbon của dầu Diesel. Áp dụng **2.68 kg CO2/lít** (Theo chuẩn IPCC 2006).

#### Ví dụ tính toán mẫu cho Hạm đội Pilot 5 xe chạy trong 1 năm:

* **Tổng quãng đường:** 300,000 km/năm (mỗi xe chạy trung bình 60,000 km/năm).
* **3 xe đầu kéo CAMC dầu** (Chạy 180,000 km/năm, tải trọng hàng trung bình 25 tấn/chuyến):
  * Tiêu hao dầu thực tế: $0.25 + (0.005 \times 25) = 0.375$ lít/km.
  * Tổng dầu tiêu thụ: $180,000 \text{ km} \times 0.375 \text{ lít/km} = 67,500$ lít.
  * Phát thải carbon: $67,500 \text{ lít} \times 2.68 \text{ kg CO2/lít} = 180,900$ kg CO2 (180.90 tấn CO2/năm).
* **2 xe tải trung Farizon dầu** (Chạy 120,000 km/năm, tải trọng hàng trung bình 8 tấn/chuyến):
  * Tiêu hao dầu thực tế: $0.18 + (0.005 \times 8) = 0.220$ lít/km.
  * Tổng dầu tiêu thụ: $120,000 \text{ km} \times 0.220 \text{ lít/km} = 26,400$ lít.
  * Phát thải carbon: $26,400 \text{ lít} \times 2.68 \text{ kg CO2/lít} = 70,752$ kg CO2 (70.75 tấn CO2/năm).
* **Tổng phát thải Đường cơ sở của hạm đội (Baseline GHG):**
  $$
  GHG_{Baseline} = 180.90 + 70.75 = 251.65 \text{ tấn } CO_2\text{/năm}
  $$

### 7.3 Phát thải thực tế của dự án xe điện LeTRON (Project Emissions)

Với mỗi chuyến xe điện sạc hỗn hợp tại Hub, lượng phát thải thực tế được tính theo công thức:

$$
GHG_{Project, i} = E_i \times EF_{Hub}
$$

Trong đó, hệ số phát thải trung bình của trạm sạc tại thời điểm sạc $EF_{Hub}$ (kg CO2/kWh) được tính dựa trên tỷ lệ sạc thực tế của 4 nguồn cấp:

$$
EF_{Hub} = S_{Grid} \times EF_{Grid} + S_{Solar} \times EF_{Solar} + S_{Wind} \times EF_{Wind} + S_{Methanol} \times EF_{Methanol}
$$

Các thông số và con số áp dụng:

* $E_i$ (kWh): Lượng điện năng sạc thực tế cho xe tại Hub đo ở đầu súng sạc.
* $S_{Grid}, S_{Solar}, S_{Wind}, S_{Methanol}$ (%): Tỷ lệ điện năng đóng góp tương ứng của từng nguồn tại trạm sạc.
* $EF_{Grid}$: Hệ số phát thải lưới điện quốc gia Việt Nam. Áp dụng **0.7228 kg CO2/kWh**.
* $EF_{Solar}$ & $EF_{Wind}$: Áp dụng **0.00 kg CO2/kWh**.
* $EF_{Methanol}$: Áp dụng **0.00 kg CO2/kWh** (Bio-Methanol tuần hoàn).

#### Ví dụ tính toán mẫu cho Hạm đội Pilot 5 xe điện chạy trong 1 năm:

* **Điện năng tiêu thụ của 3 xe CAMC điện** (Tiêu thụ định mức 1.30 kWh/km):
  $180,000 \text{ km} \times 1.30 \text{ kWh/km} = 234,000$ kWh.
* **Điện năng tiêu thụ của 2 xe Farizon điện** (Tiêu thụ định mức 0.60 kWh/km):
  $120,000 \text{ km} \times 0.60 \text{ kWh/km} = 72,000$ kWh.
* **Tổng điện năng sạc toàn hạm đội:** $306,000$ kWh/năm.
* **Phát thải thực tế dự án** (với 60% năng lượng sạch tự cấp và 40% điện lưới nhập vào):
  * Lượng điện lưới tiêu thụ (40%): $306,000 \text{ kWh} \times 40\% = 122,400$ kWh.
  * Tổng phát thải thực tế của dự án:
    $$
    GHG_{Project} = 122,400 \text{ kWh} \times 0.7228 \text{ kg CO2/kWh} = 88,470.72 \text{ kg } CO_2 \approx 88.47 \text{ tấn } CO_2\text{/năm}
    $$

### 7.4 Lượng phát thải giảm thiểu ròng (Net Carbon Reduction)

Lượng giảm phát thải khí nhà kính ròng $\Delta GHG_i$ cho chuyến xe $i$:

$$
\Delta GHG_i = GHG_{Baseline, i} - GHG_{Project, i}
$$

#### Ví dụ tính toán mẫu giảm phát thải ròng hàng năm của hạm đội pilot:

* Lượng phát thải giảm thiểu thực tế được công nhận để cấp chứng chỉ carbon:
  $$
  \Delta GHG = GHG_{Baseline} - GHG_{Project} = 251.65 - 88.47 = 163.18 \text{ tấn } CO_2\text{/năm}
  $$
* **Tỷ lệ giảm thiểu:**
  $$
  \text{Tỷ lệ giảm phát thải} = \frac{163.18 \text{ tấn}}{251.65 \text{ tấn}} \times 100\% \approx 64.84\%
  $$

<div class="page-break"></div>

### 7.5 Bảng tổng hợp các chỉ số định mức và hệ số phát thải áp dụng

Dưới đây là bảng tổng hợp các chỉ số nền được sử dụng trong thuật toán tính toán tự động của hệ điều hành LeOS:

| Ký hiệu                   | Tên chỉ số                                      | Nguồn tham chiếu / Bảo chứng pháp lý                | Giá trị áp dụng | Đơn vị           |
| :-------------------------- | :------------------------------------------------- | :-------------------------------------------------------- | :------------------ | :------------------ |
| **EF_Grid**           | Hệ số phát thải của Lưới điện Việt Nam   | Quyết định của Cục Biến đổi khí hậu (Bộ TN&MT) | **0.7228**    | kg CO2 / kWh        |
| **EF_Diesel**         | Hệ số phát thải của dầu Diesel               | Hướng dẫn kiểm kê khí nhà kính IPCC 2006          | **2.68**      | kg CO2 / lít       |
| **EF_Solar**          | Hệ số phát thải của Điện mặt trời         | Mặc định nguồn sạch tự sản tự tiêu               | **0.00**      | kg CO2 / kWh        |
| **EF_Wind**           | Hệ số phát thải của Điện gió               | Mặc định nguồn sạch tự sản tự tiêu               | **0.00**      | kg CO2 / kWh        |
| **EF_Methanol**       | Hệ số phát thải của Điện Methanol sinh học | Đánh giá vòng đời (LCA) của Bio-Methanol           | **0.00**      | kg CO2 / kWh        |
| **FE_Base (CAMC)**    | Tiêu thụ dầu cơ bản xe đầu kéo rỗng       | Thông số đăng kiểm của nhà sản xuất              | **0.25**      | lít / km           |
| **FE_Base (Farizon)** | Tiêu thụ dầu cơ bản xe tải trung rỗng       | Quy chuẩn thống kê vận tải đường bộ Việt Nam    | **0.18**      | lít / km           |
| **Alpha_Load**        | Hệ số tăng tiêu thụ dầu theo tải trọng     | Quy chuẩn thống kê vận tải đường bộ Việt Nam    | **0.005**     | lít / (km · tấn) |
| **Eff_Charge**        | Hiệu suất truyền dẫn sạc vật lý tại Hub    | Thiết kế kỹ thuật của trạm sạc nhanh Megawatt      | **94.00**     | %                   |

## 8. Monitoring, Reporting & Verification (MRV) Framework

### 8.1 Quy trình thu thập dữ liệu (Monitoring Process)

* **Tần suất thu thập:** Thiết bị Le-NodeMobile và Le-NodeHub thu thập dữ liệu tự động mỗi 5 giây.
* **Tham số theo dõi:** GPS (kinh độ, vĩ độ), Pin SoC (%), Dòng điện sạc (A), Điện áp sạc (V), Cảm biến tải trọng trục (kg).
* **Đóng gói dữ liệu:** Dữ liệu thô được lưu trữ tạm thời tại bộ nhớ đệm thiết bị biên và tự động đẩy lên Carbon/Energy Ledger qua mạng di động bảo mật 4G/5G khi có kết nối ổn định.

### 8.2 Khung báo cáo và Bằng chứng (Reporting & Evidence Register)

* **Báo cáo chuyến hàng:** Xuất tự động chứng thư giảm phát thải Le-GCP ngay khi xe hoàn thành lộ trình giao hàng được xác nhận bằng GPS hàng rào địa lý (Geofencing).
* **Nhật ký bằng chứng (Evidence Dossier):** Mỗi chuyến xe được liên kết với một hồ sơ bằng chứng số bao gồm:
  * Mã định danh thiết bị biên (Device ID).
  * Mã băm dữ liệu gốc trước khi gửi (Raw Data Hash).
  * Mã băm giao dịch trên Blockchain LeDB (TxID).
  * Biên bản sạc điện sạch lưu trữ trên Energy Ledger.

### 8.3 Quy trình kiểm toán (Verification Process)

* Đơn vị kiểm toán độc lập truy cập thông qua tài khoản Auditor Access Gateway độc lập.
* Hệ thống cung cấp tính năng tự động đối chiếu chéo (Cross-check): Kiểm toán viên chọn một chuyến xe bất kỳ, hệ thống sẽ thực hiện truy xuất chữ ký số mật mã của chip biên và đối soát mã Hash Blockchain để xác thực dữ liệu hành trình không bị chỉnh sửa.

<div class="page-break"></div>

## 9. Data Quality & Governance Framework

### 9.1 Kiểm soát chất lượng dữ liệu (Data Quality Rules)

* **Tính đầy đủ (Completeness):** Chuyến xe chỉ được xem là hợp lệ để cấp chứng thư Le-GCP nếu dữ liệu viễn trắc hành trình ghi nhận liên tục tối thiểu đạt 95% thời gian di chuyển.
* **Tính chính xác (Accuracy):** Sai lệch đối soát kép giữa lượng điện năng xả ra từ pin lưu trữ Hub sạc và lượng điện năng nạp vào hạm đội xe qua cổng CAN Bus của xe phải dưới 2%.

### 9.2 Quy trình xử lý lỗi cảm biến và Mất dữ liệu (Fallback Procedure)

* **Mất kết nối viễn thông (Network Outage):** Khi thiết bị Le-NodeMobile mất kết nối 4G/5G, dữ liệu viễn trắc sẽ được lưu giữ cục bộ trên bộ nhớ Flash mã hóa của chip biên. Khi có kết nối trở lại, thiết bị tự động đồng bộ bù dữ liệu kèm chữ ký số và timestamp gốc.
* **Lỗi cảm biến tải trọng xe (Sensor Failure):** Trong trường hợp cảm biến trục xe bị hỏng hoặc báo dữ liệu bất thường (âm hoặc vượt quá tải trọng định mức xe), hệ thống sẽ tự động kích hoạt kịch bản phòng ngừa (Fallback Scenario):
  * Áp dụng trọng lượng hàng hóa danh định dựa trên Phiếu cân xe đầu vào tại kho hàng hoặc Vận đơn điện tử (E-Waybill) đã ký số để thay thế cho biến số $W_i$.

## 10. Le-GCP & Auditor Gateway Implementation

### 10.1 Cấp Chứng thư Le-GCP (Passport Generation Logic)

* **Trigger:** Khi xe vượt qua hàng rào địa lý (Geofence) của điểm giao hàng và tắt máy, hệ thống LeOS sẽ thực thi kiểm tra tính toàn vẹn dữ liệu của chuyến đi đó.
* **Đúc chứng thư:** LeOS kích hoạt Passport Engine tổng hợp dữ liệu, tạo một tệp tin JSON chứa chứng thư và đúc (mint) mã hash giao dịch lên Blockchain LeDB.
* **Bàn giao:** Chứng thư được mã hóa gửi trực tiếp qua cổng API đến hệ thống ERP của đối tác FDI.

### 10.2 Thiết kế cổng kiểm toán Auditor Gateway

* **Giao diện Web độc lập:** Cung cấp cho các chuyên gia kiểm toán bên thứ ba giao diện Web bảo mật mã hóa xác thực 2 lớp (2FA).
* **Chức năng truy xuất:** Cho phép tìm kiếm chứng thư theo Mã chuyến hàng (Shipment ID) hoặc biển kiểm soát xe, xem chi tiết nguồn gốc năng lượng sạc tại thời điểm đó và kiểm tra trạng thái toàn vẹn của dữ liệu Blockchain.

### 10.3 Lộ trình triển khai (Roadmap)

* **Giai đoạn 1 (Tháng 8 - Tháng 10/2026):** Chạy thử nghiệm pilot hạm đội 5 xe chạy thực địa. Hoàn thiện tích hợp LeOS/LeDB và thẩm duyệt thuật toán nền với đơn vị kiểm toán.
* **Giai đoạn 2 (Quý 1/2027):** Mở rộng mạng lưới lên 20 xe điện nặng, nâng cấp công suất Hub sạc và thương mại hóa toàn diện dịch vụ cấp chứng chỉ xanh.
