import matplotlib.pyplot as plt

plt.subplot(2, 3, 1)
plt.plot([1,2,3], [4,5,6])
plt.title("Do thi 1")
plt.grid()

plt.subplot(2, 3, 6)
plt.plot([1,2,3.8], [1,4,9])
plt.title("Do thi 2")
plt.grid(axis="x")

plt.suptitle("ABC") # Title bự

plt.show()
