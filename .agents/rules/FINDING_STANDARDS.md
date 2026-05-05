---
trigger: "always_on"
description: "Chuẩn cấu trúc và chất lượng cho Audit Finding"
---

# Finding Standards

## 1. Required Structure
Mỗi Finding phải có đủ:
- **Condition**: điều gì đang xảy ra;
- **Criteria**: chuẩn đúng là gì;
- **Cause**: nguyên nhân trực tiếp hoặc giả thuyết nguyên nhân;
- **Effect / Leakage**: thiệt hại tài chính, thời gian, kiểm soát hoặc rủi ro;
- **Evidence**: nguồn chứng minh;
- **Recommendation**: hành động can thiệp;
- **ROI Hypothesis**: giá trị kỳ vọng nếu sửa lỗi.

## 2. Severity
Severity mặc định:
- `Critical`: có leakage lớn, bypass control, hoặc rủi ro compliance nghiêm trọng.
- `High`: lặp lại nhiều lần, có ảnh hưởng tài chính rõ.
- `Medium`: có pattern yếu hơn hoặc cần xác minh thêm.
- `Low`: sai lệch nhỏ, dùng để cải thiện quy trình.

## 3. Candidate vs Confirmed
- `candidate_exception`: bất thường được phát hiện bằng dữ liệu nhưng chưa đủ xác minh.
- `confirmed_finding`: bất thường đã có bằng chứng và logic ảnh hưởng đủ rõ.
- Agent không được nâng cấp candidate thành confirmed nếu thiếu Evidence Pack.

---
*Status: MANDATORY FINDING RULE*
