---
name: Query-Graph knowledge base
description: SOP truy vấn KB/Neo4j và trả lời có citation Markdown + PDF highlight
---

# Query Graph Workflow

## Mục tiêu

Dùng workflow này khi cần trả lời từ Knowledge Base/Neo4j và báo cáo phải có căn cứ kiểm chứng được.

Hệ thống bắt buộc phải:
- Quét toàn bộ thông tin liên quan trong Knowledge Base.
- Liên kết đầy đủ tất cả các bằng chứng tìm thấy.
- Xác định chính xác tọa độ (draw bbox) và tự động tạo ảnh minh chứng (evidence highlights) trực tiếp từ file PDF nguồn cho từng câu trích dẫn chi tiết.

Mỗi câu trả lời phải có:
- Kết luận ngắn.
- Quote nguyên văn từ KB.
- Link Markdown anchor.
- Link hoặc ảnh PDF highlight chính xác.
- Ghi rõ phần chưa đủ căn cứ nếu có.

## Lệnh Query

Luôn chạy một trong hai lệnh sau.

Tìm theo câu hỏi hoặc từ khóa:

```powershell
uv run .agents/skills/common/pdf-to-kb/scripts/query_legal_rag.py --search "<câu hỏi hoặc từ khóa>" --full-json
```

Tìm theo concept id nếu đã biết id:

```powershell
uv run .agents/skills/common/pdf-to-kb/scripts/query_legal_rag.py --id <concept_id> --full-json
```

Ví dụ:

```powershell
uv run .agents/skills/common/pdf-to-kb/scripts/query_legal_rag.py --search "scope 3" --full-json
```

```powershell
uv run .agents/skills/common/pdf-to-kb/scripts/query_legal_rag.py --id scope_3 --full-json
```

## Cách Lấy Bằng Chứng

Đọc trường `evidence_markdown` trong JSON output.

Mỗi item hợp lệ cần có:

- `quote`
- `markdown_link`
- `pdf_highlight_uri`
- `pdf_highlight_markdown`

Nếu item có `pdf_bbox_missing: true`, vẫn có thể dùng quote Markdown, nhưng phải ghi: `PDF highlight chưa resolve`.

Nếu item có `pdf_ambiguous: true`, chỉ dùng làm bằng chứng phụ và ghi: `PDF highlight cần kiểm tra lại do match chưa duy nhất`.

## Độ Sâu Báo Cáo

Với câu hỏi ngắn dạng khái niệm như `scope 2`, `scope 3`, `base year`, `verification`, không được chỉ trả định nghĩa một đoạn. Phải báo cáo đủ các mục sau nếu KB có bằng chứng:

- Định nghĩa hoặc bản chất.
- Phạm vi áp dụng hoặc điều kiện phân loại.
- Nghĩa vụ báo cáo/kế toán liên quan.
- Điểm loại trừ, ngoại lệ, hoặc lưu ý tránh hiểu sai.
- Ví dụ hoặc hệ quả thực tế, chỉ khi câu hỏi cần hoặc evidence trả về có căn cứ rõ.

Nếu `evidence_markdown` từ query đầu chưa đủ các mục trên, chạy thêm query bằng cùng wrapper, không tự bịa:

```powershell
uv run .agents/skills/common/pdf-to-kb/scripts/query_legal_rag.py --search "<khái niệm> reporting" --full-json
```

```powershell
uv run .agents/skills/common/pdf-to-kb/scripts/query_legal_rag.py --search "<khái niệm> not included" --full-json
```

```powershell
uv run .agents/skills/common/pdf-to-kb/scripts/query_legal_rag.py --search "<khái niệm> boundary" --full-json
```

Chỉ dùng kết quả có evidence hợp lệ. Nếu không tìm thấy, ghi ở phần `Giới hạn` là `KB chưa trả về bằng chứng đủ cho mục này`.

## Mẫu Trả Lời Bắt Buộc

```markdown
## Kết luận

<trả lời trực tiếp câu hỏi, bao gồm định nghĩa và các điều kiện chính có bằng chứng>

## Phạm vi và lưu ý

- <nghĩa vụ báo cáo/kế toán, nếu có evidence>
- <điểm loại trừ/ngoại lệ/lưu ý, nếu có evidence>
- <ví dụ hoặc hệ quả, nếu câu hỏi cần và có evidence>

## Bằng chứng

### Evidence 1: [<anchor>](<pdf_highlight_uri>)

> <quote nguyên văn>

Markdown: <markdown_link>

PDF highlight: <pdf_highlight_uri>

![PDF highlight](<pdf_highlight_uri>)

### Evidence 2: [<anchor nếu cần>](<pdf_highlight_uri nếu có>)

> <quote nguyên văn>

Markdown: <markdown_link>

PDF highlight: <pdf_highlight_uri>

![PDF highlight](<pdf_highlight_uri>)

## Giới hạn

<ghi ngắn phần chưa đủ căn cứ, mục coverage chưa tìm thấy, PDF highlight thiếu/ambiguous>
```

## Quy Tắc Báo Cáo

Chỉ dùng các claim được hỗ trợ bởi `evidence_markdown`.

Không tự thêm case study, ví dụ, số liệu hoặc diễn giải nếu câu hỏi không yêu cầu hoặc không có item evidence riêng.

Không viết `Không có giới hạn đáng kể` trừ khi có evidence trực tiếp chứng minh. Nếu chưa kiểm tra đầy đủ, ghi rõ phạm vi giới hạn của truy vấn.

Khi hỏi định nghĩa, ưu tiên item có anchor đúng khái niệm. Ví dụ với Scope 3, ưu tiên `scope_3`; chỉ dùng `scope_3_categories`, `dhl_outsourced_transportation`, `ikea_customer_transportation`, `wri_employee_commuting`, `abb_product_use_phase` khi câu hỏi yêu cầu danh mục hoặc case study.

Nếu không có evidence đủ `quote` và `markdown_link`, trả lời:

```text
Không tìm thấy căn cứ đủ trong KB để trả lời chắc chắn.
```

Nếu có Markdown evidence nhưng không có PDF highlight, trả lời được nhưng phải ghi:

```text
PDF highlight chưa resolve cho bằng chứng này.
```

## Build Lại PDF Citation Index

Chạy khi Markdown/anchor/PDF source thay đổi:

```powershell
uv run .agents/skills/common/pdf-to-kb/scripts/build_citation_index.py
```

Acceptance tối thiểu:

```text
bbox_resolve_rate >= 0.80
```

Baseline GHG hiện tại:

```text
bbox_resolve_rate = 0.966
```

## Import Graph

Chạy khi concept map hoặc Markdown anchor thay đổi:

```powershell
uv run .agents/skills/common/pdf-to-kb/scripts/import_legal_rag.py
```

Sau import, kiểm tra nhanh GHG scoped citation:

```powershell
uv run .agents/skills/common/pdf-to-kb/scripts/validate_citations.py --kb-dir Projects/ESG/kb --project-id esg --collection-id ghg_protocol --source-id ghg_protocol_corporate_standard --strict-metadata
```

Yêu cầu:

```text
issue_count = 0
```

---

Status: ACTIVE WORKFLOW
