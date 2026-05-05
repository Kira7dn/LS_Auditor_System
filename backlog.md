# LS Audit Agent Stack - Implementation Backlog (Generic Framework)

Tài liệu này là danh sách chính thức các thành phần cần xây dựng cho hệ thống LS Audit Agent. Thiết kế hướng tới khả năng tái sử dụng (Generic) cho nhiều lớp bài toán audit khác nhau, với Case "Material Planning" làm tiêu chuẩn kiểm chứng đầu tiên.

---

## 1. NHÓM CÔNG CỤ (TOOLS)
*Các công cụ CLI thực thi kỹ thuật, đảm bảo tính chính xác và hiệu suất.*

### 1.1. Xử lý & Hợp nhất dữ liệu
- [ ] `normalize_cli`: Chuẩn hóa dữ liệu thô (Schema, Data Types, UoM).
- [ ] `join_cli`: Hợp nhất nhiều nguồn dữ liệu (Supports Fuzzy Matching).
- [ ] `validate_cli`: Kiểm tra tính toàn vẹn và chất lượng dữ liệu đầu vào.

### 1.2. Phân tích & Kiểm soát
- [ ] `compute_cli`: Thực thi tính toán Metric và Leakage dựa trên Spec.
- [ ] `rule_test_cli`: Kiểm tra các quy tắc tuân thủ và logic nghiệp vụ.
- [ ] `trace_cli`: Thu thập và đóng gói bằng chứng (Evidence bundles).

### 1.3. Tiện ích & Hiển thị
- [ ] `inspect_parquet`: Công cụ soi nội dung và cấu trúc dữ liệu Parquet.
- [ ] `chart_cli`: Tạo các biểu đồ dữ liệu (Pareto, Trend, Heatmap).
- [ ] `dashboard_builder_cli`: Tự động dựng giao diện tương tác (Streamlit/UI).

---

## 2. NHÓM KỸ NĂNG (SKILLS)
*Phương pháp luận nghiệp vụ giúp Agent suy luận và tạo Working Spec.*

### 2.0. Tiện ích cốt lõi (Core Utility)
- [x] `auditor-mermaid-expert/SKILL.md`: Chuyên gia thiết kế sơ đồ Mermaid chuẩn Audit (Tích hợp Engine).

### 2.1. Khám phá & Quy trình (Full Stack Updated)
- [x] `account-scouting/SKILL.md`: Phương pháp nghiên cứu bối cảnh và giả thuyết rò rỉ.
- [x] `process-mapping/SKILL.md`: Phương pháp bóc tách quy trình và xác định điểm rủi ro.

### 2.2. Dữ liệu & Phân tích
- [x] `data-strategy/SKILL.md`: Cách thiết kế mô hình dữ liệu Audit (Join/Normalize logic).
- [x] `variance-analysis/SKILL.md`: Tư duy đối chiếu "Kế hoạch vs Thực tế" và tìm sai lệch.

### 2.3. Giải pháp & Kết luận
- [x] `root-cause-synthesis/SKILL.md`: Cách tổng hợp từ Exception sang systemic failure.
- [x] `evidence-packaging/SKILL.md`: Tiêu chuẩn hóa hồ sơ phát hiện và bằng chứng.
- [x] `solution-design/SKILL.md`: Thiết kế giải pháp can thiệp, tính ROI và Roadmap.

---

## 3. NHÓM QUY TRÌNH (WORKFLOWS)
*Luồng vận hành phối hợp giữa Tool và Skill để tạo ra Artifact.*

### 3.1. Giai đoạn Discovery
- [x] `discovery_workflow.md`: Từ Input thô -> Account Thesis & Process Map.

### 3.2. Giai đoạn Execution
- [x] `data_preparation_workflow.md`: Từ dữ liệu thô -> Unified Audit Dataset.
- [x] `audit_execution_workflow.md`: Từ Dataset -> Risk Register & Evidence Pack.

### 3.3. Giai đoạn Delivery
- [x] `solution_packaging_workflow.md`: Từ Findings -> Solution Proposal & Price.
- [x] `final_report_workflow.md`: Tổng hợp toàn bộ Artifact thành báo cáo cuối cùng.

## 4. NHÓM BIỂU MẪU (TEMPLATES)
*Các mẫu Artifact chuẩn (Markdown) ứng với từng giai đoạn workflow.*

### 4.1. Giai đoạn Discovery
- [x] `account-thesis.md`: Mẫu giả thuyết rò rỉ và thông tin khách hàng.
- [x] `process-map.md`: Mẫu sơ đồ quy trình (kèm Mermaid).
- [x] `control-point-table.md`: Mẫu bảng danh mục các điểm kiểm soát.

### 4.2. Giai đoạn Execution
- [x] `data-quality-log.md`: Mẫu báo cáo chất lượng và chuẩn hóa dữ liệu.
- [x] `business-analysis-report.md`: Mẫu báo cáo phân tích định lượng & Metric.
- [x] `candidate-exceptions.md`: Mẫu danh sách các giao dịch bất thường dự kiến.
- [x] `control-gap-matrix.md`: Mẫu ma trận lỗ hổng kiểm soát.
- [x] `risk-register.md`: Mẫu danh mục rủi ro đã xác nhận.
- [x] `evidence-pack.md`: Mẫu hồ sơ bằng chứng chi tiết.

### 4.3. Giai đoạn Delivery
- [x] `intervention-thesis.md`: Mẫu lộ trình can thiệp và ROI.
- [x] `solution-proposal.md`: Mẫu đề xuất giải pháp và báo giá.
- [x] `final-audit-report.md`: Mẫu báo cáo tổng hợp kết quả Audit.
