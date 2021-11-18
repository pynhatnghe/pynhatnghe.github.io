a = [ 2, 3, 4, 5, 6, 7, 8 ]
del a[2:4] # Xóa phần tử vị trí thứ [start, stop -1]
print(a)
a.clear()
print(a)

##################
chuoi = input("Nhập chuỗi bất kỳ")
print("Chuỗi nhập", chuoi)

# Tách chuỗi thành mảng (sử dụng ký tự phân tách)
mang_tu = chuoi.split()
mang_tu_khac = chuoi.split(' ')
print(mang_tu)
print(mang_tu_khac)
print(f"Có {len(mang_tu)} từ")

#set:tập hợp giống list nhưng các phần tử không trùng nhau
tap_hop_tu = set(mang_tu)
print(tap_hop_tu)

my_dict = dict(tap_hop_tu)
print(my_dict)