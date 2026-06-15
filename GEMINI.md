---
trigger: "always_on"
description: "Hiến pháp tối cao của hệ thống LS Auditor (Core Constitution)"
---

# LS AUDITOR - CORE CONSTITUTION (GEMINI.md)

Đây là bản Hiến pháp tối cao của hệ thống **LS Auditor**. Mọi hành động của Agent tại Workspace này phải tuân thủ các quy tắc cốt lõi về tính chính xác của dữ liệu và tính liêm chính của bằng chứng.

---

## I. NGUYÊN TẮC CỐT LÕI (CORE PRINCIPLES)

1. **Evidence Integrity:** Bằng chứng là sự sống còn. Mọi phát hiện sai phạm phải liên kết trực tiếp với dữ liệu gốc và có trích dẫn nguồn (citation) đầy đủ.
2. **Leakage-Centric:** Tập trung nhận diện các rò rỉ (tài chính, quy trình, thời gian) và quy đổi được về giá trị thiệt hại hoặc mức độ rủi ro.
3. **Systemic Thinking:** Nhận diện các lỗi hệ thống (Systemic Failures) thông qua tổng hợp các ngoại lệ, không chỉ tìm lỗi cá nhân.
4. **Generic Excellence:** Xây dựng công cụ/kỹ năng có tính tái sử dụng cao cho nhiều case audit khác nhau.

---

## II. QUY TRÌNH KHỞI ĐỘNG (BOOTSTRAP ORDER)

Agent bắt buộc thực hiện theo thứ tự:
1. Đọc **`Training/handbook/cases/backlog.md`** để nắm tiến độ và roadmap.
2. Tham chiếu các **Workflows** chuẩn trong `.agents/workflows/` và `.agents/workflows/auditor/`.
3. Kích hoạt các **Skills** tương ứng trong `.agents/skills/`.

---

## III. TIÊU CHUẨN KỸ THUẬT AUDIT

- **Data Integrity:** Không thay đổi dữ liệu gốc của khách hàng. Mọi chuẩn hóa phải thực hiện trên bản sao hoặc qua script ghi log rõ ràng.
- **Visual Evidence:** Sử dụng sơ đồ Mermaid (`markdown-mermaid-expert`) để trực quan hóa các kiểm soát quy trình.
- **Reporting Quality:** Báo cáo sắc bén, ngắn gọn, có số liệu minh chứng và trích dẫn trực tiếp tới dòng/trang của tài liệu PDF nguồn.

---

## IV. TIÊU CHUẨN LEGAL RAG / KNOWLEDGE GRAPH

Khi làm việc với các hệ thống RAG, PDF hoặc Đồ thị tri thức (ESG/Luật):
1. **Tuân thủ Workflow A-Z:** Bắt buộc sử dụng đúng quy trình tại `.agents/workflows/auditor/pdf-to-kb.md`.
2. **Citation First:** Mọi kết quả import đồ thị bắt buộc phải qua xác thực bằng chứng đạt `issue_count = 0` thông qua `validate_citations.py`.
3. **Phân biệt Namespace:** Các ID nút trên đồ thị của tài liệu khác nhau phải có tiền tố namespace riêng (ví dụ: `cbam_`, `tcvn_`) để tránh xung đột trên Neo4j.
4. **Không Suy diễn:** Câu trả lời của hệ thống RAG bắt buộc phải đi kèm trích dẫn gốc đầy đủ (`file_uri`, `anchor`, `source_pdf`, `page_number`). Nếu thiếu căn cứ, phải báo cáo rõ là không tìm thấy trong cơ sở tri thức.

---

## V. TIÊU CHUẨN MÔI TRƯỜNG KỸ THUẬT

1. **Quản lý Môi trường:** Chỉ sử dụng công cụ **`uv`** làm trình quản lý môi trường ảo (`.venv`) và thư viện. Không sử dụng `pip` hệ thống.
2. **Khai báo Thư viện:** Mọi thư viện phải được khai báo trong `pyproject.toml` qua lệnh `uv add`.
3. **Thực thi Script:** Mọi phân tích hoặc truy vấn phải chạy thông qua **`uv run <script>`** hoặc python của môi trường ảo, tuân thủ tiêu chuẩn lập trình AI-First.
4. **Tái sử dụng Mã nguồn:** Không tự viết script phân tích/truy vấn mới nếu các kỹ năng (Skills) hiện có trong dự án đã hỗ trợ các công cụ chuẩn tương đương.

---

**Status:** **ACTIVE AUDITOR RULES**
**Priority:** LEVEL 1 (OVERRIDE ALL)
