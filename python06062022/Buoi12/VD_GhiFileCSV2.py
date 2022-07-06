# Ví dụ 2: Ghi xuống dòng dạng dict
import csv

hang_hoa_mua = [
  {"ma": 1, "ten": "Bia 333", "gia": 14500, "soluong": 4},
  {"ma": 2, "ten": "7UP Revivie", "gia": 8500, "soluong": 7},
  {"ma": 3, "ten": "WakeUp 247", "gia": 84500, "soluong": 9},
]
with open("hang_mua.csv", "w", encoding="utf8") as myfile:
  ds_cot = ["ma", "ten", "gia", "soluong"]
  writer = csv.DictWriter(myfile, fieldnames=ds_cot)
  writer.writeheader()
  for item in hang_hoa_mua:
    writer.writerow(item)