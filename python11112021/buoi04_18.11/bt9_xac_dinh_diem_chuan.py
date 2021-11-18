# Giả sử có data điểm thi tốt nghiệp
marks = [29, 28.6, 29.3, 18, 20, 31, 19.8, 25, 24.3,  29.3, 18, 20, 31, 19.8, 25, 24.3, 29]

# Số lượng cần tuyển
quantity = 10

# Cách thông thường dễ nhất để xác định điểm chuẩn là sắp xếp và lấy tối khi nào đủ số
so_luong = 0
sorted_marks = sorted(marks, reverse=True)
print(sorted_marks)
while so_luong < quantity:
    diem_chuan = sorted_marks.pop(0) # Loại bỏ phần tử đầu mảng pop(index = 0)
    so_luong += 1

print(f'Điểm chuẩn là: {diem_chuan}')

# Tạo dict lưu trữ [phổ điểm : số lượng]
mang_diem = {}
for item in marks:
    mang_diem[item] = mang_diem.get(item, 0) + 1

print(mang_diem)
sorted_dict = sorted(mang_diem.items(), reverse=True)
print(sorted_dict)
soluonglay = 0
for diem, soluong in sorted_dict:
    soluonglay += soluong
    diem_chuan_cach_2 = diem
    if soluonglay > quantity:
        break
print('Điểm chuẩn là:', diem_chuan_cach_2)
