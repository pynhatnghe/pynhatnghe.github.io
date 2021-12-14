import csv

# Ví dụ 1: Ghi giá trị trực tiếp
with open("lich_khai_giang_t12.csv", "w", encoding="utf8") as csvfile:
    objcsv = csv.writer(csvfile, delimiter=",")

    objcsv.writerow(['STT', 'Chuong trinh hoc',
                    'Ngày khai giảng', 'Ca học', 'Thời lượng'])
    objcsv.writerow([1, 'ASP.NET Core 5', '17/12/2021', '246', '96h'])
    objcsv.writerow([2, 'CCNA', '19/12/2021', '357', '40h'])

# Ví dụ 2: Ghi ghi dict xuống file
data = [
    {"MaHH": 1, "TenHH": "Tivi Sony 43WR", "Gia": 13200},
    {"MaHH": 2, "TenHH": "Tủ lạnh Panasonic 360BVSVN", "Gia": 12890},
    {"MaHH": 3, "TenHH": "Máy lọc nước Karofi D66", "Gia": 10390}
]
with open("danh_muc.csv", "w", encoding="utf8") as file:
    fields = ["MaHH", "TenHH", "Gia"]
    csv_obj = csv.DictWriter(file, fieldnames=fields)
    csv_obj.writeheader()
    for item in data:
        csv_obj.writerow(item)
