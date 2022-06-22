from HinhHoc import HinhChuNhat, HinhTron, HinhHoc

HinhChuNhat.demo()

ds_hinh = []
ds_hinh.append(HinhTron(7.7))
ds_hinh.append(HinhChuNhat(5.5, 1.3))
HinhChuNhat.demo()

for item in ds_hinh:
    item.TinhDienTichChuVi()
    print(item)