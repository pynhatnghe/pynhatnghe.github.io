# Data Quận huyện lấy từ https://www.gso.gov.vn/phuong-phap-thong-ke/danh-muc/don-vi-hanh-chinh/

import csv
import json
with open("data/DSTinhKemQuanHuyen_14_12_2021.csv", encoding="utf-8") as file:
    rows = csv.reader(file)
    for row_obj in rows:
        # print(row_obj)
        print(row_obj[0], row_obj[2], row_obj[4])


# ========VD2: Đọc lên dạng Dict
# result = {
#     "Tỉnh Cà Mau": {
#         "SoXaPhuong": 7
#     }
# }
with open("data/DSTinhKemQuanHuyen_14_12_2021.csv", encoding="utf-8") as file:
    my_dicts = csv.DictReader(file)
    print(type(my_dicts))

    result = {}  # Chứa danh sách thống kê xã phường theo tỉnh thành

    for item in my_dicts:
        print(item)
        print(item['\ufeffTỉnh Thành Phố'], item['Quận Huyện'])
        tinh = item['\ufeffTỉnh Thành Phố']
        if tinh in result:
            result[tinh]["SoXaPhuong"] += 1  # tăng 1 xã
        else:
            result[tinh] = {
                "SoXaPhuong": 1
            }

    json_str = json.dumps(result, indent=4, ensure_ascii=False)
    print(json_str)
