---
trigger: model_decision
description: "Quy tắc chuẩn hóa Script dành cho AI thực thi (AI-First Scripting Standard)"
---

# AI-First Scripting Standards

Bộ tiêu chuẩn này quy định cách xây dựng các Script Python để Agent có thể thực thi, đọc hiểu và xử lý kết quả một cách tự động và chính xác.

---

## 1. Giao diện thực thi (I/O Standard)

### 1.1. Tham số đầu vào (CLI First)
Mọi script PHẢI hỗ trợ nhận tham số qua dòng lệnh.
- Sử dụng thư viện `argparse` hoặc `click`.
- Cung cấp `help` rõ ràng cho từng tham số.

### 1.2. Kết quả đầu ra (JSON Output)
- **Quy tắc vàng**: Script PHẢI trả về kết quả cuối cùng dưới dạng **JSON** qua `stdout`.
- CẤM in các dòng văn bản rườm rà (ví dụ: "Processing...", "Done!") vào `stdout`.

## 2. Cấu trúc mã nguồn

### 2.1. Type Hinting
Bắt buộc sử dụng Type Hints để Agent hiểu cấu trúc dữ liệu:
```python
def process_data(items: list[dict], threshold: float) -> dict:
    ...
```

### 2.2. Docstrings
Sử dụng Docstrings chi tiết cho Class và Function để Agent có thể tự tra cứu tài liệu thông qua các công cụ phân tích mã nguồn.

## 3. Quản lý Log và Thông báo

- **Log**: Sử dụng thư viện `logging`. Đẩy log ra `stderr` để không làm bẩn kết quả JSON ở `stdout`.
- **Progress**: Mọi thông báo tiến độ hoặc cảnh báo trung gian phải đẩy ra `stderr`.

## 4. Xử lý lỗi (Error Protocols)

Nếu xảy ra lỗi, script phải trả về cấu trúc JSON lỗi thay vì chỉ raise Exception:
```json
{
  "status": "error",
  "error_code": "DATA_MISMATCH",
  "message": "Cột 'Price' không tìm thấy trong file CSV.",
  "suggestion": "Vui lòng kiểm tra lại schema của file đầu vào."
}
```

## 5. Kỷ luật thực thi

- Luôn sử dụng `if __name__ == "__main__":` làm điểm khởi đầu.
- Script phải độc lập (Idempotent), không phụ thuộc vào trạng thái ẩn của môi trường.

---
*Status: MANDATORY FOR ALL AUDITOR SCRIPTS*