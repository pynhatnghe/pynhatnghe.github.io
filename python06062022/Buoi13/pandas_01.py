# Tựa tạo data
import pandas as pd

data = {
    "IP 13": [10, 0, 12, 3, 4, 111],
    "SS Galaxy S22": [0, 10, 1, 13, 7, 101],
}

my_df = pd.DataFrame(data)
print(my_df)
print(my_df.head(3))    # 3 dòng đầu
print(my_df.tail(3))    # 3 dòng cuối
print(my_df.sum())
print(my_df.min())
print(my_df.max())
print(my_df.mean())

my_df.to_csv("banhang.csv")
my_df.to_excel("banhang.xlsx")
my_df.to_json("banhang.json")
print(my_df.to_dict())