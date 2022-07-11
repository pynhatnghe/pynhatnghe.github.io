import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 3, 6])
ypoints = np.array([0, 150, 250])

plt.plot(xpoints, ypoints, "yo-")
plt.title("Biểu đồ giá xăng")
plt.xlabel("lít")
plt.ylabel("$ USD")
plt.show()

plt.savefig("vidu02.png")

''''
format: xyz
    x: màu, giá trị r,g,b
    y: đánh dấu tọa độ điểm:
        *: sao
        ^: tam gác
        o: tròn đen
    z: có hoặc không (-: đường nối các đỉnh)
'''