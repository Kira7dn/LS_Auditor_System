# HỆ THỐNG HỖ TRỢ KIỂM TOÁN LS (LS-ASS)
### *Thiết kế Nền móng & Chiến lược Vận hành Hệ thống*

---

## I. TẦM NHÌN CHIẾN LƯỢC & MỤC ĐÍCH TỐI THƯỢNG (STRATEGIC VISION)

### 1. Định vị Hệ thống (Strategic Positioning)
LS-ASS là hệ điều hành nội bộ của Link Strategy để chuẩn hóa quy trình khảo sát thực địa, định lượng thất thoát tài chính, đóng gói bằng chứng và thiết kế đề xuất giải pháp công nghệ. 
Hệ thống vận hành theo triết lý **Tư vấn từ Thất thoát đến Giải pháp (Leakage-to-Solution)**: Khởi đầu bằng việc phát hiện và chứng minh số tiền thất thoát dòng tiền (Leakage) thực tế của doanh nghiệp, sau đó mới đề xuất giải pháp công nghệ phù hợp (Dữ liệu, IoT, Học máy/AI, Thị giác máy tính hoặc Tích hợp) nhằm khôi phục giá trị sử dụng thực tế của hệ thống phần mềm cũ (ERP, CRM) và quy trình vận hành.

### 2. Ba Mục đích Tối thượng
*   **Mở đường thương mại (Commercial Wedge):** Sử dụng số tiền thất thoát thực tế (Leakage) để thuyết phục CFO/CEO ký hợp đồng triển khai công nghệ giá trị cao.
*   **Giải cứu hệ thống (Client Value):** Triệt tiêu các quy trình thủ công ngoài hệ thống (Zalo, Excel), khôi phục năng suất và thu hồi dòng tiền bị rò rỉ.
*   **Đóng gói tri thức (LS Leverage):** Đóng gói kinh nghiệm thực địa thành các bộ quy chuẩn có cấu hình sẵn (Domain Packs) để nhân rộng mô hình kinh doanh.

---

## II. HỢP ĐỒNG DỮ LIỆU & HỆ THỐNG SẢN PHẨM ĐẦU RA (DATA & OUTPUT CONTRACT)

### 1. Dữ liệu thô đầu vào (Input Requirements)
*   **Dữ liệu hệ thống:** Các bảng giao dịch kết xuất (PO, PR, BOM, GRN, Stock, Logs).
*   **Quy trình chính thức:** Chính sách duyệt, hạn mức chi tiêu, SOPs.
*   **Hồ sơ thực địa:** Biên bản phỏng vấn, bằng chứng quy trình tự phát (Excel, Zalo).
*   **Thông số chi phí:** Đơn giá nhân công, OpEx, chi phí duy trì phần mềm cũ.

### 2. Hệ thống sản phẩm bàn giao (Output Hierarchy)
*   **Hồ sơ Bằng chứng (Evidence Pack):** Tập hợp chứng từ đối soát, log hệ thống, công thức tính toán truy vết trực tiếp về giao dịch gốc để bảo vệ tính pháp lý của lỗi.
*   **Báo cáo Kiểm toán (Executive Report):** Tài liệu ngắn gọn trình bày số tiền thất thoát, phân tích nguyên nhân gốc rễ và tác động tài chính gửi CFO/CEO.
*   **Bản đồ Cơ hội Giải pháp (Opportunity Map):** Bảng chuyển đổi các phát hiện thất thoát thành cơ hội can thiệp công nghệ, gắn với năng lực kỹ thuật và loại hợp đồng.
*   **Tóm tắt Giải pháp Công nghệ (Solution Brief):** Tài liệu đặc tả giải pháp đề xuất (đối tượng dùng, dữ liệu cần, công nghệ áp dụng, giả thuyết ROI và giới hạn kỹ thuật).
*   **Lộ trình Triển khai (Roadmap):** Kế hoạch hành động 30-60-90 ngày (người phụ trách, chi phí, mức tiết kiệm dự kiến, thời gian hoàn vốn và các bước thương mại tiếp theo).

---

## III. BẢN ĐỒ MIỀN KIỂM TOÁN & CÔNG NGHỆ CAN THIỆP (AUDIT DOMAINS & INTERVENTION MAP)

*Quy tắc chọn công nghệ:* Chỉ đề xuất công nghệ khi nó giải quyết được thất thoát dòng tiền, giảm OpEx hoặc phục hồi giá trị phần mềm cũ. Tuyệt đối không dùng công nghệ làm nhãn trang trí.

| Miền Kiểm toán | Triệu chứng & Thất thoát (Leakage Point) | Năng lực công nghệ phát hiện/chặn | Mô hình Giải pháp Can thiệp (Intervention Solution) | Độ ưu tiên (Priority) |
| :--- | :--- | :--- | :--- | :--- |
| **1. Mua sắm & Nhà cung cấp** | Mua đắt, né hạn mức duyệt (split PO), gian lận định mức dịch vụ ngoài/outsource, thanh toán sai SLA của nhà thầu. | Phân tích spend; Đối soát chấm công chéo cho nhà thầu; AI phát hiện bất thường PO. | Bảng giám sát chi phí nhà cung cấp & quy trình duyệt/nghiệm thu dịch vụ tự động. | **High (P1)** |
| **2. Biên lợi nhuận & Giá** | Chiết khấu tràn lan, báo giá sai lệch, không cập nhật kịp thời giá vốn vào giá bán. | Quy tắc kiểm soát giá tự động; Học máy chấm điểm lợi nhuận. | Tháp kiểm soát giá bán & quy trình duyệt chiết khấu tự động (Control Gate). | **High (P1)** |
| **3. Hiệu suất Thiết bị, Downtime & Năng lượng** | Máy dừng hoạt động không rõ lý do, OEE thấp, lãng phí năng lượng (điện/khí nén) chạy không tải. | IoT kết nối máy (PLC/SCADA); Camera AI trạng thái máy; ML phát hiện hao phí năng lượng ca làm. | Hệ thống giám sát OEE & tối ưu hóa điện năng tiêu thụ thời gian thực. | **High (P1)** |
| **4. Dòng tiền & Công nợ** | Vốn kẹt ở nợ phải thu, thanh toán trùng lặp cho NCC, hóa đơn gửi chậm, treo tạm ứng. | Thuật toán đối soát dữ liệu tài chính tự động; Trợ lý AI hỗ trợ nhắc nợ và phân loại công nợ. | Trung tâm quản lý thu hồi dòng tiền & hệ thống phát hiện thanh toán bất thường. | **High (P1)** |
| **5. Hao hụt Vật liệu, Chất lượng & Hải quan (Yield & Customs)** | Hao hụt nguyên vật liệu vượt định mức BOM, tỷ lệ phế phẩm cao, lệch định mức thực tế vs hải quan gây phạt thuế/mất hoàn thuế. | Camera AI kiểm lỗi sản phẩm trên băng chuyền (CV); AI đối soát tờ khai hải quan ↔ BOM sản xuất ↔ Invoice. | Hệ thống kiểm soát chất lượng tự động hóa & công cụ kiểm toán hoàn thuế nhập khẩu. | **Medium (P2)** |
| **6. Tồn kho & Vốn lưu động (bao gồm MRO)** | Đọng vốn kho thành phẩm/phụ tùng bảo trì (MRO), lệch tồn kho vật tư, thiếu linh kiện gây dừng máy đột xuất. | Cảm biến IoT vị trí vật tư; Camera đếm hàng tự động; ML dự báo nhu cầu phụ tùng MRO và tồn kho an toàn. | Hệ thống giám sát kho thông minh & cảnh báo sớm thiếu hụt/ứ đọng vật tư bảo trì. | **Medium (P2)** |
| **7. Chi phí Lao động & Năng suất** | OT ảo/gian lận chấm công, lệch công giữa sinh trắc học và nhật ký thao tác hệ thống (ERP/CRM/PLC), lãng phí định mức lao động. | Thuật toán đối soát chéo sinh trắc học và log hệ thống; Process Mining; ML chấm điểm năng suất lao động thực tế. | Hệ thống giám sát hiệu suất lao động thời gian thực & cảnh báo sớm gian lận công nhật. | **Medium (P2)** |
| **8. Doanh thu, Tiếp thị & Dự báo nhu cầu** | Thiếu hàng bán, dự báo nhu cầu sai lệch, rò rỉ ngân sách marketing do click ảo/lead rác. | Tích hợp dữ liệu doanh nghiệp; ML dự báo nhu cầu; AI phát hiện bot và gian lận IP/chuyển đổi phễu marketing. | Hệ thống dự báo nhu cầu bán hàng & bảng kiểm soát hiệu quả tiếp thị số sạch. | **Medium (P2)** |
| **9. Hiệu quả sinh lời đa chiều** | Không rõ khách hàng, SKU hay nhà cung cấp nào thực sự mang lại lợi nhuận sau khi trừ Cost-to-Serve. | Mô hình tính giá thành đầy đủ; Thuật toán phân khúc khách hàng/sản phẩm bằng ML. | Hệ thống phân tích lợi nhuận đa chiều & bảng chấm điểm hiệu quả SKU/khách hàng. | **Low (P3)** |
| **10. Đơn hàng & SLA Giao nhận** | Giao hàng trễ hạn phát sinh phạt SLA, tỷ lệ trả hàng cao, quy trình xử lý lặp lại thủ công. | GPS định vị lộ trình; Camera xác minh giao nhận (POD); ML dự báo thời gian giao hàng (ETA). | Bảng giám sát tiến độ giao hàng & hệ thống cảnh báo sớm nguy cơ trễ SLA. | **Low (P3)** |

### *Cấu trúc Gói Nghiệp vụ (Domain Pack Structure)*
Mỗi miền kiểm toán ở trên được đóng gói thành một **Gói Nghiệp vụ (Domain Pack)** làm tài sản trí tuệ cốt lõi nạp vào Agent khi thực thi, bao gồm:
*   **Gói tri thức (Knowledge Pack):** Control points và lỗi hệ thống phổ biến của từng mảng.
*   **Từ điển thực địa (Terminology Pack):** Tập hợp từ lóng vận hành (như "làm ngoài", "nhập sau", "dùng Excel riêng") giúp AI hiểu ngôn ngữ thực tế của nhân sự.
*   **Quy tắc phát hiện rủi ro (Rule Pack):** Công thức toán học tính toán thất thoát (như Excess Purchase, Capital Lock-up, Price Leakage) và tiêu chuẩn bằng chứng tối thiểu.
*   **Bộ công cụ thực thi (Execution Pack):** Các script dòng lệnh (phân hệ lệnh ls-auditor) và các workflow tương ứng.
*   **Biểu mẫu đầu ra (Evidence & Reporting Pack):** Mẫu Evidence Pack, Executive Report và Solution Proposal.

---

## IV. QUY TRÌNH THỰC THI 5 BƯỚC & CỔNG KIỂM SOÁT (EXECUTION & STAGE GATES)

```mermaid
graph LR
    G1[Khám phá] -->|Khảo sát Gate| G2[Dữ liệu]
    G2 -->|Dữ liệu Gate| G3[Kiểm toán]
    G3 -->|Bằng chứng Gate| G4[Giải pháp]
    G4 -->|Giải pháp Gate| G5[Báo cáo]
    G5 -->|Thương mại Gate| Close[Ký Hợp đồng]
```

### Bước 1: Khám phá Quy trình thực tế (Discovery Phase)
*   **Mục tiêu:** Đối chiếu SOP với phỏng vấn thực địa để dựng bản đồ vận hành thực tế, phát hiện các quy trình ẩn (shadow processes) và lập giả thuyết thất thoát.
*   **Công cụ/Kỹ năng:** `discovery_workflow`, `process-mapping`, `account-scouting`, `auditor-mermaid-expert`.
*   **Sản phẩm:** `account-thesis.md`, `process-map.md`, `control-point-table.md`, `pain-map.md`.
*   **Cổng kiểm soát (Discovery Gate Pass):** 
    *   Mọi handoff chính phải có owner, control point, và nguồn bằng chứng.
    *   Mọi quy trình ẩn phải được gắn với một giả thuyết thất thoát có thể kiểm chứng bằng dữ liệu.

### Bước 2: Chuẩn hóa & Hợp nhất Dữ liệu (Data Ingestion Phase)
*   **Mục tiêu:** Chuyển dữ liệu thô (raw CSV/logs) thành tập dữ liệu hợp nhất (Unified Audit Dataset) có grain rõ ràng, đã join và kiểm tra chất lượng dữ liệu.
*   **Công cụ/Kỹ năng:** `data_preparation_workflow`, `data-strategy`, `ls-auditor validate/normalize/join/inspect-parquet`.
*   **Sản phẩm:** `validation.json`, `normalize.json`, `join.json`, `unified.parquet`, `data-quality-log.md`.
*   **Cổng kiểm soát (Data Gate Pass):**
    *   Xác định rõ grain, join key, required columns, UOM và tỷ lệ join rate đạt chuẩn (>90%).
    *   Không sửa dữ liệu gốc; mọi thao tác chuẩn hóa phải được ghi nhận qua script/log rõ ràng.

### Bước 3: Tính toán Thất thoát & Đóng gói Bằng chứng (Forensic Execution)
*   **Mục tiêu:** Quét tập dữ liệu hợp nhất để phát hiện các ngoại lệ (exceptions), tính toán số tiền thất thoát cụ thể và đóng gói bằng chứng có thể truy vết.
*   **Công cụ/Kỹ năng:** `audit_execution_workflow`, `variance-analysis`, `evidence-packaging`, `ls-auditor compute-risks/rule-test/prioritize/trace`.
*   **Sản phẩm:** `audit_findings.json`, `prioritized_findings.json`, `candidate-exceptions.md`, thư mục `Evidence_Packs/`.
*   **Cổng kiểm soát (Evidence Gate Pass):**
    *   Mọi ngoại lệ chính thức phải có Transaction ID, số tiền thất thoát cụ thể và công thức tính.
    *   Tuyệt đối không đưa vào báo cáo các ngoại lệ chưa được đóng gói thành Evidence Pack đầy đủ chứng từ nguồn.

### Bước 4: Tổng hợp Nguyên nhân & Thiết kế Giải pháp (Synthesis Phase)
*   **Mục tiêu:** Gom các lỗi riêng lẻ thành lỗi hệ thống (systemic failure), phân tích nguyên nhân gốc rễ và thiết kế lộ trình can thiệp công nghệ có ROI rõ ràng.
*   **Công cụ/Kỹ năng:** `solution_packaging_workflow`, `root-cause-synthesis`, `solution-design`.
*   **Sản phẩm:** `problem-classification.md`, `intervention-thesis.md`, `solution-proposal.md`, `solution-opportunity-map.md`.
*   **Cổng kiểm soát (Solution Gate Pass):**
    *   Mỗi giải pháp can thiệp phải liên kết trực tiếp với lỗi hệ thống, năng lực công nghệ và số tiền tiết kiệm dự kiến.
    *   Giải pháp phải được phân loại rõ ràng (`Control Automation`, `Decision Intelligence` hoặc `Operational Digitization`) kèm giả định ROI khả thi.

### Bước 5: Xuất bản Báo cáo cuối cùng (Publishing Phase)
*   **Mục tiêu:** Lắp ghép toàn bộ hồ sơ kiểm toán thành báo cáo CFO-ready có số liệu nhất quán, trực quan và đề xuất can thiệp thương mại sắc bén.
*   **Công cụ/Kỹ năng:** `final_report_workflow`, `writing-clearly-and-concisely`, `ls-auditor chart/assemble-report`.
*   **Sản phẩm:** `FINAL_AUDIT_REPORT.md`, `technology-solution-brief.md`, `implementation-roadmap.md`.
*   **Cổng kiểm soát (Commercial Gate Pass):**
    *   Mọi số liệu trong báo cáo cuối cùng phải khớp hoàn toàn với các artifact nguồn và hồ sơ bằng chứng.
    *   Báo cáo chỉ được bàn giao khi có các đề xuất thương mại tiếp theo rõ ràng (giải pháp đề xuất, chi phí đầu tư dự kiến, ROI và thời gian hoàn vốn).
