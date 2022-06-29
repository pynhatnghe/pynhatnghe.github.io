from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()

# Khai báo menu bar
menu_bar = Menu(root)

###############Thêm menu item + xử lý*************
file_menu = Menu(menu_bar, tearoff=False)
file_menu.add_command(label='Open')
file_menu.add_command(label='Save')
file_menu.add_separator()
file_menu.add_command(label='Exit',command=root.destroy)

menu_bar.add_cascade(label="File",menu=file_menu)

mnu_tool = Menu(menu_bar, tearoff=0)
mnu_tool.add_command(label="About")
menu_bar.add_cascade(label="Tools",menu=mnu_tool)
###############/End Thêm menu item + xử lý*************

# Nhúng (add) menubnar vào màn hình chính
root.config(menu=menu_bar)

ttk.Label(text="Chọn tháng").pack()
# Combobox
thang_chon = StringVar()
cbo_thang = ttk.Combobox(root, textvariable=thang_chon)
cbo_thang["values"] = [1,3,4,5,6]
cbo_thang.pack()

def xu_ly_thay_doi_chon(event):
    messagebox.showinfo("INFO",
        f"Vừa chọn: {thang_chon.get()}")

cbo_thang.bind('<<ComboboxSelected>>', xu_ly_thay_doi_chon)

root.mainloop()