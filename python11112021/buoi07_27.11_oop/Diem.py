'''
Định nghĩa lớp Điểm trong mặt phẳng oxy
'''
import math


class Diem:
    x: int = 0
    y: int = 0

    # Hàm constructor
    def __init__(self):
        pass

    def __init__(self, dx, dy) -> None:
        self.x = dx
        self.y = dy

    def dat_vi_tri(self, dx, dy):
        self.x = dx
        self.y = dy

    def khoach_cach_de_0(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self) -> str:
        return "(" + str(self.x) + ", " + str(self.y) + ")"


# Demo
# A = Diem()
#A.x = 7
#A.y = 9
# A.dat_vi_tri(7, 9)
# print(A.x, A.y)
B = Diem(17, 23)
print(B.x, B.y)
print(B)    # Gọi hàm __str__
print(B.khoach_cach_de_0())
