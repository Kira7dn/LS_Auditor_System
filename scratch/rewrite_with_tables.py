# -*- coding: utf-8 -*-
import sys
import hashlib
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

body = """# Phụ lục I - Hệ số Phát thải Lĩnh vực Năng lượng

<a id="qd226_btnmt_page_2"></a>
## Page 2

PHỤ LỤC I 
DANH MỤC HỆ SỐ PHÁT THẢI PHỤC VỤ KIỂM KÊ KHÍ NHÀ KÍNH LĨNH VỰC NĂNG LƯỢNG1 
(Ban hành kèm theo Quyết định số          /QĐ-BTNMT ngày       tháng 10 năm 2022  
của Bộ trưởng Bộ Tài nguyên và Môi trường) 

### 1. Các hoạt động đốt nhiên liệu

#### 1.1 Công nghiệp năng lượng

| STT | Tên hệ số phát thải khí nhà kính | Loại khí nhà kính | Nguồn phát thải | Giá trị | Đơn vị | Phương pháp áp dụng theo Hướng dẫn của IPCC |
|---|---|---|---|---|---|---|
| 1.1 | Hệ số phát thải CO2 của than antraxit | CO2 | Công nghiệp năng lượng | 98.300 | Kg CO2/TJ | Bậc 1 |
| 1.2 | Hệ số phát thải CH4 của than antraxit | CH4 | Công nghiệp năng lượng | 1 | Kg CH4/TJ | Bậc 1 |
| 1.3 | Hệ số phát thải N2O của than antraxit | N2O | Công nghiệp năng lượng | 1,5 | Kg N2O/TJ | Bậc 1 |
| 1.4 | Hệ số phát thải CO2 của than sub-bitum | CO2 | Công nghiệp năng lượng | 96.100 | Kg CO2/TJ | Bậc 1 |
| 1.5 | Hệ số phát thải CH4 của than sub-bitum | CH4 | Công nghiệp năng lượng | 1 | Kg CH4/TJ | Bậc 1 |
| 1.6 | Hệ số phát thải N2O của than sub-bitum | N2O | Công nghiệp năng lượng | 1,5 | Kg N2O/TJ | Bậc 1 |
| 1.7 | Hệ số phát thải CO2 của dầu thô | CO2 | Công nghiệp năng lượng | 73.300 | Kg CO2/TJ | Bậc 1 |
| 1.8 | Hệ số phát thải CH4 của dầu thô | CH4 | Công nghiệp năng lượng | 3 | Kg CH4/TJ | Bậc 1 |
| 1.9 | Hệ số phát thải N2O của dầu thô | N2O | Công nghiệp năng lượng | 0,6 | Kg N2O/TJ | Bậc 1 |
| 1.10 | Hệ số phát thải CO2 của dầu diesel | CO2 | Công nghiệp năng lượng | 74.100 | Kg CO2/TJ | Bậc 1 |
| 1.11 | Hệ số phát thải CH4 của dầu diesel | CH4 | Công nghiệp năng lượng | 3 | Kg CH4/TJ | Bậc 1 |
| 1.12 | Hệ số phát thải N2O của dầu diesel | N2O | Công nghiệp năng lượng | 0,6 | Kg N2O/TJ | Bậc 1 |
| 1.13 | Hệ số phát thải CO2 của dầu nhiên liệu | CO2 | Công nghiệp năng lượng | 77.400 | Kg CO2/TJ | Bậc 1 |
| 1.14 | Hệ số phát thải CH4 của dầu nhiên liệu | CH4 | Công nghiệp năng lượng | 3 | Kg CH4/TJ | Bậc 1 |
| 1.15 | Hệ số phát thải N2O của dầu nhiên liệu | N2O | Công nghiệp năng lượng | 0,6 | Kg N2O/TJ | Bậc 1 |
| 1.16 | Hệ số phát thải CO2 của khí tự nhiên | CO2 | Công nghiệp năng lượng | 56.100 | Kg CO2/TJ | Bậc 1 |
| 1.17 | Hệ số phát thải CH4 của khí tự nhiên | CH4 | Công nghiệp năng lượng | 1 | Kg CH4/TJ | Bậc 1 |
| 1.18 | Hệ số phát thải N2O của khí tự nhiên | N2O | Công nghiệp năng lượng | 0,1 | Kg N2O/TJ | Bậc 1 |
| 1.19 | Hệ số phát thải CO2 của sinh khối | CO2 | Công nghiệp năng lượng | 100.000 | Kg CO2/TJ | Bậc 1 |
| 1.20 | Hệ số phát thải CH4 của sinh khối | CH4 | Công nghiệp năng lượng | 30 | Kg CH4/TJ | Bậc 1 |

1 Bao gồm cả tiêu thụ năng lượng trong giao thông vận tải; tiêu thụ năng lượng trong ngành xây dựng; tiêu thụ năng lượng trong nông nghiệp, lâm nghiệp và thủy sản.

---

<a id="qd226_btnmt_page_3"></a>
## Page 3

| STT | Tên hệ số phát thải khí nhà kính | Loại khí nhà kính | Nguồn phát thải | Giá trị | Đơn vị | Phương pháp áp dụng theo Hướng dẫn của IPCC |
|---|---|---|---|---|---|---|
| 1.21 | Hệ số phát thải N2O của sinh khối | N2O | Công nghiệp năng lượng | 4 | Kg N2O/TJ | Bậc 1 |
| 1.22 | Hệ số phát thải CO2 của than củi | CO2 | Công nghiệp năng lượng | 112.000 | Kg CO2/TJ | Bậc 1 |
| 1.23 | Hệ số phát thải CH4 của than củi | CH4 | Công nghiệp năng lượng | 200 | Kg CH4/TJ | Bậc 1 |
| 1.24 | Hệ số phát thải N2O của than củi | N2O | Công nghiệp năng lượng | 4 | Kg N2O/TJ | Bậc 1 |

#### 1.2 Công nghiệp sản xuất và xây dựng

| STT | Tên hệ số phát thải khí nhà kính | Loại khí nhà kính | Nguồn phát thải | Giá trị | Đơn vị | Phương pháp áp dụng theo Hướng dẫn của IPCC |
|---|---|---|---|---|---|---|
| 1.25 | Hệ số phát thải CO2 của than antraxit | CO2 | Công nghiệp sản xuất và xây dựng | 98.300 | Kg CO2/TJ | Bậc 1 |
| 1.26 | Hệ số phát thải CH4 của than antraxit | CH4 | Công nghiệp sản xuất và xây dựng | 10 | Kg CH4/TJ | Bậc 1 |
| 1.27 | Hệ số phát thải N2O của than antraxit | N2O | Công nghiệp sản xuất và xây dựng | 1,5 | Kg N2O/TJ | Bậc 1 |
| 1.28 | Hệ số phát thải CO2 của dầu diesel | CO2 | Công nghiệp sản xuất và xây dựng | 74.100 | Kg CO2/TJ | Bậc 1 |
| 1.29 | Hệ số phát thải CH4 của dầu diesel | CH4 | Công nghiệp sản xuất và xây dựng | 3 | Kg CH4/TJ | Bậc 1 |
| 1.30 | Hệ số phát thải N2O của dầu diesel | N2O | Công nghiệp sản xuất và xây dựng | 0,6 | Kg N2O/TJ | Bậc 1 |
| 1.31 | Hệ số phát thải CO2 của dầu nhiên liệu | CO2 | Công nghiệp sản xuất và xây dựng | 77.400 | Kg CO2/TJ | Bậc 1 |
| 1.32 | Hệ số phát thải CH4 của dầu nhiên liệu | CH4 | Công nghiệp sản xuất và xây dựng | 3 | Kg CH4/TJ | Bậc 1 |
| 1.33 | Hệ số phát thải N2O của dầu nhiên liệu | N2O | Công nghiệp sản xuất và xây dựng | 0,6 | Kg N2O/TJ | Bậc 1 |
| 1.34 | Hệ số phát thải CO2 của khí hóa lỏng | CO2 | Công nghiệp sản xuất và xây dựng | 63.100 | Kg CO2/TJ | Bậc 1 |
| 1.35 | Hệ số phát thải CH4 của khí hóa lỏng | CH4 | Công nghiệp sản xuất và xây dựng | 1 | Kg CH4/TJ | Bậc 1 |
| 1.36 | Hệ số phát thải N2O của khí hóa lỏng | N2O | Công nghiệp sản xuất và xây dựng | 0,1 | Kg N2O/TJ | Bậc 1 |
| 1.37 | Hệ số phát thải CO2 của khí tự nhiên | CO2 | Công nghiệp sản xuất và xây dựng | 56.100 | Kg CO2/TJ | Bậc 1 |
| 1.38 | Hệ số phát thải CH4 của khí tự nhiên | CH4 | Công nghiệp sản xuất và xây dựng | 1 | Kg CH4/TJ | Bậc 1 |
| 1.39 | Hệ số phát thải N2O của khí tự nhiên | N2O | Công nghiệp sản xuất và xây dựng | 0,1 | Kg N2O/TJ | Bậc 1 |
| 1.40 | Hệ số phát thải CH4 của sinh khối | CH4 | Công nghiệp sản xuất và xây dựng | 30 | Kg CH4/TJ | Bậc 1 |
| 1.41 | Hệ số phát thải N2O của sinh khối | N2O | Công nghiệp sản xuất và xây dựng | 4 | Kg N2O/TJ | Bậc 1 |

#### 1.3 Giao thông vận tải hàng không nội địa

| STT | Tên hệ số phát thải khí nhà kính | Loại khí nhà kính | Nguồn phát thải | Giá trị | Đơn vị | Phương pháp áp dụng theo Hướng dẫn của IPCC |
|---|---|---|---|---|---|---|
| 1.42 | Hệ số phát thải CO2 của nhiên liệu hàng không (Jet Kerosene) | CO2 | Giao thông vận tải hàng không nội địa | 71.500 | Kg CO2/TJ | Bậc 1 |
| 1.43 | Hệ số phát thải CO2 của xăng hàng không (Aviation Gasoline) | CO2 | Giao thông vận tải hàng không nội địa | 70.000 | Kg CO2/TJ | Bậc 1 |
| 1.44 | Hệ số phát thải CH4 của tất cả các loại nhiên liệu | CH4 | Giao thông vận tải hàng không nội địa | 0,5 | Kg CH4/TJ | Bậc 1 |
| 1.45 | Hệ số phát thải N2O của tất cả các loại nhiên liệu | N2O | Giao thông vận tải hàng không nội địa | 2 | Kg N2O/TJ | Bậc 1 |

---

<a id="qd226_btnmt_page_4"></a>
## Page 4

#### 1.4 Giao thông vận tải đường bộ

| STT | Tên hệ số phát thải khí nhà kính | Loại khí nhà kính | Nguồn phát thải | Giá trị | Đơn vị | Phương pháp áp dụng theo Hướng dẫn của IPCC |
|---|---|---|---|---|---|---|
| 1.46 | Hệ số phát thải CO2 của dầu diesel | CO2 | Giao thông vận tải đường bộ | 74.100 | Kg CO2/TJ | Bậc 1 |
| 1.47 | Hệ số phát thải CH4 của dầu diesel | CH4 | Giao thông vận tải đường bộ | 3,9 | Kg CH4/TJ | Bậc 1 |
| 1.48 | Hệ số phát thải N2O của dầu diesel | N2O | Giao thông vận tải đường bộ | 3,9 | Kg N2O/TJ | Bậc 1 |
| 1.49 | Hệ số phát thải CO2 của xăng | CO2 | Giao thông vận tải đường bộ | 69.300 | Kg CO2/TJ | Bậc 1 |
| 1.50 | Hệ số phát thải CH4 của xăng | CH4 | Giao thông vận tải đường bộ | 33 | Kg CH4/TJ | Bậc 1 |
| 1.51 | Hệ số phát thải N2O của xăng | N2O | Giao thông vận tải đường bộ | 3,2 | Kg N2O/TJ | Bậc 1 |
| 1.52 | Hệ số phát thải CO2 của khí hóa lỏng | CO2 | Giao thông vận tải đường bộ | 63.100 | Kg CO2/TJ | Bậc 1 |
| 1.53 | Hệ số phát thải CH4 của khí hóa lỏng | CH4 | Giao thông vận tải đường bộ | 62 | Kg CH4/TJ | Bậc 1 |
| 1.54 | Hệ số phát thải N2O của khí hóa lỏng | N2O | Giao thông vận tải đường bộ | 0,2 | Kg N2O/TJ | Bậc 1 |
| 1.55 | Hệ số phát thải CO2 của khí tự nhiên | CO2 | Giao thông vận tải đường bộ | 56.100 | Kg CO2/TJ | Bậc 1 |
| 1.56 | Hệ số phát thải CH4 của khí tự nhiên | CH4 | Giao thông vận tải đường bộ | 92 | Kg CH4/TJ | Bậc 1 |
| 1.57 | Hệ số phát thải N2O của khí tự nhiên | N2O | Giao thông vận tải đường bộ | 3 | Kg N2O/TJ | Bậc 1 |

#### 1.5 Giao thông vận tải đường sắt

| STT | Tên hệ số phát thải khí nhà kính | Loại khí nhà kính | Nguồn phát thải | Giá trị | Đơn vị | Phương pháp áp dụng theo Hướng dẫn của IPCC |
|---|---|---|---|---|---|---|
| 1.58 | Hệ số phát thải CO2 của dầu diesel | CO2 | Giao thông vận tải đường sắt | 74.100 | Kg CO2/TJ | Bậc 1 |
| 1.59 | Hệ số phát thải CH4 của dầu diesel | CH4 | Giao thông vận tải đường sắt | 4,15 | Kg CH4/TJ | Bậc 1 |
| 1.60 | Hệ số phát thải N2O của dầu diesel | N2O | Giao thông vận tải đường sắt | 28,6 | Kg N2O/TJ | Bậc 1 |

#### 1.6 Giao thông vận tải đường thủy nội địa và hàng hải nội địa

| STT | Tên hệ số phát thải khí nhà kính | Loại khí nhà kính | Nguồn phát thải | Giá trị | Đơn vị | Phương pháp áp dụng theo Hướng dẫn của IPCC |
|---|---|---|---|---|---|---|
| 1.61 | Hệ số phát thải CO2 của dầu diesel | CO2 | Giao thông vận tải đường thủy nội địa và hàng hải nội địa | 74.100 | Kg CO2/TJ | Bậc 1 |
| 1.62 | Hệ số phát thải CH4 của dầu diesel | CH4 | Giao thông vận tải đường thủy nội địa và hàng hải nội địa | 7 | Kg CH4/TJ | Bậc 1 |
| 1.63 | Hệ số phát thải N2O của dầu diesel | N2O | Giao thông vận tải đường thủy nội địa và hàng hải nội địa | 2 | Kg N2O/TJ | Bậc 1 |
| 1.64 | Hệ số phát thải CO2 của dầu nhiên liệu | CO2 | Giao thông vận tải đường thủy nội địa và hàng hải nội địa | 77.400 | Kg CO2/TJ | Bậc 1 |
| 1.65 | Hệ số phát thải CH4 của dầu nhiên liệu | CH4 | Giao thông vận tải đường thủy nội địa và hàng hải nội địa | 7 | Kg CH4/TJ | Bậc 1 |
| 1.66 | Hệ số phát thải N2O của dầu nhiên liệu | N2O | Giao thông vận tải đường thủy nội địa và hàng hải nội địa | 2 | Kg N2O/TJ | Bậc 1 |

#### 1.7 Thương mại và dịch vụ

| STT | Tên hệ số phát thải khí nhà kính | Loại khí nhà kính | Nguồn phát thải | Giá trị | Đơn vị | Phương pháp áp dụng theo Hướng dẫn của IPCC |
|---|---|---|---|---|---|---|
| 1.67 | Hệ số phát thải CO2 của than antraxit | CO2 | Thương mại và dịch vụ | 98.300 | Kg CO2/TJ | Bậc 1 |
| 1.68 | Hệ số phát thải CH4 của than antraxit | CH4 | Thương mại và dịch vụ | 10 | Kg CH4/TJ | Bậc 1 |

---

<a id="qd226_btnmt_page_5"></a>
## Page 5

| STT | Tên hệ số phát thải khí nhà kính | Loại khí nhà kính | Nguồn phát thải | Giá trị | Đơn vị | Phương pháp áp dụng theo Hướng dẫn của IPCC |
|---|---|---|---|---|---|---|
| 1.69 | Hệ số phát thải N2O của than antraxit | N2O | Thương mại và dịch vụ | 1,5 | Kg N2O/TJ | Bậc 1 |
| 1.70 | Hệ số phát thải CO2 của dầu diesel | CO2 | Thương mại và dịch vụ | 74.100 | Kg CO2/TJ | Bậc 1 |
| 1.71 | Hệ số phát thải CH4 của dầu diesel | CH4 | Thương mại và dịch vụ | 10 | Kg CH4/TJ | Bậc 1 |
| 1.72 | Hệ số phát thải N2O của dầu diesel | N2O | Thương mại và dịch vụ | 0,6 | Kg N2O/TJ | Bậc 1 |
| 1.73 | Hệ số phát thải CO2 của khí hóa lỏng | CO2 | Thương mại và dịch vụ | 63.100 | Kg CO2/TJ | Bậc 1 |
| 1.74 | Hệ số phát thải CH4 của khí hóa lỏng | CH4 | Thương mại và dịch vụ | 5 | Kg CH4/TJ | Bậc 1 |
| 1.75 | Hệ số phát thải N2O của khí hóa lỏng | N2O | Thương mại và dịch vụ | 0,1 | Kg N2O/TJ | Bậc 1 |
| 1.76 | Hệ số phát thải CO2 của than củi | CO2 | Thương mại và dịch vụ | 112.000 | Kg CO2/TJ | Bậc 1 |
| 1.77 | Hệ số phát thải CH4 của than củi | CH4 | Thương mại và dịch vụ | 200 | Kg CH4/TJ | Bậc 1 |
| 1.78 | Hệ số phát thải N2O của than củi | N2O | Thương mại và dịch vụ | 1 | Kg N2O/TJ | Bậc 1 |

#### 1.8 Dân dụng

| STT | Tên hệ số phát thải khí nhà kính | Loại khí nhà kính | Nguồn phát thải | Giá trị | Đơn vị | Phương pháp áp dụng theo Hướng dẫn của IPCC |
|---|---|---|---|---|---|---|
| 1.79 | Hệ số phát thải CO2 của than antraxit | CO2 | Dân dụng | 98.300 | Kg CO2/TJ | Bậc 1 |
| 1.80 | Hệ số phát thải CH4 của than antraxit | CH4 | Dân dụng | 300 | Kg CH4/TJ | Bậc 1 |
| 1.81 | Hệ số phát thải N2O của than antraxit | N2O | Dân dụng | 1,5 | Kg N2O/TJ | Bậc 1 |
| 1.82 | Hệ số phát thải CO2 của dầu hỏa | CO2 | Dân dụng | 71.900 | Kg CO2/TJ | Bậc 1 |
| 1.83 | Hệ số phát thải CH4 của dầu hỏa | CH4 | Dân dụng | 10 | Kg CH4/TJ | Bậc 1 |
| 1.84 | Hệ số phát thải N2O của dầu hỏa | N2O | Dân dụng | 0,6 | Kg N2O/TJ | Bậc 1 |
| 1.85 | Hệ số phát thải CO2 của khí hóa lỏng | CO2 | Dân dụng | 63.100 | Kg CO2/TJ | Bậc 1 |
| 1.86 | Hệ số phát thải CH4 của khí hóa lỏng | CH4 | Dân dụng | 5 | Kg CH4/TJ | Bậc 1 |
| 1.87 | Hệ số phát thải N2O của khí hóa lỏng | N2O | Dân dụng | 0,1 | Kg N2O/TJ | Bậc 1 |
| 1.88 | Hệ số phát thải CO2 của sinh khối | CO2 | Dân dụng | 100.000 | Kg CO2/TJ | Bậc 1 |
| 1.89 | Hệ số phát thải CH4 của sinh khối | CH4 | Dân dụng | 300 | Kg CH4/TJ | Bậc 1 |
| 1.90 | Hệ số phát thải N2O của sinh khối | N2O | Dân dụng | 4 | Kg N2O/TJ | Bậc 1 |
| 1.91 | Hệ số phát thải CO2 của than củi | CO2 | Dân dụng | 112.000 | Kg CO2/TJ | Bậc 1 |
| 1.92 | Hệ số phát thải CH4 của than củi | CH4 | Dân dụng | 200 | Kg CH4/TJ | Bậc 1 |
| 1.93 | Hệ số phát thải N2O của than củi | N2O | Dân dụng | 1 | Kg N2O/TJ | Bậc 1 |

#### 1.9 Nông nghiệp, lâm nghiệp và thủy sản

| STT | Tên hệ số phát thải khí nhà kính | Loại khí nhà kính | Nguồn phát thải | Giá trị | Đơn vị | Phương pháp áp dụng theo Hướng dẫn của IPCC |
|---|---|---|---|---|---|---|
| 1.94 | Hệ số phát thải CO2 của xăng | CO2 | Nông nghiệp, lâm nghiệp và thủy sản | 69.300 | Kg CO2/TJ | Bậc 1 |
| 1.95 | Hệ số phát thải CH4 của xăng | CH4 | Nông nghiệp, lâm nghiệp và thủy sản | 10 | Kg CH4/TJ | Bậc 1 |

---

<a id="qd226_btnmt_page_6"></a>
## Page 6

| STT | Tên hệ số phát thải khí nhà kính | Loại khí nhà kính | Nguồn phát thải | Giá trị | Đơn vị | Phương pháp áp dụng theo Hướng dẫn của IPCC |
|---|---|---|---|---|---|---|
| 1.96 | Hệ số phát thải N2O của xăng | N2O | Nông nghiệp, lâm nghiệp và thủy sản | 0,6 | Kg N2O/TJ | Bậc 1 |
| 1.97 | Hệ số phát thải CO2 của dầu diesel | CO2 | Nông nghiệp, lâm nghiệp và thủy sản | 74.100 | Kg CO2/TJ | Bậc 1 |
| 1.98 | Hệ số phát thải CH4 của dầu diesel | CH4 | Nông nghiệp, lâm nghiệp và thủy sản | 10 | Kg CH4/TJ | Bậc 1 |
| 1.99 | Hệ số phát thải N2O của dầu diesel | N2O | Nông nghiệp, lâm nghiệp và thủy sản | 0,6 | Kg N2O/TJ | Bậc 1 |
| 1.100 | Hệ số phát thải CH4 của sinh khối | CH4 | Nông nghiệp, lâm nghiệp và thủy sản | 300 | Kg CH4/TJ | Bậc 1 |
| 1.101 | Hệ số phát thải N2O của sinh khối | N2O | Nông nghiệp, lâm nghiệp và thủy sản | 4 | Kg N2O/TJ | Bậc 1 |

### 2. Phát thải do phát tán

#### 2.1 Khai thác than

| STT | Tên hệ số phát thải khí nhà kính | Loại khí nhà kính | Nguồn phát thải | Giá trị | Đơn vị | Phương pháp áp dụng theo Hướng dẫn của IPCC |
|---|---|---|---|---|---|---|
| 2.1 | Hệ số phát tán CH4 trong khai thác than hầm lò* | CH4 | Khai thác than hầm lò | 1,5789 | m3CH4/tấn | Bậc 2 |
| 2.2 | Hệ số phát tán CH4 sau khai thác than hầm lò* | CH4 | Khai thác than hầm lò | 0,1697 | m3CH4/tấn | Bậc 2 |
| 2.3 | Hệ số phát tán CH4 trong khai thác than lộ thiên* | CH4 | Khai thác than lộ thiên | 0,05375 | m3CH4/tấn | Bậc 2 |
| 2.4 | Hệ số phát tán CH4 sau khai thác than lộ thiên* | CH4 | Khai thác than lộ thiên | 0,1697 | m3CH4/tấn | Bậc 2 |

#### 2.2 Khai thác dầu

| STT | Tên hệ số phát thải khí nhà kính | Loại khí nhà kính | Nguồn phát thải | Giá trị | Đơn vị | Phương pháp áp dụng theo Hướng dẫn của IPCC |
|---|---|---|---|---|---|---|
| 2.5 | Hệ số phát thải CO2 rò rỉ từ sản xuất dầu | CO2 | Khai thác dầu | 0,00215 | Nghìn tấn CO2/103m3 tổng sản phẩm dầu | Bậc 1 |
| 2.6 | Hệ số phát thải CH4 rò rỉ từ sản xuất dầu | CH4 | Khai thác dầu | 0,01035 | Nghìn tấn CH4/103m3 tổng sản phẩm dầu | Bậc 1 |
| 2.7 | Hệ số phát thải CO2 do đốt cháy tự nhiên từ sản xuất dầu | CO2 | Khai thác dầu | 0,0405 | Nghìn tấn CO2/103m3 tổng sản phẩm dầu | Bậc 1 |
| 2.8 | Hệ số phát thải CH4 do đốt cháy tự nhiên từ sản xuất dầu | CH4 | Khai thác dầu | 0,000025 | Nghìn tấn CH4/103m3 tổng sản phẩm dầu | Bậc 1 |
| 2.9 | Hệ số phát thải N2O do đốt cháy tự nhiên trong sản xuất dầu | N2O | Khai thác dầu | 0,00000064 | Nghìn tấn N2O/103m3 tổng sản phẩm dầu | Bậc 1 |
| 2.10 | Hệ số phát thải CO2 phát tán trong sản xuất dầu | CO2 | Khai thác dầu | 0,00249 | Nghìn tấn CO2/103m3 tổng sản phẩm dầu | Bậc 1 |
| 2.11 | Hệ số phát thải CH4 phát tán trong sản xuất dầu | CH4 | Khai thác dầu | 0,0196 | Nghìn tấn CH4/103m3 tổng sản phẩm dầu | Bậc 1 |

#### 2.3 Khai thác khí tự nhiên

| STT | Tên hệ số phát thải khí nhà kính | Loại khí nhà kính | Nguồn phát thải | Giá trị | Đơn vị | Phương pháp áp dụng theo Hướng dẫn của IPCC |
|---|---|---|---|---|---|---|
| 2.12 | Hệ số phát thải CO2 rò rỉ trong xử lý khí | CO2 | Khai thác khí tự nhiên | 0,0675 | Nghìn tấn CO2/106m3 tổng lượng khí thô đầu vào | Bậc 1 |

---

<a id="qd226_btnmt_page_7"></a>
## Page 7

| STT | Tên hệ số phát thải khí nhà kính | Loại khí nhà kính | Nguồn phát thải | Giá trị | Đơn vị | Phương pháp áp dụng theo Hướng dẫn của IPCC |
|---|---|---|---|---|---|---|
| 2.13 | Hệ số phát thải CO2 do đốt cháy tự nhiên trong xử lý khí | CO2 | Khai thác khí tự nhiên | 0,00355 | Nghìn tấn CO2/106m3 tổng sản phẩm khí | Bậc 1 |
| 2.14 | Hệ số phát thải CH4 do đốt cháy tự nhiên trong xử lý khí | CH4 | Khai thác khí tự nhiên | 0,0000024 | Nghìn tấn CH4/106m3 tổng sản phẩm khí | Bậc 1 |
| 2.15 | Hệ số phát thải N2O do đốt cháy tự nhiên trong xử lý khí | N2O | Khai thác khí tự nhiên | 3,9E-08 | Nghìn tấn N2O/106m3 tổng sản phẩm khí | Bậc 1 |
| 2.16 | Hệ số phát thải CO2 do đốt cháy tự nhiên trong sản xuất khí | CO2 | Khai thác khí tự nhiên | 0,0014 | Nghìn tấn CO2/106m3 tổng sản phẩm khí | Bậc 1 |
| 2.17 | Hệ số phát thải CH4 do đốt cháy tự nhiên trong sản xuất khí | CH4 | Khai thác khí tự nhiên | 0,00000088 | Nghìn tấn CH4/106m3 tổng sản phẩm khí | Bậc 1 |
| 2.18 | Hệ số phát thải N2O do đốt cháy tự nhiên trong sản xuất khí | N2O | Khai thác khí tự nhiên | 2,5E-08 | Nghìn tấn N2O/106m3 tổng sản phẩm khí | Bậc 1 |
| 2.19 | Hệ số phát thải CO2 phát tán trong sản xuất khí | CO2 | Khai thác khí tự nhiên | 0,000097 | Nghìn tấn CO2/106m3 tổng sản phẩm khí | Bậc 1 |
| 2.20 | Hệ số phát thải CH4 phát tán trong sản xuất khí | CH4 | Khai thác khí tự nhiên | 0,01219 | Nghìn tấn CH4/106m3 tổng sản phẩm khí | Bậc 1 |
| 2.21 | Hệ số phát thải CO2 phát tán trong xử lý khí | CO2 | Khai thác khí tự nhiên | 0,00025 | Nghìn tấn CO2/106m3 tổng sản phẩm khí thô đầu vào | Bậc 1 |
| 2.22 | Hệ số phát thải CH4 phát tán trong xử lý khí | CH4 | Khai thác khí tự nhiên | 0,00079 | Nghìn tấn CH4/106m3 tổng sản phẩm khí thô đầu vào | Bậc 1 |

(*): Hệ số phát thải khí nhà kính đặc trưng quốc gia.
"""

# Calculate content_hash of body
content_hash = hashlib.sha256(body.strip().encode("utf-8")).hexdigest()[:16]

frontmatter = f"""---
source_id: qd226_2022_btnmt
collection_id: qd226_btnmt
project_id: esg
title: "Phụ lục I - Hệ số Phát thải Lĩnh vực Năng lượng"
slug: 01_phu_luc_I_nang_luong
source_pdf: 226-QD-BTNMT.pdf
page_start: 2
page_end: 7
content_hash: {content_hash}
---

"""

final_text = frontmatter + body

# Write to file
dest_path = Path("Projects/ESG/kb/qd226_btnmt/01_phu_luc_I_nang_luong.md")
dest_path.write_text(final_text, encoding="utf-8")
print(f"Successfully formatted tables and wrote to {dest_path}")
print(f"New content_hash: {content_hash}")
