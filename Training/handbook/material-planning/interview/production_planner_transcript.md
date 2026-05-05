# Interview: Production Planner

**Người phỏng vấn:** LS Auditor  
**Người được phỏng vấn:** Nguyễn Minh An, Production Planner  
**Ngày:** 2026-04-08

## Transcript

**Auditor:** Anh lập nhu cầu vật tư dựa trên gì?  
**Planner:** Chủ yếu dựa trên forecast đã khóa và BOM trên ERP. Nhưng thực tế forecast đổi liên tục, nhất là sensor module.

**Auditor:** ERP tồn kho có đủ tin cậy không?  
**Planner:** Không hoàn toàn. Tồn kho casing và carton thường lệch vì Warehouse cập nhật sau ca. Nếu tôi tin ERP hoàn toàn thì có lúc line thiếu hàng.

**Auditor:** Anh có thấy được PO đang về khi chạy MRP không?  
**Planner:** Không phải lúc nào cũng thấy. Có PO Purchasing nói đã đặt rồi, nhưng màn hình MRP của tôi vẫn chưa hiện open quantity nên tôi thường đặt thêm buffer.

**Auditor:** Vì sao có PR cao hơn BOM requirement?  
**Planner:** Với casing, hao hụt do trầy xước. Với sensor, lead time dài nên tôi đặt dư để phòng khách tăng đơn.

**Auditor:** Có quy định giải trình PR vượt BOM không?  
**Planner:** Có, nhưng nếu PR urgent thì nhiều khi ghi sau. Thực tế ưu tiên là không để dừng line.

## Observation Notes
- Planner mở Excel riêng tên `Planner_Buffer_Check_Apr.xlsx`.
- File Excel có cột `buffer_override`.
- Planner nói Finance không thường phản hồi nhanh với PR urgent.
- Planner lưu email Purchasing báo hàng đang về để tự đối chiếu ngoài ERP.

## Contradictions
- SOP nói PR vượt BOM >5% phải có lý do trước khi duyệt.
- Planner nói lý do đôi khi ghi sau khi PR đã được gửi.
