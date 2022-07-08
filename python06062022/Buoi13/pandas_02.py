import pandas as pd

my_df = pd.read_excel("data/FinancialSample.xlsx")

print(my_df)
print("Số lượng dòng cột:", my_df.shape)
print(my_df.head())
print(my_df.info())
my_df.drop_duplicates()
print(my_df.info())
print(my_df.describe())

my_df.plot()
import matplotlib.pyplot as plt
plt.show()

my_df.to_excel("final_result.xlsx")