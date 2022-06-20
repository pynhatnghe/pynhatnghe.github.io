'''
Gọi API từ trang https://thongtindoanhnghiep.co/rest-api
Đọc API danh sách tỉnh thành
    https://thongtindoanhnghiep.co/api/city
==> lưu xuống file JSON theo format:
[
    {
        "SolrID": "/tp-ho-chi-minh",
        "ID": 4,
        "Title": "TP Hồ Chí Minh"
    }
]
'''
import requests
tinh = requests.get("https://thongtindoanhnghiep.co/api/city")
print(tinh.headers)
if tinh.status_code != 200:
    print("Lỗi")
    exit(0)
data_tinh = tinh.json()
arr_tinh = data_tinh["LtsItem"]
my_list = []
for item in arr_tinh:
    print(item["ID"], item["Title"], item["SolrID"])
    my_list.append(
        {
            "SolrID": item["SolrID"],
            "ID": item["ID"],
            "Title": item["Title"]
        }
    )

import json
with open("tinh_thanh.json", "w+", encoding="utf-8") as f:
    json.dump(my_list, f, indent=4)