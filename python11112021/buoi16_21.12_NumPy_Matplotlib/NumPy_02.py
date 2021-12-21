import numpy as np

# Tạo mảng a 4 dòng, 3 cột
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
], dtype=np.float64)
print(a)

# Tạo mảng b chứ các chỉ số cột (ko vượt a)
b = np.array([0, 1, 2, 0])

# Lấy 1 phần tử mỗi hàng có chỉ số trên
row_index = np.arange(4)  # [0 1 2 3]
print(a[row_index, b])

# Tăng thêm các phẩn tử mỗi dòng có chỉ số b lên 3 đơn vị
a[row_index, b] += 3
print(a)
