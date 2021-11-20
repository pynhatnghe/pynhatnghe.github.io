'''
Nhập loại lựa chọn: 6/45 hay 6/55.
Phát sinh bộ số ngẫu nhiên, mỗi bộ gồm 6 số không trùng.
In bộ số chưa sắp & đã sắp
'''
from random import randint

chon_lua = int(input('''Chọn vé số:
1. 6/45 xổ 4,6,CN
2. 6/55 xổ 3,5,7
Chọn:
'''))
print()
if chon_lua == 1:
    max = 45
elif chon_lua == 2:
    max = 55

mang_so = []
while len(mang_so) < 6:
    so_ngau_nhien = randint(1, max)
    print(so_ngau_nhien)
    if so_ngau_nhien not in mang_so:
        mang_so.append(so_ngau_nhien)

print('Vé của bạn:', mang_so)
mang_so.sort()
print('Vé của bạn:', mang_so)
