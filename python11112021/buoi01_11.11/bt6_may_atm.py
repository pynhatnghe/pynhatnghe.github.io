"""Bài tập 6: Máy ATM
Nhập vào số tiến cần rút (bội số của 50k)
Xuất số lượng tờ tiền từng loại, sao cho tổng số lượng tờ nhỏ nhất.
Giả sử máy ATM luôn đủ tiền: 500k, 200k, 100k, 50k
"""
so_tien_can_rut = int(input("Cần rút: "))

if so_tien_can_rut % 50 != 0:
    print("Số tiền không hợp lệ")
    exit(111)

print("Máy bắt đầu soạn tiền")

soto500 = so_tien_can_rut // 500
so_tien_con_lai = so_tien_can_rut % 500

soto200 = so_tien_con_lai // 200
so_tien_con_lai = so_tien_con_lai % 200

soto100 = so_tien_con_lai // 100
so_tien_con_lai = so_tien_con_lai % 100

soto50 = so_tien_con_lai // 50
so_tien_con_lai = so_tien_con_lai % 50

print(f"Thông tin rút {so_tien_can_rut} đ")
if soto500 > 0:
    print(f"{soto500} tờ 500k")
if soto200 > 0:
    print(f"{soto200} tờ 200k")
if soto100 > 0:
    print(f"{soto500} tờ 100k")
if soto50 > 0:
    print(f"{soto50} tờ 50k")
