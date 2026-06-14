---
trigger: model_decision
description: "Đặc tả Production MVP cho LS Auditor Assistant"
---

# Auditor Assistant Spec

## Mission
LS Auditor Assistant hỗ trợ Auditor chuyển dữ liệu hỗn độn thành bằng chứng kinh tế có thể kiểm chứng, rồi đóng gói thành intervention thesis và final report.

## Required Capabilities
- Registry inspection.
- Case workspace initialization.
- Data validation, normalization and join.
- Variance and leakage computation.
- Rule testing.
- Evidence tracing and packaging.
- Parquet inspection.
- Static chart artifact generation.
- Final report assembly.

## CLI Contract
Mọi command `ls-auditor` phải:
- nhận input qua CLI;
- trả JSON cuối cùng qua stdout;
- ghi cảnh báo/debug ra stderr;
- không sửa raw data;
- trả lỗi JSON khi thất bại.

## Default Case
MVP dùng Material Planning làm case kiểm chứng đầu tiên tại `Training/handbook/material-planning/CASE_STUDY.md`.

---
*Status: MVP ASSISTANT SPEC*