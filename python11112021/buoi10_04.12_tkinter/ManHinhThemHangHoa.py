from tkinter import *
from tkinter import font
from tkinter import messagebox
from dbcommon import MyDatabase
from tkinter import ttk


def openManHinhThemHangHoa(root):
    mhHangHoa = Toplevel(root)
    mhHangHoa.geometry("280x300")
    mhHangHoa.resizable(False, False)
    mhHangHoa.title("Màn hình Thêm Hàng hóa")

    Label(mhHangHoa, text="Quản lý Hàng hóa",
          font="Arial 13 bold").grid(row=0, columnspan=2)
    Label(mhHangHoa, text="Mã hàng hóa").grid(row=1, column=0)
    mahh = StringVar()
    Entry(mhHangHoa, textvariable=mahh).grid(row=1, column=1)

    Label(mhHangHoa, text="Tên hàng hóa").grid(row=2, column=0)
    tenhh = StringVar()
    Entry(mhHangHoa, textvariable=tenhh).grid(row=2, column=1)

    Label(mhHangHoa, text="Mô tả").grid(row=3, column=0)
    mota = StringVar()
    Entry(mhHangHoa, textvariable=mota).grid(row=3, column=1)

    Label(mhHangHoa, text="Đơn giá").grid(row=4, column=0)
    dongia = IntVar()
    Entry(mhHangHoa, textvariable=dongia).grid(row=4, column=1)

    Label(mhHangHoa, text="SKU").grid(row=5, column=0)
    sku = StringVar()
    Entry(mhHangHoa, textvariable=sku).grid(row=5, column=1)

    Label(mhHangHoa, text="Loại").grid(row=6, column=0)
    selected_loai = StringVar()
    myconnection = MyDatabase.sql_connection()
    dsLoai = MyDatabase.query_data(
        myconnection, "SELECT MaLoai, TenLoai FROM Loai")
    print(dsLoai)
    idx = 1
    for size in dsLoai:
        ttk.Radiobutton(mhHangHoa, text=size[1], value=size[0], variable=selected_loai)\
            .grid(row=6 + idx, column=0)
        idx += 1
