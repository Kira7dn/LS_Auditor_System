# TIÊU CHUẨN ĐỐI CHIẾU TUÂN THỦ (COMPLIANCE CRITERIA)
Các ngưỡng benchmark kiểm toán dùng để lọc bất thường trong dữ liệu giao dịch:

1.  **Chênh lệch Độ ẩm Sợi Merino (Moisture Regain Standard):**
    *   Tỷ lệ độ ẩm chuẩn thương mại: **18.25%**.
    *   Dung sai cho phép thanh toán theo hóa đơn mà không cần điều chỉnh khối lượng: **+/- 0.5%** (Tức là từ 17.75% đến 18.75%).
    *   Nếu tỷ lệ ẩm đo được $> 18.75\%$, bắt buộc phải quy đổi khối lượng giảm tương ứng trước khi thanh toán hóa đơn.
2.  **Sai lệch sản lượng Cắt - May (Cross-PO Yield Balance):**
    *   Ngưỡng chênh lệch: $Sewing\_Qty \le Cutting\_Qty$.
    *   Nếu $Sewing\_Qty > Cutting\_Qty$, hệ thống lập tức gắn cờ **Mượn sản lượng chéo PO (Cross-PO Yield Borrowing)**.
3.  **Độ trễ ghi sổ kho ERP (ERP Posting Lag):**
    *   Thời gian cho phép từ khi quét QR thực tế tại xưởng đến khi ghi nhận sổ kho trên ERP: $\le 24	ext{ giờ}$.
    *   Độ trễ $> 24	ext{ giờ}$: Gắn cờ cảnh báo **Giao dịch hồi tố (Retroactive Adjustments)**.
4.  **Chỉ số hiệu năng lò hơi (Boiler Coal-to-Steam Yield):**
    *   Ngưỡng tiêu hao chuẩn: $1	ext{ tấn than cám} ightarrow 8 - 10	ext{ } m^3	ext{ hơi nước}$.
    *   Tỷ lệ phát thải chuẩn: $pprox 2.4 - 2.6	ext{ tấn } CO2 / 	ext{1 tấn than cám}$ (cho than chất lượng chuẩn).
    *   Bất thường: Nếu tỷ lệ hơi sinh ra $< 7 m^3 / 	ext{tấn than}$ hoặc phát thải CO2 $> 2.8	ext{ tấn CO2} / 	ext{tấn than}$ (nghi ngờ than pha trộn bùn, kém chất lượng hoặc lò bị rò rỉ nhiệt).