'''
Format thêm cho đồ thị
- Màu color (c)
- Độ dày linewidth (lw)
- Kiểu nét linestyle (ls)
'''
import matplotlib.pyplot as plt
import random
import numpy as np

# Đố cặp điểm
N = random.randint(5, 15)

xpoints = []
ypoints = []

for idx in range(N):
    xpoints.append(random.randint(1, 25))
    ypoints.append(random.randint(1, 25))

plt.plot(xpoints, ypoints, ls="dashdot", c="green", lw=2)
plt.show()