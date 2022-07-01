from tkinter import *
from DatabaseUtils import SqliteUtil
from tkinter import messagebox

def mo_man_hinh_them_loai(root):
    def them_moi_loai():
        sql_select = f'''
        SELECT * FROM Loai WHERE TenLoai ='{ten_loai.get()}' 
        '''
        data_return = SqliteUtil.query(sql_select)

        if len(data_return) > 0:
            messagebox.showwarning("Cảnh báo", "Đã tồn tại")
        else:
            sql = f'''
            INSERT INTO Loai(TenLoai) VALUES('{ten_loai.get()}')
            '''
            print(sql)
            ma_loai = SqliteUtil.insert_and_get_lasted_id(sql)
            if ma_loai:
                messagebox.showinfo(
                    "Thông báo",
                f"Thêm thành công loại {ten_loai.get()} mã {ma_loai}"
                )

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
        mh_loai, text="Thêm mới", command=them_moi_loai
    ).grid(column=1,row=1,sticky=E)

    mh_loai.mainloop()
