'''
Tìm ngày chủ nhật cuối cùng của năm nhập vào
'''
from datetime import date, timedelta
nam = int(input("Nhập năm cần tra: "))

# set ngày cuối cùng của năm (31/12/nam)
# ngay_cuoi_nam = date(nam, 12, 31)
ngay_cuoi_nam = date(month=12, day=31, year=nam)

# hàm weekday() trả về ngày trong tuần
# Mon = 0, Tue = 1, Wed = 2, ..., Sun = 6
ngay_chu_nhat_cuoi = ngay_cuoi_nam
while ngay_chu_nhat_cuoi.weekday() != 6:
    ngay_chu_nhat_cuoi -= timedelta(days=1)
print(f"Ngày chủ nhật cuối củng của năm {nam} là ",
      ngay_chu_nhat_cuoi)