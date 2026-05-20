# HỆ THỐNG HỖ TRỢ KIỂM TOÁN LS (LS-ASS)
### *Thiết kế Nền móng & Chiến lược Vận hành Hệ thống*

---

## I. TẦM NHÌN CHIẾN LƯỢC & MỤC ĐÍCH TỐI THƯỢNG (STRATEGIC VISION & PURPOSE)

### 0. Định vị Hệ thống Nội bộ (Internal Operating System)
LS-ASS là hệ điều hành nội bộ của Link Strategy để chuẩn hóa quy trình khảo sát thực địa, định lượng thất thoát tài chính, đóng gói bằng chứng và thiết kế đề xuất giải pháp công nghệ cho khách hàng. Hệ thống giúp đội ngũ LS biến dữ liệu vận hành, quy trình thực tế và các vấn đề nhức nhối thương mại của doanh nghiệp thành giải pháp công nghệ có hiệu quả đầu tư (ROI) rõ ràng (như Dữ liệu, IoT, Học máy/Trí tuệ nhân tạo, Thị giác máy tính hoặc Tích hợp hệ thống).

### 0.1. Nguyên tắc Kiểm toán hướng Giải pháp (Audit-to-Solution)
Kiểm toán là bước tiếp cận thương mại đầu tiên để phát hiện các vấn đề nhức nhối thực tế có thể quy đổi ra giá trị tiền mặt. Giá trị kinh doanh của LS nằm ở việc chuyển đổi các vấn đề đã có bằng chứng rõ ràng thành giải pháp công nghệ khả thi, đo lường được hiệu quả và có lộ trình cải tiến lâu dài.

### 0.2. Định vị Thị trường (Market Positioning)
LS-ASS phục vụ mô hình Tư vấn từ Thất thoát đến Giải pháp (Leakage-to-Solution Consulting) của Link Strategy: tìm điểm rò rỉ dòng tiền trong vận hành, chứng minh bằng bằng chứng số liệu, thiết kế giải pháp công nghệ phù hợp và đẩy nhanh tiến độ ký hợp đồng triển khai với khách hàng. Phương pháp này giúp quá trình kiểm toán bắt đầu từ giá trị kinh tế thực tế trước, sau đó mới lựa chọn công nghệ phù hợp để thu hồi giá trị đó.

### 1. Phục hồi và Tối ưu hóa Giá trị Hệ thống Hiện có (System Recovery & Optimization)
Nhiều hệ thống phần mềm doanh nghiệp (như ERP, CRM, phần mềm quản trị) không đạt hiệu quả do nhân sự không thích nghi được hoặc tự phát sinh các quy trình ngoài hệ thống (như chat Zalo, dùng file Excel riêng). Hệ thống LS-ASS ra đời để khôi phục giá trị sử dụng thực tế của các phần mềm hiện có này, giúp tối ưu hóa dòng tiền mà không cần đầu tư xây mới hệ thống từ đầu.

### 2. Ba Mục đích Tối thượng
*   **Mở đường thương mại (Commercial Wedge):** Sử dụng số tiền thất thoát thực tế trong vận hành (Leakage) để thuyết phục Ban Giám đốc/Giám đốc Tài chính ký hợp đồng triển khai công nghệ giá trị cao.
*   **Giải cứu hệ thống (Client Value):** Triệt tiêu thói quen làm việc thủ công ngoài hệ thống, khôi phục năng suất và thu hồi dòng tiền bị rò rỉ cho khách hàng.
*   **Đóng gói tri thức (LS Leverage):** Đóng gói kinh nghiệm khảo sát thực địa thành các bộ quy chuẩn cấu hình sẵn nhằm nhân rộng mô hình kinh doanh của Link Strategy.

---

## II. HỢP ĐỒNG NGHIỆP VỤ (BUSINESS CONTRACT)

```
┌───────────────────────────────────────────┐
│              INPUT (ĐẦU VÀO)              │
│  - Dữ liệu thô hệ thống (Raw CSVs/Logs)   │
│  - Quy trình chính thức (SOPs, Policies)  │
│  - Hồ sơ thực địa (Phỏng vấn, Zalo/Excel) │
│  - Thông số chi phí vận hành (OpEx)       │
└─────────────────────┬─────────────────────┘
                      │
                      ▼
        ┌───────────────────────────┐
        │  LS AUDIT SUPPORT SYSTEM  │
        │ AI + Data Solution Layer  │
        └─────────────┬─────────────┘
                      │
                      ▼
┌───────────────────────────────────────────┐
│             OUTPUT (ĐẦU RA)               │
│  - Báo cáo kiểm toán kèm bằng chứng rõ    │
│  - Bản đồ cơ hội giải pháp công nghệ      │
│  - Tài liệu tóm tắt giải pháp công nghệ   │
│  - Lộ trình triển khai + Hiệu quả ROI     │
└───────────────────────────────────────────┘
```

### 1. Input (Đầu vào thực tế do Khách hàng cung cấp & Auditor thu thập)
*   **Dữ liệu thô hệ thống (Raw Data):** Các tệp dữ liệu giao dịch kết xuất từ phần mềm doanh nghiệp (như Đơn mua hàng PO, Yêu cầu mua hàng PR, Định mức nguyên vật liệu BOM, Tồn kho, Tiêu hao vật tư, Phiếu nhập kho GRN, Nhật ký hệ thống).
*   **Văn bản chính sách & Quy trình vận hành chính thức (SOPs/Policies):** Quy quy chế, hạn mức phê duyệt và hướng dẫn quy trình vận hành chính thức của doanh nghiệp.
*   **Hồ sơ nghiệp vụ thực địa (Fieldwork Dossier):** Biên bản phỏng vấn trực tiếp nhân sự (Interview Transcripts) và ghi chép/hình ảnh về các quy trình tự phát bằng tay ngoài hệ thống (qua Zalo, Excel).
*   **Thông số chi phí vận hành (Operational Costs):** Các số liệu về thời gian lãng phí, đơn giá nhân công, và chi phí duy trì phần mềm cũ để làm cơ sở tính toán kinh tế.

### 2. Output (Đầu ra thực tế bàn giao cho Ban Giám đốc)
*   **Báo cáo kiểm toán (CFO-Ready PDF/DOCX Report):** Văn bản in ấn chuyên nghiệp chỉ rõ số tiền thất thoát dòng tiền (Leakage) và các lỗ hổng kiểm soát kèm bằng chứng đối soát rõ ràng.
*   **Bản đồ cơ hội giải pháp (Solution Opportunity Map):** Bảng chuyển đổi các phát hiện sai phạm thành cơ hội can thiệp công nghệ, nêu rõ vấn đề cần giải quyết, giá trị thu hồi và các năng lực công nghệ liên quan.
*   **Tóm tắt giải pháp công nghệ (Technology Solution Brief):** Mô tả giải pháp công nghệ phù hợp (Dữ liệu, IoT, Học máy, AI Agent, Thị giác máy tính hoặc Tích hợp hệ thống), phạm vi dữ liệu sử dụng và ước tính hiệu quả đầu tư (ROI).
*   **Lộ trình triển khai & ROI (Implementation Roadmap):** Kế hoạch hành động 30-60-90 ngày nêu rõ người chịu trách nhiệm, chi phí đầu tư, số tiền tiết kiệm được, thời gian hoàn vốn và các bước tiếp theo để ký kết hợp đồng thương mại.

---

## III. TIẾN TRÌNH TÁC CHIẾN & CƠ CHẾ LOGIC VẬN HÀNH (HOW IT WORKS)

LS-ASS vận hành theo logic: chọn vùng có tiền, dùng công nghệ để phát hiện và ngăn chặn thất thoát, rồi đóng gói thành bằng chứng kiểm toán và đề xuất giải pháp có ROI. Kiểm toán không dừng ở việc "bắt lỗi"; mục tiêu là tìm các vấn đề nhức nhối đủ lớn để mở ra hợp đồng phát triển giải pháp Dữ liệu, IoT, Học máy, AI Agent hoặc Thị giác máy tính.

### 0. Logic Thương mại (Commercial Logic)

Mỗi dự án kiểm toán phải trả lời được 4 câu hỏi cốt lõi trước khi đi vào phân tích chi tiết:

*   **Tiền đang thất thoát ở đâu?** Doanh thu giảm, biên lợi nhuận thu hẹp, đọng vốn lưu động, chi phí vận hành tăng cao, hoặc hệ thống phần mềm cũ không tạo ra hiệu quả đầu tư.
*   **Dữ liệu nào chứng minh được?** Dữ liệu từ phần mềm ERP/CRM/SaaS, file Excel, nhật ký hệ thống, chứng từ giấy, dữ liệu cảm biến, camera hình ảnh hoặc biên bản phỏng vấn.
*   **Công nghệ nào ngăn chặn được thất thoát?** Đường ống xử lý dữ liệu (data pipeline), bảng theo dõi dashboard, bộ quy tắc kiểm soát tự động (rule engine), mô hình dự báo học máy (ML forecast), cảm biến IoT, thị giác máy tính (CV), quy trình tự động hóa AI.
*   **Giải pháp nào có thể bán được cho khách hàng?** Tự động hóa kiểm soát, hỗ trợ ra quyết định thông minh, hoặc số hóa quy trình vận hành với lộ trình, chi phí, mức tiết kiệm và thời gian hoàn vốn cụ thể.

### 0.1. Các Miền Kiểm toán Thương mại dẫn dắt bởi Công nghệ (Technology-Led Commercial Audit Domains)

Các miền kiểm toán của LS-ASS được thiết kế từ giao điểm giữa vấn đề nhức nhối thực tế và năng lực công nghệ. Mỗi miền kiểm toán phải chỉ ra: tiền thất thoát ở đâu, dữ liệu/cảm biến/AI nào có thể phát hiện, và giải pháp công nghệ nào có thể ngăn chặn thất thoát để tạo hợp đồng triển khai.

*   **Kiểm soát doanh thu và Dự báo nhu cầu (Revenue Intelligence & Demand Sensing):**
    *   *Vấn đề nhức nhối:* Thất thoát doanh thu do không nắm bắt được nhu cầu thực tế của thị trường, dự báo sai, phản ứng chậm, thiếu hàng để bán hoặc bỏ lỡ đơn hàng.
    *   *Góc độ công nghệ:* Tích hợp dữ liệu doanh nghiệp, học máy dự báo nhu cầu, hệ thống gợi ý bằng AI, bảng theo dõi doanh thu.
    *   *Giải pháp đề xuất:* Hệ thống dự báo nhu cầu thị trường, trung tâm quản lý dự báo bán hàng, giám sát cơ hội tăng trưởng doanh thu.
*   **Kiểm soát biên lợi nhuận và Chính sách giá (Margin Intelligence & Pricing Control):**
    *   *Vấn đề nhức nhối:* Doanh số cao nhưng lợi nhuận thấp do chiết khấu tràn lan, báo giá sai lệch, chi phí đầu vào tăng nhưng không cập nhật kịp thời vào giá bán, hoặc thiếu cảnh báo khi biên lợi nhuận bị âm.
    *   *Góc độ công nghệ:* Phân tích biên lợi nhuận, bộ quy tắc kiểm soát giá tự động, chấm điểm lợi nhuận bằng học máy, tự động hóa phê duyệt giá.
    *   *Giải pháp đề xuất:* Tháp kiểm soát giá bán, hệ thống cảnh báo biên lợi nhuận rủi ro, quy trình phê duyệt chiết khấu tự động.
*   **Tối ưu hóa chi phí mua sắm và Quản lý nhà cung cấp (Procurement spend & Vendor Optimization):**
    *   *Vấn đề nhức nhối:* Mua hàng đắt, mua khẩn cấp ngoài kế hoạch, nhà cung cấp kém chất lượng, chia nhỏ đơn hàng để né phê duyệt hạn mức, không gom nhu cầu mua sắm hoặc không tận dụng các điều khoản ưu đãi trong hợp đồng nguyên tắc.
    *   *Góc độ công nghệ:* Phân tích chi phí mua sắm, chấm điểm nhà cung cấp, phát hiện giao dịch mua hàng bất thường, trợ lý AI hỗ trợ tìm kiếm nguồn hàng.
    *   *Giải pháp đề xuất:* Bảng giám sát tiết kiệm chi phí mua sắm, chấm điểm rủi ro nhà cung cấp, quy trình mua sắm tự động.
*   **Giám sát tồn kho và Giải phóng vốn lưu động (Inventory Visibility & Working Capital Release):**
    *   *Vấn đề nhức nhối:* Vốn bị đọng nhiều trong kho, số liệu tồn kho trên phần mềm lệch với thực tế, các đơn hàng mua chưa về không được theo dõi, đặt hàng vượt nhu cầu thực tế hoặc nhiều vật tư bị lưu kho quá lâu.
    *   *Góc độ công nghệ:* Tích hợp dữ liệu kho, cảm biến IoT theo dõi vị trí vật tư, đếm hàng tự động bằng camera (thị giác máy tính), học máy dự báo mức tồn kho an toàn.
    *   *Giải pháp đề xuất:* Hệ thống giám sát tồn kho thời gian thực, cảnh báo vật tư ứ đọng, trung tâm quản lý giải phóng vốn lưu động.
*   **Đo lường vận hành và Tối ưu hóa năng suất (Operational Sensing & Productivity Optimization):**
    *   *Vấn đề nhức nhối:* Máy móc dừng hoạt động (downtime), tỷ lệ hàng lỗi cao, nghẽn cổ chai quy trình, thời gian sản xuất kéo dài và năng suất lao động thấp nhưng không có dữ liệu tin cậy để đo lường.
    *   *Góc độ công nghệ:* Thiết bị IoT kết nối máy móc, dữ liệu cảm biến, thị giác máy tính giám sát quy trình, học máy phát hiện bất thường vận hành, bảng theo dõi năng suất sản xuất.
    *   *Giải pháp đề xuất:* Hệ thống đo lường vận hành thực địa, trung tâm điều hành năng suất sản xuất, hệ thống phát hiện dừng máy và hao phí.
*   **Giám sát đơn hàng và Đảm bảo cam kết dịch vụ (Fulfillment Visibility & Service Performance):**
    *   *Vấn đề nhức nhối:* Giao hàng trễ hạn, vi phạm cam kết dịch vụ (SLA) với khách hàng, phát sinh chi phí phạt, hàng bị trả lại nhiều, hoặc quy trình xử lý đơn hàng phức tạp phải làm đi làm lại.
    *   *Góc độ công nghệ:* Dữ liệu định vị theo dõi lộ trình, thiết bị IoT/GPS giám sát xe, camera xác minh tình trạng giao nhận hàng (Proof of Delivery), học máy dự báo thời gian giao nhận dự kiến (ETA) và rủi ro trễ hẹn.
    *   *Giải pháp đề xuất:* Bảng giám sát tiến độ giao hàng, hệ thống cảnh báo sớm nguy cơ trễ hẹn SLA, quy trình tự động hóa kiểm soát dịch vụ giao nhận.
*   **Kiểm soát dòng tiền và Thu hồi công nợ (Cashflow Intelligence & Finance Recovery):**
    *   *Vấn đề nhức nhối:* Tiền mặt bị kẹt ở công nợ khách hàng kéo dài, thanh toán trùng lặp cho nhà cung cấp, chi tạm ứng bị treo lâu ngày không quyết toán, điều khoản thanh toán bất lợi hoặc gửi hóa đơn thanh toán chậm.
    *   *Góc độ công nghệ:* Tự động đối soát dữ liệu tài chính, thuật toán phát hiện thanh toán bất thường, trợ lý AI hỗ trợ nhắc nợ, tự động hóa quy trình tài chính.
    *   *Giải pháp đề xuất:* Trung tâm quản lý thu hồi dòng tiền, hệ thống phát hiện thanh toán bất thường, trợ lý ưu tiên danh sách thu nợ.
*   **Phân tích hiệu quả sinh lời theo Khách hàng / Nhà cung cấp / Mã hàng (Profitability Intelligence):**
    *   *Vấn đề nhức nhối:* Không xác định được nhóm khách hàng, nhà cung cấp, sản phẩm (SKU) hoặc đối tác nào thực sự mang lại lợi nhuận hoặc gây lỗ sau khi tính đầy đủ chi phí phục vụ (Cost-to-Serve).
    *   *Góc độ công nghệ:* Mô hình tính giá thành sản phẩm và chi phí phục vụ, phân tích lợi nhuận đa chiều, thuật toán phân khúc khách hàng/sản phẩm bằng học máy, bảng theo dõi lợi nhuận điều hành.
    *   *Giải pháp đề xuất:* Hệ thống phân tích lợi nhuận đa chiều, bảng chấm điểm hiệu quả khách hàng/nhà cung cấp, công cụ tối ưu hóa cơ cấu sản phẩm bán ra.
*   **Quản lý năng suất nhân sự và Tự động hóa quy trình (Workforce Intelligence & Automation):**
    *   *Vấn đề nhức nhối:* Chi phí làm thêm giờ (overtime) tăng bất thường, phê duyệt chậm trễ, phân bổ nhân sự không hợp lý, phụ thuộc quá nhiều vào một vài cá nhân, hoặc nhiều tác vụ lặp đi lặp lại bằng tay chưa được tự động hóa.
    *   *Góc độ công nghệ:* Phân tích quy trình làm việc (Process Mining), phân tích khối lượng công việc, trợ lý ảo AI tự động hóa quy trình.
    *   *Giải pháp đề xuất:* Bảng quản lý năng suất làm việc, tự động hóa quy trình phê duyệt cấp cao, trợ lý AI hỗ trợ xử lý tác vụ vận hành.
*   **Phục hồi hiệu quả sử dụng phần mềm doanh nghiệp (System Adoption & Digital Workflow Recovery):**
    *   *Vấn đề nhức nhối:* Đã đầu tư phần mềm (ERP, CRM) nhưng nhân viên vẫn dùng Excel/Zalo để làm việc ngoài hệ thống, nhập dữ liệu trễ hạn, bỏ trống nhiều chức năng hoặc số liệu trên hệ thống không đáng tin cậy.
    *   *Góc độ công nghệ:* Phân tích nhật ký sử dụng hệ thống (system logs), tích hợp dữ liệu tự động, trợ lý AI hướng dẫn thao tác, bảng theo dõi mức độ tương thích hệ thống.
    *   *Giải pháp đề xuất:* Hệ thống giám sát mức độ sử dụng phần mềm, khôi phục luồng làm việc số hóa, chương trình cải thiện hiệu quả đầu tư phần mềm doanh nghiệp.

### 0.2. Danh mục Năng lực Công nghệ (Technology Capability Catalog)

Danh mục Năng lực Công nghệ là bộ công cụ dùng để thiết kế giải pháp sau kiểm toán. Mỗi sai lệch kiểm toán trọng yếu phải được kết nối với ít nhất một năng lực công nghệ bên dưới để chứng minh rằng LS không chỉ phát hiện thất thoát mà còn có phương án can thiệp cụ thể.

*   **Kỹ thuật dữ liệu & Phân tích (Data Engineering & Analytics):**
    *   Hợp nhất dữ liệu từ ERP, CRM, Excel, nhật ký hệ thống và các tệp vận hành rời rạc.
    *   Xây dựng kho dữ liệu tích hợp, bảng theo dõi dashboard, giám sát giao dịch bất thường và đo lường tiền thất thoát.
    *   Ứng dụng cho việc đối soát giao dịch, theo dõi chỉ số đo lường hiệu quả (KPI), phát hiện rò rỉ dòng tiền và đo lường hiệu quả đầu tư (ROI).
*   **Thiết bị cảm biến & IoT (IoT & Operational Sensing):**
    *   Thu thập dữ liệu thực tế từ máy móc sản xuất, nhà kho, dây chuyền, phương tiện vận tải và điểm giao nhận.
    *   Đối chiếu số liệu từ cảm biến với số liệu trên phần mềm để phát hiện dừng máy, thất thoát vật tư, sai lệch kho hoặc vi phạm cam kết dịch vụ.
    *   Ứng dụng trong quản lý kho, tối ưu hóa năng suất sản xuất, và dịch vụ giao nhận đơn hàng.
*   **Học máy & Dự báo (Machine Learning & Forecasting):**
    *   Dự báo nhu cầu mua/bán, lượng tồn kho tối ưu, thời gian giao hàng, rủi ro khách hàng rời đi, rủi ro nợ xấu, sự cố máy móc và thiết lập mức chuẩn vận hành tối ưu.
    *   Tự động phát hiện các quy luật bất thường phức tạp vượt ngoài các quy tắc kiểm tra thông thường (như hành vi mua hàng bất thường, rủi ro nhà cung cấp, trễ hạn thanh toán).
    *   Ứng dụng trong dự báo nhu cầu bán hàng, kiểm soát giá bán, thu hồi dòng tiền và tối ưu hóa hiệu quả sinh lời.
*   **Trợ lý AI & Tự động hóa quy trình (AI Agents & Workflow Automation):**
    *   Tự động đọc tài liệu quy trình, phân tích biên bản phỏng vấn, dựng sơ đồ quy trình, lập danh sách rủi ro dữ liệu, chạy kiểm tra chất lượng dữ liệu, đóng gói hồ sơ bằng chứng và soạn thảo báo cáo.
    *   Điều phối quy trình xử lý ngoại lệ sau kiểm toán: quy trình duyệt nhanh, đánh giá giao dịch lỗi, phân công công việc sửa sai và gửi báo cáo định kỳ cho ban giám đốc.
    *   Ứng dụng trong phục hồi hiệu quả sử dụng phần mềm, tối ưu hóa năng suất nhân sự và các khâu kiểm tra thủ công.
*   **Thị giác máy tính - Camera thông minh (Computer Vision):**
    *   Đọc và phân tích thông tin từ hình ảnh, video giám sát, chứng từ scan, mã vạch hàng hóa, biển số xe, pallet hàng hoặc khu vực nhà kho.
    *   Đối chiếu hình ảnh thực tế với dữ liệu trên hệ thống để phát hiện thiếu hàng, sai quy cách đóng gói, lệch tồn kho vật lý, vi phạm an toàn lao động, thời gian xe chờ quá lâu hoặc chứng từ giao nhận không khớp.
    *   Ứng dụng mạnh trong quản lý kho, năng suất sản xuất, giao nhận đơn hàng và đối soát hóa đơn chứng từ.

Mỗi phát hiện sai lệch trọng yếu phải được đóng gói thành một trong ba hướng giải pháp:

*   **Tự động hóa Kiểm soát (Control Automation):** Tự động chặn hoặc cảnh báo sớm các giao dịch sai trước khi phát sinh thất thoát dòng tiền.
*   **Hỗ trợ Ra quyết định Thông minh (Decision Intelligence):** Cung cấp các công cụ dashboard, dự báo xu hướng, chấm điểm rủi ro hoặc gợi ý hành động để hỗ trợ ban điều hành quyết định chính xác hơn.
*   **Số hóa Quy trình Vận hành (Operational Digitization):** Thay thế các thao tác thủ công qua Excel, Zalo bằng quy trình số hóa tự động, cảm biến thực tế, trợ lý AI hoặc liên thông tích hợp hệ thống phần mềm.

### 0.3. Bộ tài sản Vận hành & Tri thức của Agent (Agent Knowledge & Execution Stack)

Để AI Agent thực thi ổn định theo chuẩn nghiệp vụ của Link Strategy, mọi giai đoạn của LS-ASS phải được trang bị đủ 5 tầng tài sản sau:

*   **Gói tri thức chuyên ngành (Domain Knowledge Pack):** Tri thức nghiệp vụ quy chuẩn, danh mục các điểm kiểm soát cốt lõi (Control Points), và các lỗi hệ thống thường gặp trong từng mảng nghiệp vụ kiểm toán.
*   **Từ điển thực địa (Terminology Pack):** Tập hợp thuật ngữ thực tế và từ lóng vận hành giúp AI hiểu được các cách nói phi chính thức của nhân sự như "làm ngoài hệ thống", "nhắn Zalo trước rồi nhập sau", "dùng Excel riêng", "đặt dư cho chắc".
*   **Quy tắc phát hiện rủi ro (Rule Pack):** Bộ quy tắc kiểm tra dữ liệu để phát hiện bất thường, các ngưỡng cảnh báo, công thức tính toán số tiền thất thoát và tiêu chuẩn bằng chứng tối thiểu.
*   **Bộ công cụ thực thi (Execution Pack):** Các quy trình công việc, kỹ năng phân tích và script dòng lệnh (CLI commands) để làm sạch, ghép nối, tính toán dữ liệu và lập báo cáo.
*   **Tiêu chuẩn Bằng chứng & Báo cáo (Evidence & Reporting Pack):** Biểu mẫu hồ sơ bằng chứng, các mẫu báo cáo và tiêu chuẩn duyệt qua từng giai đoạn để đảm bảo mọi kết luận đều có số liệu đối chiếu rõ ràng về dữ liệu nguồn gốc.

### 0.4. Mô hình hoạt động của Gói Nghiệp vụ (Domain Pack Operating Model)

Mỗi gói nghiệp vụ chuyên biệt (Domain Pack) là tài sản trí tuệ cốt lõi của Link Strategy, giúp AI Agent nắm rõ quy trình cần kiểm tra, dữ liệu cần thu thập, quy tắc đối chiếu và mô hình giải pháp công nghệ tương ứng.

Mỗi gói nghiệp vụ bắt buộc có:

*   **Thư viện Vấn đề Nhức nhối (Pain Point Library):** Danh sách các triệu chứng trục trặc trong kinh doanh thường gặp, các câu nói phổ biến của khách hàng và dấu hiệu nhận biết vấn đề đủ lớn để tiến hành kiểm toán.
*   **Danh mục Nguồn dữ liệu (Data Source Checklist):** Các bảng dữ liệu cần thu thập, phương án thay thế khi dữ liệu bị thiếu, người sở hữu dữ liệu và mức độ tin cậy của từng nguồn.
*   **Bản đồ Quy trình & Kiểm soát (Process / Control Map):** Sơ đồ quy trình chuẩn, các khâu bàn giao công việc, điểm kiểm soát cốt lõi, người chịu trách nhiệm, bằng chứng đối chiếu mong đợi và các điểm dễ bị bypass (né tránh kiểm soát).
*   **Thư viện Dấu hiệu Rủi ro (Risk Pattern Library):** Các quy luật bất thường có thể quét tự động bằng dữ liệu, nhật ký hệ thống, camera hoặc kết quả phỏng vấn.
*   **Thư viện Công thức tính Thất thoát (Leakage Formula Library):** Các công thức toán học quy đổi sai lệch dữ liệu thành tiền mặt bị mất, bao gồm các giả định kinh tế, đơn vị đo lường, giới hạn và độ tin cậy của phép tính.
*   **Tiêu chuẩn xác minh bằng chứng (Evidence Requirement Matrix):** Bộ tài liệu/số liệu tối thiểu cần thu thập để nâng một giao dịch nghi ngờ (exception) thành một sai phạm đã xác nhận (confirmed finding).
*   **Phương án Giải pháp Công nghệ (Technology Solution Options):** Các mô hình thiết kế giải pháp bằng Dữ liệu, IoT, Học máy, Trí tuệ nhân tạo hoặc Thị giác máy tính để khắc phục triệt để điểm thất thoát dòng tiền.
*   **Mô hình ROI (ROI Model):** Phương pháp ước tính số tiền tiết kiệm được, chi phí đầu tư giải pháp, thời gian thu hồi vốn và phân tích độ nhạy khi các giả định thay đổi.
*   **Điểm duyệt Thủ công (Human Checkpoints):** Các cột mốc bắt buộc phải có sự xác nhận của chuyên gia kiểm toán hoặc của chính khách hàng trước khi đưa ra kết luận hoặc đề xuất giải pháp.
*   **Tài liệu Đầu ra tiêu chuẩn (Output Artifacts):** Các sản phẩm hoàn thiện bàn giao gồm danh mục sai phạm, hồ sơ bằng chứng, bản đồ cơ hội giải pháp, tài liệu tóm tắt giải pháp công nghệ và lộ trình triển khai.

### 0.5. Cổng Kiểm soát & Điểm phê duyệt (Stage Gates & Human Checkpoints)

Agent không được phép chạy quy trình tự động một cách mù quáng. Mỗi giai đoạn bắt buộc phải đi qua các Cổng kiểm soát (Gates) để bảo vệ chất lượng dữ liệu, tính pháp lý của bằng chứng và tính khả thi của giải pháp công nghệ đề xuất.

*   **Cổng Khảo sát (Discovery Gate):**
    *   Xác định vấn đề nhức nhối đủ lớn để quy đổi thành tiền mặt hoặc hiệu quả ROI rõ ràng.
    *   Có ít nhất một nguồn dữ liệu hoặc tài liệu thực tế khả dụng để kiểm chứng giả thuyết rủi ro.
    *   Chuyên gia kiểm toán xác nhận phạm vi công việc, nhân sự đầu mối phía khách hàng và góc tiếp cận thương mại.
*   **Cổng Dữ liệu (Data Gate):**
    *   Xác định rõ mức độ chi tiết dữ liệu (grain), khóa liên kết giữa các bảng, các cột thông tin bắt buộc, đơn vị đo lường và khoảng thời gian phân tích dữ liệu.
    *   Trường hợp dữ liệu bị thiếu hoặc tỷ lệ kết nối giữa các bảng quá thấp, AI Agent phải hạ mức độ phân tích hoặc ghi nhận giới hạn phạm vi kiểm toán.
    *   Chuyên gia kiểm toán hoặc người sở hữu dữ liệu phía khách hàng xác nhận sơ đồ khớp nối dữ liệu và các giả định chuẩn hóa.
*   **Cổng Bằng chứng (Evidence Gate):**
    *   Mọi phát hiện sai phạm chính thức đều bắt buộc phải đi kèm Hồ sơ Bằng chứng (Evidence Pack) chi tiết.
    *   Số tiền thất thoát tính toán phải truy vết được về các giao dịch nguồn gốc, tài liệu minh chứng hoặc công thức tính rõ ràng.
    *   Chuyên gia kiểm toán xác nhận mức độ tin cậy của bằng chứng trước khi đưa vào báo cáo gửi ban giám đốc khách hàng.
*   **Cổng Giải pháp (Solution Gate):**
    *   Giải pháp đề xuất bắt buộc phải có giả thuyết về hiệu quả đầu tư (ROI) và lộ trình triển khai chi tiết.
    *   Mỗi đề xuất giải pháp phải liên kết trực tiếp với một phát hiện sai phạm, nguyên nhân gốc rễ, năng lực công nghệ và số tiền tiết kiệm dự kiến.
    *   Khách hàng hoặc bộ phận triển khai kỹ thuật xác nhận tính khả thi của giải pháp, các giới hạn kỹ thuật và nhân sự chịu trách nhiệm vận hành sau bàn giao.
*   **Cổng Thương mại (Commercial Gate):**
    *   Báo cáo kiểm toán cuối cùng phải đưa ra được các đề xuất ký kết hợp đồng thương mại tiếp theo rõ ràng cho Link Strategy.
    *   Mỗi cơ hội giải pháp phải có phạm vi công việc, ước tính nguồn lực triển khai, giá trị mang lại và lý do vì sao khách hàng cần Link Strategy triển khai giải pháp này.
    *   Không bàn giao hồ sơ kiểm toán cuối cùng nếu chưa liên kết được các cơ hội giải pháp công nghệ với các điểm thất thoát dòng tiền lớn đã chứng minh.

### 0.6. Hệ thống Tài liệu Đầu ra (Output Hierarchy)

LS-ASS tạo ra nhiều loại tài liệu đầu ra, mỗi loại giữ một vai trò thương mại riêng biệt để tránh làm loãng thông tin gửi khách hàng.

*   **Hồ sơ Bằng chứng Kiểm toán (Audit Evidence Pack):** Tổng hợp dữ liệu đối soát, chứng từ, hình ảnh, nhật ký hệ thống hoặc biên bản phỏng vấn để bảo vệ tính chính xác của các phát hiện sai phạm.
*   **Báo cáo Kiểm toán cho Ban Giám đốc (Executive Audit Report):** Tài liệu tóm tắt ngắn gọn số tiền thất thoát, các phát hiện sai phạm lớn nhất, nguyên nhân gốc rễ và đánh giá tác động tài chính gửi CFO/CEO.
*   **Bản đồ Cơ hội Giải pháp (Solution Opportunity Map):** Bảng chuyển đổi các phát hiện sai phạm thành cơ hội triển khai công nghệ, gắn với năng lực kỹ thuật và loại hợp đồng thương mại tương ứng.
*   **Tóm tắt Giải pháp Công nghệ (Technology Solution Brief):** Mô tả chi tiết giải pháp dự kiến xây dựng bao gồm vấn đề cần giải quyết, đối tượng sử dụng, dữ liệu đầu vào cần thiết, công nghệ áp dụng, phạm vi thực hiện, giả thuyết hiệu quả ROI và các giới hạn kỹ thuật.
*   **Lộ trình Triển khai Giải pháp (Implementation Roadmap):** Lịch trình thực hiện 30-60-90 ngày nêu rõ người phụ trách, các cột mốc hoàn thành, chi phí, dự kiến số tiền thu hồi, rủi ro và các bước tiếp theo để ký kết hợp đồng.

### 0.7. Quy tắc lựa chọn Công nghệ (Technology Selection Rules)

AI Agent đề xuất công nghệ dựa trên vấn đề nhức nhối thực tế và bằng chứng kiểm toán thu thập được, tuyệt đối không đưa từ ngữ công nghệ vào làm nhãn trang trí. Công nghệ chỉ được đề xuất khi nó giải quyết được thất thoát dòng tiền, giảm thiểu chi phí vận hành, gia tăng doanh số, tăng tốc phê duyệt ra quyết định hoặc khôi phục giá trị sử dụng của hệ thống phần mềm cũ.

*   **Đề xuất Kỹ thuật Dữ liệu & Phân tích khi:**
    *   Dữ liệu nghiệp vụ đã có nhưng nằm rải rác ở nhiều phần mềm (ERP, CRM), nhiều file Excel, nhật ký hệ thống hoặc chứng từ lưu trữ.
    *   Nhu cầu chính là đối soát thông tin giao dịch, làm bảng theo dõi dashboard quản trị, giám sát ngoại lệ hoặc đo lường dòng tiền thất thoát.
*   **Đề xuất Thiết bị cảm biến & IoT khi:**
    *   Trạng thái thực tế của máy móc, nhà kho, dây chuyền sản xuất, xe vận tải không được hệ thống phần mềm ghi nhận đáng tin cậy.
    *   Vấn đề liên quan đến dừng máy sản xuất, thất thoát vật tư hao phí, điều kiện bảo quản thực tế, hoặc các sai lệch ở hiện trường giao nhận.
*   **Đề xuất Học máy & Dự báo khi:**
    *   Cần dự báo xu hướng nhu cầu mua bán, chấm điểm rủi ro tài chính, thiết lập mức chuẩn vận hành tối ưu, phân khúc khách hàng hoặc tìm quy luật bất thường phức tạp vượt qua các quy tắc kiểm tra cố định.
    *   Dữ liệu lịch sử đã có đủ dài và các yếu tố ảnh hưởng tương đối ổn định để xây dựng mô hình dự báo đáng tin cậy.
*   **Đề xuất Trợ lý AI & Tự động hóa quy trình khi:**
    *   Quy trình vận hành gồm nhiều bước lặp đi lặp lại thủ công, phải xử lý lượng lớn văn bản tài liệu, hoặc phát sinh quá nhiều ngoại lệ cần phê duyệt thủ công.
    *   Vấn đề nằm ở việc chậm trễ duyệt cấp hạn mức, chậm nhập dữ liệu lên hệ thống, hoặc thiếu sự kết nối tự động giữa các phòng ban.
*   **Đề xuất Thị giác máy tính - Camera thông minh khi:**
    *   Bằng chứng kiểm toán quan trọng nằm dưới dạng hình ảnh, video giám sát, chứng từ scan, mã vạch sản phẩm hoặc khu vực hàng hóa thực tế.
    *   Vấn đề cần xác thực sự hiện diện của hàng hóa vật lý, kiểm tra chất lượng sản phẩm, đếm số lượng tự động, theo dõi thời gian chờ đợi tại bãi đỗ xe hoặc phát hiện lỗi chứng từ.

---

### Các Giai đoạn Thực thi Chi tiết:

1.  **Giai đoạn 1: Khám phá Quy trình thực tế (Discovery)**
    *   *Mục tiêu:* Đối chiếu SOP, chính sách, phỏng vấn và workaround ngoài hệ thống để dựng bản đồ vận hành thực tế, xác định control gaps và hình thành audit thesis.
    *   *Agent cần biết gì:*
        *   Glossary nghiệp vụ theo domain được chọn; ví dụ PR, PO, GRN, BOM, MRP, DIOH trong Inventory/Procurement hoặc lead, quote, order, SLA trong Revenue/Fulfillment.
        *   Process ontology theo dòng tiền được audit: revenue, margin, spend, working capital, productivity, cashflow hoặc system adoption.
        *   Thư viện Control Point cho các điểm phê duyệt, đối soát, xác minh và bàn giao.
    *   *Agent cần luật/rule nào:*
        *   Fieldwork interpretation dictionary để chuyển lời nói thực địa thành risk hypothesis.
        *   Mapping "nhắn Zalo trước rồi nhập hệ thống sau" thành rủi ro retroactive documentation.
        *   Mapping "Excel riêng" thành shadow process.
        *   Mapping "đặt dư cho chắc" thành defensive ordering.
    *   *Agent cần script/tool nào:*
        *   [discovery_workflow](file:///.agents/workflows/auditor/discovery_workflow.md)
        *   [process-mapping](file:///.agents/skills/auditor/process-mapping/SKILL.md)
        *   [account-scouting](file:///.agents/skills/auditor/account-scouting/SKILL.md)
        *   [auditor-mermaid-expert](file:///.agents/skills/auditor/auditor-mermaid-expert/SKILL.md)
    *   *Agent tạo artifact nào:*
        *   `account-thesis.md`
        *   `process-map.md`
        *   `control-point-table.md`
        *   `pain-map.md`
    *   *Điều kiện pass stage:*
        *   Mọi handoff quan trọng phải có owner, control point, evidence source và risk hypothesis.
        *   Mọi quy trình ẩn phải được gắn với một control gap hoặc một giả thuyết leakage có thể kiểm chứng ở giai đoạn dữ liệu.

2.  **Giai đoạn 2: Chuẩn hóa & Hợp nhất Dữ liệu (Data Ingestion)**
    *   *Mục tiêu:* Chuyển raw CSV/log rời rạc thành Unified Audit Dataset có grain rõ ràng, join được, đo được chất lượng dữ liệu và đủ điều kiện chạy test kiểm toán.
    *   *Agent cần biết gì:*
        *   Data dictionary theo domain.
        *   Grain của từng bảng.
        *   Required columns và optional columns.
        *   Khóa liên kết và ý nghĩa nghiệp vụ của các bảng nguồn; ví dụ PR/PO/BOM/Stock/Consumption/GRN cho Inventory/Procurement hoặc Lead/Quote/Order/Invoice/Payment cho Revenue/Cashflow.
    *   *Agent cần luật/rule nào:*
        *   Schema library.
        *   Alias map cho tên cột.
        *   Normalization specs cho ngày, tiền tệ, UOM, mã vật tư và vendor.
        *   Join specs cho PR -> PO -> GRN -> Inventory -> Consumption -> BOM.
        *   Data quality rules cho null, duplicate, orphan record, join rate, UOM mismatch và ngày giao dịch bất khả thi.
    *   *Agent cần script/tool nào:*
        *   [data_preparation_workflow](file:///.agents/workflows/auditor/data_preparation_workflow.md)
        *   [data-strategy](file:///.agents/skills/auditor/data-strategy/SKILL.md)
        *   `ls-auditor validate`
        *   `ls-auditor normalize`
        *   `ls-auditor join`
        *   `ls-auditor inspect-parquet`
    *   *Agent tạo artifact nào:*
        *   `validation.json`
        *   `normalize.json`
        *   `join.json`
        *   `unified.parquet`
        *   `data-quality-log.md`
        *   `unified-dataset-summary.md`
    *   *Điều kiện pass stage:*
        *   Không được chuyển sang phân tích nếu grain, join key, UOM, required columns hoặc join rate chưa rõ.
        *   Mọi thao tác chuẩn hóa phải tạo artifact dẫn xuất và không được sửa raw data.

3.  **Giai đoạn 3: Tính toán Thất thoát & Đóng gói Bằng chứng (Forensic Execution)**
    *   *Mục tiêu:* Quét Unified Audit Dataset để phát hiện candidate exceptions, tính leakage, ưu tiên rủi ro trọng yếu và đóng gói bằng chứng có thể truy vết.
    *   *Agent cần biết gì:*
        *   Risk pattern library theo domain thương mại được chọn.
        *   Ví dụ Inventory/Procurement: defensive ordering, split PO, emergency buying, mua thêm khi DIOH > 90, PO vượt PR, GRN trước PO.
        *   Ví dụ Revenue/Cashflow: lead bỏ sót, quote chậm, discount leakage, invoice delay, overdue AR, duplicate payment.
        *   Ví dụ Operations/System Adoption: downtime không ghi nhận, rework lặp lại, Excel/Zalo workaround, nhập liệu sau, module hệ thống không được dùng.
    *   *Agent cần luật/rule nào:*
        *   Leakage formula library.
        *   Excess purchase: `(ordered_qty - required_qty_by_bom) * unit_price`.
        *   Capital lock-up: `excess_inventory_qty * unit_cost`.
        *   Price leakage: `(unit_price - target_price) * qty`.
        *   Evidence requirement matrix cho từng loại finding: transaction ID, kỳ dữ liệu, source dataset, control point, calculation trail và confidence level.
    *   *Agent cần script/tool nào:*
        *   [audit_execution_workflow](file:///.agents/workflows/auditor/audit_execution_workflow.md)
        *   [variance-analysis](file:///.agents/skills/auditor/variance-analysis/SKILL.md)
        *   [evidence-packaging](file:///.agents/skills/auditor/evidence-packaging/SKILL.md)
        *   `ls-auditor compute-risks`
        *   `ls-auditor rule-test`
        *   `ls-auditor prioritize`
        *   `ls-auditor trace`
    *   *Agent tạo artifact nào:*
        *   `audit_findings.json`
        *   `prioritized_findings.json`
        *   `candidate-exceptions.md`
        *   `risk-register.md`
        *   `Evidence_Packs/`
    *   *Điều kiện pass stage:*
        *   Mọi exception phải có transaction ID, variance, leakage và risk status.
        *   Chưa có Evidence Pack thì chỉ được gọi là `candidate_exception`, không được nâng thành `confirmed_finding`.

4.  **Giai đoạn 4: Tổng hợp Nguyên nhân & Thiết kế Giải pháp (Synthesis)**
    *   *Mục tiêu:* Gom các exception riêng lẻ thành lỗi hệ thống, xác định root cause và thiết kế intervention roadmap có ROI rõ ràng.
    *   *Agent cần biết gì:*
        *   Root cause taxonomy: policy gap, process bypass, data latency, master data issue, incentive misalignment, ERP adoption failure và approval design failure.
        *   Solution pattern library: freeze rule, approval gate, BOM tolerance control, inventory dashboard, MRP visibility fix và monthly governance review.
        *   Technology capability map để nối root cause với Data, IoT, ML, AI Agent hoặc CV.
    *   *Agent cần luật/rule nào:*
        *   Exception-to-root-cause mapping.
        *   Systemic failure classification rules để phân biệt human error với design failure.
        *   ROI assumption library cho savings rate, recovery period, implementation cost, confidence level và payback logic.
        *   Solution classification rule: mỗi intervention phải thuộc `Control Automation`, `Decision Intelligence` hoặc `Operational Digitization`.
    *   *Agent cần script/tool nào:*
        *   [solution_packaging_workflow](file:///.agents/workflows/auditor/solution_packaging_workflow.md)
        *   [root-cause-synthesis](file:///.agents/skills/auditor/root-cause-synthesis/SKILL.md)
        *   [solution-design](file:///.agents/skills/auditor/solution-design/SKILL.md)
        *   `synthesis_helper.py`
        *   `roi_calculator.py`
    *   *Agent tạo artifact nào:*
        *   `problem-classification.md`
        *   `intervention-thesis.md`
        *   `solution-proposal.md`
        *   `solution-opportunity-map.md`
    *   *Điều kiện pass stage:*
        *   Mỗi systemic risk phải nối được với exception IDs, control gap và leakage.
        *   Mỗi solution phải nối được với finding, root cause, owner, cost, saving, ROI assumption và payback period.
        *   Mỗi solution phải chỉ rõ capability công nghệ được dùng và loại hợp đồng triển khai có thể mở ra.

5.  **Giai đoạn 5: Xuất bản Báo cáo cuối cùng (Publishing)**
    *   *Mục tiêu:* Lắp ghép toàn bộ audit dossier thành báo cáo CFO/CEO đọc được, có số liệu nhất quán, bằng chứng truy vết được và đề xuất can thiệp có tính thương mại.
    *   *Agent cần biết gì:*
        *   Report structure contract gồm executive summary, leakage summary, top findings, evidence index, root cause, intervention roadmap, ROI, limitations và appendix.
        *   CFO language/style guide để viết ngắn, sắc, tập trung vào dòng tiền và rủi ro quản trị.
        *   Solution proposal structure để biến audit conclusion thành buildable technology brief.
    *   *Agent cần luật/rule nào:*
        *   Number traceability map để mọi số liệu trong report khớp với artifact nguồn.
        *   Consistency checker cho leakage, finding và ROI.
        *   Diagram requirements cho process map, control gap map, evidence flow và root cause tree.
    *   *Agent cần script/tool nào:*
        *   [final_report_workflow](file:///.agents/workflows/auditor/final_report_workflow.md)
        *   [writing-clearly-and-concisely](file:///.agents/skills/common/writing-clearly-and-concisely/SKILL.md)
        *   `ls-auditor chart`
        *   `ls-auditor assemble-report`
        *   Công cụ export PDF/DOCX nếu môi trường bàn giao yêu cầu.
    *   *Agent tạo artifact nào:*
        *   `FINAL_AUDIT_REPORT.md`
        *   `technology-solution-brief.md`
        *   `implementation-roadmap.md`
        *   Evidence index.
        *   Appendix.
        *   PDF/DOCX nếu có export tool.
    *   *Điều kiện pass stage:*
        *   Mọi số liệu trong final report phải truy vết được về artifact nguồn.
        *   Mọi finding phải có evidence confidence.
        *   Số leakage trong report, risk register, evidence pack và solution proposal phải đồng nhất.
        *   Mỗi solution opportunity phải có pain point, technology capability, ROI hypothesis, implementation scope và next-step commercial ask.

