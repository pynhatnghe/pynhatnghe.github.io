# Nhập vào số lượng phần tử N
# Nhập giá trị từng phần tử
# Xuất mảng (dạng mảng, dạng chuỗi)
# Nhập vào giá trị cần tìm ==> Tìm thấy hay không thấy?

N = int(input("Nhập số phần tử:"))

mang = []
for index in range(N):
    temp = int(input(f"Nhập phần tử thứ {index}:"))
    mang.append(temp)

print(mang)
string_ints = [str(phan_tu) for phan_tu in mang]
print(type(string_ints))
print(string_ints)
print(",".join(string_ints))

# Nhập vào giá trị cần tìm ==> Tìm thấy hay không thấy?
can_tim_x = int(input('Cần tìm:'))
if can_tim_x in mang:
    print(f"Tìm thấy {can_tim_x} đầu tiên tại vị trị thứ {mang.index(can_tim_x)}")
else:
    print(f"Không tìm thấy {can_tim_x} trong mảng")