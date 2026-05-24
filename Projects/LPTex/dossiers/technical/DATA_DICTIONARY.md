# TỪ ĐIỂN DỮ LIỆU & KIẾN TRÚC MÔ PHỎNG (DATA DICTIONARY)

Để phục vụ cho động cơ kiểm toán LS-ASS, cấu trúc các bảng dữ liệu mô phỏng được định nghĩa như sau:

## 1. Bảng `moisture_settlement` (Đối soát độ ẩm sợi nhập từ DWS)
*   **po_number** (VARCHAR): Mã lệnh mua sợi Merino từ DWS.
*   **dws_weight_kg** (FLOAT): Trọng lượng sợi giao ghi trên phiếu cân của DWS (Trọng lượng ướt thực tế).
*   **moisture_pct** (FLOAT): Tỷ lệ độ ẩm đo thực tế bằng thiết bị cầm tay tại kho LPTex lúc nhận hàng (%).
*   **adjusted_dry_weight_kg** (FLOAT): Trọng lượng quy khô tiêu chuẩn thương mại ($18.25\%$).
    *   *Công thức:* $W_{adj} = W_{dws} 	imes rac{100\% - Moisture\%}{100\% - 18.25\%}$
*   **invoice_weight_kg** (FLOAT): Trọng lượng tính tiền trên hóa đơn của DWS gửi về ERP.
*   **invoice_amount_usd** (FLOAT): Số tiền thanh toán thực tế trên hóa đơn.

## 2. Bảng `yield_borrowing` (Đối chéo sản lượng Cắt - May liên PO)
*   **po_number** (VARCHAR): Mã PO sản xuất veston.
*   **cutting_qty** (INT): Số lượng chi tiết thân áo đã cắt hoàn thành từ bàn cắt (quét QR-code đầu ra).
*   **sewing_qty** (INT): Số lượng áo veston hoàn thành may ráp thực tế đầu ra chuyền may (quét QR-code nhập kho thành phẩm).
*   **timestamp_cut** (TIMESTAMP): Thời gian quét QR tại bàn cắt.
*   **timestamp_sew** (TIMESTAMP): Thời gian quét QR nhập kho thành phẩm.

## 3. Bảng `boiler_emissions` (Đối chéo phát thải lò hơi & than cám)
*   **date** (DATE): Ngày vận hành.
*   **coal_purchased_tons** (FLOAT): Khối lượng than cám nhập kho theo hóa đơn VAT mua than (tấn).
*   **steam_produced_m3** (FLOAT): Lượng hơi nước sinh ra đo bằng đồng hồ áp suất lò hơi ($m^3$).
*   **co2_emission_sensor_kg** (FLOAT): Lượng phát thải CO2 thực tế đo bằng cảm biến đo khói thải của lò hơi (kg).
*   **electricity_kwh** (FLOAT): Lượng điện tiêu thụ của phân xưởng dệt nhuộm (kWh).