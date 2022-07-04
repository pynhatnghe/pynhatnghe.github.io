import sys
import os

print(sys.argv)
if len(sys.argv) < 3:
    print('Chưa đủ tham số')
    exit(0) #Thoát - dừng chương trình

print("Start finding....")
thu_muc = sys.argv[1]
ten_file = sys.argv[2]
print(f"Cần tìm file {ten_file} trong thư mục {thu_muc}")
items = os.listdir(thu_muc)

if ten_file in items and os.path.isfile(
    os.path.join(thu_muc, ten_file)
):
    print("Tìm thấy file")
else:
    print('Không tìm thấy')
