# CHÍNH SÁCH SỬ DỤNG HỢP LỆ

**Link Strategy (LS Auditor / LS-ASS)**

_Cập nhật lần cuối: [NGÀY/THÁNG/NĂM]_

Chính sách Sử dụng Hợp lệ này (“Chính sách”) quy định các hành vi được phép và bị nghiêm cấm khi sử dụng nền tảng, công cụ chẩn đoán và các công cụ CLI của Link Strategy (“LS Auditor”, “chúng tôi”, hoặc “của chúng tôi”).

Chính sách này là một phần không thể tách rời của Điều khoản Dịch vụ. Bằng việc sử dụng Dịch vụ, bạn đồng ý tuân thủ Chính sách này.

---

## 1. Mục đích của Chính sách này

Link Strategy được thiết kế nhằm giúp các tổ chức doanh nghiệp và nhà quản lý thực hiện chẩn đoán rủi ro vận hành & tài chính, xác định các điểm thất thoát dòng tiền (leakage) và triển khai các rào chắn kiểm soát tự động.

Chính sách này được ban hành để:

- Bảo vệ an ninh, tính toàn vẹn và hiệu năng của các dịch vụ chẩn đoán của chúng tôi
- Ngăn ngừa các hành vi tải lên dữ liệu độc hại, cào thông tin hệ thống hoặc dịch ngược mã nguồn
- Đảm bảo quyền tiếp cận công bằng các tài nguyên chẩn đoán AI cho mọi người dùng

Chính sách này áp dụng đối với tất cả các dữ liệu, file log, sơ đồ quy trình và cấu trúc dữ liệu được tải lên hoặc xử lý thông qua Dịch vụ.

---

## 2. Nguyên tắc Sử dụng Chung

Bạn chỉ được phép sử dụng Dịch vụ cho các mục đích chẩn đoán doanh nghiệp và cải tiến vận hành hợp pháp và đã được ủy quyền hợp lệ từ cấp có thẩm quyền của doanh nghiệp bạn.

Bạn đồng ý không sử dụng Dịch vụ dưới bất kỳ hình thức nào:

- Vi phạm các quy định quản trị doanh nghiệp, quy định về quyền riêng tư của người lao động hoặc luật bảo vệ dữ liệu cá nhân
- Gây ra các rủi ro vận hành, tài chính hoặc uy tín cho Link Strategy hoặc các khách hàng khác của chúng tôi
- Tìm cách vượt qua các rào cản bảo mật, cấu trúc thanh toán hoặc kiểm soát hệ thống của chúng tôi

---

## 3. Các Hành vi bị Nghiêm cấm

Các hành vi dưới đây bị nghiêm cấm hoàn toàn khi bạn tương tác với nền tảng, các endpoint API hoặc các script CLI của chúng tôi.

### 3.1 Tải lên Dữ liệu Độc hại & Gây rối Hệ thống

Bạn không được:

- Tải lên các file log bị hỏng, dữ liệu rác được cấu trúc có chủ đích hoặc các tệp tin chứa mã độc, trojan, virus
- Nhập dữ liệu được thiết kế nhằm gây rối loạn hoặc gây ra lỗi tràn bộ đệm (buffer overflow) cho các công cụ phân tích dữ liệu của chúng tôi (như `normalize_cli`, `join_cli`...)
- Sử dụng bảng điều khiển chẩn đoán của chúng tôi để lưu trữ hoặc truyền tải các tài liệu bất hợp pháp

---

### 3.2 Vi phạm Sở hữu Trí tuệ & Dịch ngược Mã nguồn

Bạn không được:

- Tìm cách tải xuống, trích xuất, biên dịch ngược (decompile) hoặc dịch ngược (reverse-engineer) các gói luật đối soát độc quyền của chúng tôi (**Audit Rule Packs** - bao gồm `compute_cli`, `rule_test_cli`)
- Sao chép, nhân bản hoặc tái tạo lại logic vận hành của bộ công cụ **LS-ASS CLI toolchain** hoặc các cấu trúc schema tùy chỉnh của nó nếu không có sự đồng ý bằng văn bản của chúng tôi
- Bán, chuyển nhượng hoặc phân phối lại các báo cáo chẩn đoán và sơ đồ Mermaid được tạo ra từ hệ thống cho các đơn vị tư vấn hoặc công ty phần mềm đối thủ cạnh tranh

---

### 3.3 Lạm dụng Phiên chẩn đoán & API

Bạn không được:

- Tìm cách bypass giới hạn Credit chẩn đoán, số phiên giới hạn hàng tháng hoặc các giao thức giới hạn tần suất yêu cầu (rate-limiting)
- Sử dụng các script tự động, bot hoặc công cụ cào dữ liệu để tạo ra hàng loạt phiên chat chẩn đoán AI giả mạo, gây cạn kiệt tài nguyên máy chủ của các khách hàng khác
- Giả mạo token ủy quyền API để truy cập trái phép vào workspace hoặc lịch sử chẩn đoán của doanh nghiệp khác

---

### 3.4 Giả mạo & Khai báo Thông tin Sai lệch

Bạn không được:

- Tải lên dữ liệu giao dịch hoặc log vận hành của doanh nghiệp mà bạn không sở hữu hoặc không có thẩm quyền/phê duyệt từ cấp quản lý để chạy đối soát
- Giả mạo doanh nghiệp khác, hoặc đóng vai là CFO/CEO của công ty khác để chạy các đánh giá chẩn đoán so sánh rủi ro
- Chia sẻ rộng rãi các báo cáo PDF chẩn đoán tự động ra công chúng và tuyên bố sai lệch rằng đó là báo cáo kiểm toán pháp lý chính thức được chứng nhận bởi cơ quan quản lý nhà nước

---

## 4. Sử dụng AI & Tính Liêm chính của Đối soát

Khi tương tác với AI Auditor Agent:

- Bạn không được tìm cách "jailbreak" hoặc áp dụng các kỹ thuật prompt-engineering nhằm ép buộc AI Agent đưa ra các đoạn mã nguồn độc hại, nội dung tiếp thị không liên quan hoặc các quan điểm cá nhân lệch lạc
- Bạn đồng ý coi các số liệu thất thoát và sơ đồ Mermaid do AI tạo ra là các giả thuyết tham khảo, và tuyệt đối không dùng chúng làm bằng chứng duy nhất để đưa ra các hình thức kỷ luật nhân sự hoặc khiếu nại pháp lý chính thức khi chưa có sự xác thực đối soát thủ công từ chuyên gia con người (Layer 2)

---

## 5. Các Biện pháp Xử lý Vi phạm

Link Strategy có quyền thực hiện các biện pháp xử lý vi phạm nhanh chóng, bao gồm:

- Hạn chế quyền truy cập API chẩn đoán của tài khoản
- Hủy bỏ các credit chẩn đoán đang hoạt động
- Tạm dừng hoặc khóa vĩnh viễn tài khoản người dùng
- Xóa bỏ dữ liệu đã tải lên ngay lập tức nếu phát hiện chứa mã độc hoặc dữ liệu phá hoại

Chúng tôi có thể thực hiện các hành động này có hoặc không có thông báo trước, tùy thuộc vào mức độ nghiêm trọng và rủi ro của hành vi vi phạm.

---

## 6. Báo cáo Hành vi Vi phạm

Nếu bạn phát hiện bất kỳ lỗ hổng bảo mật nào, hoặc các hành vi lạm dụng, vi phạm chính sách của nền tảng Link Strategy, vui lòng báo cáo ngay cho chúng tôi tại:

📧 **abuse@linkstrategy.vn**

---

## 7. Mối liên hệ với các Chính sách khác

Chính sách này cần được đọc cùng với:

- Điều khoản Dịch vụ
- Chính sách Sử dụng AI
- Chính sách Bảo mật

Trong trường hợp có bất kỳ sự xung đột nào, Điều khoản Dịch vụ sẽ là văn bản được ưu tiên áp dụng cao nhất.
