"""
Nhập số nguyên hệ 10
Chuyển đồi sang hệ 2
"""
N = int(input("Nhập số nguyên (hệ 10): "))

chuoi_nhi_phan = ""
tmp = N
while tmp > 0:
    so_du = tmp % 2 # --> kết quả so_du là sô
    # chuoi_nhi_phan = str(so_du) + chuoi_nhi_phan
    chuoi_nhi_phan = f"{so_du}{chuoi_nhi_phan}"
    tmp = tmp // 2

print(f"{N} đổi sang nhị phân là: {chuoi_nhi_phan}")