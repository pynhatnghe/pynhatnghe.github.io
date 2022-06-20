'''Định nghĩa lớp hình chữ nhật chứa thông tin dài, rộng
Tính diện tích, chu vi
'''

class hinh_chu_nhat:
    # Fields (field_name = default_value)
    dai = 0
    rong = 0

    # Method
    def xuat(self):
        print("Dài", self.dai, "rộng:", self.rong)
        print("Diện tích:", self.tinh_dien_tich())

    def tinh_dien_tich(self):
        return self.dai * self.rong