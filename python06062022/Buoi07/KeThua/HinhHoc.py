import math

class HinhHoc:
    dien_tich = 0
    chu_vi = 0

    def TinhDienTichChuVi(self):
        pass

    def __str__(self):
        return "HinhHoc class"

class HinhChuNhat(HinhHoc):
    def __init__(self, d = 1, r = 1):
        self.dai = d
        self.rong = r

    def TinhDienTichChuVi(self):
        self.dien_tich = self.dai * self.rong
        self.chu_vi = (self.dai + self.rong) * 2

    def __str__(self):
        return (f"HCN {self.dai} x {self.rong}"
            + f", S = {self.dien_tich}, P = {self.chu_vi}")

class HinhTron(HinhHoc):
    def __init__(self, r = 1):
        self.ban_kinh = r

    def TinhDienTichChuVi(self):
        self.dien_tich =  math.pi * self.ban_kinh * self.ban_kinh
        self.chu_vi = 2 * math.pi * self.ban_kinh

    def __str__(self):
        return (f"Tròn R={self.ban_kinh}"
            + f", S = {self.dien_tich}, P = {self.chu_vi}")