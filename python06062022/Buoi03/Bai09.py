'''
Nhập vào số nguyên
In ra chuỗi đảo ngược của số đó
Tình tổng các chữ số
'''
so_nguyen = int(input("Nhập số nguyên: "))
tong = 0
chuoi_so_nguyen = str(so_nguyen)
print("Chuỗi đảo ngược: ", chuoi_so_nguyen[::-1])
for ki_tu in chuoi_so_nguyen:
    tong += int(ki_tu)
print("Tổng các chữ số: ", tong)