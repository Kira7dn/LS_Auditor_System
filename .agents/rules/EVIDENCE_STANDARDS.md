---
trigger: model_decision
description: "Chuẩn bằng chứng bắt buộc cho mọi phát hiện Audit"
---

# Evidence Standards

## 1. No Evidence, No Finding
Agent chỉ được gọi một nhận định là Finding khi có bằng chứng truy vết được. Nếu chưa đủ bằng chứng, gọi là Candidate Exception.

## 2. Evidence Pack Minimum
Mỗi Evidence Pack phải có:
- `finding_id`;
- source dataset hoặc raw extract;
- transaction/document ID;
- timestamp hoặc kỳ dữ liệu;
- mô tả bất thường;
- logic tính leakage;
- limitation và assumption;
- link hoặc path tới artifact nguồn.

## 3. Traceability
- Mỗi số liệu trong báo cáo phải truy ngược được về artifact hoặc source record.
- Không dùng số tổng hợp trong final report nếu không có file trung gian hoặc script tạo ra số đó.

## 4. Evidence Confidence
Mỗi bằng chứng phải được phân loại:
- `confirmed`: đã đối chiếu đủ nguồn;
- `probable`: đủ dữ liệu để nghi vấn, cần auditor xác minh;
- `weak`: chỉ dùng làm hướng điều tra, không dùng làm kết luận.

---
*Status: MANDATORY EVIDENCE RULE*