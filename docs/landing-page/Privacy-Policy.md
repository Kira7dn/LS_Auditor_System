# CHÍNH SÁCH BẢO MẬT

**Link Strategy (LS Auditor / LS-ASS)**

_Cập nhật lần cuối: [NGÀY/THÁNG/NĂM]_

Chính sách Bảo mật này (“Chính sách”) mô tả cách thức Link Strategy (“Link Strategy”, “chúng tôi”, hoặc “của chúng tôi”) thu thập, sử dụng và bảo vệ thông tin cá nhân cùng dữ liệu vận hành doanh nghiệp khi bạn truy cập hoặc sử dụng nền tảng Link Strategy, bao gồm AI Auditor Agent và LS Audit Support System (gọi chung là “Dịch vụ”).

Bằng việc sử dụng Dịch vụ của chúng tôi, bạn đồng ý với việc thu thập và sử dụng thông tin theo đúng quy định tại Chính sách này.

---

## 1. Phạm vi Áp dụng

Chính sách này áp dụng cho:

- Khách truy cập vào website và các trang landing page của chúng tôi
- Người dùng doanh nghiệp đã đăng ký tài khoản trên nền tảng LS Auditor
- Thành viên được thêm vào không gian làm việc (workspace) của khách hàng doanh nghiệp

Chính sách này cần được đọc cùng với:

- Điều khoản Dịch vụ
- Chính sách Sử dụng AI
- Chính sách Sử dụng Hợp lệ
- Các Thỏa thuận Bảo mật (NDA) được ký kết riêng cho các dự án có phí

---

## 2. Thông tin Chúng tôi Thu thập

Chúng tôi chỉ thu thập các thông tin thực sự cần thiết để thực hiện chẩn đoán vận hành, chạy đối soát dữ liệu và tối ưu hóa độ tin cậy của Dịch vụ.

### 2.1 Thông tin Liên hệ Doanh nghiệp

- Họ tên, địa chỉ email công việc, chức vụ và số điện thoại
- Tên công ty, lĩnh vực hoạt động và quy mô nhân sự/vận hành ước tính
- Thông tin đăng nhập tài khoản và dữ liệu xác thực hệ thống

---

### 2.2 Dữ liệu Vận hành & Quy trình

- Sơ đồ quy trình, mô tả luồng công việc và các kịch bản vận hành do người dùng nhập vào trong các phiên chẩn đoán tự động
- Danh sách các hệ thống phần mềm đang sử dụng tại doanh nghiệp (ví dụ: các nhà cung cấp ERP, CRM, HRM...)
- Chỉ số ước tính việc nhân sự bypass quy trình hệ thống để làm tay (tần suất dùng Excel/Zalo)

Dữ liệu này được người dùng cung cấp hoàn toàn tự nguyện để AI Auditor Agent dựng sơ đồ Mermaid và chỉ ra các điểm kiểm soát yếu (CCP).

---

### 2.3 Dữ liệu Giao dịch & Kiểm toán (Chỉ dành cho Dự án Có phí)

Đối với các khách hàng tiến hành **Đối soát Dữ liệu có phí (Tầng 2)**:

- Log giao dịch, đơn đặt hàng, biên bản giao nhận, chứng từ thanh toán và các bảng dữ liệu tài chính được tải lên để đối soát
- Cấu trúc bảng cơ sở dữ liệu (schema), API logs và các tệp dữ liệu kết xuất từ hệ thống cũ
- Các bộ luật xác thực và logic đối soát được thiết lập riêng cho doanh nghiệp

Mọi dữ liệu giao dịch và kiểm toán này được cô lập nghiêm ngặt trong phân vùng cơ sở dữ liệu nhiều tầng (multi-tenant) hoặc triển khai trên đám mây ảo riêng biệt (VPC).

---

### 2.4 Dữ liệu Tương tác AI

- Các câu lệnh (prompts), mô tả và chỉ thị của người dùng nhập vào phiên chat với AI Auditor
- Các câu trả lời của AI, điểm số đánh giá rủi ro và sơ đồ Mermaid được tạo ra

Dữ liệu này được xử lý động để cung cấp dịch vụ chẩn đoán theo thời gian thực.

---

### 2.5 Dữ liệu Kỹ thuật & Log Hệ thống

- Địa chỉ IP, loại trình duyệt, hệ điều hành và timestamp của hệ thống
- Thời gian phiên truy cập, lượng credit chẩn đoán đã tiêu thụ và các tính năng đã sử dụng

Dữ liệu này được dùng duy nhất cho mục đích bảo mật hệ thống, ngăn chặn lạm dụng nền tảng và tối ưu hóa hiệu năng máy chủ.

---

## 3. Cách thức Chúng tôi Sử dụng Thông tin

Chúng tôi sử dụng thông tin thu thập được nghiêm ngặt cho các mục đích:

- Cung cấp, vận hành và duy trì tính ổn định của Dịch vụ
- Chạy các chẩn đoán tự động bằng AI, vẽ bản đồ quy trình và tính toán chỉ số rủi ro rò rỉ
- Xuất báo cáo chẩn đoán dưới dạng PDF theo yêu cầu
- Quản lý thanh toán, đăng ký thuê bao và lượng credit chẩn đoán của tài khoản
- Ngăn chặn các hành vi gian lận, dịch ngược mã nguồn hoặc lạm dụng hệ thống
- Tuân thủ các nghĩa vụ pháp lý và quy chuẩn kiểm toán hiện hành

Chúng tôi **tuyệt đối không** bán, cho thuê, trao đổi thông tin liên hệ hay dữ liệu vận hành của doanh nghiệp bạn cho bất kỳ đơn vị quảng cáo hoặc bên thứ ba nào khác.

---

## 4. Cam kết Bảo vệ Dữ liệu đối với Công nghệ AI

Link Strategy áp dụng các tiêu chuẩn an toàn dữ liệu nghiêm ngặt đối với việc xử lý bằng trí tuệ nhân tạo:

- **Không Huấn luyện Mô hình AI Công cộng:** Chúng tôi **KHÔNG** sử dụng dữ liệu giao dịch, log vận hành, file cơ sở dữ liệu hay mô tả quy trình của doanh nghiệp bạn tải lên để huấn luyện (train), tinh chỉnh (fine-tune) hoặc cải tiến các mô hình AI công cộng hoặc dùng chung của bên thứ ba.
- **Xử lý Tạm thời (On-Demand):** Dữ liệu được gửi tới các endpoint của mô hình AI theo thời gian thực dựa trên hành động kích hoạt của người dùng và không được lưu trữ bởi bên cung cấp mô hình AI cho các mục đích độc lập khác.
- **Cô lập Dữ liệu:** Tất cả ngữ cảnh tương tác và các luật đối soát tùy chỉnh được mã hóa và cô lập hoàn toàn trong môi trường tài khoản của riêng bạn.

---

## 5. Các Đơn vị Cung cấp Dịch vụ bên thứ ba

Chúng tôi có thể hợp tác với các nhà cung cấp hạ tầng công nghệ uy tín để vận hành nền tảng, bao gồm:

- Nhà cung cấp dịch vụ lưu trữ đám mây bảo mật (như AWS, Google Cloud)
- Dịch vụ quản lý cơ sở dữ liệu và giám sát an ninh mạng chuyên nghiệp
- Nhà cung cấp API AI doanh nghiệp (sử dụng hợp đồng cấp doanh nghiệp có điều khoản xóa dữ liệu ngay sau khi xử lý)
- Hệ thống gửi email tự động và quản lý ticket hỗ trợ khách hàng

Tất cả các bên thứ ba này đều bị ràng buộc pháp lý bởi các thỏa thuận xử lý dữ liệu chặt chẽ và nghĩa vụ bảo mật thông tin tuyệt đối.

---

## 6. Thời gian Lưu trữ & Tiêu hủy Dữ liệu An toàn

Chúng tôi chỉ lưu trữ dữ liệu của bạn trong thời gian cần thiết để thực hiện các mục đích nêu trong Chính sách này, hoặc theo các mốc thời gian quy định tại NDA và hợp đồng ký kết với khách hàng:

- **Các Phiên Tự chẩn đoán Miễn phí:** Nội dung tương tác chat và báo cáo PDF chẩn đoán sẽ được lưu trữ tự động trong 30 ngày và xóa vĩnh viễn sau 90 ngày, trừ khi người dùng chuyển đổi sang tài khoản trả phí.
- **Các Dự án Đối soát Có phí:** Dữ liệu thô và log giao dịch tải lên phục vụ cho quá trình đối soát sẽ được lưu giữ trong suốt sprint kiểm toán và được xóa an toàn khỏi hệ thống trong vòng 30 ngày kể từ khi nghiệm thu dự án (trừ khi khách hàng kích hoạt gói giám sát liên tục SaaS).
- **Vô danh hóa (Anonymization):** Chúng tôi có thể lưu trữ các chỉ số rủi ro tổng hợp đã được vô danh hóa hoàn toàn (ví dụ: điểm số ERP Graveyard trung bình theo ngành) để xây dựng báo cáo benchmark thị trường. Dữ liệu này tuyệt đối không chứa bất kỳ thông tin nào giúp định danh công ty hay giao dịch cụ thể của bạn.

---

## 7. Biện pháp An ninh Bảo mật

Link Strategy áp dụng các biện pháp an ninh chuyên nghiệp để bảo vệ dữ liệu vận hành nhạy cảm của bạn:

- Mã hóa toàn bộ dữ liệu trên đường truyền (TLS 1.3) và dữ liệu được lưu trữ tĩnh (AES-256)
- Yêu cầu xác thực đa yếu tố (MFA) đối với mọi quyền truy cập quản trị hệ thống
- Thường xuyên quét lỗ hổng bảo mật và chạy các script phân tích dữ liệu trong môi trường cô lập (sandbox)

Không có phương thức truyền tải hoặc lưu trữ nào an toàn 100%, nhưng chúng tôi cam kết áp dụng các tiêu chuẩn an toàn thông tin khắt khe nhất để bảo vệ tài sản dữ liệu của doanh nghiệp bạn.

---

## 8. Thay đổi đối với Chính sách này

Chúng tôi có thể cập nhật Chính sách Bảo mật này theo thời gian.

Các thay đổi quan trọng sẽ được thông báo trực tiếp trên website hoặc gửi qua email của bạn. Việc tiếp tục sử dụng Dịch vụ sau khi Chính sách mới có hiệu lực đồng nghĩa với việc bạn đồng ý với các cập nhật đó.

---

## 9. Liên hệ

Nếu có câu hỏi, yêu cầu truy xuất dữ liệu hoặc yêu cầu xóa dữ liệu, vui lòng liên hệ:

📧 **privacy@linkstrategy.vn**
