"""
Chương trình chuyển một số có 3 chữ số thành phát âm tiếng Việt
 - Đầu vào : số tự nhiên trong phạm vi từ 0 đến 999
 - Đầu ra : phát âm tiếng Việt của số đó
"""
bangso = ['không', 'một', 'hai', 'ba', 'bốn',
          'năm', 'sáu', 'bảy', 'tám', 'chín']


def doc_3_chu_so(N):
    tram = N // 100
    donvi = N % 10
    chuc = (N // 10) % 10

    doc_thanh_chuoi = ""
    if tram > 0:
        doc_thanh_chuoi += bangso[tram] + " trăm"

    # Xử lý hàng chục
    if chuc > 1:
        doc_thanh_chuoi += ' ' + bangso[chuc] + " mươi"
    elif chuc == 1:
        doc_thanh_chuoi += ' mười'
    elif donvi > 0:
        doc_thanh_chuoi += " lẻ"

    # Xứ lý hàng đơn vị
    if donvi > 0:
        doc_thanh_chuoi += " " + bangso[donvi]

    return doc_thanh_chuoi


# Demo
if __name__ == '__main__':
    print(doc_3_chu_so(900))
    print(doc_3_chu_so(350))
    print(doc_3_chu_so(111))
    print(doc_3_chu_so(109))
    print(doc_3_chu_so(195))

    so_nguyen_can_doc = int(input("Nhập số nguyên cần đọc"))
    # 1 234 567 878
    phan_cach = ["đơn vị", "nghìn", "triệu", "tỷ"]
    mang_bo_3 = []
    tmp = so_nguyen_can_doc
    while tmp > 0:
        bo_ba = tmp % 1000  # Trách 3 số cuối cùng
        mang_bo_3.append(bo_ba)
        tmp = tmp // 1000

    print(mang_bo_3)
    ketqua = ""
    for step in range(0, len(mang_bo_3)):
        # print(phan_cach[step])
        # print(mang_bo_3[step])
        ketqua = doc_3_chu_so(mang_bo_3[step]) + ' ' \
            + phan_cach[step] + ' ' + ketqua

    print(ketqua)
