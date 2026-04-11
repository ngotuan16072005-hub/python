# Fix lỗi import (đảm bảo Python nhận đúng thư mục)
import sys
import os
sys.path.append(os.path.dirname(__file__))

# Import trực tiếp (tránh lỗi __init__.py)
from math_utils.phanso import cong, tru, nhan, chia
from math_utils.hinhhoc import (
    chu_vi_hinh_tron,
    dien_tich_hinh_tron,
    chu_vi_hinh_chu_nhat,
    dien_tich_hinh_chu_nhat
)

# ===== PHẦN PHÂN SỐ =====
print("=== PHÂN SỐ ===")
print("Cộng:", cong(5, 3))
print("Trừ:", tru(5, 3))
print("Nhân:", nhan(5, 3))
print("Chia:", chia(5, 3))

# ===== PHẦN HÌNH HỌC =====
print("\n=== HÌNH HỌC ===")
print("Chu vi hình tròn:", chu_vi_hinh_tron(2))
print("Diện tích hình tròn:", dien_tich_hinh_tron(2))

print("Chu vi HCN:", chu_vi_hinh_chu_nhat(4, 3))
print("Diện tích HCN:", dien_tich_hinh_chu_nhat(4, 3))