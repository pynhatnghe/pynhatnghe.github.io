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


a = HinhHoc()
print(a)
b = HinhChuNhat(7, 9)
b.tinh_dientich_chuvi()
print(b)
