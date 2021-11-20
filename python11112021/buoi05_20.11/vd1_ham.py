"""Hàm tính tổng các số trong mảng"""


def tinh_tong(mang: list):
    '''Tính Tổng giá trị các phần tử trong mảng'''
    tong = 0
    for phan_tu in mang:
        tong += int(phan_tu)

    return tong


def chao_mung(ten: str = "Nhất Nghệ", lop="Python"):
    """Chào mừng"""
    print(f"Chào mừng bạn {ten} đến với lớp {lop}")


# Hàm main
if __name__ == "__main__":
    chao_mung("An", "Visualization")
    chao_mung("ASP.NET CORE")
    chao_mung(lop="ASP.NET CORE")
    chao_mung()
    print(tinh_tong([1, 3, 5]))
    print(tinh_tong({1: "Hai", "5": "Bảy"}))
