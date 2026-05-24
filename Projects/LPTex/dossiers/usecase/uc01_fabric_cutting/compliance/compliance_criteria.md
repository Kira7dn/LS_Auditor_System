# TIÊU CHUẨN ĐỐI CHIẾU TUÂN THỦ: KHÂU CẮT VẢI (COMPLIANCE CRITERIA)

Các quy tắc và ngưỡng benchmark dùng để lọc bất thường trong dữ liệu bàn cắt LPTex:

## 1. Sai lệch sản lượng Cắt - May (Cross-PO Yield Balance)
* **Quy tắc:** $Sewing\_Qty \le Cutting\_Qty$.
* **Mô tả:** Số lượng may ráp thành phẩm của một PO không bao giờ được vượt quá số lượng chi tiết đã cắt ra của chính PO đó.
* **Hình thức xử lý:** Nếu $Sewing\_Qty > Cutting\_Qty$, gắn cờ cảnh báo **Mượn sản lượng liên PO (Cross-PO Yield Borrowing)**.

## 2. Độ trễ ghi sổ kho ERP (ERP Posting Lag)
* **Quy tắc:** $Posted\_Timestamp - Issued\_Timestamp \le 24 \text{ giờ}$.
* **Mô tả:** Giao dịch xuất kho nguyên vật liệu phải được ghi nhận lên hệ thống ERP trong vòng 24 giờ kể từ khi thực tế xuất xưởng để kế toán kịp đối soát.
* **Hình thức xử lý:** Khoảng chênh lệch thời gian $> 24 \text{ giờ}$ sẽ bị gắn cờ **Giao dịch hồi tố (Retroactive Adjustments)**.

## 3. Sai lệch Hệ số Co rút Vải (Shrinkage Rate Variance)
* **Quy tắc:** $|Actual\_Shrinkage\_Pct - CAD\_Shrinkage\_Pct| \le 0.5\%$.
* **Mô tả:** Hệ số co rút thiết kế trên CAD marker phải khớp với độ co rút thực tế đo được sau hoàn tất vải nhuộm để tránh thừa/thiếu kích thước chi tiết.
* **Hình thức xử lý:** Chênh lệch vượt quá $0.5\%$ sẽ được gắn cảnh báo **Sai lệch co rút (Shrinkage Mismatch)** và tính toán lượng vải lãng phí quy đổi.
