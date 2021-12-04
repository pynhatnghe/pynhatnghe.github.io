from tkinter import *
from dbcommon import MyDatabase

root = Tk()
# Config
root.geometry("450x300")
root.resizable(False, False)
root.title("Quản lý hàng hóa")

# Menu
menuBar = Menu(root)
mnuLoai = Menu(menuBar, tearoff=0)
mnuLoai.add_command(label="Thêm loại")
mnuLoai.add_command(label="Quit", command=root.destroy)
menuBar.add_cascade(label="Quản lý loại", menu=mnuLoai)
mnuHangHoa = Menu(menuBar, tearoff=0)
mnuHangHoa.add_command(label="Hàng hóa")
menuBar.add_cascade(label="Quản lý Hàng hóa", menu=mnuHangHoa)

root.config(menu=menuBar)


# Create loai, hanghoa


def create_loai(connect):
    sql = '''
    CREATE TABLE Loai(
        MaLoai integer PRIMARY KEY AUTOINCREMENT,
        TenLoai varchar(40)
    )
    '''
    MyDatabase.run_statement(connect, sql)


def create_hanghoa(connect):
    sql = '''
    CREATE TABLE HangHoa(
        MaHH char(6) PRIMARY KEY,
        TenHH varchar(40),
        MoTa varchar(55),
        DonGia decimal(10,2),
        SKU varchar(15) NULL,
        MaLoai interger NULL,
        FOREIGN KEY (MaLoai) REFERENCES Loai(MaLoai)
    )
    '''
    MyDatabase.run_statement(connect, sql)


myconnection = MyDatabase.sql_connection()
if myconnection:
    create_loai(myconnection)
    create_hanghoa(myconnection)


# Main
root.mainloop()
