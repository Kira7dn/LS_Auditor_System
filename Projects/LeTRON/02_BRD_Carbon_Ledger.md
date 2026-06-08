# DỰ ÁN: CARBON LEDGER SERVICE (SỔ CÁI CARBON BẤT BIẾN)

---

### I. TÓM TẮT CHIẾN LƯỢC (STRATEGIC SUMMARY)

Dự án **Carbon Ledger Service** là sáng kiến "Trust Machine" cốt lõi của **Link Strategy**, được thiết kế để biến dữ liệu phát thải thành tài sản tài chính có tính thanh khoản cao hằng năm. Dự án tập trung tối ưu hóa 3 trụ cột lợi nhuận chiến lược:

* **Giá trị Tín chỉ Carbon Premium (ROI qua Hiệu ứng Niềm tin):** Tín chỉ được bảo chứng bởi hạ tầng "Iron-clad" của Link Strategy, thiết kế chuẩn ISO 14064-3 để tối ưu hóa giá trị thanh khoản trên các sàn giao dịch quốc tế (Verra, Gold Standard).
* **Tối ưu hóa Chi phí Thuế & Vận hành (Dual-Utility Data):** Không chỉ cung cấp bằng chứng phát thải thực tế cho CBAM (EU), hệ thống còn tận dụng dữ liệu cảm biến để giám sát thất thoát nhiên liệu và hàng hóa, tạo ra khả năng tối ưu hóa chi phí vận hành nhanh chóng và minh bạch.
* **Hạ tầng Kiểm toán Số (Audit-Ready Architecture):** Số hóa việc đóng gói hồ sơ "Evidence Bundle", được thiết kế để tương thích tuyệt đối với quy trình thẩm định của các đơn vị VVB quốc tế (SGS, Bureau Veritas), rút ngắn đáng kể thời gian chuẩn bị hồ sơ kiểm toán.
* **Tích hợp OEM Chiến lược (Non-Invasive OEM Integration):** Tận dụng trực tiếp dữ liệu từ hãng xe điện (OEM) làm "Source of Truth" nguyên bản, đảm bảo tính an toàn kỹ thuật và độ tin cậy dữ liệu cao nhất hiện nay mà không xâm lấn kiến trúc chuẩn của phương tiện.
* **Bảo chứng Uy tín Hàng hóa Việt (National Export Shield):** Đóng vai trò là "Lá chắn Xanh" cho doanh nghiệp xuất khẩu, sử dụng dữ liệu bất biến để minh chứng trách nhiệm môi trường, bảo vệ uy tín và khả năng cạnh tranh của hàng hóa "Made in Vietnam" trước các rào cản kỹ thuật khắt khe như CBAM (EU).

---

### II. BỐI CẢNH VÀ LÝ DO ĐẦU TƯ (BUSINESS JUSTIFICATION)

#### 1. Thách thức hiện hữu (Current Challenges)

* **Khủng hoảng niềm tin quốc tế:** Các tổ chức quốc tế và sàn giao dịch carbon (Verra, Gold Standard) đòi hỏi bằng chứng sơ cấp cực kỳ khắt khe, trong khi dữ liệu nội địa thường dễ bị can thiệp.
* **Áp lực CBAM 2026 (EU):** Việc thiếu bằng chứng bất biến về lượng phát thải "embedded" khiến doanh nghiệp xuất khẩu đối mặt với mức thuế carbon cao nhất từ phía liên minh Châu Âu.
* **Quy trình thẩm định chậm chạp:** Việc thẩm tra (Verification) hiện vẫn phụ thuộc vào hồ sơ giấy, gây trễ nhịp cơ hội bán tín chỉ carbon khi thị trường biến động.

#### 2. Mục tiêu kinh doanh trọng tâm (Core Business Goals)

* **Thiết lập "Tiêu chuẩn Vàng" về Minh bạch:** Cung cấp hồ sơ bằng chứng (Evidence Bundle) chuẩn ISO 14064-3, giúp rút ngắn đáng kể thời gian kiểm toán từ các đơn vị VVB quốc tế.
* **Tối ưu hóa Tài chính qua Thuế Carbon:** Đảm bảo dữ liệu phát thải "đúng ngay từ tầng vật lý" để tối ưu hóa mức đóng góp carbon, giảm trực tiếp dòng chi phí thuế CBAM cho doanh nghiệp.
* **Xây dựng Tài sản Số Bất biến:** Biến dữ liệu carbon thành một loại tài sản số có tính thanh khoản cao nhờ bảo chứng công nghệ S3 Object Lock và Blockchain (DLT).
* **Việt Nam Tiên phong:** Thiết lập kiến trúc "Sovereign Trust Machine" kết nối trực tiếp từ lớp vật lý của xe điện đến thị trường tài chính Carbon toàn cầu, góp phần bảo vệ danh tiếng hàng hóa nội địa trên chuỗi cung ứng xanh thế giới.

---

### III. PHẠM VI NGHIỆP VỤ (SCOPE OF BUSINESS REQUIREMENTS)

#### 1. Hệ tiêu chuẩn Tuân thủ (Compliance Standards)

Hệ thống vận hành dưới bộ quy tắc ràng buộc cấp độ tài chính để đảm bảo giá trị pháp lý quốc tế:

* **[R1] Tính Bất biến Tuyệt đối (Hard Immutability):** Tự động kích hoạt S3 Object Lock ngay khi VVB duyệt sổ, chặn 100% việc xoá/lệnh sửa dữ liệu trong 10-20 năm.
* **[R2] Bằng chứng Sơ cấp (Primary Evidence):** Mọi con số phát thải phải có khả năng tính toán lại từ dữ liệu gốc (GPS thô, ảnh hàng hoá) có độ phân giải cao.
* **[R3] Chống chối bỏ (Non-repudiation):** Mã băm SHA256 được khởi tạo ngay tại tầng Ingestion để chứng minh dữ liệu không bị can thiệp từ điểm phát sinh đến server.
* **[R4] Triple-Verification Protocol:** Đối soát 3 chiều giữa Cảm biến tải trọng + AI Năng lượng + AI Camera.
* **[R5] Non-invasive OEM Strategic Integration:** Khả năng kết nối trực tiếp với hạ tầng dữ liệu của hãng xe (OEM) qua API/Edge Gateway theo cơ chế độc lập, đảm bảo an toàn vận hành xe đồng thời lấy được dữ liệu gốc (Native Data) có độ tin cậy cao nhất.

#### 2. Quản trị Quy trình Thẩm định 6 bước (6-Step VVB Standard)

Hệ thống số hóa toàn bộ quy trình kiểm toán theo tiêu chuẩn ISO 14064-3:

1. **Tiếp nhận (Intake):** VVB xem xét Hồ sơ thiết kế (PDD) trực tiếp trên hệ thống.
2. **Niêm yết tham vấn:** Công khai mã băm lên Public DLT (Blockchain) để đảm bảo tính minh bạch cộng đồng.
3. **Đánh giá kỹ thuật:** Kiểm toán viên thẩm định logic tính toán phát thải và tính bổ sung (additionality) của dự án.
4. **Thẩm tra hiện trường từ xa:** Thay thế Site-visit truyền thống bằng GPS Trace Audit và Evidence Bundle (ảnh thô).
5. **Reconciliation:** Hệ thống tự động đối soát chéo dữ liệu thô với báo cáo tổng hợp.
6. **Hard-Locking:** Kích hoạt cơ chế khoá sổ vĩnh viễn sau khi nhận phê duyệt cuối cùng từ VVB.

#### 3. Cổng truy cập Kiểm toán viên (Auditor Access Gateway)

Cung cấp hạ tầng đặc quyền cho các đơn vị thẩm định độc lập (SGS, Bureau Veritas...):

* **Endpoint /api/v1/audit:** Cung cấp Evidence Bundle mà không qua Database ứng dụng để loại bỏ rủi ro UI ảo.
* **Integrity Report:** Tra cứu sai lệch thời gian thực giữa Dữ liệu Vận hành (DynamoDB) và Sự thật Chân lý (S3 Archive).

---

### IV. CÁC ĐỐI TƯỢNG NGƯỜI DÙNG (USER PERSONAS)

1. **VVB (Thẩm định viên quốc tế):** Cần truy cập Evidence Bundle sạch để ra quyết định thẩm định từ xa.
2. **Export Manager (Quản lý xuất khẩu):** Cần dữ liệu carbon chính xác để tối ưu hoá thuế CBAM khi khai báo với hải quan EU.
3. **ESG Specialist (Chuyên viên môi trường):** Cần báo cáo tính bổ sung (Additionality) để đăng ký dự án trên Verra/Gold Standard.

---

### V. CÁC KỊCH BẢN SỬ DỤNG ĐIỂN HÌNH (GENERAL USE CASE SCENARIOS)

#### 1. UC-01: Thẩm định hồ sơ quốc tế (International Audit Gate)

* **AI Action:** Cấp quyền cho thẩm định viên (VVB) truy xuất bộ bằng chứng gốc (Raw Evidence) qua API an toàn.

#### 2. UC-02: Quyết toán Carbon kỳ báo cáo (Period Finalization)

* **AI Action:** Tự động tổng hợp và "Hard-lock" dữ liệu phát thải quý khi kết thúc kỳ quyết toán.

#### 3. UC-03: Chứng minh nguồn gốc phát thải (Origin Tracking)

* **AI Action:** Liên kết dữ liệu hành trình GPS thực tế với lượng nhiên liệu tiêu thụ để bác bỏ mọi nghi ngờ về gian lận lộ trình.

---