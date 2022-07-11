import matplotlib.pyplot as plt

plt.subplot(2, 1, 1)
beers = ["332", "Kem", "Cola", "Crystal Tiger"]
prices = [19100, 25000, 9120, 36000]
plt.bar(beers, prices, color="#FF0FF0", width=0.7)

plt.subplot(2, 1, 2)
plt.barh(beers, prices, height=0.8)

plt.show()