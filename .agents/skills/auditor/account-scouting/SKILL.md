---
name: account-scouting
description: Kỹ năng nghiên cứu bối cảnh khách hàng, phân tích chuỗi giá trị và dự báo rủi ro rò rỉ (Leakage) trước khi thực hiện Audit hiện trường.
---

# Account Scouting Skill

Kỹ năng này giúp Agent đóng vai trò một "Tiền trạm Audit", sử dụng các dữ liệu thứ cấp và nghiên cứu ngành để lập bản đồ rủi ro ban đầu cho khách hàng.

## When to Use This Skill

- Khi bắt đầu một dự án Audit mới cho một khách hàng/nhà máy chưa có dữ liệu lịch sử.
- Khi cần xây dựng giả thuyết rủi ro (Pain Hypothesis) để thuyết phục khách hàng.
- Khi chuẩn bị danh mục câu hỏi phỏng vấn cho các Stakeholders chính.

## Core Capabilities

### 1. Phân tích bối cảnh ngành (Industry Context)
- Nhận diện các rủi ro đặc thù theo ngành (Ví dụ: Ngành may mặc rủi ro ở vải vụn/phụ liệu; Ngành thực phẩm rủi ro ở hạn sử dụng và điều kiện bảo quản).
- So sánh hiệu suất (Benchmarking) của khách hàng với trung bình ngành.

### 2. Dự báo rò rỉ tài chính (Leakage Prediction)
- Sử dụng mô hình "Value Chain Leakage" để dự đoán tiền đang mất ở đâu (Tồn kho, mua hàng, vận hành hay phế phẩm).
- Ước tính quy mô Leakage dựa trên doanh thu và đặc điểm vận hành.

### 3. Lập bản đồ Stakeholder (Stakeholder Mapping)
- Xác định ai là người "chịu đau" nhất nếu rủi ro xảy ra.
- Tìm kiếm các mâu thuẫn lợi ích tiềm ẩn giữa các bộ phận (Ví dụ: Planning muốn tồn kho thấp, nhưng Production muốn tồn kho cao để an toàn).

## Key Patterns

### Pattern 1: Value Chain Risk Identification
Agent phải phân tích qua 4 lớp:
1. **Input**: Rủi ro từ nhà cung cấp, giá mua, chất lượng nguyên liệu.
2. **Process**: Rủi ro từ quy trình sản xuất, lãng phí, sai lỗi.
3. **Output**: Rủi ro từ thành phẩm, lưu kho, giao hàng.
4. **Support**: Rủi ro từ phê duyệt, chứng từ, hệ thống IT.

### Pattern 2: The "Wedge" Questioning
Cách đặt câu hỏi để mở khóa thông tin:
- "Nếu Kế hoạch sản xuất thay đổi bất ngờ, hệ thống PR/PO của anh/chị mất bao lâu để phản ứng?"
- "Làm thế nào để anh/chị biết được vật tư đang tồn trong kho là vật tư 'chết' hay vật tư dự phòng?"

## Quick Start (Example Thesis)

```markdown
## Account: Nhà máy May Mặc ABC
- **Hypothesis 1**: Rò rỉ lớn nhất nằm ở việc quản lý định mức vải (BOM vs Actual). 
- **Reasoning**: Ngành may có tỷ lệ hao hụt cao, nếu không kiểm soát chặt chẽ việc cấp phát vải thừa, giá vốn sẽ tăng 3-5%.
- **Evidence needed**: Đối chiếu lệnh sản xuất vs Phiếu xuất kho vs Số dư vải vụn.
```

## Best Practices
- **Be Skeptical**: Luôn giả định rằng quy trình thực tế khác xa với SOP.
- **Follow the Money**: Mọi rủi ro đều phải quy đổi được ra giá trị tài chính.
- **Use Proxy Data**: Nếu không có số liệu nội bộ, hãy dùng số liệu báo cáo tài chính của đối thủ cạnh tranh để dự phóng.

## Common Pitfalls
- **Hời hợt**: Chỉ liệt kê thông tin chung chung mà không đưa ra giả thuyết cụ thể.
- **Lạc quan**: Tin vào những lời quảng cáo về hệ thống ERP của khách hàng mà không kiểm chứng kẽ hở.
- **Thiếu trọng tâm**: Liệt kê quá nhiều rủi ro nhỏ mà bỏ qua những "tảng băng chìm" về dòng tiền.
