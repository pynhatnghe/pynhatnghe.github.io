# List: Mảng động, truy xuất bằng chỉ số từ 0 ---> len - 1
mang_list = ['Anh', 'Quỳnh', 'Nhất', 'Nghệ']

welcome = "Nhất Nghệ chào mời các bạn đến lớp PYTHON"

print("@".join(mang_list))
print('@'.join(welcome))
print(''.join(reversed(welcome)))

#  ký tự chữ thường ở đầu, ký tự chữ hoa ở sau
mang_thuong = []
mang_hoa = []
for ky_tu in welcome:
    if ky_tu.isupper():
        mang_hoa.append(ky_tu)
    elif ky_tu.islower():
        mang_thuong.append(ky_tu)
    
print(''.join(mang_thuong) + ''.join(mang_hoa))
        