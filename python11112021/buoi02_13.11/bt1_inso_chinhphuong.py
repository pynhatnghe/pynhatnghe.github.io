'''
Nhập số nguyên  dương N. In ra các số chính phương (N^2) nhỏ hơn N.
'''
so_nguyen = int(input('Nhập số nguyên: '))
print(f"Các số chính phương nhỏ hơn {so_nguyen} là: ")
import math
max_loop = int(math.sqrt(99))
for item in range(1, max_loop + 1):
    print(item**2)
    
step = 1
while step**2 < so_nguyen:
    print(step**2)
    step += 1