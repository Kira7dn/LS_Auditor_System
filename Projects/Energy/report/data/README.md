# Data extracted from Project_Design_Document.md

Nguồn: `../Project_Design_Document.md`

Các file này chuẩn hóa thông số trong PDD để chuẩn bị viết script tính toán năng lượng và phát thải.

## Files

- `calculation_parameters.json`: file tổng hợp, phù hợp để script đọc trực tiếp.
- `parameters.csv`: bảng phẳng các hệ số, định mức, tỷ lệ và thông số MRV.
- `assets.csv`: danh mục tài sản và công suất/dung lượng thiết kế.
- `energy_balance_example_daily.csv`: ví dụ cân bằng năng lượng 1 ngày tại Hub.
- `fleet_emissions_example.csv`: ví dụ phát thải năm theo nhóm xe và tổng hạm đội.
- `formulas.json`: công thức và biến tính toán.
- `validation_references.csv`: ma trận nguồn xác nhận và việc còn thiếu.
- `renewable_resource_profiles.csv`: metadata và thống kê tóm tắt cho dữ liệu hệ số điện mặt trời/gió Renewables.ninja.
- `ninja_pv_21.0158_106.8009_uncorrected.csv`: hệ số điện mặt trời theo giờ tại tọa độ khảo sát.
- `ninja_wind_21.0158_106.8009_uncorrected.csv`: hệ số điện gió theo giờ tại tọa độ khảo sát.
- `ninja_pv_21.0158_106.8009_uncorrected.raw.json`: raw JSON từ file PV, gồm `metadata` và 8760 `records`.
- `ninja_wind_21.0158_106.8009_uncorrected.raw.json`: raw JSON từ file wind, gồm `metadata` và 8760 `records`.

## Notes for calculation scripts

- Các tỷ lệ phần trăm trong JSON có cả `value_percent` và `value_fraction` khi cần tính toán.
- `Eff_RMFC` chưa có giá trị. `EF_RMFC_EP` đang để dạng biểu thức `0.144 / Eff_RMFC`.
- `k_empty` xuất hiện trong công thức baseline nhưng PDD chưa cung cấp giá trị.
- Với hai file `ninja_*`, cột `electricity` là kW phát ra trên mỗi 1 kW công suất lắp đặt, nên có thể dùng trực tiếp làm hệ số công suất theo giờ. Tổng năm hiện tại: PV `1295.225 kWh/kW/năm` (`CF_Solar = 14.786%`), Wind `1587.008 kWh/kW/năm` (`CF_Wind = 18.117%`).
- Trong các file `.raw.json`, trường `records[].electricity_kw_per_kw` chính là cột `electricity` đã chuẩn hóa kiểu số. Với wind có thêm `records[].wind_speed_mps`.
