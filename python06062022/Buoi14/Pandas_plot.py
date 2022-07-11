import pandas as pd

car_sales = pd.read_csv("car-sales.csv")
print(car_sales)
print(car_sales.shape)

# Chỉnh sửa dữ liệu cột Price thành số
# bỏ [$,.]
car_sales["Price"] = car_sales["Price"].str.replace(
    '[\$\,\.]', ""
).str[:-2]
print(car_sales)

# Ép cột Price sang số nguyên
car_sales["Price"] = car_sales["Price"].astype(int)
print(car_sales)

# Định nghĩa Total Save
car_sales["Total Sales"] = \
    car_sales["Price"].astype(int).cumsum()

car_sales["Sale Date"] = pd.date_range("1/1/2020",
    periods=len(car_sales))

car_sales.plot(x="Sale Date", y="Total Sales");

import matplotlib.pyplot as plt
plt.show()