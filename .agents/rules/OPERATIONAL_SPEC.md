---
trigger: "always_on"
description: "Quy chuẩn vận hành kỹ thuật và cơ chế thực thi tự động (Operational Specification)"
---

# Operational Specification

Tài liệu này quy định cấu trúc kỹ thuật và tiêu chuẩn vận hành tối cao cho hệ thống Agent trong Workspace **LS Auditor**.

---

## 1. Cơ chế Vận hành Tự động (Auto-Execution)

Hệ thống sử dụng các chỉ dẫn đặc biệt để tối ưu hóa tốc độ thực thi của Agent:

- **`// turbo` Annotation**: Khi xuất hiện phía trên một khối lệnh (bash/python) trong Workflow, Agent được phép **Tự động thực thi (Auto-run)** lệnh đó mà không cần chờ xác nhận từ User, với điều kiện các tham số đã được xác định rõ ràng.
- **`uv run` Discipline**: Mọi script thực thi phải thông qua `uv run` để đảm bảo môi trường ảo (Hermetic Environment) luôn đồng bộ và sạch sẽ.

---

## 2. Tiêu chuẩn Script "AI-First"

Mọi công cụ phân tích trong `skills/` phải tuân thủ nghiêm ngặt [.agents/rules/SCRIPT_STANDARDS.md](./SCRIPT_STANDARDS.md):
- **Input**: Nhận tham số qua CLI (`argparse`).
- **Output**: Luôn trả về kết quả cuối cùng dưới dạng **JSON string** qua `stdout`.
- **Logging**: Đẩy mọi thông tin debug/cảnh báo ra `stderr`.
- **Type Safety**: Bắt buộc sử dụng Type Hints cho toàn bộ mã nguồn.

---

## 3. Cấu trúc Tài sản Tri thức

Hệ thống được tổ chức theo triết lý "Sovereign Knowledge":

- **`.agents/rules/`**: Hiến pháp vận hành (`GEMINI.md`) và các tiêu chuẩn kỹ thuật.
- **`.agents/workflows/auditor/`**: Các luồng điều phối công việc đã được "Hardened" (Tối ưu cho AI).
- **`.agents/skills/auditor/`**: Các kỹ năng nghiệp vụ chuyên sâu kèm theo scripts thực thi chuẩn JSON.
- **`.agents/templates/auditor/`**: Hệ thống Artifacts mẫu dùng để đóng gói bằng chứng và báo cáo.

---

## 4. Hierarchy & Context Loading

Thứ tự ưu tiên nạp tri thức để đảm bảo tính liêm chính của bằng chứng:
1. **`GEMINI.md`**: Constitution cấp cao, định nghĩa nguyên tắc bất biến.
2. **`.agents/rules/OPERATIONAL_SPEC.md`**: Cơ chế vận hành, bootstrap và auto-execution.
3. **`.agents/rules/DATA_GOVERNANCE.md`**, **`EVIDENCE_STANDARDS.md`**, **`FINDING_STANDARDS.md`**: Luật nghiệp vụ bắt buộc cho dữ liệu, bằng chứng và phát hiện.
4. **`.agents/rules/SCRIPT_STANDARDS.md`**: Kỷ luật kỹ thuật cho CLI/script.
5. **`.agents/workflows/auditor/`**: Quy trình theo giai đoạn.
6. **`.agents/skills/`**: Phương pháp chuyên môn và công cụ hỗ trợ.
7. **`asset-index.json`**: Registry tra cứu tài sản hiện có.

Nếu hai chỉ dẫn mâu thuẫn, lớp có số thứ tự nhỏ hơn thắng. Workflow và Skill không được hạ chuẩn Evidence/Data/Finding.

## 5. Case Workspace Discipline

- Mọi case audit phải chạy trong `Projects/<case_id>/`.
- Raw data nằm trong `Projects/<case_id>/raw/` và không được ghi đè.
- Artifact dẫn xuất nằm trong `Projects/<case_id>/artifacts/`.
- Evidence Pack nằm trong `Projects/<case_id>/Evidence_Packs/`.
- Template gốc trong `.agents/templates/auditor/` chỉ được copy sang case workspace, không được ghi đè khi thực thi case.

---
*Status: MANDATORY OPERATIONAL RULE*
