# Xuất hóa đơn
from jinja2 import Template

hoadon_template = '''
            HÓA ĐƠN BÁN HÀNG
Họ tên khách hàng: {{ data.ho_ten}}. Số ĐT: {{ data.phone}}
Số tiền trả: {{ data.tong_tien}}.
Cảm ơn quý khách đã mua hàng
'''
hoadon = Template(hoadon_template)
data_hoadon = {
    "ho_ten": "Trần Anh Hùng",
    "phone": 909123456,
    "tong_tien": 1234567
}
result = hoadon.render(data=data_hoadon)
print(result)