"""
Hàm enumerate trả về tuple (bộ) tương ứng index (Chỉ số phẩn tử), value (giá trị phần tử)
"""
months = ["Jan", "Feb", "Nov", "Dec", "Mar"]
print(enumerate(months))
for index, value in enumerate(months):
    print(index, value)
    
thong_tin = {
    "HoTen": "Nguyễn Anh Huỳnh",
    "Tuoi": 20,
    "DocThan": True
}
for index, value in enumerate(thong_tin):
    print(index, value)
    