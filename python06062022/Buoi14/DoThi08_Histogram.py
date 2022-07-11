import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(30, 0.1, 20)

plt.hist(data, 11)
plt.show()