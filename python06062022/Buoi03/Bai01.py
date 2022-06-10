'''Nhập vào 1 chuỗi, xuất kí tự ở vị trí chẵn'''
chuoi = input("Nhập vào chuỗi: ")
# Cắt bỏ khoảng trắng 2 đầu
chuoi = chuoi.strip()
# Bỏ khoảng trắng dư ở giữa
while chuoi.find("  ") > -1: # Tìm thấy
    chuoi = chuoi.replace("  ", " ")

print("Chuỗi đã xử lý: ", chuoi)
mang_vi_tri_chan = []
for vi_tri in range(len(chuoi)):
    if vi_tri % 2 == 0:
        mang_vi_tri_chan.append(chuoi[vi_tri])

print("".join(mang_vi_tri_chan))

# Nếu dùng while
index = 0
while index < len(chuoi):
    if index % 2 == 0:
        print(chuoi[index], end="")
    index += 1

