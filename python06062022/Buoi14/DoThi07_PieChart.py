import matplotlib.pyplot as plt

# Số lượng bán tháng này
kpis = [121, 34, 198, 234]
mylabels = ["Civic", "BMW", "Accord", "Ford"]
myexplode = [0.1, 0, 0.1, 0.1]

plt.pie(kpis, labels=mylabels, explode=myexplode)
plt.show()