# BÀi tập 1 : Nhập chuỗi
"""Chỗ này là ghi chú nhiều dòng
Các bạn chú ý nhé.
"""

chuoi_nhap = input("Nhập vào chuỗi:")

# Xử lý các kí tự khoảng trắng dư: lstrip(), rstrip(), strip()
chuoi_nhap = chuoi_nhap.strip()

'''
Để loại bỏ khoảng trắng ở giữa thì lặp lại việc tìm 2 khoảng trắng liên tiếp thay = 1 khoảng trắng
'''
print('Có 2 khoảng trắng liên tiếp: ', chuoi_nhap.find('  '))
while chuoi_nhap.find('  ') > -1: #Còn có
    chuoi_nhap = chuoi_nhap.replace('  ', ' ')

print("Chuỗi đã nhập:", chuoi_nhap)
print("Chuỗi có", len(chuoi_nhap), "ký tự")

# xuất kí tự ở vị trí chẵn
index = 0
while index < len(chuoi_nhap):
    if index % 2 == 1: #Lấy theo vị trí lẻ của ngôn ngữ lập trình
        print(chuoi_nhap[index])
    index += 1 # index = index + 1