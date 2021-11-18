#Dùng mảng (list) các dict
danh_sach_hoc_vien = [
    {
        "HoTen": "Quỳnh Anh",
        "Tuoi": 20,
        "NgheNghiep": "Sinh viên",
        "MaHV": "HV001"
    },
    {
        "MaHV": "HV002",
        "HoTen": "Hồng Anh",
        "Tuoi": 33,
        "NgheNghiep": "Giáo vụ"
    }
]
# In ra học viên
for hoc_vien in danh_sach_hoc_vien:
    print(hoc_vien)
    print(f"{hoc_vien['HoTen']} - {hoc_vien['NgheNghiep']}")
    
# Nhập vào họ tên cần tìm?
can_tim = input("Họ tên cần tìm")
mang_dict_hocvien = {}
for hoc_vien in danh_sach_hoc_vien:
    mang_dict_hocvien[hoc_vien['MaHV']] = hoc_vien
    if hoc_vien['HoTen'].upper() == can_tim.upper():
        print(f"Tìm thấy {can_tim} trong danh sách")
        print(hoc_vien)
        
print(mang_dict_hocvien)
print(mang_dict_hocvien.get('HV002'))
print(mang_dict_hocvien.get('HV003'))
print(mang_dict_hocvien['HV003'])
    
