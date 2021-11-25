import json

with open("datahocvien.json", "r") as file:
    json_str = file.read()

print(json_str)

mydict = json.loads(json_str)
print(type(mydict))
print('Họ tên', mydict["hoten"])
print('Khóa đang học:', len(mydict["khoa_dang_hoc"]))
for khoahoc in mydict["khoa_dang_hoc"]:
    # print(type(khoahoc))
    print(khoahoc["ten"], khoahoc["ngaykg"])
