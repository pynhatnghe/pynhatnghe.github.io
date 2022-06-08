'''
Giá bán lẻ điện sinh hoạt
Bậc 1: Cho kWh từ 0 - 50        1.678
Bậc 2: Cho kWh từ 51 - 100      1.734
Bậc 3: Cho kWh từ 101 - 200     2.014
Bậc 4: Cho kWh từ 201 - 300     2.536
Bậc 5: Cho kWh từ 301 - 400     2.834
Bậc 6: Cho kWh từ 401 trở lên   2.927
Yêu cầu: Nhập chỉ số cũ, chỉ số mới & tính tiền
'''

chuoi_chiso_cu = input("Nhập chỉ số cũ: ")
chuoi_chiso_cu = int(chuoi_chiso_cu)
chuoi_chiso_moi = int(input("Nhập chỉ số mới: "))
dien_tieu_thu = chuoi_chiso_moi - chuoi_chiso_cu
print("CSC: ", chuoi_chiso_cu, "CSM: ", chuoi_chiso_moi,
      "Tiêu thụ: ", dien_tieu_thu, "kWh")
tong_tien = 0
if dien_tieu_thu < 51: # <= 50kwh
    tong_tien = dien_tieu_thu * 1678
elif dien_tieu_thu < 101: # 51 <= x <= 100 kwh
      tong_tien = 50 * 1678 + (dien_tieu_thu - 50) * 1734
      1 == 2
elif dien_tieu_thu < 201: # 101 <= x <= 200 kwh
    tong_tien = 50 * 1678 + 50 * 1734 \
                + (dien_tieu_thu - 100) * 2014
elif dien_tieu_thu < 301: # 201 <= x <= 300 kwh
    tong_tien = (50*1678 + 50*1734 + 100*2014
                 + (dien_tieu_thu - 200)*2536)
print("tien phai tra: ", tong_tien)