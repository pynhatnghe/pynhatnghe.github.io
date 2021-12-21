import numpy as np
import matplotlib.pyplot as plt
import matplotlib

print(matplotlib.__version__)


xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints, marker='o')
plt.show()
