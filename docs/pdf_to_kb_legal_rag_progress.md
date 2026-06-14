# Lộ trình Tiến độ PDF-to-KB Legal RAG

Cập nhật lần cuối: 2026-06-14

Tài liệu này theo dõi các tính năng cấp cao, trạng thái độ chín (maturity) và lộ trình phát triển của pipeline `pdf-to-kb`.

---

## 1. Trạng thái Độ chín của Tính năng

Hệ thống hỗ trợ lập chỉ mục đa tài liệu động, tự động nạp dữ liệu vào Neo4j, xác thực tính toàn vẹn của trích dẫn và kết xuất hình ảnh bằng chứng highlighted với độ chính xác cao.

| Phân hệ tính năng | Mức độ hoàn thiện | Ghi chú |
| :--- | :---: | :--- |
| **Trích xuất PDF sang Markdown KB** | 80% | Trích xuất văn bản có nhận diện cấu trúc layout, neo cố định (anchors) và metadata nguồn. |
| **Nạp dữ liệu & Phân vùng phạm vi (Scoping)** | 85% | Nhập dữ liệu an toàn (idempotent), băm nguồn và tự động loại bỏ các nút cũ (prune stale). |
| **Xác thực toàn vẹn trích dẫn** | 85% | Trực tiếp đối khớp các con trỏ đồ thị với các neo Markdown vật lý; xác thực metadata nghiêm ngặt. |
| **Tự động highlight PDF** | 85% | Giải quyết tọa độ bbox từ chỉ mục, tự động cắt ảnh highlight và nhúng visual footer nguồn. |
| **Truy vấn kết hợp (Graph + FTS)** | 85% | Truy vấn đồ thị nhiều bước (multi-hop) kết hợp với tìm kiếm toàn văn SQLite FTS5. Top-5 hit rate đạt 0.85 (GHG). |
| **Nạp dữ liệu hỗ trợ bởi LLM** | 70% | LLM trích xuất các thực thể/quan hệ có xác thực độ tin cậy và cấu trúc schema. |

---

## 2. Các Tính năng Cốt lõi Hiện tại

- **Giải quyết Preset Động:** Các lệnh wrapper (`query_legal_rag.py`, `answer_legal_rag.py`, `build_citation_index.py`) tự động nhận diện phạm vi (`collection_id`, `source_id`, `kb_dir`) qua từ khóa tìm kiếm (ví dụ: "CBAM") để tránh thiết lập mặc định cứng.
- **Đối khớp Highlight Cấp Đoạn văn:** Ưu tiên lập chỉ mục và highlight theo khối nội dung đoạn văn (`paragraph`) thay vì chỉ highlight tiêu đề điều khoản (`heading`) nhằm đảm bảo bằng chứng khớp chính xác câu trích dẫn.
- **Mở rộng Ngữ cảnh Highlight:** Tự động cắt trang PDF với khoảng đệm dọc mở rộng **`120.0` points** nhằm giữ lại đầy đủ ngữ cảnh xung quanh đoạn văn bản được bôi vàng.
- **Nhúng Footer Trực quan & Link Clickable:** Renders đường dẫn nguồn (`Source: <markdown_file>#<anchor>`) và phủ liên kết `file:///` tương tác lên cả ảnh PNG crop và tệp PDF xuất ra để người dùng click mở trực tiếp tệp Markdown gốc.
- **Chốt chặn Kiểm chứng (Guardrails):** Bộ máy truy vấn từ chối hoặc cảnh báo các tuyên bố (claims) không có trích dẫn vật lý thực tế đi kèm.

---

## 3. Lộ trình Phát triển (Roadmap)

### Các Cột mốc Đã hoàn thành
- [x] **Milestone 1: Nền tảng Đa tài liệu & Xác thực (100%):** Hoàn thiện import graph an toàn, bộ validator kiểm tra trích dẫn, xử lý alias đồng bộ và bộ câu hỏi đánh giá (20 câu).
- [x] **Milestone 2: Tự động Scoping & Highlight Ngữ cảnh (100%):** Hoàn thiện wrapper presets động, đối khớp bbox ưu tiên đoạn văn, mở rộng vùng crop, nhúng clickable link nguồn vào ảnh/PDF.

### Các Cột mốc Tiếp theo
- [ ] **Milestone 3: Tối ưu hóa Truy vấn & Mở rộng (Query Expansion):**
  - Mở rộng bộ câu hỏi đánh giá độ chính xác lên 50-100 câu hỏi thực tế.
  - Tích hợp kỹ thuật mở rộng truy vấn (query expansion) cho các thuật ngữ pháp lý/tuân thủ đồng nghĩa.
  - Thử nghiệm tích hợp thêm tầng truy vấn vector (Vector RAG) hoặc tầng xếp hạng lại (Reranking).
- [ ] **Milestone 4: Làm cứng Hệ thống cho Môi trường Production:**
  - Nâng cấp chỉ mục bằng chứng chi tiết tới cấp độ câu (sentence-level).
  - Tự động hóa bảng giám sát chất lượng đồ thị (phát hiện nút mồ côi, quan hệ yếu, lỗ hổng trích dẫn).
  - Tích hợp cơ chế phát hiện thay đổi (change detection) đối với các tệp Markdown nguồn.
  - Xuất tệp Manifest chi tiết cho mỗi lượt chạy giúp tái tạo toàn bộ hệ thống từ đầu một cách nhất quán.
