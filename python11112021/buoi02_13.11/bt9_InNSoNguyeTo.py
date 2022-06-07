'''
Nhập vào số nguyên dương N.
Hãy in ra N số nguyên tố đầu tiên.
'''

N = int(input("Nhập số nguyên dương N:"))


def LaSoNguyenTo(so_nguyen: int):
    if so_nguyen < 2:
        return False  # Không nguyên tố

    '''Số nguyên tố chỉ có 2 ước số 1 và chính nó.
    Nếu trong đoạn từ 2 --> so_nguyen - 1 mà có 1 số nguyên j nào đó: so_nguyen chia hết cho j ==> ko nguyên tố
    '''
    for j in range(2, so_nguyen):
        if so_nguyen % j == 0:
            return False  # Không nguyên tố

    return True


dem_so_luong_so_nguyen_to = 0
bien_so_chay = 1
while dem_so_luong_so_nguyen_to < N:
    # Xử lý In so nguyen to ke tiep
    if LaSoNguyenTo(bien_so_chay) == True:
        print(bien_so_chay)
        dem_so_luong_so_nguyen_to += 1

    bien_so_chay += 1
