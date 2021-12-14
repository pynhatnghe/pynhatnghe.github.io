# Data Quận huyện lấy từ https://www.gso.gov.vn/phuong-phap-thong-ke/danh-muc/don-vi-hanh-chinh/

import csv
with open("data/DSTinhKemQuanHuyen_14_12_2021.csv", encoding="utf-8") as file:
    rows = csv.reader(file)
    for row_obj in rows:
        # print(row_obj)
        print(row_obj[0], row_obj[2], row_obj[4])


# ========VD2: Đọc lên dạng Dict
with open("data/DSTinhKemQuanHuyen_14_12_2021.csv", encoding="utf-8") as file:
    my_dicts = csv.DictReader(file)
    print(type(my_dicts))
    for item in my_dicts:
        # print(item)
        print(item['\ufeffTỉnh Thành Phố'], item['Quận Huyện'])
