'''Ví dụ xuất file JSON'''
import json

# Cách 1: File json ==> chuỗi json ==> Đổi dict
with open("nhatnghe1.json", "r") as file:
    chuoi_json = file.read()
print(chuoi_json)
my_dict1 = json.loads(chuoi_json)
print(my_dict1)


# Cách 2: dict ==> file json
with open("nhatnghe2.json", "r") as file:
    my_dict2 = json.load(file)
print(my_dict2)
