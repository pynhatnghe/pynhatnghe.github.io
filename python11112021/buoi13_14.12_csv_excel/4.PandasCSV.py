# Cài thư viện Pandas: pip install pandas
import pandas
df = pandas.read_csv('data/hrdata.csv', index_col='Phone',
                     parse_dates=['BirthDate'])
print(df)

# Save dataframe xuống file csv khác
df.to_csv("hrdata_edited.csv")
