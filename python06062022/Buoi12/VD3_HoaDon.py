# Xuất hóa đơn
from jinja2 import Template

hoadon_template = '''
            HÓA ĐƠN BÁN HÀNG
- Họ tên khách hàng: {{ data.ho_ten}}.
- Giới tính: 
    {% if data.gioi_tinh %}
        Nam
    {% else %}
        Nữ
    {% endif %}  
- Số ĐT: {{ data.phone}}
Số tiền trả: {{ data.tong_tien}}.
        DANH SÁCH HÀNG HÓA ĐÃ MUA
{% for hanghoa in data.hang_hoa_mua %}
    {{ hanghoa.ten}}" {{ hanghoa.gia }} x {{hanghoa.soluong}}
{% endfor %}
Cảm ơn quý khách đã mua hàng./.
'''
hoadon = Template(hoadon_template)
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
result = hoadon.render(data=data_hoadon)
print(result)