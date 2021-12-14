import pandas as pd

my_dataset = {
    "cars": ["BMW", "Volvo", "Mercedes", "Ford"],
    "prices": [34, 29, 33, 31]
}

mydf = pd.DataFrame(my_dataset, index=['No 1', 22, 33, 44])
print(mydf)


# Ghi xuống file excel từ dataframe
# Ghi cách 1
with pd.ExcelWriter("Pandas_data.xlsx") as file:
    mydf.to_excel(file)

# Ghi cách 2
mydf.to_excel("Pandas_ABC.xlsx")
