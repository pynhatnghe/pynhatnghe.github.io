import requests
import json

myreq = requests.get('https://thongtindoanhnghiep.co/api/city')

print(myreq.text)

mydict = json.loads(myreq.text)

dstinh = []
for item in mydict["LtsItem"]:
    dstinh.append({
        "ma_tinh": item["ID"],
        "ten_tinh": item["Title"],
        "so_danh_nghiep": item["TotalDoanhNghiep"]
    })

json_str = json.dumps(dstinh, indent=4)
print(json_str)

with open("tinhthanh.json", "w") as file:
    file.write(json_str)
