from jinja2 import Environment, FileSystemLoader

# giữ thư mục đang đứng (trong thư mục có file template
env = Environment(loader=FileSystemLoader("."))
# Tạo biến template lấy nội dung từ file template
template = env.get_template("hoadon_template.txt")

data_hoadon = {
    "ho_ten": "Trần Anh Hùng",
    "phone": 909123456,
    "gioi_tinh": True,
    "tong_tien": 1234567,
    "hang_hoa_mua": [
      {"ma": 1, "ten": "Bia 333", "gia": 14500, "soluong": 4},
      {"ma": 2, "ten": "7UP Revivie", "gia": 8500, "soluong": 7},
      {"ma": 3, "ten": "WakeUp 247", "gia": 84500, "soluong": 9},
    ]
}
result = template.render(data=data_hoadon)
print(result)