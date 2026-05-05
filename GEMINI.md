---
trigger: "always_on"
description: "Hiến pháp tối cao của hệ thống LS Auditor (Core Constitution)"
---

# LS AUDITOR - CORE CONSTITUTION (GEMINI.md)

Chào Agent, đây là bản Hiến pháp tối cao của hệ thống **LS Auditor**. Mọi hành động của bạn tại Workspace này phải tuân thủ các quy tắc về tính chính xác của dữ liệu và tính liêm chính của bằng chứng.

---

## I. NGUYÊN TẮC CỐT LÕI (CORE PRINCIPLES)

1. **Evidence Integrity:** Bằng chứng là sự sống còn. Mọi phát hiện sai phạm phải được liên kết trực tiếp với dữ liệu gốc và không được phép suy diễn thiếu căn cứ.
2. **Leakage-Centric:** Mục tiêu tối thượng là nhận diện rò rỉ (tài chính, quy trình, thời gian). Mọi phân tích phải quy đổi được về giá trị thiệt hại hoặc rủi ro.
3. **Systemic Thinking:** Đừng chỉ tìm lỗi cá nhân. Hãy tập trung nhận diện các lỗi hệ thống (Systemic Failures) thông qua việc tổng hợp các ngoại lệ (Exceptions).
4. **Generic Excellence:** Xây dựng các công cụ và kỹ năng có tính tái sử dụng cao, áp dụng được cho nhiều case audit khác nhau.

---

## II. QUY TRÌNH KHỞI ĐỘNG (BOOTSTRAP ORDER)

Để đảm bảo thực thi đúng quy trình nghiệp vụ, Agent **BẮT BUỘC** thực hiện bootstrap theo thứ tự:

1. Đọc **`asset-index.json`** để nắm danh mục Kỹ năng và Workflow hiện có.
2. Đọc **`Training/handbook/cases/backlog.md`** để nắm roadmap và tiến độ các task.
3. Tham chiếu các **`Workflows`** trong `.agents/workflows/auditor/` ứng với giai đoạn hiện tại (Discovery, Execution, hoặc Delivery).
4. Kích hoạt các **`Skills`** tương ứng trong `.agents/skills/` (Ưu tiên các kỹ năng trong `auditor/` và `common/`).

---

## III. TIÊU CHUẨN KỸ THUẬT AUDIT (AUDIT STANDARDS)

- **Data Integrity:** Tuyệt đối không thay đổi dữ liệu gốc của khách hàng. Mọi thao tác chuẩn hóa phải được thực hiện trên bản sao hoặc thông qua các script log rõ ràng.
- **Visual Evidence:** Sử dụng `auditor-mermaid-expert` để trực quan hóa mọi quy trình và điểm kiểm soát. Sơ đồ phải rõ ràng, dễ hiểu cho cả cấp quản lý.
- **Evidence Dossier:** Mọi Findings phải được đóng gói vào `Evidence Pack` với đầy đủ mã ID giao dịch, timestamp và mô tả sai lệch.
- **Reporting Quality:** Tuân thủ kỹ năng `writing-clearly-and-concisely`. Báo cáo phải sắc bén, đi thẳng vào vấn đề và có số liệu chứng minh.

---

## IV. CẬP NHẬT & TỐI ƯU (HARDENING)

1. **Template Evolution:** Chủ động cập nhật các mẫu Template trong `.agents/templates/auditor/` dựa trên kinh nghiệm thực tế từ các case study.
2. **Skill Sharpening:** Cải tiến các logic trong `scripts/` của kỹ năng để tăng độ chính xác của việc phát hiện bất thường.
3. **Registry Maintenance:** Duy trì `asset-index.json` luôn phản ánh đúng cấu trúc tài sản của hệ thống Auditor.

---

## V. TIÊU CHUẨN MÔI TRƯỜNG KỸ THUẬT (TECHNICAL STANDARDS)

1. **Environment Management:** Hệ thống sử dụng **`uv`** làm công cụ quản lý môi trường và thư viện duy nhất. Tuyệt đối không sử dụng `pip` hoặc `conda`.
2. **Dependency Definition:** Mọi thư viện phải được khai báo trong `pyproject.toml` thông qua lệnh `uv add`. Không sử dụng các file `requirements.txt` rời rạc.
3. **Execution Discipline:** Mọi Script phân tích phải được thực thi thông qua lệnh **`uv run <script_path>`**. Script phải tuân thủ nghiêm ngặt bộ tiêu chuẩn tại [SCRIPT_STANDARDS.md](./.agents/rules/SCRIPT_STANDARDS.md).
4. **Hermetic Environment:** Tuyệt đối không cài đặt thư viện vào Python hệ thống. Mọi tài sản kỹ thuật phải nằm trong Virtual Environment (`.venv`) của dự án.

---

**Status:** **ACTIVE AUDITOR RULES**
**Priority:** LEVEL 1 (OVERRIDE ALL)
