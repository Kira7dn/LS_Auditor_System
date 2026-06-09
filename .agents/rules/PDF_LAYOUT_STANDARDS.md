# Quy tắc Thiết kế Markdown để Xuất PDF (PDF_LAYOUT_STANDARDS.md)

Tài liệu này định nghĩa các quy tắc định dạng Markdown tối ưu cho công cụ kết xuất PDF (`export_md_pdf.py`). Mọi tài liệu thiết kế (PDD), báo cáo (Report), hay chứng thư trong hệ thống phải tuân thủ nghiêm ngặt để đảm bảo bố cục chuyên nghiệp, không bị ngắt trang lỗi hoặc xuất hiện trang rỗng.

---

## 1. Cơ chế Phân trang của Trình Kết xuất (Smart Layout Compiler)
Hệ thống sử dụng thuật toán **phân trang động thông minh** được tích hợp trực tiếp trong script Python (`export_md_pdf.py`). 
* **Không ngắt trang cứng bằng CSS:** Tiêu đề H2 (`##`) không còn bị tự động ngắt trang cưỡng bức.
* **Ngắt trang động theo dung lượng thực tế:** Trình kết xuất tự động ước lượng độ dài (dòng chữ, công thức, bảng biểu, hình ảnh) của từng chương và tự động chèn `<div class="page-break"></div>` chỉ khi:
  * Tổng dung lượng tích lũy của trang hiện tại cộng phần mới vượt quá giới hạn trang A4 (~36 dòng nội dung cơ bản).
  * Trang hiện tại đã dùng hết $>85\%$ dung lượng.
  * Chương tiếp theo rất dài/nặng và trang hiện tại đã chứa một lượng nội dung nhất định.
  * **ĐẶC BIỆT:** Thuật toán sẽ ép buộc **không bao giờ ngắt trang** khi trang hiện tại chứa dưới 12 dòng để triệt tiêu hoàn toàn các trang trống hoặc các đoạn văn mồ côi.

---

## 2. Các Quy tắc Viết Markdown (Markdown Layout Rules)

### Quy tắc 1: Cấu trúc Tiêu đề và nội dung
* Tập trung viết Markdown một cách tự nhiên. Sử dụng `##` cho các chương lớn và `###`/`####` cho các phần mục con.
* Tuyệt đối **KHÔNG sử dụng thủ công** thẻ `<div class="page-break"></div>` trong file Markdown gốc, ngoại trừ các trường hợp thực sự đặc biệt mà thuật toán không thể tự xử lý (như phân tách rõ ràng phần Phụ lục lớn). Thẻ div thủ công sẽ phá hỏng thuật toán tối ưu hóa của trình dịch và tạo ra các trang trống thừa thãi.

### Quy tắc 2: Căn chỉnh Hình ảnh (Images)
* Hình ảnh lớn (đặc biệt là sơ đồ) có nguy cơ bị đẩy hoàn toàn sang trang sau nếu trang hiện tại không đủ không gian.
* **Giải pháp:** 
  * Luôn kiểm soát kích thước ảnh bằng HTML (ví dụ: khống chế chiều cao tối đa ở mức `height="360px"` để trang giấy có đủ khoảng thở).
  * Căn giữa hình ảnh bằng thuộc tính: `style="display:block; margin:15px auto;"`.

### Quy tắc 3: Thiết kế Bảng (Tables)
* Từng dòng trong bảng (`tr`) được bảo vệ không bị ngắt đôi giữa trang. 
* **Giải pháp:** Đối với các bảng có trên 15 dòng, hãy chủ động chia tách thành các bảng nhỏ hơn theo danh mục để thuật toán phân trang hoạt động tối ưu nhất.

### Quy tắc 4: Khối Code (` ``` `) và Khối Trích dẫn (`>`)
* Tránh viết các khối code quá dài (trên 20 dòng) mà không ngắt đoạn để tránh việc nguyên khối code bị đẩy sang trang tiếp theo gây trống trang hiện tại.

### Quy tắc 5: Viết và Hỗ trợ Công thức Toán học (LaTeX/MathJax)
* Công thức toán học đặt trong cặp dấu `$$...$$` (block math) hoặc `$...$` (inline math) sẽ được tự động biên dịch và render sắc nét nhờ thư viện **KaTeX** được script xuất PDF tự động tích hợp trước khi in. Người viết tài liệu **không cần nhúng thủ công** bất kỳ link CDN KaTeX nào vào file Markdown.
