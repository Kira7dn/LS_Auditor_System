---
name: pdf-to-kb
description: >
  Chuyển đổi PDF học thuật/báo cáo sang Knowledge Base Markdown có cấu trúc heading,
  metadata citation và ánh xạ Neo4j graph cho RAG cần truy vết nguồn. Dùng PyMuPDF để đọc
  font size/style thực tế từ PDF, phát hiện chapter boundary, phân loại heading/body/callout/note-box,
  và xuất từng chapter thành file .md với YAML frontmatter. Kết quả phụ thuộc layout PDF và phải
  được validation trước khi dùng cho tác vụ pháp lý/kiểm toán có rủi ro cao.
---

## 0. Quy tắc tuân thủ & Thực thi bắt buộc của Agent (Agent Compliance)
> [!IMPORTANT]
> Đây là các rào cản hành vi bắt buộc mà Agent phải tuân thủ nghiêm ngặt khi kích hoạt Skill này để đảm bảo độ tin cậy pháp lý.

1.  **Xử lý dữ liệu trích xuất & Truy xuất tài liệu gốc (Retrieval Context Parsing & Verification):**
    *   Các tập lệnh CLI (như `query_graph.py`) đóng vai trò là công cụ truy xuất dữ liệu thô (Retrieval Engine) để cung cấp danh sách tham chiếu cấu trúc JSON.
    *   Agent có trách nhiệm phân tích (parse) danh sách này và **BẮT BUỘC phải sử dụng các đường dẫn tệp tin vật lý (`file_path` / `file_uri`) để truy xuất, mở trực tiếp tài liệu gốc nhằm đọc và kiểm chứng toàn bộ ngữ cảnh xung quanh** (không chỉ dựa vào chuỗi văn bản tóm tắt ngắn `matched_text` trong JSON).
    *   Mọi báo cáo kết luận cuối cùng phải được tổng hợp dựa trên ngữ cảnh đầy đủ đã được xác thực từ tài liệu gốc.
2.  **Bắt buộc trích dẫn dạng liên kết vật lý (Physical Citations):**
    *   Mọi câu trả lời trên giao diện chat và mọi báo cáo được viết ra đĩa cứng **BẮT BUỘC** phải chứa các đường dẫn liên kết Markdown mở được (`[link_text](file://...)`) trỏ thẳng tới tệp Markdown vật lý và thẻ anchor `<a id="..."></a>` nguồn trong Workspace hiện hành.
    *   Đường dẫn liên kết phải tuân thủ định dạng tương thích với hệ điều hành đang chạy của người dùng. Không bao giờ bọc liên kết trong dấu backticks (``` `link` ```) vì sẽ làm hỏng chức năng click trên giao diện IDE.
    *   Mỗi material claim phải có citation riêng khớp với đoạn chứng minh. Không dùng anchor rộng hoặc gần nhất để chứng minh cho case study/đoạn nằm ở chỗ khác.
    *   Nếu câu hỏi chỉ hỏi định nghĩa/điều kiện chính, không tự động mở rộng sang case study hoặc ví dụ trừ khi người dùng yêu cầu.
3.  **Tái sử dụng tối đa - Cấm tự viết code nháp trùng lặp (No Redundancy):**
    *   Trước khi viết bất kỳ đoạn code hoặc script tạm thời nào để truy vấn database hoặc xử lý tài liệu, Agent bắt buộc phải kiểm tra thư mục `scripts/` của Skill. Nếu đã có sẵn công cụ tương đương, **KHÔNG ĐƯỢC PHÉP** viết code mới.
4.  **Lưu trữ đúng cấu trúc thư mục dự án (Correct Placement):**
    *   Tất cả các báo cáo kết quả, báo cáo chất lượng RAG phải được lưu vào thư mục nghiệp vụ tương ứng đã được định nghĩa trong cấu trúc dự án hiện hành, tuyệt đối không lưu ở thư mục tạm `brain/` hay thư mục gốc (root).

---

## 1. Khi nào sử dụng (When to Use)

- Cần chuyển một file PDF (báo cáo, tiêu chuẩn, sách kỹ thuật) thành Knowledge Base Markdown.
- Cần hierarchy heading (`##`, `###`) đúng theo cấu trúc thực tế của tài liệu, không phải page markers.
- Cần bộ tài liệu RAG có citation rõ ràng để LLM đối chiếu kiểm tra thực tế.
- Cần ánh xạ tài liệu lên cơ sở dữ liệu đồ thị Neo4j mà không gặp lỗi ảo giác (Hallucination).

## 2. Năng lực cốt lõi (Core Capabilities)

- **Font-aware heading detection**: Phân loại tiêu đề H2/H3 và Note Box qua font size/bold; cần tuning/validation theo từng layout PDF.
- **Source citation metadata**: Ghi `source_id`, `source_pdf`, `page_start`, `page_end`, `content_hash` vào frontmatter khi trích xuất.
- **Stable Anchor Linking**: Hướng dẫn gắn thẻ neo HTML cố định `<a id="..."></a>` vào tài liệu.
- **Deterministic Section Graph**: Tự động sinh node Chapter/Section/ScopeRule từ markdown heading + anchor, có citation metadata.
- **Concept Map Validation**: Tự động hóa kiểm tra chéo (Linter) lỗi đứt gãy liên kết trước khi ghi Neo4j. `concept_map.json` là curated overlay/bổ sung, không phải nguồn graph duy nhất.
- **Ingestion Idempotency**: Tự động khởi tạo Schema Constraints, `MERGE` node/edge, gắn `import_batch_id`/`source_map_hash` và đánh dấu stale relationships.
- **Graph + Fulltext Retrieval**: Truy vấn Neo4j có multi-hop giới hạn và tìm kiếm văn bản cục bộ bằng SQLite FTS5/BM25, chưa phải semantic/vector search.
- **Prototype Quality Gates**: Với repo `LS_Auditor_System`, dùng thêm graph quality report, retrieval eval, answer guardrail và run manifest để đo chất lượng legal-grade prototype.

## 2.1. Layout chuẩn cho nhiều PDF/source

Với một bộ tài liệu gồm nhiều PDF, không đặt lẫn PDF, KB, concept map và report ở root project. Dùng layout:

```text
Projects/ESG/
  sources/<source_id>/
    pdf/
    raw/
    manifest.source.json
  kb/<collection>/
  graph/
    concept_map.json
    canonical_aliases.json
    citation_reports/
    import_reports/
    llm_candidates/
    quality_reports/
  eval/
  manifests/
  archive/
```

Mỗi PDF/bộ tài liệu mới phải có `source_id` ổn định và `manifest.source.json`. Markdown extract đi vào `kb/<collection>`, còn `concept_map.json` là expert overlay chung hoặc theo collection tùy thiết kế ontology.

Mọi bước ghi/đọc Neo4j phải có scope:

```text
--project-id <project_id>
--collection-id <collection_id>
--source-id <source_id>
```

GHG baseline hiện dùng:

```text
--project-id esg --collection-id ghg_protocol --source-id ghg_protocol_corporate_standard
```

Scoping v1 chưa đổi unique constraint `Concept.id`, nên trước khi import domain khác có ID trùng cần làm tiếp namespace/scoped-id migration.

## 3. Quy trình từng bước chi tiết (End-to-End Workflow)

Để hoàn tất quy trình từ một tài liệu PDF thô sang Đồ thị tri thức nghiệp vụ Neo4j mà không bị đứt chuỗi liên kết:

### Bước 1: Quét ranh giới chương (Scan Boundaries)
Chạy script để tự động phát hiện số lượng và ranh giới trang của các chương:
```bash
uv run .agents/skills/common/pdf-to-kb/scripts/scan_chapter_pages.py --pdf path/to/document.pdf
```
Kết quả sẽ tạo ra file `document.chapters.json`.

### Bước 2: Thiết lập cấu hình chương
Mở file JSON vừa tạo và định nghĩa trường `slug` (viết thường, không khoảng trắng, ví dụ: `principles`) và `title` tương ứng với mỗi chương.

### Bước 3: Trích xuất PDF thành Markdown KB
Chạy trình trích xuất chính thức để chuyển đổi nội dung:
```bash
uv run .agents/skills/common/pdf-to-kb/scripts/extract_pdf_to_kb.py --pdf document.pdf --out Projects/ESG/kb/ghg_protocol --config document.chapters.json --backup
```
*Lưu ý*: Script sẽ in báo cáo Validation (số dòng, số H2/H3) trên `stderr` để bạn đánh giá chất lượng. Dữ liệu thô của các chương được lưu dạng `NN_slug.md` (ví dụ: `01_principles.md`).
Mặc định script ghi metadata citation vào YAML frontmatter; có thể đặt `--source-id` để dùng ID nguồn ổn định.

### Bước 4: Khóa cứng Anchor tiêu đề trong Markdown (Anchor Stabilization)
Để liên kết nghiệp vụ từ đồ thị sang nội dung không bị gãy khi bạn viết lại tiêu đề hoặc cập nhật tài liệu, hãy mở các file Markdown vừa sinh ra và chèn thẻ HTML anchor cố định ngay trên dòng Heading bạn muốn trỏ tới:
```html
<a id="principles_relevance"></a>
## Relevance
```
*Quy chuẩn*: Mã `id` viết thường, dùng dấu gạch dưới, phản ánh duy nhất vị trí điều khoản.

### Bước 5: Khai báo Bản đồ Tri thức bổ sung (`concept_map.json`)
Xây dựng file cấu hình `concept_map.json` tại thư mục làm việc để bổ sung/ghi đè ánh xạ nghiệp vụ đã được sinh tự động từ Markdown. Tệp này gồm 4 lớp (Normative, Method, Evidence, Control):
```json
{
  "nodes": [
    {
      "id": "relevance",
      "label": "Principle",
      "name": "Relevance Principle",
      "doc_id": "principles",
      "anchor": "principles_relevance"
    }
  ],
  "edges": [
    {
      "from": "scope_2",
      "to": "relevance",
      "type": "APPLIES_PRINCIPLE"
    }
  ]
}
```
*Lưu ý*:
* `doc_id` must match file name slug (e.g. `01_principles.md` -> `principles`).
* `anchor` must match exactly 100% with the `<a id="..."></a>` HTML tag written in Step 4.

### Bước 6: Kiểm chứng chéo và nạp dữ liệu (Validation & Import)
Trong repo `LS_Auditor_System`, dùng wrapper preset thay vì tự ghép các flag import:
```bash
uv run .agents/skills/common/pdf-to-kb/scripts/import_legal_rag.py
```
Wrapper dùng `Projects/ESG/graph/concept_map.json` làm global expert map và `Projects/ESG/kb` làm root KB. Importer tự infer `collection_id` từ thư mục con của KB và `source_id` từ frontmatter Markdown.

Không truyền global `concept_map.json` cùng một KB con như `Projects/ESG/kb/ghg_protocol`. Chỉ gọi raw `import_concept_map.py` khi debug script lõi.

Script sẽ tự động:
1. Đọc tệp `.env` để kết nối database.
2. Sinh deterministic graph từ Markdown: mỗi chapter và mỗi heading có anchor trở thành node graph có citation.
3. Kiểm tra chéo: Quét từng Node trong `concept_map.json` -> Check file `*doc_id.md` trên đĩa cứng -> Tìm thẻ anchor HTML linh hoạt (`<a id="anchor"></a>` hoặc single quote/spacing tương đương).
4. Nếu phát hiện bất kỳ liên kết nào bị hỏng, script sẽ **hủy bỏ tiến trình và báo lỗi chi tiết** để bảo vệ tính toàn vẹn của đồ thị.
5. Nếu kiểm tra đạt, đẩy graph tự động và overlay `concept_map.json` lên Neo4j, gắn citation metadata, và đánh dấu/prune relationship stale nếu không còn active.
6. Dùng `--strict-citation` nếu muốn fail khi markdown thiếu `source_pdf`/page/hash metadata; dùng `--prune-stale` nếu muốn xóa edge/node auto stale thay vì chỉ đánh dấu.
7. Dùng `--no-auto-sections` nếu chỉ muốn import curated `concept_map.json` mà không sinh graph từ headings.

### Bước 7: Kiểm tra citation graph trước khi truy vấn
Chạy validator để kiểm tra node Neo4j có trỏ được về file Markdown và anchor thật hay không:
```bash
uv run .agents/skills/common/pdf-to-kb/scripts/validate_citations.py --kb-dir Projects/ESG/kb/ghg_protocol
 
# Chế độ nghiêm ngặt: coi thiếu source_pdf/page/hash là lỗi
uv run .agents/skills/common/pdf-to-kb/scripts/validate_citations.py --kb-dir Projects/ESG/kb/ghg_protocol --project-id esg --collection-id ghg_protocol --source-id ghg_protocol_corporate_standard --strict-metadata

# Kiểm tra riêng một batch import/concept_map cụ thể
uv run .agents/skills/common/pdf-to-kb/scripts/validate_citations.py --kb-dir Projects/ESG/kb/ghg_protocol --strict-metadata --source-map-hash <source_map_hash>
```
Mặc định output compact chỉ trả `issue_count` và sample. Dùng `--full-json` để xem toàn bộ issue.

### Bước 8: Bổ sung graph bằng LLM có kiểm soát
LLM được dùng để tạo graph bổ sung từ từng section Markdown đã có anchor và citation metadata. Không import trực tiếp kết quả LLM vào Neo4j nếu chưa qua bước validate. `concept_map.json` do chuyên gia tạo là lớp enhance/override cuối cùng, không phải bước approval thủ công cho từng candidate LLM.

```bash
# Dry-run không gọi API, dùng để kiểm tra pipeline JSONL
uv run .agents/skills/common/pdf-to-kb/scripts/extract_llm_entities.py --kb-dir Projects/ESG/kb/ghg_protocol --out Projects/ESG/graph/llm_candidates/llm_candidates.dryrun.jsonl --dry-run --limit-sections 3

# Gọi OpenAI API thật, nên chạy giới hạn trước để đo chất lượng
uv run .agents/skills/common/pdf-to-kb/scripts/extract_llm_entities.py --kb-dir Projects/ESG/kb/ghg_protocol --out Projects/ESG/graph/llm_candidates/llm_candidates.jsonl --limit-sections 10

# Validate evidence_quote, ontology, edge type, anchor và source metadata
uv run .agents/skills/common/pdf-to-kb/scripts/validate_llm_candidates.py --candidates Projects/ESG/graph/llm_candidates/llm_candidates.jsonl --kb-dir Projects/ESG/kb/ghg_protocol --out Projects/ESG/graph/llm_candidates/llm_candidates.validated.jsonl

# Kiểm tra tác động import/alias trước, không ghi Neo4j
uv run .agents/skills/common/pdf-to-kb/scripts/import_llm_candidates.py --candidates Projects/ESG/graph/llm_candidates/llm_candidates.validated.jsonl --aliases Projects/ESG/graph/canonical_aliases.json --project-id esg --collection-id ghg_protocol --source-id ghg_protocol_corporate_standard --dry-run

# Import LLM graph sau khi validated; alias map giúp redirect node LLM về canonical expert/section node
uv run .agents/skills/common/pdf-to-kb/scripts/import_llm_candidates.py --candidates Projects/ESG/graph/llm_candidates/llm_candidates.validated.jsonl --aliases Projects/ESG/graph/canonical_aliases.json --project-id esg --collection-id ghg_protocol --source-id ghg_protocol_corporate_standard

# Import lại global concept_map.json sau cùng để lớp chuyên gia override/enhance graph
uv run .agents/skills/common/pdf-to-kb/scripts/import_legal_rag.py
```
Nguyên tắc bắt buộc:
* Mỗi candidate phải có `evidence_quote` xuất hiện nguyên văn trong section text đã trích xuất.
* Node/edge LLM phải nằm trong ontology/whitelist edge hiện hành.
* `confidence` của từng node/edge phải đạt ngưỡng mặc định `0.5`; có thể chỉnh bằng `--min-confidence`.
* Citation của candidate kế thừa từ markdown section: `file_path`, `anchor`, `source_pdf`, `page_start`, `page_end`, `content_hash`.
* Dùng `canonical_aliases.json` để map node LLM trùng nghĩa về node chuyên gia/section; luôn chạy `--dry-run` trước khi import.
* Với tài liệu luật/chuẩn mực, chạy batch nhỏ trước để đo tỷ lệ pass. Sau khi import LLM, luôn import `concept_map.json` sau cùng vì đây là graph chuyên gia có quyền ưu tiên cao nhất.

### Bước 9: Truy vấn kết hợp đồ thị và văn bản vật lý (Graph + Fulltext Retrieve)
Chạy script truy vấn đồ thị để tìm kiếm Concepts và trích xuất dữ liệu tài liệu gốc. Công cụ kết hợp quan hệ Đồ thị từ Neo4j và tìm kiếm văn bản cục bộ bằng SQLite FTS5/BM25:
```bash
# Truy vấn chính xác theo Concept ID
uv run .agents/skills/common/pdf-to-kb/scripts/query_graph.py --id scope_3

# Tìm kiếm theo từ khóa liên quan trên cả Graph và Local KB
uv run .agents/skills/common/pdf-to-kb/scripts/query_graph.py --search "scope 3" --project-id esg --collection-id ghg_protocol --source-id ghg_protocol_corporate_standard

# Duyệt graph đa tầng có giới hạn
uv run .agents/skills/common/pdf-to-kb/scripts/query_graph.py --id scope_3 --depth 2 --mode paths --limit 10

# Tránh lẫn node legacy bằng cách lọc theo source_map_hash của lần import sạch
uv run .agents/skills/common/pdf-to-kb/scripts/query_graph.py --search "scope 3" --source-map-hash <source_map_hash>
```
*Lưu ý*: 
* Script luôn trả về cấu trúc Graph, danh sách dòng văn bản từ Markdown (`local_text_matches`) và `citations` dưới dạng JSON chuẩn.
* Mặc định output được rút gọn để tránh bị cắt trong CLI. Dùng `--full-json` khi cần xem toàn bộ relationships/paths/citations.
* Query compact có trường `citation_missing_fields`; nếu còn thiếu `source_pdf`, `page_start`, `page_end`, `content_hash` thì chưa đủ chuẩn citation pháp lý.
* Đây chưa phải semantic/vector search. Với truy vấn pháp lý, nếu không có citation phù hợp thì không được suy diễn ngoài KB.

### Bước 10: Kiểm chất lượng prototype legal-grade
Trong repo `LS_Auditor_System`, chạy các script bổ trợ sau để đo và khóa chất lượng trước khi xem hệ thống là đủ dùng:
```bash
# Graph quality: duplicate, generic LLM node, orphan requirement, citation gaps
uv run .agents/skills/common/pdf-to-kb/scripts/analyze_graph_quality.py --env .env --out-dir Projects/ESG

# Retrieval eval: đo hit-rate trên bộ câu hỏi vàng ban đầu
uv run .agents/skills/common/pdf-to-kb/scripts/run_retrieval_eval.py --questions Projects/ESG/eval/retrieval_questions.jsonl --kb-dir Projects/ESG/kb/ghg_protocol --env .env --project-id esg --collection-id ghg_protocol --source-id ghg_protocol_corporate_standard --top-k 5

# Answer guardrail: chỉ trả lời bằng cited evidence, refuse nếu thiếu căn cứ
uv run .agents/skills/common/pdf-to-kb/scripts/answer_question.py --question "Scope 3 là gì?" --kb-dir Projects/ESG/kb/ghg_protocol --env .env --project-id esg --collection-id ghg_protocol --source-id ghg_protocol_corporate_standard

# Run manifest: ghi lại hashes, metrics, graph/eval/citation summary
uv run .agents/skills/common/pdf-to-kb/scripts/write_run_manifest.py --env .env --project-id esg --collection-id ghg_protocol --source-id ghg_protocol_corporate_standard --kb-dir Projects/ESG/kb/ghg_protocol --concept-map Projects/ESG/graph/concept_map.json --aliases Projects/ESG/graph/canonical_aliases.json --graph-quality Projects/ESG/graph/quality_reports/graph_quality_report.json --citation-validation Projects/ESG/graph/citation_reports/citation_validation.latest.json --retrieval-eval Projects/ESG/eval/retrieval_eval_report.json --alias-apply-report Projects/ESG/graph/import_reports/canonical_aliases_apply_report.json --out Projects/ESG/manifests/run_manifest.latest.json
```
Acceptance hiện tại cho GHG KB:
* `validate_citations.py --strict-metadata`: `issue_count = 0`
* Retrieval eval: `20` câu, Top-5 hit rate `0.85`, citation completeness `1.0`
* Unit/static tests: `16 passed`
* Answer guardrail không trả material claim nếu thiếu citation đầy đủ.

---

## 4. Công cụ đi kèm (Local Assets)

| Script | Mô tả |
|--------|-------|
| `extract_pdf_to_kb.py` | **Main script**: Trích xuất PDF → KB Markdown |
| `scan_chapter_pages.py` | Phát hiện ranh giới chapter của PDF |
| `debug_pdf_page.py` | Xem chi tiết độ lớn font và kiểu style của 1 trang PDF |
| `import_concept_map.py` | Trình xác thực tĩnh (10 quy tắc) và import đồ thị Neo4j |
| `extract_llm_entities.py` | Dùng OpenAI API để đề xuất node/edge candidate theo từng anchored section |
| `validate_llm_candidates.py` | Kiểm tra candidate LLM có evidence/citation/ontology hợp lệ trước import |
| `import_llm_candidates.py` | Import candidate LLM đã qua validator vào Neo4j với provenance |
| `query_graph.py` | Truy vấn Concept, ánh xạ mối quan hệ và trích dẫn tài liệu |
| `validate_citations.py` | Kiểm tra graph node có trỏ đúng file Markdown/anchor/citation metadata |
| `analyze_graph_quality.py` | Tạo report chất lượng graph: duplicate, generic LLM node, overlap, orphan, citation gaps |
| `apply_canonical_aliases.py` | Dry-run/apply canonical aliases trong Neo4j; destructive merge chỉ khi dùng `--apply` |
| `run_retrieval_eval.py` | Chạy eval set và xuất hit-rate/citation completeness |
| `answer_question.py` | Answer prototype có guardrail: chỉ trả lời bằng citations đầy đủ, refuse nếu thiếu căn cứ |
| `write_run_manifest.py` | Ghi manifest audit cho một vòng hardening |
| `import_legal_rag.py` | Wrapper chạy import concept map/RAG graph theo preset dự án |
| `query_legal_rag.py` | Wrapper truy vấn graph/local text theo preset dự án |
| `answer_legal_rag.py` | Wrapper trả lời câu hỏi kèm bằng chứng theo preset dự án |
| `build_citation_index.py` | Tạo index để mapping markdown anchor với tọa độ trang/bbox trên PDF nguồn |
| `build_pdf_citation_index.py` | Lớp thư viện lõi để scan và build chỉ mục trích dẫn từ PDF |
| `pdf_bbox_citations.py` | Thư viện tính toán tọa độ bbox và trích xuất/dynamic search cho bằng chứng PDF |
| `render_pdf_highlights.py` | Vẽ highlight và sinh ảnh minh chứng PNG từ tọa độ bbox |
| `convert_docx_to_md.py` | Chuyển đổi file DOCX sang cấu trúc Markdown có anchor tương ứng |
| `convert_html_to_md.py` | Chuyển đổi file HTML sang cấu trúc Markdown tương tự |
| `font_config.json` | Tệp cấu hình thresholds font size để tuning |

