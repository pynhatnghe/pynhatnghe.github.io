from jinja2 import Template

'''
Yêu cầu xuất hóa đơn theo mẫu
'''
order_template = '''
            HÓA ĐƠN THANH TOÁN
- Khách hàng: {{ data.ho_ten }}
- Số điện thoại: {{ data.dien_thoai }}
    DANH SÁCH HÀNG MUA
{# Ghi chú vùng hiển thị thông tin hàng mua #}
{% for item in data.hang_hoa %}
    {{ item.so_luong }} x {{ item.ten }} - {{ item.gia }} đ = {{ item.so_luong * item.gia}} đ.
{% endfor%}
        Tổng tiền: {{ data.tong_tien }} đ.
    Cảm ơn quý khách đã tin dùng dịch vụ của chúng tôi.
'''
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
hoadon_template = Template(order_template)
print(hoadon_template.render(data=data_hoadon))
