import matplotlib.pyplot as plt
# 1. Prepare data
x = [1, 2, 3, 4]
y = [11, 22, 33, 44]
# 2. Setup plot
fig, ax = plt.subplots(figsize=(10,10)) # figsize dimension is inches
# 3. Plot data
ax.plot(x, y)
# 4. Customize plot
ax.set(title="Sample Simple Plot", xlabel="x-axis", ylabel="y-axis")
# 5. Save & show
fig.savefig("simple-plot.png")
