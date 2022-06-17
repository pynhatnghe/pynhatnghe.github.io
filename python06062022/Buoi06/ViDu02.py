# Một người mua mặt hàng vào hôm nay
# Nhập vào 1 số N : số ngày vận chuyển
# In ra ngày dự kiến nhận hàng
from datetime import datetime, timedelta

ngay_mua = datetime.now()
so_ngay_van_chuyen = int(input("Số ngày vận chuyển: "))
ngay_nhan_du_kien = ngay_mua + timedelta(
    days=so_ngay_van_chuyen
)
print("Ngày nhận hàng (dự kiến):", ngay_nhan_du_kien)