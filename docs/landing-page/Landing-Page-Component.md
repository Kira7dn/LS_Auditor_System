## 0) Design tokens (mapping màu → variant)

- **Primary (default):** Deep Navy (brand trust / corporate infrastructure / audit authority)
- **Secondary:** Antique Gold (financial growth / ROI / value recovery)
- **Accent:** Sage Teal (AI forensics / smart-but-controlled automation)
- **Muted:** Slate Gray scale (body text, thin grid lines, borders)
- **Background:** `background` / `muted` theo theme shadcn (sleek dark mode / high-contrast light mode)

> Trong Shadcn: `Button variant="default|secondary|outline|ghost"`, `Badge variant="default|secondary|outline"`, `Alert variant="default|destructive"` (destructive chỉ khi hiển thị rủi ro rò rỉ khẩn cấp).

---

## 1) App Shell / Layout (global)

### A. `LandingLayout`

- **Container:** `<div>` (page wrapper)
- **Component:** `Header` (sticky, frosted glass effect)
- **Component:** `Main`
- **Component:** `Footer`

### B. `Header`

- **Container:** `Container` (div max-w)
- **Navigation:** `NavigationMenu` (Solutions, Monetization, Case Studies, AI Diagnostics)
- **Logo:** `Image` (LS logo - minimalist geometric representation of connecting dots)
- **Buttons:**
  - `Button variant="ghost"` (Operator Circle / Newsletter)
  - `Button variant="outline"` (Secondary CTA: “Read Case Studies”)
  - `Button variant="default"` (**Primary CTA**: “Run Free Diagnosis”)

---

## 2) Hero Section (Chống rò rỉ dòng tiền vận hành)

### Component tree

- **Section Container:** `<section>` + `Container` (Dark corporate background with subtle grid lines)
- **Text stack:** `<div>` (Centered or Left-aligned for split screen)
- **Headline:** `Typography (H1)` — "Khai thác dòng tiền kẹt trong các hệ thống phần mềm cũ"
- **Sub-headline:** `Typography (lead)` — "Kiểm soát thất thoát (Leakage) và xử lý triệt để việc nhân sự bypass quy trình qua Excel, Zalo."
- **Supporting paragraph:** `Typography (p)` — "Hệ thống AI Auditor Agent giúp bạn tự động chẩn đoán rủi ro kiểm soát, dựng sơ đồ quy trình Mermaid và ước tính thiệt hại tài chính chỉ trong 10 phút."
- **Clarifying line:** `Badge` group or `Text + Separator`
  - `Badge variant="secondary"` (Gold) cho “Leakage-Led Consulting”
  - `Badge variant="outline"` (Slate) cho “Enterprise NDA Secured”
  - `Badge variant="outline"` (Teal border/text) cho “AI-assisted, Operator-controlled”

- **CTA row:**
  - `Button variant="default"` (**Primary/Navy**) — “Khởi chạy AI Diagnostics miễn phí”
  - `Button variant="outline"` (**Neutral**) — “Xem cách LS Auditor chẩn đoán rủi ro”

- **Interactive Diagnostic Assets Quick Access (Lead Magnets):**
  - Grid 2 cột:
    - Card 1: **ERP Graveyard Score** (Đo lường mức độ lãng phí & tỷ lệ bỏ hoang ERP)
      - *UI/UX Behavior:* Khảo sát nhanh 5 câu trắc nghiệm (nhà cung cấp ERP, tuổi đời hệ thống, số lượng phê duyệt ngoài luồng, tỷ lệ báo cáo dùng Excel). Tính toán điểm số phế thải (0-100) và xuất cảnh báo tức thì ngay sau khi nhập email công việc.
    - Card 2: **Shadow Operation Scanner** (Đo lường tần suất nhân sự làm việc ngoài hệ thống)
      - *UI/UX Behavior:* Thanh kéo tương tác (Slider) chọn số lượng workflow bị bypass qua Zalo/Excel. Render biểu đồ trực quan hóa tỷ lệ phần trăm dữ liệu "bị mù" (không được hệ thống ghi nhận) theo thời gian thực.

---

## 3) Section 2 — “Giải cứu giá trị hệ thống phần mềm cũ”

### Component tree

- **Section Container:** `<section>` + `Container`
- **Grid:** `<div className="grid ...">` (2 columns desktop)
- **Left column (Copy & Thesis):**
  - `Typography (H2)` — "Tại sao hơn 70% dự án ERP không bao giờ đi vào vận hành thực tế?"
  * `Typography (p)` — Giải thích hiện tượng "Software Graveyard" (Nghĩa địa phần mềm): Phần mềm mua giá tỷ đồng nhưng tỷ lệ hấp thụ workflow thực tế giảm sâu sau 18 tháng. Nhân viên chuyển sang làm tay qua Excel và Zalo gây mất kiểm soát dòng tiền nghiêm trọng.
  - `Button variant="outline"` (Teal) cho "Xem báo cáo nghiên cứu sâu"

- **Right column (Operational Anti-Patterns):** dùng `Card`
  - `Card` (tone nhẹ, `muted` background)
    - `CardHeader` (title “Shadow Operations”)
    - `CardContent` — Bullet các lỗ hổng:
      - Duyệt giá mua sắm bằng Zalo không lưu vết.
      - Chốt công nợ, tồn kho lệch qua file Excel cá nhân.
      - Dữ liệu đối soát tĩnh, chỉ nhìn thấy lỗi khi tiền đã mất.

  - `Card` (tone nhẹ)
    - `CardHeader` (title “Invisible Leakage”)
    - `CardContent` — Bullet các thất thoát:
      - Trả tiền cho license không dùng (lãng phí ghế hoạt động).
      - Rò rỉ trong mua sắm và chiết khấu nhà cung cấp do không đối soát tự động.
      - Máy móc downtime và đứt gãy SLA giao hàng không quy trách nhiệm được.

  - `Card` (tone nhẹ)
    - `CardHeader` (title “AI Adoption Failure”)
    - `CardContent` — Bullet các lãng phí:
      - Tích hợp AI đắt đỏ vào một quy trình vận hành vốn đã hỗn loạn và chắp vá.
      - Dữ liệu thô chưa được làm sạch khiến mô hình AI chẩn đoán sai lệch.
      - Thiếu điểm kiểm soát (CCP) rõ ràng dẫn đến việc ứng dụng AI không đo lường được ROI.

---

## 4) Section 3 — “LS Auditor là gì?”

### Component tree

- **Section Container:** `<section>` + `Container`
- **Intro copy:** `Typography (H2 + p)` — "Không chỉ là kiểm toán. Đây là hệ thống can thiệp tự động."
- **Clarifying block (Tránh hiểu nhầm):** `Alert`
  - `Alert variant="default"` (Neutral/muted)
  - Nhấn mạnh: *"LS Auditor KHÔNG phải là một đơn vị tư vấn giấy tờ truyền thống, cũng KHÔNG phải công cụ đăng bài hay tăng trưởng nóng. Chúng tôi là Auditor-led Intervention Studio."*
    - `Badge variant="outline"` + icon (lucide) trong `AlertTitle`

- **Conceptual breakdown (4 pillars):** `Card` grid
  - 4 × `Card`
    - `CardHeader` (Title: Detect Leakage / Map Controls / Trace Evidence / Automate Intervention)
    - `CardContent` — 1-2 câu giải thích:
      - *Detect Leakage:* Định lượng dòng tiền thất thoát thay vì bắt lỗi cá nhân.
      - *Map Controls:* Tự động vẽ bản đồ quy trình Mermaid để phát hiện điểm gãy.
      - *Trace Evidence:* Trích xuất Evidence Pack với log giao dịch thật, không suy diễn.
      - *Automate Intervention:* Chặn rủi ro bằng tích lũy module/SaaS thay vì tăng nhân sự.

---

## 5) Section 4 — Lĩnh vực Đối soát Trọng điểm (Pre-built Domain Packs)

### Component tree

- **Section Container:** `<section>` + `Container`
- **Headline + intro:** `Typography (H2 + p)` — "Sẵn sàng cho các bài toán đối soát phức tạp"
  - *Sub-headline:* "Chúng tôi cung cấp các gói thư viện luật (Domain Packs) được đóng gói sẵn cho các lĩnh vực rủi ro cao nhất."
- **Grid:** `<div className="grid ...">` (4 columns desktop)
  - 4 × `Card` (tương ứng với 4 nhóm đối soát cốt lõi)
    - **Card 1: Mua sắm & Nhà cung cấp (Procurement & Supplier - P1)**
      - `CardHeader` (Title: Procurement Audit)
      - `CardContent`:
        - Kiểm tra chênh lệch đơn giá mua thực tế và đơn giá ký hợp đồng khung.
        - Phát hiện rò rỉ chiết khấu và điều khoản thanh toán phạt chậm.
        - Đối soát chất lượng giao hàng và thời gian đáp ứng nhà cung cấp.
    - **Card 2: Hiệu suất & Downtime Thiết bị (Equipment Efficiency & Downtime - P1)**
      - `CardHeader` (Title: Asset Efficiency)
      - `CardContent`:
        - Phân tích log thiết bị để phát hiện downtime không khai báo.
        - Đối soát dữ liệu ca máy với bảng lương và năng suất thực tế.
        - Cảnh báo đứt gãy SLA giao hàng do sự cố thiết bị tại hiện trường.
    - **Card 3: Tồn kho & Kho vận (Inventory & Warehouse - P2)**
      - `CardHeader` (Title: Inventory Control)
      - `CardContent`:
        - Đối soát sai lệch giữa dữ liệu hệ thống (ERP) và kiểm kê thực tế.
        - Phát hiện thất thoát hàng hóa trong luồng luân chuyển nội bộ.
        - Nhận diện hàng chậm luân chuyển và rủi ro hết hạn sử dụng.
    - **Card 4: Đối soát Dòng tiền & Công nợ (Cashflow & Invoicing - P2)**
      - `CardHeader` (Title: Cashflow Reconciliation)
      - `CardContent`:
        - Tự động khớp hóa đơn đầu vào, phiếu nhập kho và chứng từ thanh toán (3-Way Matching).
        - Phát hiện thanh toán trùng lặp hoặc thanh toán sai đối tượng.
        - Giám sát tiến độ thu hồi công nợ và rủi ro dòng tiền âm.

---

## 6) Section 5 — “Quy trình chẩn đoán tự động (Trong thực tế)”

### Component tree (flow 4 bước chẩn đoán)

- **Section Container:** `<section>` + `Container`
- **Stepper:** (custom wrapper) + mỗi step dùng `Card`
  - 4 × `Card`
    - `CardHeader`
      - `Badge variant="secondary"` (Gold) hiển thị “Bước 1/2/3/4”
      - `CardTitle`

    - `CardContent`
      - `ul/li` (các hành động và output của từng bước)
      - *Bước 1 (Mô tả vận hành):* Nhập kịch bản quy trình hiện tại của doanh nghiệp.
      - *Bước 2 (Mô hình hóa rủi ro):* AI Agent tự động vẽ sơ đồ Mermaid và xác định Điểm kiểm soát yếu (CCP).
      - *Bước 3 (Ước tính rò rỉ):* Nhận báo cáo định lượng thiệt hại tài chính dự kiến (PDF).
      - *Bước 4 (Ký NDA đối soát):* Kết nối với chuyên gia con người của LS để chạy phân tích dữ liệu thật.

- **Reassurance block:**
  - `Alert variant="default"` (Muted) chứa câu: *"Bảo mật tuyệt đối: Mọi thông tin mô tả quy trình của bạn được xử lý cục bộ và không dùng để train các mô hình AI công cộng."*

---

## 7) Section 6 — Khả năng kỹ thuật của LS-ASS

### Component tree

- **Section Container:** `<section>` + `Container`
- **Headline + intro:** `Typography (H2 + p)` — "Bộ công cụ chẩn đoán và can thiệp vận hành toàn diện"
- **Capabilities list:** dùng `Accordion` (Feature → What it does → Why it matters)
  - `Accordion type="single" collapsible`
  - `AccordionItem` × 5
    - `AccordionTrigger` (Feature name)
    - `AccordionContent`
      - `Badge variant="outline"` (Teal) cho “Cách hoạt động”
      - `Badge variant="secondary"` (Gold) cho “Giá trị thương mại”
      - Nội dung:
        1. *Normalize & Join CLI (normalize_cli, join_cli):* Hợp nhất và chuẩn hóa các nguồn dữ liệu thô rời rạc (ERP, Excel, Zalo Logs) về một định dạng thống nhất.
        2. *Forensic Risk Engine (compute_cli):* Chạy các quy tắc đối soát tự động để phát hiện các ngoại lệ và giao dịch bất thường.
        3. *Rule Test CLI (rule_test_cli):* Môi trường sandbox chạy thử và kiểm thử độ chính xác của các gói luật đối soát tùy chỉnh trước khi áp dụng.
        4. *Mermaid Control Point Mapper:* Tự động vẽ luồng dữ liệu và đánh dấu các điểm thắt nút cổ chai, điểm kiểm soát yếu (CCP).
        5. *Evidence Pack Packager:* Đóng gói hồ sơ bằng chứng có đầy đủ timestamp, transaction ID để đảm bảo tính liêm chính của bằng chứng.
        6. *Intervention Templates:* Các blueprint/safeguards lập trình sẵn để cắm trực tiếp vào hệ thống cũ nhằm khóa chặn rủi ro thất thoát.

---

## 8) Section 7 — Chỉ số hấp thụ & Hiệu quả (Adoption KPIs)

### Component tree

- **Section Container:** `<section>` + `Container`
- **Outcomes grid:** 4 × `Card`
  - `CardHeader` (Outcome title)
  - `CardContent`
    - *Workflow Completion Rate:* Nâng tỷ lệ task chạy trong hệ thống lên >90% (loại bỏ Excel/Zalo).
    - *Manual Workaround Rate:* Giảm tần suất nhân sự làm ngoài hệ thống xuống dưới 5%.
    - *Audit Retrieval Time:* Giảm thời gian trích xuất bằng chứng từ >30 phút xuống dưới 5 phút.
    - *License Utilization:* Tối ưu hóa ghế active ERP để cắt giảm tới 30% chi phí license lãng phí.

---

## 9) Pricing Section (Monetization Ladder)

### Component tree

- **Section Container:** `<section>` + `Container`
- **Monetization Cards (4 Offers):** `Card` grid
  
  - **1. AI Self-Diagnostic (Tầng 1)**
    - `Badge variant="outline"` (Muted) — "Free & Instant"
    - `CardTitle` — "Tự chẩn đoán rủi ro"
    - `CardContent` — Interactive chat session với AI Auditor Agent, nhận sơ đồ Mermaid & báo cáo rủi ro sơ bộ.
    - `Button variant="secondary"` (Gold) — "Start Chat Now"

  - **2. Business Graveyard Audit (Tầng 2)**
    - `Badge variant="secondary"` (Gold) — "NDA Secured"
    - `CardTitle` — "Đối soát dữ liệu có phí"
    - `CardContent` — Ký NDA bảo mật, đối soát dữ liệu thô (ERP, Logs) để xuất hồ sơ bằng chứng (Evidence Pack) chỉ rõ số tiền thất thoát. Giá chỉ định: **$3k - $10k / Sprint**.
    - `Button variant="default"` (Primary/Navy) — "Request Diagnostic Project"

  - **3. Intervention Pilot (Tầng 3)**
    - `Badge variant="default"` (Primary/Navy) — "ROI Guaranteed"
    - `CardTitle` — "Triển khai can thiệp"
    - `CardContent` — Tái lập quy trình, cài đặt hệ thống can thiệp, khóa điểm lỗi (AI/IoT/ML) với cam kết thu hồi dòng tiền. Giá chỉ định: **$10k - $35k / Pilot**.
    - `Button variant="default"` (Primary/Navy) — "Talk to Intervention Team"

  - **4. SaaS Enterprise License (Tầng 4)**
    - `Badge variant="outline"` (Teal) — "Continuous Protection"
    - `CardTitle` — "Giám sát định kỳ"
    - `CardContent` — Thuê bao phần mềm duy trì các luật đối soát tự động, cảnh báo rò rỉ thời gian thực. Giá chỉ định: **$2k - $8k / Tháng**.
    - `Button variant="outline"` (Neutral) — "Contact for Enterprise Contract"

---

## 10) Footer

- **Container:** `Container`
- **Links:** `NavigationMenu` (TOS, Privacy, Acceptable Use, AI Policy)
- **Legal:** `Typography muted` — "© 2026 Link Strategy. All rights reserved. LS Auditor and LS-ASS are registered trademarks of Link Strategy."
- **Contact:** `Typography` — "legal@linkstrategy.vn | privacy@linkstrategy.vn"
- **Mini CTA:** `Button variant="outline"` (Neutral) — "Join Operator Circle Newsletter"
