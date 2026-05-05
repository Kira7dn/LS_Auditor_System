---
name: variance-analysis
description: Kỹ năng phân tích sai lệch, tính toán rò rỉ tài chính (Leakage) và nhận diện các mẫu hành vi bất thường trong dữ liệu giao dịch.
---

# Variance Analysis Skill

Kỹ năng này là trung tâm của việc thực thi Audit, giúp Agent chuyển đổi các con số chênh lệch thành các "Phát hiện Audit" (Audit Findings) có giá trị kinh tế.

## When to Use This Skill

- Khi đã có bộ dữ liệu hợp nhất (Unified Dataset).
- Khi cần thực hiện các bài đối chiếu (Reconciliation) giữa Plan vs Actual hoặc Input vs Output.
- Trước khi đóng gói các phát hiện vào `candidate-exceptions.md`.

## Core Capabilities

### 1. Phân tích chênh lệch định lượng (Quantitative Variance)
- Tính toán chênh lệch Số lượng (Quantity Variance): So sánh nhu cầu thực tế (BOM/Plan) với lượng đặt mua (PR/PO).
- Tính toán chênh lệch Giá (Price Variance): So sánh đơn giá mua với giá thị trường hoặc giá lịch sử.
- Tính toán chênh lệch Thời gian (Lead-time Variance): So sánh thời gian giao hàng cam kết vs thực tế.

### 2. Định lượng rò rỉ tài chính (Leakage Quantification)
- Tính toán giá trị "Vốn kẹt" (Capital Lock-up) do tồn kho quá mức.
- Tính toán giá trị "Thất thoát trực tiếp" do đơn giá cao hoặc mua hàng không qua phê duyệt.
- Ước tính ROI nếu triệt tiêu được các sai lệch này.

### 3. Phân tích mẫu hành vi (Behavioral Profiling)
- Nhận diện hành vi "Đặt hàng phòng thủ" (Buffer-building): Bộ phận sản xuất luôn yêu cầu nhiều hơn nhu cầu thực tế.
- Nhận diện hành vi "Mua hàng khẩn cấp" (Emergency Buying): Thường xuyên mua lẻ với giá cao dù có thể mua sỉ theo kế hoạch.

## Key Patterns

### Pattern 1: The "90-Day Rule" for Inventory
Agent phải tìm các vật tư có:
- [Số lượng tồn kho] / [Mức tiêu thụ trung bình tháng] > 3.
- Kết luận: Tồn kho dư thừa trên 90 ngày sử dụng -> Rủi ro đọng vốn.

### Pattern 2: The "Split-PO" Detection
Tìm các giao dịch có tổng giá trị lớn bị chia nhỏ thành nhiều PO dưới hạn mức phê duyệt để bypass quy trình duyệt của cấp cao hơn.

## Quick Start (Leakage Formula)

```python
# Ví dụ công thức tính Leakage do đặt dư vật tư
excess_qty = actual_purchased_qty - required_qty_by_bom
leakage_value = excess_qty * unit_price
print(f"Giá trị rò rỉ: {leakage_value}")
```

## Best Practices
- **Context is King**: Không phải chênh lệch nào cũng là sai phạm. Luôn tìm hiểu xem có sự kiện đặc biệt nào (Ví dụ: Lễ tết, Đứt gãy chuỗi cung ứng) giải thích cho sự chênh lệch đó không.
- **Pareto Principle**: Tập trung vào 20% mã vật tư gây ra 80% giá trị rò rỉ.
- **Trend over Snapshot**: Một lần sai lệch có thể là tai nạn, nhưng sai lệch liên tục trong 6 tháng là một lỗi hệ thống.

## Common Pitfalls
- **Nhầm lẫn đơn vị tính**: Dẫn đến giá trị rò rỉ bị tính khống lên hàng triệu đô la.
- **Bỏ qua Inventory On-hand**: Chỉ nhìn vào PO mà không nhìn vào kho hiện tại dẫn đến kết luận sai về nhu cầu mua thêm.
- **Thiếu bằng chứng đối chiếu**: Đưa ra kết luận rò rỉ mà không chỉ ra được chứng từ nào (PO No nào, PR No nào) gây ra lỗi đó.

## Assistant Contract
- **Trigger**: Khi có unified dataset và cần lượng hóa leakage.
- **Input**: dataset path, metric spec, thresholds.
- **Output**: leakage analysis JSON, candidate exceptions.
- **Artifacts**: `Projects/<case_id>/artifacts/leakage_analysis.json`, `candidate-exceptions.md`.
- **Failure Modes**: sai đơn vị tính, thiếu actual/plan fields, threshold không phù hợp ngữ cảnh.
- **Acceptance Checklist**: mọi exception có transaction ID, variance, leakage và risk status.
