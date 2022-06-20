'''Định nghĩa lớp hình chữ nhật chứa thông tin dài, rộng
Tính diện tích, chu vi
'''

class hinh_chu_nhat:
    # Fields (field_name = default_value)
    dai = 0
    rong = 0

    # Contructors (hàm tạo/dựng)
    def __int__(self, p_dai = 1, p_rong = 1):
        self.dai = p_dai
        self.rong = p_rong

    # Method __str__ trả về chuỗi
    def __str__(self):
        return (f"HCN {self.dai} x {self.rong}"
                + f", S = {self.tinh_dien_tich()}")

    # Method
    def xuat(self):
        print("Dài", self.dai, "rộng:", self.rong)
        print("Diện tích:", self.tinh_dien_tich())

    def tinh_dien_tich(self):
        return self.dai * self.rong