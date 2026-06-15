---
name: Query-Graph knowledge base
description: SOP truy vấn KB/Neo4j và trả lời có citation Markdown + PDF highlight
---

# Query Graph Workflow

## 1. Mục tiêu & Yêu cầu Bằng chứng
Sử dụng workflow này để truy vấn Knowledge Base/Neo4j. Hệ thống bắt buộc tự động xác định tọa độ (draw bbox) và tạo ảnh minh chứng (evidence highlights) từ PDF nguồn.

Mỗi phản hồi phải trích xuất từ `evidence_markdown` trong JSON output:
- **Thuộc tính bắt buộc**: `quote`, `markdown_link`, `pdf_highlight_uri`, `pdf_highlight_markdown`.
- **Xử lý ngoại lệ**:
  - Nếu `pdf_bbox_missing: true`: ghi `PDF highlight chưa resolve cho bằng chứng này`.
  - Nếu `pdf_ambiguous: true`: ghi `PDF highlight cần kiểm tra lại do match chưa duy nhất`.

## 2. Câu lệnh Thực thi

### Truy vấn thông tin:
```powershell
# Tìm theo từ khóa hoặc câu hỏi
uv run .agents/skills/common/pdf-to-kb/scripts/query_legal_rag.py --search "<câu hỏi hoặc từ khóa>" --full-json

# Tìm theo Concept ID (ví dụ: scope_3)
uv run .agents/skills/common/pdf-to-kb/scripts/query_legal_rag.py --id <concept_id> --full-json
```

### Điền khuyết thông tin (nếu query đầu chưa đủ các khía cạnh định nghĩa/phạm vi/ngoại lệ):
```powershell
uv run .agents/skills/common/pdf-to-kb/scripts/query_legal_rag.py --search "<khái niệm> reporting/not included/boundary" --full-json
```

### Phân vùng Dữ liệu (Presets):
Hệ thống tự động nhận diện phân vùng tri thức để truy vấn dựa trên từ khóa trong `--search` hoặc `--id`:
- **`cbam`**: CBAM Guidance.
- **`nd06`**: Nghị định 06/2022/NĐ-CP.
- **`qd226`**: Quyết định 226/QĐ-BTNMT.
- **`14064-1` / `14064_1`**: ISO 14064-1:2025.
- **`14064-2` / `14064_2`**: ISO 14064-2.
- **`14067`**: ISO 14067.
- **`csrd` / `esrs`**: ESRS CSRD Guide.
- **`samsung`**: Samsung Sustainability Report 2025.
- **`ghg` / `scope`**: GHG Protocol Corporate Standard (Mặc định nếu không trùng từ khóa nào khác).


*Mẹo: Bạn có thể cưỡng chế chọn phân vùng cụ thể bằng cách thêm `--preset <tên_preset>` (ví dụ: `--preset qd226`).*

## 3. Quy Tắc Trình Bày & Mẫu Báo Cáo


Báo cáo kết quả phải tuân thủ đúng cấu trúc tại [query-graph-report.md](file:///d:/BusinessAnalyze/LS/LS_Auditor_System/.agents/templates/auditor/query-graph-report.md).

### Quy tắc nghiêm ngặt:
- **Độ sâu**: Báo cáo khái niệm phải bao gồm: Định nghĩa, Phạm vi áp dụng, Nghĩa vụ kế toán, Ngoại lệ/Loại trừ, và Ví dụ thực tế (chỉ khi có bằng chứng). Nếu thiếu, ghi rõ ở phần **Giới hạn** là `KB chưa trả về bằng chứng đủ cho mục này`.
- **Cấm tự diễn giải**: Không tự ý thêm case study, ví dụ, số liệu hay diễn giải ngoài phạm vi `evidence_markdown`.
- **Xác thực giới hạn**: Không ghi "Không có giới hạn đáng kể" trừ khi có bằng chứng trực tiếp chứng minh.
- **Không có bằng chứng**: Trả về `Không tìm thấy căn cứ đủ trong KB để trả lời chắc chắn` nếu không có đủ `quote` và `markdown_link`.
- **Ưu tiên khái niệm**: Khi hỏi định nghĩa, ưu tiên các item có anchor chuẩn khái niệm (ví dụ: `scope_3` thay vì các category chi tiết như `scope_3_categories`, trừ khi câu hỏi yêu cầu cụ thể).

## 4. Đồng bộ & Kiểm tra Graph (Khi dữ liệu nguồn thay đổi)

```powershell
# 1. Build lại chỉ mục tọa độ PDF (Yêu cầu bbox_resolve_rate >= 0.80, baseline GHG là 0.966)
uv run .agents/skills/common/pdf-to-kb/scripts/build_citation_index.py

# 2. Import lại đồ thị vào Neo4j
uv run .agents/skills/common/pdf-to-kb/scripts/import_legal_rag.py

# 3. Xác thực tính toàn vẹn (Yêu cầu issue_count = 0)
uv run .agents/skills/common/pdf-to-kb/scripts/validate_citations.py --kb-dir Projects/ESG/kb --project-id esg --collection-id ghg_protocol --source-id ghg_protocol_corporate_standard --strict-metadata
```

---
Status: ACTIVE WORKFLOW
