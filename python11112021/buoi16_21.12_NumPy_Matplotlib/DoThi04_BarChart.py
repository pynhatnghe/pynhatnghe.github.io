import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 2, 1)
plt.bar(x, y, color="red", width=0.5)

plt.subplot(2, 2, 4)
plt.barh(x, y)

plt.subplot(2, 2, 2)
index = np.arange(4)
y2 = np.array([3.3, 7.5, 1.9, 8.8])
plt.bar(index, y2, color='yellow', label="Fig 2")
plt.xlabel("Thực phẩm")
plt.ylabel("Doanh thu")


plt.show()
'''
thuộc tính bar/barh:
- width: độ dày cột dành cho bar()
- height: độ dày cột dành cho barh()
'''
