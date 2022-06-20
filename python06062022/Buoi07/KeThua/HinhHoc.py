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