import matplotlib.pyplot as plt
import numpy as np

# plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x, y)
plt.title("DEMO 1")
plt.xlabel("Số người")
plt.ylabel("Thu nhập")

# plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 5)
plt.plot(x, y)
plt.title("DEMO 2")
plt.xlabel("Số người")
plt.ylabel("Thu nhập")

plt.suptitle("Đồ thị Tổng hợp")
plt.show()

'''
plt.subplot(tổng sổ dòng, tổng số cột, hình thứ mấy)
Mọi hình (subplot) phải có cùng tổng số dòng, tổng số cột

.suptitle(): chỉ có trên plot có nhiều subplot
'''
