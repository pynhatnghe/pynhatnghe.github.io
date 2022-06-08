try:
    so_luong = input("Nhập số lượng: ")
    so_luong = int(so_luong)
    print("Số lượng ", so_luong)
    n = 1/0
except ZeroDivisionError as err:
    print("Lỗi chia 0", err)
except Exception as ex:
    print(ex)
print("DONE")
