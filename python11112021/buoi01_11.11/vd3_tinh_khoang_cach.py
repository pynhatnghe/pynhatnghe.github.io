'''
Chương trình tính khoảng cách 2 điểm trong Oxy
A(xa, ya) <------> B(xb, yb)

Can_Bac_Hai((xb - xa)^2 + (yb - ya)^2)
'''
xa = float(input("Nhập hoành độ điểm A: "))
xb = float(input("Nhập tung độ điểm A: "))
ya = float(input("Nhập hoành độ điểm B: "))
yb = float(input("Nhập tung độ điểm B: "))

khoang_cach = ( (xb - xa)**2 + (yb - ya)**2 )**0.5

import math
khoang_cach_2diem = math.sqrt((xb - xa)**2 + (yb - ya)**2)

print(khoang_cach)
print(khoang_cach_2diem)