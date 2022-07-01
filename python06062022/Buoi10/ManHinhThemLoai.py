from tkinter import *

def mo_man_hinh_them_loai(root):
    # Khai báo màn hình con của root
    mh_loai = Toplevel(root)
    mh_loai.title("Thêm loại")

    ten_loai = StringVar()
    Label(mh_loai, text="Tên loại").grid(column=0,row=0)
    Entry(
        mh_loai,
        textvariable=ten_loai
    ).grid(column=1,row=0)
    Button(
        mh_loai, text="Thêm mới"
    ).grid(column=1,row=1,sticky=E)

    mh_loai.mainloop()
