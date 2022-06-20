'''Ví dụ xuất file JSON'''
import json
my_dict = {
    "hoTen": "Nhất Nghệ",
    "tuoi": 19,
    "dienThoai": "02839292174",
    "gioiTinh": True,
    "khoaHoc": [
        { "tenMon": "Python", "hocPhi": 2.99},
        { "tenMon": "ASP.NET Core", "hocPhi": 4.49},
        { "tenMon": "ReactJS + WebAPI", "hocPhi": 2.49},
    ]
}

# Cách 1: Đổi dict ==> chuỗi json
chuoi_json = json.dumps(my_dict, indent=4)
print(chuoi_json)
with open("nhatnghe1.json", "w") as file:
    file.write(chuoi_json)

# Cách 2: dict ==> file json
with open("nhatnghe2.json", "w") as file:
    json.dump(my_dict, file, indent=4)