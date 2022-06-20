from HinhChuNhat import hinh_chu_nhat

if __name__ == "__main__":
    ds_hinh_chu_nhat = []
    hcn1 = hinh_chu_nhat()
    hcn1.dai = 7.7
    hcn1.rong = 5.5
    ds_hinh_chu_nhat.append(hcn1)
    hcn2 = hinh_chu_nhat()
    hcn2.dai = 101
    hcn2.rong = 5.05
    ds_hinh_chu_nhat.append(hcn2)

    hcn3 = hinh_chu_nhat(12, 2)
    ds_hinh_chu_nhat.append(hcn3)
    ds_hinh_chu_nhat.append(hinh_chu_nhat(13, 4))
    ds_hinh_chu_nhat.append(hinh_chu_nhat(108))

    for hinh in ds_hinh_chu_nhat:
        print(hinh) # Gọi hàm __str__
        hinh.xuat()