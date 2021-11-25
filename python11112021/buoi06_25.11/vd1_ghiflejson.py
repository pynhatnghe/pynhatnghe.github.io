import json

hocvien = {
    'hoten': 'Lê Hải Nam',
    'tuoi': 19,
    'dien_thoai': 989789789,
    'khoa_dang_hoc': [
        {
            "ten": "Python",
            "ngaykg": "11/11/2021"
        },
        {
            "ten": "WebAPI",
            "ngaykg": "29/11/2021"
        }
    ]
}
json_str = json.dumps(hocvien, indent=4)
print(json_str)
with open("datahocvien.json", "w") as file:
    file.write(json_str)
