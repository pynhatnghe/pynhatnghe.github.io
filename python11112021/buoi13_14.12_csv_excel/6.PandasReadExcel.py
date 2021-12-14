import pandas


df = pandas.read_excel("data/FinancialSample.xlsx", header=None, skiprows=3)
print(df)  # Chỉ in tượng trưng 10 dòng (5 đầu, 5 cuối)
print("Số lượng dòng cột:", df.shape)


# In 10 dòng đầu
print(df.head(10))

# Thống kê
print(df.describe())

# Lấy dòng header
row_header = df.head()
print(row_header)

# Save dataframe
df.to_excel("FinancialResult.xlsx")
