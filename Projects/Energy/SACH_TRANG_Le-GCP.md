

**1.  ****TUYÊN NGÔN CÔNG NGH****Ệ**
**2.  ****KI****Ế****N TRÚC THU TH****Ậ****P D****Ữ**** LI****Ệ****U ****BIÊN  (****Edge Telemetry Architecture)**
2.1  Node Hub Dịch vụ (Le-NodeHub)
2.2  Node Động lực học (Le-NodeMobile)
**3.  ****GIAO TH****Ứ****C MÃ HÓA ZERO ****TRUST  (****Zero Trust Encryption Protocol)**
3.1  Quy trình Mã hóa Viễn trắc (Telemetry Cryptography)
3.2  Offline Resilience Protocol
**4.  ****QUY TRÌNH ĐÚC CH****Ứ****NG THƯ S****Ố**** TRÊN LÕI ****LeDB****  (****Blockchain Minting)**
4.1  Quá trình Đúc (Minting Workflow)
4.2  Chi phí lưu trữ và xác thực blockchain
**5.  ****BLOCKCHAIN PLATFORM DECISION  **
5.1  Nền tảng lựa chọn: Hyperledger Besu
5.2  Thông số kỹ thuật vận hành
5.3  Cam kết Data Portability
**6.  ****ENERGY ATTRIBUTION CHAIN  **
6.1  Chuỗi quy chiếu 5 lớp (5-Layer Attribution Chain)
6.2  I-REC Certificate Management
6.3  Sơ đồ Kiến trúc Tổng thể Energy Attribution
**7.  ****C****Ổ****NG GIAO TI****Ế****P KI****Ể****M TOÁN & TÍCH H****Ợ****P ERP**
**8.  ****B****Ả****O M****Ậ****T & X****Ử**** LÝ TRANH CH****Ấ****P**
**9.  ****MÔ HÌN****H CHI PHÍ VÀ TÍNH KINH T****Ế**
**10.  ****PH****Ụ**** L****Ụ****C**
**11.  ****K****Ế****T LU****Ậ****N**



Trong kỷ nguyên của Cơ chế Điều chỉnh Biên giới Carbon (**CBAM**) và Quy chế SFDR (Article 9), việc tuyên bố "Phát thải bằng 0" (Net-Zero) bằng các phép tính ước lượng trên giấy tờ đã trở nên vô giá trị. Tính minh bạch của dữ liệu chuỗi cung ứng logistics (Scope 3) giờ đây quyết định sự sinh tồn của các rào cản thương mại xuyên lục địa.
**LeTRON**** Green Cargo Passport (Le-GCP)** ra đời để định nghĩa lại sự tin cậy. Le-GCP không phải là một dịch vụ vận tải — đây là một **Giao ****th****ứ****c**** ****D****ữ**** ****li****ệ****u**** ****Khí**** ****h****ậ****u**** (Climate Data Protocol)**. Bằng việc kết hợp hạm đội xe điện hạng nặng, hạ tầng sạc vi lưới tái tạo và kiến trúc phần mềm bất biến, chúng tôi biến mỗi kilômét vận tải thành một khối tài sản Carbon số hóa, được xác thực tuyệt đối từ cấp độ phần cứng.


Dữ liệu của Le-GCP được hình thành ngay tại thời điểm vật lý phát sinh dòng điện và chuyển động, thông qua 2 điểm chạm biên (Edge Nodes):


Hệ thống SCADA tại các Siêu Hub Vàng Danh, Uông Bí, Bắc Ninh, Thái Nguyên liên tục xuất dữ liệu nguồn gốc điện năng. Mọi dòng điện nạp vào hạm đội thông qua Trạm sạc Megawatt đều được gắn mã định danh chứng minh xuất xứ 100% tái tạo. Dữ liệu bao gồm:
**▸****  **Công suất sạc (kW) tại mỗi phiên
**▸****  **Tổng năng lượng truyền (kWh)
**▸****  **Mã định danh trạm sạc
**▸****  **Dấu thời gian bắt đầu / kết thúc
**▸****  **Chứng chỉ xuất xứ năng lượng (I-REC — xem chi tiết Mục 6)


Mỗi xe đầu kéo trong hạm đội được cấy ghép một hộp đen viễn trắc **Le-****NodeMobile** chạy hệ điều hành **LeOS**. Le-NodeMobile giao tiếp trực tiếp với hệ thống CAN-Bus của xe (CAMC BEV hoặc Bio-Methanol) để trích xuất các thông số thực thời:
**▸****  **Tọa độ GPS (độ chính xác ± 3m)
**▸****  **Mức tiêu hao pin hoặc nhiên liệu (kWh hoặc lít Bio-Methanol)
**▸****  **Trọng tải hàng hóa thực tế (từ cảm biến khí nén treo sau)
**▸****  **Trạng thái thùng xe (đang mở/đóng, nhiệt độ hàng nếu có yêu cầu)
**▸****  **Vận tốc, gia tốc, quãng đường tích lũy


Hệ điều hành LeOS của LeTRON hoạt động dựa trên nguyên lý an ninh lõi: ***"******Không****** tin ******tư******ở******ng****** ******b******ấ******t****** ******k******ỳ****** ai, ******k******ể****** ******c******ả****** ******qu******ả******n****** ******tr******ị****** ******viên****** ******h******ệ****** ******th******ố******ng******" (Zero Trust)***. Le-GCP áp dụng cấu trúc mã hóa đa lớp ngay tại thiết bị phần cứng.



**  ****Bư****ớ****c**** 1 — ****Ch****ữ**** ****ký**** ****Ph****ầ****n**** ****c****ứ****ng**** (HSM)  **
Mỗi thiết bị Le-NodeMobile chứa một vi mạch bảo mật độc lập với khóa riêng tư (Private Key) được ghi chết (Hard-coded) từ nhà máy. Khóa này được chứng nhận bởi **Infineon OPTIGA™ TPM** (nhà cung cấp bên thứ ba). LeDB lưu trữ khóa công khai tương ứng để xác minh chữ ký.

**  ****Bư****ớ****c**** 2 — ****Băm**** ****D****ữ**** ****li****ệ****u**** ****Đ****ộ****ng**** (Dynamic Hashing)  **
Mỗi chu kỳ 5 giây, gói dữ liệu vật lý (tọa độ + điện năng + tải trọng + timestamp) được kết hợp với một nonce (số ngẫu nhiên) để tạo ra một chuỗi băm duy nhất thông qua thuật toán SHA-256:



**  ****Bư****ớ****c**** 3 — ****Niêm**** ****phong**** ****D****ữ**** ****li****ệ****u**** (Data Sealing)  **
Gói dữ liệu + chữ ký số được truyền qua giao thức mạng **TLS 1.3** tới máy chủ biên (Le-NodeHub) đặt tại Siêu Hub. Bất kỳ nỗ lực can thiệp vật lý nào vào hộp Le-NodeMobile hoặc ngắt kết nối mạng bất hợp pháp đều khiến hệ thống tự động đánh dấu vô hiệu hóa toàn bộ chuyến đi đó khỏi quy trình đúc tín chỉ carbon.

**  ****Bư****ớ****c**** 4 ****— ****Xác**** ****minh**** ****chéo**** ****đa**** ****bên**** (Multi-party Co-signing)  **
Đối với các chuyến hàng yêu cầu kiểm toán cấp độ CBAM+, Le-GCP hỗ trợ cơ chế **đ****ồ****ng**** ****ký**** (co-signing)** giữa LeDB và **TÜV ****Rheinland**. Chỉ những gói có đủ hai chữ ký mới được chấp nhận lên blockchain.


Hệ điều hành LeOS triển khai cơ chế **Store-and-Forward Buffering** để đảm bảo tính liên tục của dữ liệu khi mất kết nối:

**  Buffer ****n****ộ****i**** ****b****ộ****  **
Le-NodeMobile được trang bị bộ nhớ flash cục bộ **32 GB** — đủ lưu trữ tối thiểu **72 ****gi****ờ** dữ liệu viễn trắc liên tục (tần suất 5 giây/lần). Mỗi gói dữ liệu được ký HSM và đóng hash đầy đủ ngay tại thời điểm thu thập — timestamp vật lý được bảo toàn bất kể trạng thái kết nối.

**  ****Cơ**** ****ch****ế**** ****đ****ồ****ng**** ****b****ộ**** ****khi**** ****ph****ụ****c**** ****h****ồ****i**** ****k****ế****t**** ****n****ố****i****  **
**▸****  **Gửi toàn bộ gói dữ liệu đã buffer theo thứ tự timestamp lên Le-NodeHub
**▸****  **Xác minh tính liên tục của chuỗi hash (khoảng trống timestamp > 10 giây → cảnh báo)
**▸****  **Khoảng trống bất thường → chuyến đi bị gắn cờ vàng (yellow-flag) → xem xét thủ công
**▸****  **Dữ liệu đồng bộ thành công mới được đưa vào quy trình đúc GCP

**  ****B****ằ****ng**** ****ch****ứ****ng**** ****toàn**** ****v****ẹ****n**** ****d****ữ**** ****li****ệ****u**** offline  **
Mỗi gói buffer cục bộ chứa **Chain-of-Custody Hash**: mỗi hash mới = SHA-256 (Payload_mới + Hash_trước) — tạo thành chuỗi Merkle-like bất biến. Bất kỳ nỗ lực xóa hoặc sửa đổi dữ liệu buffer đều phá vỡ chuỗi hash, được phát hiện ngay khi đồng bộ.


**LeTRON**** DIGITAL BRAIN (****LeDB**) là Bộ não trung ương và sổ cái blockchain độc quyền của Tập đoàn. LeDB đóng vai trò là tổ chức phát hành và lưu trữ các chứng thư Le-GCP thông qua cơ chế Đo lường, Báo cáo và Thẩm định tự động (Automated MRV).



**  ****Bư****ớ****c**** 1 — ****Ti****ế****p**** ****nh****ậ****n**** ****và**** ****Đ****ố****i**** ****soát**** ****Kép**** (Dual-Verification)  **
LeDB nhận dữ liệu được mã hóa từ xe tải (Le-NodeMobile) và trạm sạc (Le-NodeHub). Smart Contracts tự động kích hoạt thuật toán đối soát:


Nếu sai số vượt ngưỡng, chuyến đi bị gắn cờ đỏ (red-flagged) và chuyển sang kiểm tra thủ công bởi bộ phận vận hành của LeDB.

**  ****Bư****ớ****c**** 2 — ****Tính**** ****toán**** ****Gi****ả****m**** ****tr****ừ**** Carbon (Carbon Abatement Calculation)  **
Hệ thống áp dụng phương pháp luận **ISO 14064-2** để tính toán CO₂ tương đương (tCO₂e) được cắt giảm so với baseline Diesel cùng tải trọng và lộ trình:


Trong đó **grid_factor_renewable**** = 0** do nguồn điện 100% tái tạo từ LeSE (xem chi tiết Mục 6 — Energy Attribution Chain).

**  ****Bư****ớ****c**** 3 — ****Ghi**** ****s****ổ**** ****S****ổ**** ****cái**** (Ledger**** Commitment)  **
Kết quả tính toán được đóng gói thành một Block và gắn vào blockchain nội bộ LeDB. Mỗi block chứa tối đa 10.000 giao dịch, được xác thực bởi cơ chế đồng thuận **Proof-of-Authority (****PoA****)** với validators: LeDB, TÜV Rheinland và đối tác kiểm toán được ủy quyền. Tại thời điểm này, dữ liệu trở thành **b****ấ****t**** ****bi****ế****n**** (Immutable)**.

**  ****Bư****ớ****c**** 4 — ****Phát**** ****hành**** ****Ch****ứ****ng**** ****thư**** (GCP Issuance)  **
Hợp đồng Thông minh tự động sinh ra một Chứng thư số **Le-GCP** (NFT/Token ERC-1155) có chứa đầy đủ metadata của chuyến hàng:
**▸****  **ID chuyến hàng duy nhất (GCP-ID)
**▸****  **Ngày phát hành, ngày hết hạn (mặc định 30 ngày sau khi hoàn thành vận tải)
**▸****  **Thông tin shipper, consignee, tuyến đường
**▸****  **Tổng tCO₂e đã được bù trừ
**▸****  **Liên kết đến hash gốc trên blockchain
**▸****  **Mã QR code: https://verify.letrongroup.com/gcp?id=...





Với dự kiến **1 ****tri****ệ****u**** ****chuy****ế****n**** ****hàng****/****năm** vào năm 2028, tổng chi phí blockchain hàng năm ước tính **dư****ớ****i**** 50.000 USD** — hoàn toàn nằm trong ngân sách vận hành.




LeTRON lựa chọn **Hyperledger ****Besu** — triển khai Ethereum Enterprise do Linux Foundation phát triển — làm nền tảng blockchain cho toàn bộ hệ sinh thái LeDB. Đây là lựa chọn được sử dụng phổ biến nhất trong các dự án blockchain năng lượng và carbon toàn cầu, bao gồm **Energy Web Chain** và **BNP Paribas Climate Data Platform**.







**▸****  **Toàn bộ dữ liệu GCP export được ra JSON chuẩn qua JSON-RPC API public tại bất kỳ thời điểm nào, kể cả khi LeTRON không còn hoạt động
**▸****  **Mỗi đối tác FDI có quyền yêu cầu bản sao đầy đủ GCP theo định dạng machine-readable (CSV, JSON, XML)
**▸****  **LeDB cam kết duy trì ≥ 2 validator node độc lập (ngoài LeTRON) để đảm bảo mạng tiếp tục hoạt động
**▸****  **Smart Contract code được audit bởi bên thứ ba độc lập và mã nguồn công bố công khai (open-source)


Toàn bộ tuyên bố "Net-Zero" của Le-GCP đặt nền tảng trên một giả định quan trọng: **đi****ệ****n**** ****năng**** ****n****ạ****p**** ****vào**** ****đ****ộ****i**** ****xe**** ****LeSM**** ****là**** 100% ****tái**** ****t****ạ****o**** — ****grid_factor_renewable**** = 0**. Phần này định nghĩa chính xác cách LeTRON chứng minh điều đó theo chuẩn kiểm toán quốc tế.





LeTRON đăng ký tham gia hệ thống **I-REC Standard** (International Renewable Energy Certificate) — chuẩn chứng nhận năng lượng tái tạo được công nhận tại 50+ quốc gia, được Liên Hợp Quốc khuyến nghị cho báo cáo Scope 2/Scope 3.

**  ****Quy**** ****trình**** ****qu****ả****n**** ****lý**** I-REC ****t****ạ****i**** ****LeTRON****  **
**▸****  **LeSE đăng ký các nhà máy Solar và Tuabin gió tại Siêu Hub với tư cách Producer trên nền tảng I-REC Standard
**▸****  **Mỗi tháng, APX Group (hoặc đơn vị registry ủy quyền tại Việt Nam) cấp I-REC cho sản lượng điện tái tạo thực tế
**▸****  **LeDB tự động retire (vô hiệu hóa) I-REC tương ứng với lượng điện đã nạp cho đội xe LeSM — ngăn double-counting
**▸****  **Bằng chứng retire được lưu on-chain, xác minh công khai qua I-REC public registry







Sức mạnh pháp lý của Le-GCP nằm ở khả năng đối thoại tự động với các tổ chức kiểm toán quốc tế và hệ thống của khách hàng FDI.


LeDB cung cấp một cổng API chỉ đọc (Read-only API) cấp quyền truy cập thời gian thực cho các chuyên gia kiểm toán độc lập:



Chứng thư Le-GCP được đẩy tự động qua API (Webhook / gọi trực tiếp) vào các hệ thống **SAP, Oracle, Microsoft Dynamics** của Samsung, Foxconn, LG ngay khi xe tải hoàn thành việc dỡ hàng. Điều này cho phép:
**▸****  **Tự động cập nhật báo cáo Scope 3 theo tháng/quý
**▸****  **Kết xuất báo cáo CBAM sẵn sàng nộp cho cơ quan hải quan EU
**▸****  **Đối soát hóa đơn vận tải và chứng chỉ carbon trong cùng một luồng




Toàn bộ hệ thống từ Le-NodeMobile, LeOS, Le-NodeHub đến LeDB blockchain trải qua penetration testing hàng năm bởi tổ chức bảo mật độc lập (tối thiểu ISO 27001). Lỗ hổng phát hiện phải được vá trong vòng 30 ngày; mọi chuyến hàng bị ảnh hưởng sẽ bị gắn cờ và kiểm tra thủ công.










**▸****  **Tránh thuế CBAM: Mỗi tấn CO₂ chứng nhận giảm tiết kiệm 65–110 EUR/năm. Lô hàng 20 tấn (~15 tCO₂e logistics) tiết kiệm 975–1.650 EUR
**▸****  **Tăng khả năng cạnh tranh: Đối tác châu Âu sẵn sàng trả cao hơn cho sản phẩm có chứng chỉ chuỗi cung ứng Net-Zero với I-REC attribution đầy đủ
**▸****  **Tự động hóa báo cáo: Tiết kiệm hàng trăm giờ nhân công/năm cho thu thập và báo cáo dữ liệu phát thải




**Le-****NodeMobile**** (****xe**** ****t****ả****i****)****  →****  Le-****NodeHub** (máy chủ biên tại Siêu Hub)  →  **LeDB**** Blockchain** (validator: LeTRON, TÜV Rheinland)  →  **Auditor Gateway** (TÜV) và **Client ERP Integration** (SAP, Oracle, Microsoft Dynamics). Luồng dữ liệu hai chiều qua mạng 4G/5G bảo mật và REST API.






**Payload + timestamp + nonce:**

**SHA-256 hash:**

**Blockchain transaction ID:**



Khi quét mã QR (**https://verify.letrongroup.com/gcp?id=GCP-VN-2406-000123**), người dùng thấy: thông tin chuyến hàng, tổng tCO₂e bù trừ, danh sách I-REC IDs, trạng thái "Verified by LeDB & TÜV Rheinland", và liên kết blockchain explorer.
*Domain verify.letrongroup.com **d**ự** **ki**ế**n** live Q3/2026.*


**LeTRON**** Green Cargo Passport (Le-GCP) ****phiên**** ****b****ả****n**** 1.0** là sự hội tụ tuyệt đối giữa phần cứng công nghiệp hạng nặng, mật mã học hiện đại và các chuẩn mực kiểm toán quốc tế. Bằng việc chuyển giao quyền lực xác minh từ con người sang giao thức Zero Trust và sổ cái bất biến LeDB, LeTRON GROUP không chỉ kiến tạo một giải pháp vận tải Net-Zero — mà đang thiết lập một **tiêu**** ****chu****ẩ****n**** ****d****ữ**** ****li****ệ****u**** ****toàn**** ****c****ầ****u**** ****m****ớ****i**** ****cho**** ****n****ề****n**** ****kinh**** ****t****ế**** ****tu****ầ****n**** ****hoàn**.




### Bảng trích xuất 1


| WHITE PAPER Series A  ·  Investor Edition  ·  1.0 | WHITE PAPER Series A  ·  Investor Edition  ·  1.0 | 10 June 2026  ·  CONFIDENTIAL | 10 June 2026  ·  CONFIDENTIAL |
| --- | --- | --- | --- |
| LeTRON GROUP  ·  LeDB DIGITAL BRAIN Green Cargo Passport Le-GCP | LeTRON GROUP  ·  LeDB DIGITAL BRAIN Green Cargo Passport Le-GCP | LeTRON GROUP  ·  LeDB DIGITAL BRAIN Green Cargo Passport Le-GCP | LeTRON GROUP  ·  LeDB DIGITAL BRAIN Green Cargo Passport Le-GCP |
|  |  |  |  |
| "Biến mỗi kilômét vận tải thành một khối tài sản Carbon số hóa, được xác thực tuyệt đối từ cấp độ phần cứng." | "Biến mỗi kilômét vận tải thành một khối tài sản Carbon số hóa, được xác thực tuyệt đối từ cấp độ phần cứng." | "Biến mỗi kilômét vận tải thành một khối tài sản Carbon số hóa, được xác thực tuyệt đối từ cấp độ phần cứng." | "Biến mỗi kilômét vận tải thành một khối tài sản Carbon số hóa, được xác thực tuyệt đối từ cấp độ phần cứng." |
| Phiên bản | 1.0 — Final | 1.0 — Final | 1.0 — Final |
| Ngày ban hành | 10 tháng 06 năm 2026 | 10 tháng 06 năm 2026 | 10 tháng 06 năm 2026 |
| Bản quyền | LETRON DIGITAL BRAIN (LeDB) | LETRON DIGITAL BRAIN (LeDB) | LETRON DIGITAL BRAIN (LeDB) |
| Phân loại | Đối tác  ·  Nhà đầu tư  ·  Tổ chức kiểm toán | Đối tác  ·  Nhà đầu tư  ·  Tổ chức kiểm toán | Đối tác  ·  Nhà đầu tư  ·  Tổ chức kiểm toán |
| Phê duyệt | Lê Minh Tiến — Chủ tịch HĐQT Tập đoàn LeTRON | Lê Minh Tiến — Chủ tịch HĐQT Tập đoàn LeTRON | Lê Minh Tiến — Chủ tịch HĐQT Tập đoàn LeTRON |




### Bảng trích xuất 2


| MỤC LỤC TABLE OF CONTENTS |
| --- |




### Bảng trích xuất 3


| 1 | TUYÊN NGÔN CÔNG NGHỆ |
| --- | --- |




### Bảng trích xuất 4


| 2 | KIẾN TRÚC THU THẬP DỮ LIỆU BIÊN Edge Telemetry Architecture |
| --- | --- |




### Bảng trích xuất 5


|  | 2.1  Node Hub Dịch vụ (Le-NodeHub) |
| --- | --- |




### Bảng trích xuất 6


|  | 2.2  Node Động lực học (Le-NodeMobile) |
| --- | --- |




### Bảng trích xuất 7


| 3 | GIAO THỨC MÃ HÓA ZERO TRUST Zero Trust Encryption Protocol |
| --- | --- |




### Bảng trích xuất 8


|  | 3.1  Quy trình Mã hóa Viễn trắc Telemetry Cryptography |
| --- | --- |




### Bảng trích xuất 9


| Hash  =  SHA-256 ( Payload  +  Timestamp  +  Nonce ) |
| --- |




### Bảng trích xuất 10


|  | 3.2  Offline Resilience Protocol Giao thức Dự phòng Mất kết nối |
| --- | --- |




### Bảng trích xuất 11


| 4 | QUY TRÌNH ĐÚC CHỨNG THƯ SỐ TRÊN LÕI LeDB Blockchain Minting Process |
| --- | --- |




### Bảng trích xuất 12


|  | 4.1  Quá trình Đúc (Minting Workflow) |
| --- | --- |




### Bảng trích xuất 13


| Tổng kWh tiêu hao (xe)  ≈  Tổng kWh tái tạo đã nạp (hub)   |   Sai số cho phép < 0.5% |
| --- |




### Bảng trích xuất 14


| Abatement (tCO₂e) = (Diesel_baseline × distance × load_factor) − (Actual_kWh × grid_factor_renewable) |
| --- |




### Bảng trích xuất 15


|  | 4.2  Chi phí lưu trữ và xác thực blockchain |
| --- | --- |




### Bảng trích xuất 16


| Loại giao dịch | Chi phí (USD) | Ghi chú |
| --- | --- | --- |
| Phát hành GCP tiêu chuẩn (không có co-signing) | $0.01 – $0.03 | Tùy thuộc tải mạng |
| Phát hành GCP có co-signing TÜV | $0.05 – $0.10 | Bao gồm kiểm định điện tử TÜV |
| Truy xuất lịch sử (tra cứu) | Miễn phí | Qua cổng API public |




### Bảng trích xuất 17


| 5 | BLOCKCHAIN PLATFORM DECISION Hyperledger Besu |
| --- | --- |




### Bảng trích xuất 18


|  | 5.1  Nền tảng được lựa chọn: Hyperledger Besu Ethereum Enterprise |
| --- | --- |




### Bảng trích xuất 19


| Tiêu chí | Hyperledger Besu ✓ | Hyperledger Fabric | Polygon Edge |
| --- | --- | --- | --- |
| EVM compatibility | ✓ Hoàn toàn | ✗ Không | ✓ Có |
| Smart Contract (ERC-1155) | ✓ Native | ✗ Cần bridge | ✓ Có |
| Kiểm toán độc lập | ✓ TÜV/DNV | ◐ Hạn chế | ◐ Mới |
| Data export / portability | ✓ JSON-RPC | ✓ Có | ✓ Có |
| Proof-of-Authority (PoA) | ✓ QBFT/IBFT2 | ✓ Có | ✓ Có |




### Bảng trích xuất 20


|  | 5.2  Thông số kỹ thuật vận hành |
| --- | --- |




### Bảng trích xuất 21


| Tham số | Giá trị / Cấu hình LeDB |
| --- | --- |
| Consensus mechanism | QBFT (Quorum Byzantine Fault Tolerant) — kháng tối đa ⌊(n-1)/3⌋ validator lỗi |
| Block time | 2 giây (target) — finality sau 1 block xác nhận |
| Validator nodes | Tối thiểu 3: LeDB · TÜV Rheinland · đối tác FDI · |
| Transaction throughput | ~500 TPS — tương đương 43.2 triệu GCP/ngày |
| Smart contract standard | ERC-1155 Multi-token (mỗi GCP là 1 unique token với metadata đầy đủ) |
| Network type | Private permissioned — chỉ node được ủy quyền mới tham gia mạng |
| Data retention | Bất biến vĩnh viễn on-chain; off-chain raw data ≥ 10 năm (CBAM requirement) |




### Bảng trích xuất 22


|  | 5.3  Cam kết Data Portability |
| --- | --- |




### Bảng trích xuất 23


| 6 | ENERGY ATTRIBUTION CHAIN  Chuỗi Quy chiếu Nguồn gốc Năng lượng |
| --- | --- |




### Bảng trích xuất 24


|  | 6.1  Chuỗi quy chiếu 5 lớp 5-Layer Attribution Chain |
| --- | --- |




### Bảng trích xuất 25


| Lớp | Điểm kiểm soát | Bằng chứng / Xác minh |
| --- | --- | --- |
| L1 | LeSE Solar/Wind Output | SCADA đo sản lượng điện thực tế từ tấm pin Solar và Tuabin gió tại Siêu Hub |
| L2 | I-REC Certificate Issuance | Mỗi MWh điện tái tạo → 1 I-REC Certificate do APX Group cấp. Mã số ghi vào LeDB. |
| L3 | Hub Charging Session Linking | Mỗi phiên sạc Megawatt → SCADA Le-NodeHub ghép cặp kWh tiêu thụ với I-REC. Tỷ lệ phủ: 100% |
| L4 | Vehicle Telemetry Attribution | Le-NodeMobile ghi nhận Charging Session ID vào metadata hành trình. Mỗi kWh quy về session cụ thể |
| L5 | GCP Carbon Claim | Le-GCP phát hành với carbon claim = 0 kgCO₂e, đính kèm I-REC IDs phủ đủ toàn bộ kWh. CBAM Ready. |




### Bảng trích xuất 26


|  | 6.2  I-REC Certificate Management |
| --- | --- |




### Bảng trích xuất 27


| ⚠  Lưu ý lộ trình: Việt Nam đang xây dựng khung pháp lý DPPA. LeTRON cam kết chuyển sang I-REC đầy đủ dự kiến Q1/2027. Giai đoạn pilot (2026) sử dụng EAC nội bộ được TÜV Rheinland xác nhận. |
| --- |




### Bảng trích xuất 28


|  | 6.3  Sơ đồ Energy Attribution Flow |
| --- | --- |




### Bảng trích xuất 29


| [LeSE Solar/Wind] | ↓  SCADA đo sản lượng thực |
| --- | --- |
| [APX Group / I-REC Registry] | →  I-REC Certificate  (1 cert / MWh) |
| [Trạm sạc Megawatt — Le-NodeHub] | →  Charging Session ID + kWh |
| [CAMC BEV — Le-NodeMobile] | →  Telemetry (GPS + kWh + load + hash) |
| [LeDB Blockchain] | →  Dual-Verify → Carbon Abatement → I-REC Retire |
| [Le-GCP Certificate] | →  grid_factor = 0  ·  tCO₂e = 0  ·  CBAM Ready ✓ |




### Bảng trích xuất 30


| 7 | CỔNG GIAO TIẾP KIỂM TOÁN & TÍCH HỢP ERP API & Audit Gateway |
| --- | --- |




### Bảng trích xuất 31


|  | 7.1  Auditor Gateway Dành cho TÜV Rheinland |
| --- | --- |




### Bảng trích xuất 32


| Endpoint | Chức năng |
| --- | --- |
| GET  /v1/audit/verify/{gcp_id} | Xác thực tính hợp lệ của một GCP |
| POST /v1/audit/batch_verify | Xác thực hàng loạt tối đa 10.000 GCP |
| GET  /v1/audit/ledger/block/{height} | Truy xuất toàn bộ block |
| GET  /v1/audit/irec/{gcp_id} | Lấy danh sách I-REC IDs phủ chuyến hàng  [v2.0] |




### Bảng trích xuất 33


|  | 7.2  Client ERP Integration Dành cho Tập đoàn FDI |
| --- | --- |




### Bảng trích xuất 34


| 8 | BẢO MẬT & XỬ LÝ TRANH CHẤP |
| --- | --- |




### Bảng trích xuất 35


|  | 8.1  Kiểm thử xâm nhập và bảo mật định kỳ |
| --- | --- |




### Bảng trích xuất 36


|  | 8.2  Cơ chế xử lý tranh chấp (Dispute Resolution) |
| --- | --- |




### Bảng trích xuất 37


| Giai đoạn | Hành động |
| --- | --- |
| Yêu cầu giải thích  (24 giờ) | Bên khiếu nại gửi yêu cầu kèm ID chuyến hàng đến LeDB qua email có xác thực |
| Truy xuất dữ liệu gốc  (48 giờ) | LeDB trích xuất gói dữ liệu thô (raw data) đã lưu trữ an toàn, kèm hash tương ứng |
| Xác minh bên thứ ba  (72 giờ) | TÜV hoặc bên trọng tài chỉ định sử dụng Auditor Gateway để băm lại dữ liệu gốc và so sánh với hash trên blockchain |
| Phán quyết & bồi thường | Lỗi hệ thống LeTRON → hoàn trả toàn bộ phí Le-GCP.  Gian lận từ khách hàng → chuyển giao cơ quan pháp luật |




### Bảng trích xuất 38


| 9 | MÔ HÌNH CHI PHÍ VÀ TÍNH KINH TẾ |
| --- | --- |




### Bảng trích xuất 39


|  | 9.1  Chi phí vận hành mỗi GCP (ước tính 2027) |
| --- | --- |




### Bảng trích xuất 40


| Hạng mục | Chi phí (USD) | Ghi chú |
| --- | --- | --- |
| Lưu trữ blockchain (phí gas) | 0.01 – 0.03 | Tùy tải mạng nội bộ |
| Xác thực HSM và ký số | 0.005 | Phân bổ chi phí phần cứng |
| Băng thông và lưu trữ dữ liệu thô | 0.010 | Off-chain storage, backup |
| Kiểm toán tự động (Auditor Gateway) | 0.005 | Trả cho TÜV theo hợp đồng khung |
| I-REC certificate management  (v2.0) | 0.002 – 0.005 | Phí APX Registry, phân bổ theo kWh |
| Tổng chi phí biến đổi | 0.03 – 0.05 | Chưa gồm CAPEX hệ thống |




### Bảng trích xuất 41


|  | 9.2  Lợi ích kinh tế cho khách hàng FDI |
| --- | --- |




### Bảng trích xuất 42


| 10 | PHỤ LỤC |
| --- | --- |




### Bảng trích xuất 43


|  | 10.1  Sơ đồ kiến trúc tổng thể (Architecture Diagram) |
| --- | --- |




### Bảng trích xuất 44


|  | 10.2  Ví dụ dữ liệu thô từ Le-NodeMobile |
| --- | --- |




### Bảng trích xuất 45


| {   "timestamp":            "2026-06-10T14:32:00Z",   "gcp_id":               "GCP-VN-2406-000123",   "vehicle_id":           "CAMC-BEV-042",   "lat": 21.0278,  "lng": 105.8342,   "speed_kmh":            65.2,   "power_kwh":            120.5,   "cargo_kg":             24500,   "odometer_km":          12456.7,   "charging_session_id":  "HUB-VD-20260610-0042",   "irec_ids":   ["IREC-VN-2026-06-00441", "IREC-VN-2026-06-00442"],   "nonce":      "a8f3c9e2",   "signature":  "3045022100d1e2..." } |
| --- |




### Bảng trích xuất 46


|  | 10.3  Hash mẫu và blockchain transaction |
| --- | --- |




### Bảng trích xuất 47


| 2026-06-10T14:32:00Z|CAMC-BEV-042|21.0278|105.8342|120.5|24500|a8f3c9e2 |
| --- |




### Bảng trích xuất 48


| 0x7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1f3e4a5c6d7e8f9a0b1c2d3e4f5 |
| --- |




### Bảng trích xuất 49


| 0x9e4c2f5a1b3c7d8e9f0a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f |
| --- |




### Bảng trích xuất 50


|  | 10.4  Minh họa mã QR của GCP |
| --- | --- |




### Bảng trích xuất 51


| 11 | KẾT LUẬN |
| --- | --- |




### Bảng trích xuất 52


| Tài liệu này được phê duyệt bởi: Ông Lê Minh Tiến Chủ tịch HĐQT  ·  Tập đoàn LeTRON Le-GCP White Paper 1.0  ·  10/06/2026  ·  CONFIDENTIAL |
| --- |

