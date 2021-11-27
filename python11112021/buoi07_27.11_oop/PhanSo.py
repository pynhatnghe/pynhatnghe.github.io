'''
Chương trình tính toán trên phân số
'''
from math import *
import math


class PhanSo:
    TuSo: int
    MauSo: int

    def __init__(self, tu, mau):
        self.TuSo = tu
        self.MauSo = mau

    def __str__(self) -> str:
        return str(self.TuSo) + "/" + str(self.MauSo)

    def __add__(self, phanso):
        mau = self.MauSo * phanso.MauSo
        tu = self.TuSo * phanso.MauSo + phanso.TuSo * self.MauSo
        return PhanSo(tu, mau)

    def rut_gon(self):
        # Tìm ước số chung lớn nhất
        ucln = math.gcd(self.TuSo, self.MauSo)
        self.TuSo /= ucln
        self.MauSo /= ucln


ps1 = PhanSo(2, 3)
print(ps1)
ps2 = PhanSo(4, 3)
ps3 = ps1 + ps2
ps3.rut_gon()
print(ps3)
