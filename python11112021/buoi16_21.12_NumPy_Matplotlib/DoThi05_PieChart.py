import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

data_labels = ["333", "Crystal Tiger", "Heken", "Bud"]
# Độ hở
do_ho = [0.1, 0.05, 0.02, 0]

plt.pie(y, labels=data_labels, explode=do_ho, shadow=True)
plt.legend(title="GIÁ BÁN BIA")
plt.show()
