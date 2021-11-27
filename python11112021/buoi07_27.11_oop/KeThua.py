import math


class HinhHoc:
    DienTich = 0
    ChuVi = 0

    def __str__(self) -> str:
        return "S = " + str(self.DienTich) + ", P = " + str(self.ChuVi)

    def tinh_dientich_chuvi(self):
        pass


class HinhChuNhat(HinhHoc):
    Dai = 0
    Rong = 0

    def __init__(self, d, r):
        self.Dai = d
        self.Rong = r

    def tinh_dientich_chuvi(self):
        self.DienTich = (self.Dai * self.Rong)
        self.ChuVi = (self.Dai + self.Rong) * 2

    def __str__(self):
        return "D = " + str(self.Dai) + ", R = " + str(self.Rong) + ",S = " + str(self.DienTich) + ", P = " + str(self.ChuVi)


class HinhTron(HinhHoc):
    BanKinh = 0

    def __init__(self, r):
        self.BanKinh = r

    def tinh_dientich_chuvi(self):
        self.DienTich = math.pi * (self.BanKinh ** 2)
        self.ChuVi = math.pi * self.BanKinh * 2

    def __str__(self):
        return "R = " + str(self.BanKinh) + ", S = " + str(self.DienTich) + ", P = " + str(self.ChuVi)


mang_hinh = []
mang_hinh.append(HinhChuNhat(34, 56))
mang_hinh.append(HinhChuNhat(13, 5))
mang_hinh.append(HinhTron(23))

for item in mang_hinh:
    item.tinh_dientich_chuvi()
    print(item)
