from tkinter import *
from tkinter import font


def openManHinhThemLoai(root):
    mhLoai = Toplevel(root)
    mhLoai.geometry("300x100")
    mhLoai.resizable(False, False)
    mhLoai.title("Màn hình Thêm loại")
    Label(mhLoai, text="Quản lý Thêm loại",
          font="Arial 13 bold").grid(row=0, columnspan=3)
    Label(mhLoai, text="Tên loại").grid(row=1, column=0)
    tenLoai = StringVar()
    Entry(mhLoai, textvariable=tenLoai).grid(row=1, column=1)
    Button(mhLoai, text="Thêm").grid(row=1, column=2)
