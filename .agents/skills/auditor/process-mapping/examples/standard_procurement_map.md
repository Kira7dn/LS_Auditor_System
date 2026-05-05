# GOLD STANDARD: SƠ ĐỒ QUY TRÌNH MUA HÀNG (STYLED MERMAID)

## 1. Sơ đồ quy trình (Flowchart)

```mermaid
graph LR
    classDef actor fill:#ccf,stroke:#333,stroke-width:2px;
    classDef control fill:#ff9,stroke:#d4a017,stroke-width:2px;
    classDef error fill:#f99,stroke:#c0392b,stroke-width:2px;
    classDef success fill:#cfc,stroke:#27ae60,stroke-width:2px;

    User[Người dùng] -->|Yêu cầu| PR[Lập PR]
    PR --> CP1{Kiểm tra định mức/Ngân sách}
    
    CP1 -- Vượt mức --> Reject[Từ chối/Yêu cầu giải trình]
    CP1 -- Hợp lệ --> Approve[Phê duyệt PR]
    
    Approve --> PO[Tạo PO]
    PO --> CP2{Đối chiếu PR vs PO}
    
    CP2 -- Sai lệch --> Fix[Sửa lại PO]
    CP2 -- Khớp --> Send[Gửi PO cho NCC]

    class PR,PO actor;
    class CP1,CP2 control;
    class Reject error;
    class Send success;
```

## 2. Danh mục điểm kiểm soát (Mapping)

| ID CP | Tên điểm kiểm soát | Logic kiểm tra (Validation Rules) |
| --- | --- | --- |
| **CP1** | Budget Check | Tổng giá trị PR <= Ngân sách còn lại của bộ phận. |
| **CP2** | PR-PO Match | Mã vật tư, Số lượng và Đơn giá trên PO phải khớp với PR đã duyệt. |

## 3. Ghi chú chuyên gia (Expert Notes)
- Các điểm màu **Vàng** là nơi rủi ro rò rỉ (Leakage) cao nhất nếu không được thực thi nghiêm túc.
- Điểm **CP2** thường bị bỏ qua trong các doanh nghiệp vận hành thủ công, dẫn đến việc bộ phận Thu mua tự ý thay đổi số lượng/giá so với yêu cầu ban đầu.
