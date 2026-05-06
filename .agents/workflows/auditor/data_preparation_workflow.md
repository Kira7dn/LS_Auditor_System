---
description: "Quy trình chuẩn bị, làm sạch và hợp nhất dữ liệu Audit"
---

# LS-WORKFLOW-DATA-PREPARATION

Workflow này hướng dẫn Agent cách làm sạch, chuẩn hóa và tạo bộ dữ liệu hợp nhất (Unified Dataset) từ các nguồn rời rạc.

## 1. Nạp Ngữ cảnh (Context Loading)
Agent PHẢI nạp các tri thức sau:
- [asset-index.json](../../../asset-index.json)
- [SCRIPT_STANDARDS.md](../../rules/SCRIPT_STANDARDS.md)

## 2. Thực thi Chuẩn bị (Data Execution)

### Bước 2.1: Thiết kế kiến trúc dữ liệu (Data Strategy)
Xác định cách Join các bảng dữ liệu dựa trên thư viện Schema.

// turbo
```bash
uv run .agents/skills/auditor/data-strategy/scripts/data_architect.py --cycle "[cycle-key]"
```

### Bước 2.2: Chuẩn hóa & Hợp nhất (Normalize & Join)
Sử dụng bộ công cụ `ls-auditor` để thực hiện chuẩn hóa và hợp nhất các bảng thành file `.parquet`.

// turbo
```bash
uv run ls-auditor join --spec "[join-spec-path]" --out "Projects/[case-id]/artifacts/unified_audit_dataset.parquet"
```

### Bước 2.3: Tổng hợp & Mô tả (Deep Summary)
**BẮT BUỘC:** Do người dùng không thể đọc trực tiếp định dạng `.parquet`, Agent phải sử dụng công cụ `inspect-parquet` để thực hiện phân tích tóm tắt bộ dữ liệu sau khi hợp nhất.

// turbo
```bash
uv run ls-auditor inspect-parquet --input "Projects/[case-id]/artifacts/unified_audit_dataset.parquet"
```

Báo cáo lại cho người dùng theo đúng cấu trúc của template **`.agents/templates/auditor/unified-dataset-summary.md`**:
- **📊 Tóm tắt Tổng thể (Global Stats):** Trích xuất thông số dòng và Key IDs.
- **🔍 Phân tích định lượng (Business Metrics):** Tính toán các chỉ số nghiệp vụ quan trọng từ Sum/Mean/Min/Max.
- **⚠️ Lỗ hổng kiểm soát (Control Gaps):** Nhận diện các điểm yếu về dữ liệu và quy trình (Nulls, Visibility).
- **📋 Data Preview:** Trình bày bảng dữ liệu mẫu.

## 3. Xác nhận & Bàn giao (Delivery)
Kết thúc workflow, Agent PHẢI bàn giao chính xác 02 Artifacts sau:

1.  **`unified_audit_dataset.parquet`**: Bộ dữ liệu hợp nhất chuẩn hóa phục vụ phân tích.
2.  **`unified-dataset-summary.md`**: Báo cáo tổng hợp duy nhất bao gồm:
    - Chất lượng dữ liệu & Khớp nối (Data Quality).
    - Phân tích định lượng (Business Metrics).
    - Lỗ hổng kiểm soát & Preview dữ liệu.

// turbo
```bash
# Dọn dẹp file trung gian
rm Projects/[case-id]/artifacts/*.json Projects/[case-id]/artifacts/*.txt
```

---
**Status:** ACTIVE HARDENED WORKFLOW (Antigravity Optimized)
**Target:** AI Agent (Executor)
**Owner:** Auditor Brain
