# Workflow: Chuyển đổi tài liệu PDF sang Knowledge Base & Neo4j (pdf-to-kb)

Luồng công việc này hướng dẫn cách sử dụng kỹ năng `pdf-to-kb` để phân rã báo cáo/tiêu chuẩn PDF thành tài liệu Markdown và đẩy mối quan hệ thực thể nghiệp vụ sạch lên Neo4j Aura thông qua Bản đồ tri thức (Concept Map) kiểm chứng.

---

## Giai đoạn 1: Trích xuất PDF sang Markdown KB

### Bước 1: Quét ranh giới chương (Scan Boundaries)
Chạy script quét ranh giới để phát hiện các trang bắt đầu và kết thúc của từng chương:
```bash
uv run C:/Users/kira7/.gemini/config/skills/pdf-to-kb/scripts/scan_chapter_pages.py --pdf <duong_dan_file_pdf>
```
Script sẽ tự động tìm kiếm dựa trên bookmarks hoặc mẫu chữ `C H A P T E R  N` và tạo ra tệp cấu hình `<tên_file>.chapters.json`.

### Bước 2: Bổ sung Title & Slug chương
Mở file JSON và điền `title` cùng `slug` tương ứng.

### Bước 3: Thực thi trích xuất và Validation
Trích xuất toàn bộ sang thư mục Knowledge Base:
```bash
uv run C:/Users/kira7/.gemini/config/skills/pdf-to-kb/scripts/extract_pdf_to_kb.py --pdf <duong_dan_file_pdf> --out Projects/ESG/ghg_kb --config <duong_dan_file_json> --backup
```
Kiểm tra báo cáo validation trên `stderr` để đảm bảo số dòng và heading đầy đủ.

---

## Giai đoạn 2: Khóa cứng Anchors & Định hình Đồ thị Tri thức

### Bước 4: Khóa cứng Anchors cố định trong Markdown (Anchor Stabilization)
Để đảm bảo đồ thị và tài liệu Markdown luôn đồng bộ dù tiêu đề có thay đổi, hãy mở các file Markdown trong thư mục `Projects/ESG/ghg_kb` và chèn thẻ HTML anchor cố định ngay trên dòng Heading bạn muốn liên kết:
```html
<a id="principles_relevance"></a>
## Relevance
```
*Lưu ý*: `id` viết thường, dùng dấu gạch dưới, mô tả duy nhất vị trí điều khoản nghiệp vụ.

### Bước 5: Thiết lập Bản đồ Tri thức (`concept_map.json`)
Xác định danh mục thực thể tĩnh nghiệp vụ (`nodes`) phân tách theo 4 lớp (Normative, Method, Evidence, Control) kèm con trỏ liên kết Markdown (`doc_id`, `anchor`) và các mối liên kết chéo (`edges`). Lưu tệp cấu hình tại thư mục `Projects/ESG/concept_map.json`.

*   `doc_id` của node bắt buộc phải khớp với phần slug của file Markdown (ví dụ: file `01_principles.md` -> `principles`).
*   `anchor` của node bắt buộc phải trùng khớp 100% với `id` của thẻ `<a id="..."></a>` đã chèn ở Bước 4.

### Bước 6: Chạy import và kiểm chứng liên kết
Thực thi script `import_concept_map.py` để tự động hóa kiểm tra tính hợp lệ liên kết trên ổ đĩa vật lý trước khi nạp vào Neo4j:
```bash
uv run C:/Users/kira7/.gemini/config/skills/pdf-to-kb/scripts/import_concept_map.py --map Projects/ESG/concept_map.json --kb-dir Projects/ESG/ghg_kb
```
Script sẽ nạp các biến môi trường kết nối trực tiếp từ `.env`, kiểm tra chéo các anchor liên kết thực tế trên ổ cứng và báo lỗi dừng tiến trình nếu phát hiện bất kỳ liên kết hỏng nào.

---
*Status: ACTIVE WORKFLOW*
