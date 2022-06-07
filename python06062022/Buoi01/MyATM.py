"""
Chương trình tính số tờ tiền trả lại của máy ATM
 - Đầu vào : Số tiền máy ATM cần trả lại (bội số của 5k)
 - Đầu ra: Số tờ của từng loại tiền 100k, 50k, 20k, 5k
 sao cho tổng số tờ trả lại ít nhất
"""
tien_can_doi = int(input("Nhập số tiền cần đổi (1000 đ): "))
print("Số tiền cần đổi: ", tien_can_doi)

# Tạo mảng (LIST) lưu mệnh giá
mang_menh_gia = [100, 50, 20, 5, 200]
mang_menh_gia.sort() # sắp tăng dần
mang_menh_gia.reverse() # đảo giảm dần

# Khai báo mảng số tở rỗng (ko có phần tử)
mang_so_to = []

# duyệt qua từng mệnh giá để chia lấy số lượng
for m_gia in mang_menh_gia:
    # print(m_gia)
    so_to = tien_can_doi // m_gia # dấu //: chia lấy nguyên
    mang_so_to.append(so_to) # Thêm vào mảng
    # tien_can_doi = tien_can_doi % m_gia
    tien_can_doi %= m_gia # dấu %: chia lấy dư

print("Mệnh giá: ", mang_menh_gia)
print("Số tờ: ", mang_so_to)
print("Dư: ", tien_can_doi)