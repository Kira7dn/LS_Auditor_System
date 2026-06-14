# Workflow: Chuyển đổi tài liệu PDF sang Knowledge Base & Neo4j (pdf-to-kb)

Luồng công việc này hướng dẫn cách sử dụng kỹ năng `pdf-to-kb` để phân rã các báo cáo, tiêu chuẩn PDF thành tài liệu Markdown và đẩy mối quan hệ nghiệp vụ sạch lên Neo4j Aura thông qua Bản đồ tri thức (Concept Map) kiểm chứng, hỗ trợ môi trường đa tài liệu.

---

## Giai đoạn 1: Trích xuất PDF sang Markdown KB

### Bước 1: Quét ranh giới chương (Scan Boundaries)
Chạy script quét ranh giới để phát hiện các trang bắt đầu và kết thúc của từng chương:
```bash
uv run C:/Users/kira7/.gemini/config/skills/pdf-to-kb/scripts/scan_chapter_pages.py --pdf Projects/ESG/sources/<source_id>/pdf/<file_name>.pdf
```
Script sẽ tự động tìm kiếm dựa trên bookmarks hoặc tạo ra tệp cấu hình `<tên_file>.chapters.json`. Nếu cấu trúc tài liệu phức tạp (ví dụ: tiếng Việt), hãy kiểm tra và bổ sung `start_page`, `end_page`, `slug`, và `title` thủ công.

### Bước 2: Thực thi trích xuất và Validation
Trích xuất toàn bộ nội dung PDF sang thư mục Knowledge Base riêng biệt (không để lẫn lộn các tiêu chuẩn với nhau):
```bash
uv run C:/Users/kira7/.gemini/config/skills/pdf-to-kb/scripts/extract_pdf_to_kb.py \
  --pdf Projects/ESG/sources/<source_id>/pdf/<file_name>.pdf \
  --out Projects/ESG/kb/<collection_id> \
  --config Projects/ESG/sources/<source_id>/pdf/<file_name>.chapters.json \
  --backup \
  --source-id <source_id>
```
Kiểm tra báo cáo validation trên `stderr` để đảm bảo số dòng và heading đầy đủ.

---

## Giai đoạn 2: Khóa cứng Anchors & Định hình Đồ thị Tri thức

### Bước 3: Khóa cứng Anchors cố định trong Markdown (Anchor Stabilization)
Để đảm bảo đồ thị và tài liệu Markdown luôn đồng bộ, chèn thẻ HTML anchor cố định ngay trên dòng Heading bạn muốn liên kết:
```html
<a id="tcvn_principles_relevance"></a>
### 4.2  Tính liên quan
```
*Lưu ý*: `id` viết thường, dùng dấu gạch dưới, mô tả duy nhất vị trí điều khoản nghiệp vụ.

### Bước 4: Thiết lập Bản đồ Tri thức (`concept_map.json`)
Xác định danh mục thực thể tĩnh nghiệp vụ (`nodes`) phân tách theo các lớp (Standard, Principle, Requirement, BoundaryRule, ScopeRule, v.v...) và các mối liên kết chéo (`edges`). Lưu tệp cấu hình tại `Projects/ESG/graph/concept_map.json`.

> [!IMPORTANT]
> **Quy tắc tránh xung đột Unique ID (Namespace Separation)**:
> Do Neo4j áp dụng ràng buộc duy nhất trên `Concept.id`, khi thêm tài liệu mới cùng nguồn hoặc cấu trúc (như TCVN vs GHG Protocol), **bắt buộc phải gắn tiền tố namespace** vào các node ID mới (ví dụ: `tcvn_org_boundaries` thay vì `org_boundaries`). 
> Liên kết chúng lại bằng quan hệ tương đương `VERSION_OF` hoặc `ALTERNATIVE_TO`.

*   `doc_id` của node bắt buộc phải khớp chính xác với tên file Markdown (ví dụ: file `04_principles.md` -> `04_principles`).
*   `anchor` của node bắt buộc phải trùng khớp 100% với `id` của thẻ `<a id="..."></a>` đã chèn ở Bước 3.

### Bước 5: Chạy import và kiểm chứng liên kết
Thực thi script `import_concept_map.py` với đường dẫn thư mục cha `--kb-dir Projects/ESG/kb` để script tự động quét đệ quy các tài liệu và kiểm tra chéo các anchor liên kết thực tế trước khi nạp:
```bash
uv run C:/Users/kira7/.gemini/config/skills/pdf-to-kb/scripts/import_concept_map.py \
  --map Projects/ESG/graph/concept_map.json \
  --kb-dir Projects/ESG/kb \
  --project-id esg \
  --collection-id <collection_id> \
  --source-id <source_id> \
  --strict-citation \
  --prune-stale
```

---

## Giai đoạn 3: Kiểm tra và Truy vấn thông tin

### Bước 6: Xác thực Bằng chứng Vật lý (Citation Validation)
Chạy validator để kiểm tra xem mọi Node và Anchor trên đồ thị Neo4j có trỏ khớp 100% về file Markdown vật lý tương ứng trên đĩa hay không:
```bash
uv run C:/Users/kira7/.gemini/config/skills/pdf-to-kb/scripts/validate_citations.py \
  --kb-dir Projects/ESG/kb \
  --project-id esg \
  --strict-metadata
```
**Chỉ tiêu chấp nhận**: Bắt buộc `issue_count = 0`. Nếu có lỗi đứt gãy liên kết, không được chuyển sang chạy tầng RAG.

### Bước 7: Truy vấn kết hợp & Hỏi đáp Guardrail
* **Truy vấn thô**:
  ```bash
  uv run C:/Users/kira7/.gemini/config/skills/pdf-to-kb/scripts/query_graph.py \
    --search "<từ_khóa>" \
    --kb-dir Projects/ESG/kb \
    --project-id esg \
    --collection-id <collection_id> \
    --source-id <source_id>
  ```
* **Hỏi đáp kiểm chứng bằng chứng**:
  ```bash
  uv run scripts/answer_question.py \
    --question "<câu_hỏi>" \
    --kb-dir Projects/ESG/kb \
    --project-id esg \
    --collection-id <collection_id> \
    --source-id <source_id>
  ```

---
*Status: ACTIVE WORKFLOW*
