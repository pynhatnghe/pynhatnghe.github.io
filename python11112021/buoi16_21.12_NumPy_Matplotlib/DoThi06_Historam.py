import matplotlib.pyplot as plt
import numpy as np

# x = np.random.randn(100)  # Tạo 100 phần tử ngẫu nhiên
x = np.random.normal(170, 10, 250)
print(x)


plt.hist(x, 11)  # 11: số tầng
plt.show()
