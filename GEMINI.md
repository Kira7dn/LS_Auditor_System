---
trigger: "always_on"
description: "Hiến pháp tối cao của hệ thống LS Auditor (Core Constitution)"
---

# LS AUDITOR - CORE CONSTITUTION (GEMINI.md)

Chào Agent, đây là bản Hiến pháp tối cao của hệ thống **LS Auditor**. Mọi hành động của bạn tại Workspace này phải tuân thủ các quy tắc về tính chính xác của dữ liệu và tính liêm chính của bằng chứng.

---

## I. NGUYÊN TẮC CỐT LÕI (CORE PRINCIPLES)

1. **Evidence Integrity:** Bằng chứng là sự sống còn. Mọi phát hiện sai phạm phải được liên kết trực tiếp với dữ liệu gốc và không được phép suy diễn thiếu căn cứ.
2. **Leakage-Centric:** Mục tiêu tối thượng là nhận diện rò rỉ (tài chính, quy trình, thời gian). Mọi phân tích phải quy đổi được về giá trị thiệt hại hoặc rủi ro.
3. **Systemic Thinking:** Đừng chỉ tìm lỗi cá nhân. Hãy tập trung nhận diện các lỗi hệ thống (Systemic Failures) thông qua việc tổng hợp các ngoại lệ (Exceptions).
4. **Generic Excellence:** Xây dựng các công cụ và kỹ năng có tính tái sử dụng cao, áp dụng được cho nhiều case audit khác nhau.

---

## II. QUY TRÌNH KHỞI ĐỘNG (BOOTSTRAP ORDER)

Để đảm bảo thực thi đúng quy trình nghiệp vụ, Agent **BẮT BUỘC** thực hiện bootstrap theo thứ tự:

1. Đọc **`Training/handbook/cases/backlog.md`** để nắm roadmap và tiến độ các task.
2. Tham chiếu các **Workflows** trong `.agents/workflows/` khi task liên quan đến quy trình chuẩn toàn hệ thống.
3. Tham chiếu các **`Workflows`** trong `.agents/workflows/auditor/` ứng với giai đoạn hiện tại (Discovery, Execution, hoặc Delivery).
4. Kích hoạt các **`Skills`** tương ứng trong `.agents/skills/` (ưu tiên `auditor/`, `common/`, và skill domain-specific được nhắc trực tiếp).

---

## III. TIÊU CHUẨN KỸ THUẬT AUDIT (AUDIT STANDARDS)

- **Data Integrity:** Tuyệt đối không thay đổi dữ liệu gốc của khách hàng. Mọi thao tác chuẩn hóa phải được thực hiện trên bản sao hoặc thông qua các script log rõ ràng.
- **Visual Evidence:** Sử dụng `auditor-mermaid-expert` để trực quan hóa mọi quy trình và điểm kiểm soát. Sơ đồ phải rõ ràng, dễ hiểu cho cả cấp quản lý.
- **Evidence Dossier:** Mọi Findings phải được đóng gói vào `Evidence Pack` với đầy đủ mã ID giao dịch, timestamp và mô tả sai lệch.
- **Reporting Quality:** Tuân thủ kỹ năng `writing-clearly-and-concisely`. Báo cáo phải sắc bén, đi thẳng vào vấn đề và có số liệu chứng minh.

---

## IV. TIÊU CHUẨN LEGAL RAG / KNOWLEDGE GRAPH

Khi task liên quan đến PDF, Knowledge Base, RAG, Neo4j graph, chuẩn mực ESG/GHG/luật hoặc tài liệu có rủi ro pháp lý:

1. **Bắt buộc dùng workflow A-Z:** Đọc `.agents/workflows/auditor/pdf-to-kb.md` và skill `.agents/skills/common/pdf-to-kb/SKILL.md` trước khi extract/import/query một bộ tài liệu mới.
2. **Citation First:** Không coi kết quả là đạt nếu `validate_citations.py --strict-metadata` chưa trả `issue_count = 0`.
3. **Expert Overlay Priority:** `concept_map.json` do chuyên gia tạo là lớp enhance/override cuối cùng; sau LLM import phải import lại `concept_map.json`.
4. **Multi-source Layout:** Với `Projects/ESG`, PDF nguồn đặt trong `sources/<source_id>/`, Markdown extract đặt trong `kb/<collection>/`, graph overlay/report đặt trong `graph/`, manifest đặt trong `manifests/`. Không đặt thêm PDF/report sinh mới trực tiếp ở root project.
5. **Graph Scope:** Mọi import/query/validation phải truyền hoặc dùng mặc định `project_id`, `collection_id`, `source_id`. Với GHG hiện tại: `project_id=esg`, `collection_id=ghg_protocol`, `source_id=ghg_protocol_corporate_standard`.
6. **LLM Is Candidate, Not Truth:** LLM chỉ sinh candidate graph. Candidate phải qua validator evidence/citation/ontology/confidence trước khi import.
7. **Canonicalization Discipline:** Dùng `canonical_aliases.json`; luôn dry-run trước khi apply alias. Chỉ apply alias chắc chắn, giữ `deferred_candidates` để review ontology.
8. **Quality Gates:** Với prototype legal-grade, phải có graph quality report, retrieval eval, answer guardrail và run manifest.
9. **Answer Guardrail:** Không trả lời claim thiếu citation đầy đủ (`file_uri`, `anchor`, `source_pdf`, `page_start`, `page_end`, `content_hash`). Nếu thiếu căn cứ, trả lời rõ là không tìm thấy căn cứ đủ trong KB.
10. **Current GHG KB Baseline:** GHG KB hiện đạt prototype với `171` Concept nodes, `142` relationships, citation issues `0`, retrieval eval `20` câu, Top-5 hit rate `0.85`, citation completeness `1.0`, tests `16 passed`.

---

## V. CẬP NHẬT & TỐI ƯU (HARDENING)

1. **Template Evolution:** Chủ động cập nhật các mẫu Template trong `.agents/templates/auditor/` dựa trên kinh nghiệm thực tế từ các case study.
2. **Skill Sharpening:** Cải tiến các logic trong `scripts/` của kỹ năng để tăng độ chính xác của việc phát hiện bất thường.
3. **Workflow Maintenance:** Duy trì `GEMINI.md`, global workflows và skill docs luôn phản ánh đúng quy trình hiện hành.

---

## VI. TIÊU CHUẨN MÔI TRƯỜNG KỸ THUẬT (TECHNICAL STANDARDS)

1. **Environment Management:** Workspace sử dụng **`uv`** làm công cụ quản lý môi trường và thư viện duy nhất. Tuyệt đối không sử dụng `pip` hoặc `conda`.
2. **Dependency Definition:** Mọi thư viện phải được khai báo trong `pyproject.toml` thông qua lệnh `uv add`. Không sử dụng các file `requirements.txt` rời rạc.
3. **Execution Discipline:** Mọi Script phân tích phải được thực thi thông qua lệnh **`uv run <script_path>`**. Script phải tuân thủ nghiêm ngặt bộ tiêu chuẩn tại [SCRIPT_STANDARDS.md](./.agents/rules/SCRIPT_STANDARDS.md).
4. **Hermetic Environment:** Tuyệt đối không cài đặt thư viện vào Python hệ thống. Mọi tài sản kỹ thuật phải nằm trong Virtual Environment (`.venv`) của dự án.
5. **Anti-Redundancy & Skill-First Discipline:** Tuyệt đối không tự viết script phân tích/truy vấn mới (ví dụ: truy vấn Neo4j/Cypher, xử lý PDF) nếu các file script chuẩn của bộ Skills (như `query_graph.py`, `validate_citations.py`...) đã có sẵn và hỗ trợ chức năng tương đương. Agent bắt buộc phải đọc và kiểm tra tài liệu của Skill trước khi thực hiện code mới.

---

**Status:** **ACTIVE AUDITOR RULES**
**Priority:** LEVEL 1 (OVERRIDE ALL)
