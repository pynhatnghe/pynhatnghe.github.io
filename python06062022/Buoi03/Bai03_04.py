'''
- Nhập vào chuỗi
- In chuỗi đảo ngược
- Kiểm tra chuỗi phải là chuỗi palindom hay ko?
(chuỗi viết thứ tự ngược vẫn là chính nó)
'''
chuoi = input("Nhập vào chuỗi cần xét: ").strip()
print("Đã nhập: ", chuoi)
# Cách 1
chuoi_dao_nguoi = chuoi[::-1]
print("Chuỗi đảo: ", chuoi_dao_nguoi)
# Cách 2
chuoi_dao = ''
for ki_tu in chuoi:
    chuoi_dao = ki_tu + chuoi_dao
print("Đảo:", chuoi_dao)

if chuoi.lower() == chuoi_dao.lower():
    print("Đây là chuỗi palindone")
