from tkinter import *
from tkinter import font
from tkinter import messagebox
from dbcommon import MyDatabase


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

    def xu_ly_them_loai():
        myconnection = MyDatabase.sql_connection()
        sqlSelect = f"SELECT * FROM Loai WHERE TenLoai = '{tenLoai.get()}' "
        result = MyDatabase.query_data(myconnection, sqlSelect)
        print(result)
        if len(result) > 0:  # Đã có
            messagebox.showwarning(
                title="Cảnh báo", message=f"Đã tồn tại loại {tenLoai.get()}")
        else:
            sqlInsert = f"INSERT INTO Loai(TenLoai) VALUES('{tenLoai.get()}')"

            ma_loai = MyDatabase.insert_and_get_lasted_id(
                myconnection, sqlInsert)
            messagebox.showinfo(message=f"Mã loại vừa sinh: {ma_loai}")
        myconnection.close()

    Button(mhLoai, text="Thêm", command=xu_ly_them_loai).grid(row=1, column=2)
