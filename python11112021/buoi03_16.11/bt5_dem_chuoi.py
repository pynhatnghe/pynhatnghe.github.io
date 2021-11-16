chuoi = input("Nhập chuỗi")

# Yêu cầu: Đếm số lần xuất hiện các kí tự trong chuỗi
print('Chữ a xuất hiện', chuoi.count('a'))
#Định nghĩa dict (dạng key ==> value) để thống kê kí tự nhập
mang = {}
for ky_tu in chuoi:
    mang[ky_tu] = chuoi.count(ky_tu)

print(mang)

# Cách 2: Đếm số lượng các kí tự
mang_ki_tu = {}
# Duyệt qua từng ký tự
for ky_tu in chuoi:
    # Kiểm tra xem kí tự này đã có trong mang_ki_tu (kiểm tra key)
    if ky_tu in mang_ki_tu: # Đã có
        mang_ki_tu[ky_tu] += 1
    else: # Chưa có
        mang_ki_tu[ky_tu] = 1

print(mang_ki_tu)


# Đếm có bao nhiêu ký tự in hoa .isupper(), chữ thường .islower(), số .isnumberic()
dem_hoa = 0
dem_thuong = 0
dem_ki_tu_so = 0
for ky_tu in chuoi:
    if ky_tu.isupper():
        dem_hoa += 1
    elif ky_tu.islower():
        dem_thuong += 1 # dem_thuong = dem_thuong + 1
    elif ky_tu.isnumeric():
        dem_ki_tu_so += 1
print(f"Có {dem_hoa} kí tự chữ hoa")
print(f"Có {dem_thuong} kí tự chữ thường")
print(f"Có {dem_ki_tu_so} kí tự chữ số")

for idx, value in enumerate(chuoi):
    print(f"{idx} ===> {value}")