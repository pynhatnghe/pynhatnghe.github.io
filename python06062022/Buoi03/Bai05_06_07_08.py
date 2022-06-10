'''
Bài 05 + 06 + 07 + 08
- Nhập chuỗi và chuỗi cần tìm
5. Đếm số lần xuất hiện của chuỗi con trong chuỗi
6. In ra chuỗi đó với ký tự chữ thường ở đầu, ký tự chữ hoa ở
sau
7. Đếm số kí tự chữ hoa, chữ thường, kí tự đặc biệt trong chuỗi cho trước.
8. Thống kê số lần xuất hiện của các ký tự trong chuỗi
'''
chuoi = input("Nhập chuỗi kí tự: ").strip()

# Bài 5
chuoi_can_tim = input("Chuổi cần tìm: ").strip()
so_lan_xuat_hien = chuoi.count(chuoi_can_tim)
print(f"Chuỗi '{chuoi_can_tim}' xuất hiện {so_lan_xuat_hien}"
      + f" lần trong chuỗi '{chuoi}'")
# Bài 8 (dùng dict để lưu trữ dạng {'a': 1, 'h': 10}
thong_ke = {}
for ki_tu in chuoi:
    if ki_tu not in thong_ke:
        thong_ke[ki_tu] = chuoi.count(ki_tu)
        print(thong_ke)
print(thong_ke)

# Bài 6:
chuoi_chu_hoa = ''
chuoi_chu_thuong = ""
for ki_tu in chuoi:
    if ki_tu.islower():
        chuoi_chu_thuong += ki_tu
    elif ki_tu.isupper():
        chuoi_chu_hoa += ki_tu
print(chuoi_chu_thuong + chuoi_chu_hoa)