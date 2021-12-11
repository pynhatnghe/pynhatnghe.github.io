from jinja2 import Environment, FileSystemLoader

# Khai báo thư mục chứa template
env = Environment(loader=FileSystemLoader("."))

# Load template
template = env.get_template("hoa_don_template.txt")

# Chuẩn bị data
data_hoadon = {
    "ho_ten": "Lê Anh Đào",
    "dien_thoai": "02839292174",
    "hang_hoa": [
        {"ten": "Sony Smart TV 43' 2021", "so_luong": 1, "gia": 13299},
        {"ten": "Tủ lạnh Panosonic 360l", "so_luong": 2, "gia": 12990},
        {"ten": "Máy lọc không khí Daikin", "so_luong": 1, "gia": 4299}
    ]
}
data_hoadon["tong_tien"] = (sum(item["so_luong"] * item["gia"]
                            for item in data_hoadon["hang_hoa"]))

result = template.render(data=data_hoadon)
with open("hoadon.txt", "w", encoding="utf-8") as myfile:
    myfile.write(result)
