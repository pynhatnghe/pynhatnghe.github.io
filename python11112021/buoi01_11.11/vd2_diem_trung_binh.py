# Nhập vào điểm 3 môn Toán, Lý, Hóa, Tính trung lập
print("CHUONG TRINH TINH TRUNG BINH")

# Diem : so thuc ==> float

diem_toan = float(input("Nhập điểm Toán"))
diem_ly = float(input("Nhập điểm Lý"))
diem_hoa = float(input("Nhập điểm Hóa"))

print(f"Điểm Toán {diem_toan}, Lý {diem_ly}, Hóa {diem_hoa}.")

diem_trung_binh = (diem_toan * 2 + diem_ly + diem_ly) / 4
print(f"Điểm trung bình: {diem_trung_binh}")