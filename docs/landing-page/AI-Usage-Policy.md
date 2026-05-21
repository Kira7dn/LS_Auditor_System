# CHÍNH SÁCH SỬ DỤNG AI

**Link Strategy (LS Auditor / LS-ASS)**

_Cập nhật lần cuối: [NGÀY/THÁNG/NĂM]_

Chính sách Sử dụng AI này (“Chính sách”) giải thích cách thức các tính năng trí tuệ nhân tạo (“AI”) được tích hợp, sử dụng và kiểm soát trong nền tảng Link Strategy, cụ thể thông qua AI Auditor Agent (Trợ lý Kiểm toán AI) và LS Audit Support System (Hệ thống Hỗ trợ Kiểm toán LS - “LS Auditor”, “chúng tôi”, hoặc “của chúng tôi”).

Chính sách này là một phần của Điều khoản Dịch vụ và áp dụng cho tất cả người dùng Dịch vụ của chúng tôi.

---

## 1. Vai trò của AI trong Link Strategy (Mô hình AI Forensic Guide)

Link Strategy sử dụng AI như một **trợ lý chẩn đoán vận hành chuyên sâu** (AI Forensic Guide), nhằm nâng cao năng lực cho các nhà tư vấn con người, các giám đốc tài chính (CFO), giám đốc điều hành (CEO) và các nhà quản lý vận hành.

Các tính năng AI được thiết kế để:

- **Mô hình hóa Luồng công việc:** Chuyển đổi các mô tả bằng văn bản của người dùng về quy trình doanh nghiệp thành sơ đồ luồng vận hành chuẩn hóa bằng cú pháp Mermaid.
- **Xác định Lỗ hổng Kiểm soát:** Chỉ ra các Điểm kiểm soát Trọng yếu (CCP) và các điểm yếu vận hành khi các thủ tục đang được thực hiện thủ công hoặc bypass ngoài hệ thống (Zalo/Excel).
- **Đưa ra Giả thuyết Rò rỉ:** Tính toán các chỉ số rò rỉ tài chính và lãng phí vận hành ban đầu dựa trên các benchmark ngành và thông tin đầu vào từ người dùng (**Quantified Suspicion** - Hoài nghi định lượng).

Hệ thống AI **KHÔNG được thiết kế** để:

- Thay thế cho kiểm toán viên pháp lý chính thức hoặc tự ý phát hành báo cáo tài chính được chứng thực pháp lý
- Thực hiện các hành động sửa đổi dữ liệu tự động hoặc can thiệp trực tiếp vào các bản ghi cơ sở dữ liệu của khách hàng mà không có sự kiểm soát của con người
- Thay thế hoàn toàn sự thẩm định chuyên môn của con người trong các quyết định quản trị doanh nghiệp

---

## 2. Kiến trúc Kiểm soát bởi Con người (Human-in-Control)

Mọi tính năng AI trong hệ thống LS Auditor vận hành nghiêm ngặt dưới mô hình **con người kiểm soát hoàn toàn**:

- **Kích hoạt bởi Người dùng:** Các phiên quét chẩn đoán và chat tương tác với AI Auditor chỉ được khởi chạy khi có hành động kích hoạt trực tiếp từ người dùng.
- **Trạng thái Khuyến nghị (Advisory Status):** Các kết quả đầu ra của AI chỉ được coi là các giả thuyết logic và được đánh dấu là "Candidate Exceptions" (Ngoại lệ chờ xác thực) hoặc "Pending Verification" (Chờ đối soát) cho đến khi được kiểm chứng bằng transaction logs thực tế (Layer 2).
- **Không Tự ý Thực thi:** Hệ thống sẽ không bao giờ tự động tạo ra hoặc áp đặt bất kỳ thay đổi nào lên hệ thống vận hành của doanh nghiệp nếu không có sự xem xét, cấu hình và phê duyệt thủ công từ người quản lý.

---

## 3. Phạm vi & Giới hạn của Kết quả từ AI

Bạn thừa nhận và đồng ý rằng các phân tích chẩn đoán hỗ trợ bởi AI:

- **Đưa ra Giả thuyết, Không đưa ra Sự thật:** Các ước tính về dòng tiền rò rỉ, bypass quy trình và mức độ rủi ro là kết quả giả lập từ mô hình toán học. Giá trị rò rỉ thực tế chỉ có thể được kết luận sau khi chạy đối soát dữ liệu giao dịch thật (Layer 2).
- **Phụ thuộc vào Chất lượng Dữ liệu Đầu vào:** Nếu thông tin mô tả quy trình của người dùng bị thiếu, không chính xác hoặc lỗi thời, sơ đồ Mermaid và mức rủi ro do AI tạo ra cũng sẽ phản ánh các sai lệch đó.
- **Tính chất So sánh Tiêu chuẩn:** Các khuyến nghị do AI đưa ra dựa trên các thông lệ vận hành tốt nhất (best practices) của ngành và cần được tùy chỉnh lại để phù hợp với bối cảnh đặc thù của từng doanh nghiệp.

Kết quả đầu ra của AI **không được sử dụng làm căn cứ duy nhất** để thực hiện các biện pháp kỷ luật lao động, báo cáo thuế hay khởi kiện pháp lý khi chưa qua bước đối soát xác thực bằng dữ liệu giao dịch thực tế do chuyên gia con người thực hiện.

---

## 4. Bảo vệ Quyền riêng tư & Dữ liệu Vận hành Doanh nghiệp

Chúng tôi thấu hiểu tính chất nhạy cảm cao của dữ liệu vận hành và tài chính doanh nghiệp:

- **Tuyệt đối Không Huấn luyện Mô hình Công cộng:** Chúng tôi cam kết **KHÔNG** sử dụng bất kỳ dữ liệu đầu vào, mô tả quy trình, log hệ thống hay nội dung chat tương tác nào của bạn để huấn luyện, cải tiến các mô hình AI dùng chung hoặc công cộng của bên thứ ba.
- **Môi trường Cô lập Doanh nghiệp:** Tất cả dữ liệu đầu vào và prompts tương tác của bạn được mã hóa, cô lập hoàn toàn trong sandbox của doanh nghiệp bạn.
- **Hợp đồng Doanh nghiệp Chặt chẽ:** Đối với các API mô hình AI nền tảng từ bên thứ ba, chúng tôi chỉ sử dụng các gói dịch vụ cấp doanh nghiệp (Enterprise Tier) có cam kết bằng văn bản về việc không lưu giữ dữ liệu (Zero Data Retention) cho các tác vụ xử lý chẩn đoán.

---

## 5. Rào chắn Bảo vệ & Sử dụng Công bằng

Để duy trì tính ổn định của hệ thống và ngăn ngừa hành vi lạm dụng tài nguyên AI, chúng tôi áp dụng:

- **Giới hạn Credit Chẩn đoán:** Kiểm soát tần suất sử dụng để ngăn chặn bot spam và các cuộc tấn công từ chối dịch vụ.
- **Bộ lọc Đầu vào:** Hệ thống tự động lọc và chặn các câu lệnh không liên quan, độc hại hoặc có tính chất phá hoại.
- **Cảnh báo Đối soát:** Hệ thống luôn đính kèm nhãn cảnh báo trên các kết quả AI tạo ra để hướng dẫn người dùng tiến hành các dự án đối soát dữ liệu thật (Paid Diagnostic Project) để kiểm chứng số liệu.

---

## 6. Cập nhật và Nâng cấp Nền tảng AI

Các mô hình AI và công cụ chẩn đoán được nâng cấp định kỳ để cải thiện độ chính xác, tốc độ vẽ sơ đồ Mermaid và khả năng ước tính thất thoát tài chính.

Link Strategy có thể:

- Thay đổi, cập nhật hoặc thay thế các mô hình AI nền tảng
- Điều chỉnh số lượng credit chẩn đoán tiêu thụ hoặc giới hạn phiên sử dụng với thông báo hợp lý trước khi áp dụng
- Bổ sung hoặc lược bỏ một số khả năng của công cụ CLI dựa trên hiệu năng thực tế

---

## 7. Liên hệ

Mọi câu hỏi liên quan tới quản trị AI, an toàn dữ liệu hoặc các nội dung của Chính sách này, vui lòng liên hệ:

📧 **legal@linkstrategy.vn**
