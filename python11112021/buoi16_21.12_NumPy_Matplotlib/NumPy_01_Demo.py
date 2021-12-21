import numpy as np

# Tạo mảng 1 chiều
a = np.array([1, 5, 4])

print(type(a))
print(a.shape)
print(a[0], a[1], a[2])
# Thay đổi phần tử thứ 2 (index = 1)
a[1] = 9
print(a)

# Tạo mảng 2 chiều 2 dòng, 3 cột
b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("Shape", b.shape)
print(b)
print(b[0, 0], b[1, 2])

c = np.zeros((3, 4))  # Tạo một numpy array với tất cả phẩn tử là 0
print(c)

d = np.ones([3, 5])
print(d)

# Tạo ma trận đơn vị n chiều
e = np.eye(7)
print(e)

# Tạo mảng với giá trị ngẫu nhiên
f = np.random.random((3, 3))
print(f)

# Tạo mảng 1 chiều có giá trị liên tiếp từ 0 đến n
g = np.arange(11)
print(g)

ff = np.random.random((3, 3, 4))
print(ff)


'''Cách truy xuất phần tử trong mảng.
Mảng 1 chiều: a[index]
Mảng 2 chiều: b[row_index, col_index]
'''
fslice = f[:3, 1:3]  # Chú ý chỉ số cuối không bằng (giống list)
print(fslice)
