---
name: auditor-mermaid-expert
description: Chuyên gia thiết kế sơ đồ Mermaid chuẩn Audit. Tích hợp Engine tự động tạo style cho Flowchart, ERD và C4 Diagrams.
---

## 1. Khi nào sử dụng (When to Use)
- Cần vẽ quy trình nghiệp vụ (Flowcharts).
- Cần thiết kế kiến trúc dữ liệu Audit (ERD).
- Cần mô hình hóa kiến trúc hệ thống cấp cao (C4 Diagrams).
- Cần mô hình hóa rủi ro và các điểm kiểm soát.

## 2. Năng lực cốt lõi (Core Capabilities)
- **Auto-Styling**: Sử dụng `scripts/mermaid_expert_helper.py` để tự động gán màu sắc có ý nghĩa (Vàng: Control, Đỏ: Risk, Xanh: Actor).
- **Modern Visual Styles**: Hỗ trợ `look: handDrawn` cho giai đoạn discovery và `layout: elk` cho các quy trình phức tạp.
- **Config Blocks**: Tích hợp khối cấu hình `---config: ... ---` để tùy chỉnh theme đồng bộ.
- **Audit Compliance**: Sơ đồ phải hiển thị rõ các mã ID điểm kiểm soát (CP-xx).

## 3. Quy tắc "Expert" (Patterns)
- **Pattern 1: Color Semantics (Dark Mode — Chuẩn chính thức)**:
    ```
    classDef actor   fill:#0d2d6e,stroke:#60a5fa,stroke-width:2px,color:#e0f2fe;
    classDef control fill:#3d2d00,stroke:#fbbf24,stroke-width:2px,stroke-dasharray: 5 5,color:#fef3c7;
    classDef risk    fill:#3d0a0a,stroke:#f87171,stroke-width:2px,color:#fecaca;
    classDef system  fill:#052e16,stroke:#4ade80,stroke-width:2px,color:#bbf7d0;
    ```
    - **Actor** (navy `#0d2d6e` / xanh dương `#60a5fa`): Tác nhân người — VVB, Khách hàng.
    - **Control** (vàng tối `#3d2d00` / amber `#fbbf24`, nét đứt): Điểm kiểm soát CP-xx.
    - **Risk** (đỏ sẫm `#3d0a0a` / đỏ `#f87171`): Rủi ro rò rỉ, nguy hiểm.
    - **System** (xanh lá đậm `#052e16` / `#4ade80`): Hệ thống kỹ thuật, dịch vụ Cloud.
- **Pattern 2: Visual Fidelity**:
    - Sử dụng `look: handDrawn` khi thảo luận sơ bộ với khách hàng để tạo cảm giác thân thiện.
    - Sử dụng `look: classic` cho báo cáo Audit chính thức xuất PDF.

## 4. Công cụ đi kèm (Local Assets)
- **Script**: `scripts/mermaid_expert_helper.py` (Engine tạo mã Mermaid chuẩn hiện đại).
- **CLI**: Sử dụng `mmdc -i input.mmd -o output.png` để xuất ảnh chất lượng cao.

## 5. Pro Tips
- 💡 Sử dụng `%%` để ghi chú logic kiểm soát bên trong sơ đồ.
- 💡 Chia nhỏ sơ đồ C4 thành các cấp độ Context, Container, và Component để quản lý độ phức tạp.
- 💡 Luôn gán `classDef` hoặc sử dụng `config` block để đảm bảo tính thẩm mỹ "Premium".

## 6. Lưu ý (Pitfalls)
- Không vẽ sơ đồ quá 15 nodes trong một file Markdown để đảm bảo khả năng hiển thị.
- Luôn kiểm tra tính tương thích của renderer khi sử dụng các tính năng mới như `elk` layout.

## 7. Assistant Contract
- **Trigger**: Khi cần trực quan hóa process, control gaps, evidence flow hoặc report summary.
- **Input**: node list, connection list, diagram type.
- **Output**: Mermaid code with audit styling.
- **Artifacts**: `Projects/<case_id>/artifacts/*.mmd` hoặc nhúng trong report.
- **Failure Modes**: thiếu control/risk labels, sơ đồ quá dày, không có legend.
- **Acceptance Checklist**: sơ đồ có actors, controls, risks, data/system nodes và đọc được ở cấp quản lý.
