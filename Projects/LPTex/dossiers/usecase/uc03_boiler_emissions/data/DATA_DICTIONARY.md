# DATA DICTIONARY: USE CASE 03 (BOILER EMISSIONS & ESG CARBON LEDGER)

Định nghĩa cấu trúc dữ liệu mô phỏng phục vụ thuật toán giám sát phát thải lò hơi và năng lượng điện LPTex:

## 1. Bảng `boiler_emissions` (Giám sát Phát thải & Tiêu hao năng lượng)
* **date** (DATE): Ngày vận hành.
* **coal_purchased_tons** (FLOAT): Khối lượng than cám nhập kho theo hóa đơn VAT mua than từ kế toán (tấn).
* **steam_produced_m3** (FLOAT): Lượng hơi nước sinh ra thực tế đo bằng đồng hồ đo lưu lượng hơi ($m^3$).
* **co2_emission_sensor_kg** (FLOAT): Lượng phát thải CO2 đo bằng cảm biến ống khói lò hơi (kg).
* **electricity_kwh** (FLOAT): Lượng điện tiêu thụ toàn nhà máy Thủ Đức (kWh).

## 2. Bảng `coal_purchase_invoices` (Hóa đơn mua than & Đối trễ ghi sổ ERP)
* **invoice_id** (VARCHAR): Mã hóa đơn tài chính VAT từ nhà cung cấp than.
* **purchase_order_ref** (VARCHAR): Mã Lệnh mua hàng (PO) tương ứng.
* **coal_grade** (VARCHAR): Cấp chất lượng than ghi trên hóa đơn.
* **tons_purchased** (FLOAT): Khối lượng than mua ghi trên hóa đơn (tấn).
* **invoice_date** (DATE): Ngày ký phát hành hóa đơn.
* **erp_posted_date** (DATE): Ngày kế toán thực tế nhập liệu và ghi sổ chi phí lên ERP.
* **amount_vnd** (FLOAT): Số tiền thanh toán chưa thuế (VND).

## 3. Bảng `boiler_coal_consumption` (Nhật ký tiêu hao than thực tế tại lò)
* **date** (DATE): Ngày vận hành.
* **coal_fed_wheelbarrow_tons** (FLOAT): Khối lượng than cám thực tế nạp vào lò, ghi chép tay theo số xe rùa trung chuyển (tấn).
* **steam_flow_m3** (FLOAT): Lượng hơi nước sinh ra trong ngày ($m^3$).
* **boiler_efficiency_indicator** (VARCHAR): Đánh giá hiệu năng lò hơi (OK: đạt tiêu chuẩn, LOW_EFFICIENCY: hiệu suất kém).

## 4. Bảng `factory_power_consumption` (Tiêu thụ điện năng chi tiết - Scope 2)
* **date** (DATE): Ngày đo.
* **spinning_workshop_kwh** (FLOAT): Chỉ số điện tiêu thụ tại xưởng Sợi (kWh).
* **weaving_workshop_kwh** (FLOAT): Chỉ số điện tiêu thụ tại xưởng Dệt (kWh).
* **sewing_workshop_kwh** (FLOAT): Chỉ số điện tiêu thụ tại xưởng May (kWh).
* **total_factory_kwh** (FLOAT): Tổng lượng điện tiêu thụ toàn nhà máy Thủ Đức (kWh).
