"""
N = 7
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
"""
N = int(input("Nhập cửu chương: "))
for index in range(11):
    # print(f"{N} x {index} = {N * index}")
    print('%4d x %2d = %d' % (N, index, N * index))
