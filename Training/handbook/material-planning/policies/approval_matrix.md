# Approval Matrix

## Thuật ngữ & viết tắt
- **Approval matrix:** bảng quy định ai được duyệt giao dịch theo loại và ngưỡng giá trị.
- **PR:** yêu cầu mua hàng nội bộ.
- **PO:** đơn đặt hàng gửi nhà cung cấp.
- **DIOH:** số ngày tồn kho đủ dùng.
- **Split PO:** chia nhỏ PO để giữ từng PO dưới ngưỡng phê duyệt.
- **Finance Controller:** người kiểm soát tài chính và phê duyệt các giao dịch vượt ngưỡng.

## 1. Purchase Request

| Loại PR | Ngưỡng | Người duyệt |
| --- | ---: | --- |
| Standard PR | <= 20,000 USD | Production Manager |
| Standard PR | > 20,000 USD | Plant Manager |
| Urgent PR | Mọi giá trị | Plant Manager + Finance Controller |
| PR vượt BOM > 5% | Mọi giá trị | Plant Manager |
| PR cho vật tư DIOH > 90 | Mọi giá trị | Finance Controller |

## 2. Purchase Order

| Loại PO | Ngưỡng | Người duyệt |
| --- | ---: | --- |
| Standard PO | <= 50,000 USD | Purchasing Manager |
| Standard PO | > 50,000 USD | Finance Controller |
| Emergency PO | Mọi giá trị | Finance Controller |
| Vendor mới | Mọi giá trị | Procurement Head |

## 3. Control Note
Nghiêm cấm chia nhỏ PO để giữ từng PO dưới 50,000 USD nếu các PO có cùng vendor, material, ngày tạo và cùng plan.
