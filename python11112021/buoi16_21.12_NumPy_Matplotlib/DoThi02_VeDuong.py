'''
Vẽ đường
'''
import matplotlib.pyplot as plt
import random
import numpy as np

# Sinh số ngẫu nhiên từ 5 --> 50
n = random.randint(5, 10)

xpoints = []
ypoints = []

# Khởi tạo ngẫu nhiên n phần tử cho x/y
for i in range(0, n):
    xpoints.append(random.randint(1, 20))
    ypoints.append(random.randint(1, 20))
print(xpoints, ypoints)
plt.plot(xpoints, ypoints, linestyle='dotted', color='r', lw='1')

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

# Setting cho đồ thị
plt.title("Đồ thị các điểm")
plt.xlabel("Trục x")
plt.ylabel("Trục y")

# Tùy chọn hiển thị lưới
# plt.grid()  # Cả 2
plt.grid(axis='x')  # Chỉ có trục x

plt.show()  # Chỉ có 1
'''
linestyle (ls):
- dotted: dấu chấm
- dashed: dấu gạch
- 'solid' (default): nét liền đặc
- dashdot: chấm gạch

color (c):
- viết tắt tiếng anh
- #rrggbb (giá trị r,g,b từ 0 --> F) ví dụ: c = '#4CAF50

Độ dày nét vẽ
linewidth = '20.5'
lw = '12'
'''
