---
trigger: "always_on"
description: "Quy chuẩn định dạng liên kết trích dẫn và tự động cuộn trong IDE"
---

# Citation & Link Navigation Standards

Tài liệu này quy định chi tiết cấu trúc cú pháp viết liên kết trích dẫn (Citations) trong các báo cáo và tài liệu kiểm toán, đảm bảo khi người dùng click vào liên kết, IDE sẽ tự động mở và cuộn đến đúng vị trí nguồn.

---

## 1. Định dạng liên kết tuyệt đối (Dành cho việc Click từ khung Chat / Terminal)
Khi viết liên kết trong khung chat của Agent hoặc các tài liệu báo cáo thô cần mở trực tiếp từ bên ngoài, sử dụng giao thức `file://` tuyệt đối kèm số dòng:

*   **Cú pháp:** `[tên_file.md:L<số_dòng>](file:///<đường_dẫn_tuyệt_đối_viết_hoa_ổ_đĩa>#L<số_dòng>)`
*   **Quy chuẩn đường dẫn trên Windows:** Bắt buộc viết hoa chữ cái ổ đĩa, dùng dấu gạch chéo xuôi `/` thay cho dấu gạch chéo ngược `\`.
*   *Ví dụ:* `[10_verification.md:L29](file:///D:/BusinessAnalyze/LS/LS_Auditor_System/Projects/ESG/kb/ghg_protocol/10_verification.md#L29)`

> [!NOTE]
> Để IDE tự động cuộn đến dòng, hãy đảm bảo tệp tin mục tiêu **chưa được mở sẵn** hoặc hãy đóng tab tệp tin đó trước khi click vào link trên khung chat.

---

## 2. Định dạng liên kết tương đối (Dành cho chế độ Markdown Preview của IDE)
Khi viết liên kết nằm bên trong các tài liệu Markdown để người dùng đọc ở chế độ Xem trước (Preview Mode), sử dụng đường dẫn tương đối (Relative Path) và neo tiêu đề (Slugified Heading):

*   **Cú pháp:** `[tên_tiêu_đề](./<đường_dẫn_tương_đối>#<tiêu_đề_slug>)`
*   **Quy tắc tạo tiêu đề slug:** Viết thường toàn bộ tiêu đề, loại bỏ ký tự đặc biệt, thay khoảng trắng bằng dấu gạch ngang `-`.
*   *Ví dụ:* `[Establishing the verification parameters](./10_verification.md#establishing-the-verification-parameters)`

---

## 3. Quy tắc cấm bọc ký tự định dạng (No Backtick Wrapping)
*   **Tuyệt đối KHÔNG** bọc phần liên kết hoặc text liên kết trong dấu phẩy ngược (ví dụ sai: `[` `link` `](file://...)`). Dấu phẩy ngược sẽ biến liên kết thành khối code thô và làm vô hiệu hóa hoàn toàn khả năng click-to-open của trình duyệt Markdown trong IDE.

---

## 4. Quy tắc Trực quan hóa Dẫn chứng trên Chat (Visual Chat Evidence Rule)
*   **Nguyên tắc**: Do giới hạn kỹ thuật của IDE chat webview không thể tự động cuộn dòng khi click link tuyệt đối từ cửa sổ chat, Agent **bắt buộc** phải trực quan hóa dẫn chứng ngay trên giao diện chat.
*   **Cách thực hiện**: Khi đưa ra bất kỳ trích dẫn nào, ngoài việc cung cấp liên kết tuyệt đối trỏ về file nguồn, Agent phải hiển thị một khối code block (Markdown block) trích xuất nguyên văn văn bản thực tế kèm theo số dòng (line numbers) xung quanh (tối thiểu 3 dòng trước và sau thẻ neo).
*   *Ví dụ định dạng hiển thị*:
    > 📖 **Dẫn chứng tại [filename.md: Dòng 29-32](file:///D:/...)**
    > ```markdown
    > 29: <a id="anchor_name"></a>
    > 30: ## Heading Text
    > 31: Actual content line 1...
    > 32: Actual content line 2...
    > ```

---
*Status: MANDATORY CITATION STANDARD*
*Priority: LEVEL 1 (MANDATORY)*
