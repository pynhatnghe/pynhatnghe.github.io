"""
Nhập vào năm và tháng.
Xuất năm đó có là năm nhuận hay không?
Và thàng đó có bao nhiêu ngày
"""
thang = int(input("Nhập tháng:"))
nam = int(input("Nhập năm:"))

#la_nam_nhuan = False

if nam % 400 == 0:
    la_nam_nhuan = True
elif nam % 4 == 0 and nam % 100 != 0:
    la_nam_nhuan = True
else:
    la_nam_nhuan = False

if la_nam_nhuan == True:
    print(f"Năm {nam} là năm nhuận")
else:
    print(f"Năm {nam} không là năm nhuận")

so_ngay = 0
# Python có kiểu dữ liệu dict (dictionary): dạng key ===> value
liet_ke_so_ngay_theo_thang = {
    1: 31,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

liet_ke_so_ngay_theo_thang[2] = 29 if la_nam_nhuan else 28

# print(liet_ke_so_ngay_theo_thang[thang])
print(liet_ke_so_ngay_theo_thang.get(thang, 'Invalid month'))