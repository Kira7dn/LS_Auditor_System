---
trigger: model_decision
description: "Chuẩn viết và bảo trì rule cho LS Auditor Agent"
---

# Rule Authoring Standard

## 1. Rule Scope
Mỗi rule phải trả lời:
- Rule áp dụng khi nào?
- Agent phải làm gì?
- Agent không được làm gì?
- Cách kiểm tra tuân thủ là gì?

## 2. Avoid Duplication
- Constitution chỉ chứa nguyên tắc bất biến.
- Operational Spec chỉ chứa cơ chế vận hành.
- Workflow chỉ chứa bước theo giai đoạn.
- Skill chỉ chứa phương pháp chuyên môn.

## 3. Required Frontmatter
Mỗi rule file phải có:

```yaml
---
trigger: "always_on | workflow | manual"
description: "Mô tả ngắn"
---
```

---
*Status: RULE MAINTENANCE STANDARD*