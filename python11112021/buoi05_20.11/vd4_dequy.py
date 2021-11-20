'''Đệ quy: Hàm gọi chính hàm đó'''

# N! = 1*2*3*...*N


def giai_thua(N: int):
    # Điều kiện dừng
    if N == 1:
        return 1
    else:
        return N * giai_thua(N - 1)


print(giai_thua(11))
