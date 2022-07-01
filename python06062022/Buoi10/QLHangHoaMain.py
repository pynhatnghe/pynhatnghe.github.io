from tkinter import *

root = Tk()
root.title("Quản lý Hàng hóa")

# Khai báo menu bar
menu_bar = Menu(root)

###############Thêm menu item + xử lý*************
mnu_loai = Menu(menu_bar, tearoff=False)
mnu_loai.add_command(label='Danh sách')
mnu_loai.add_command(label='Thêm mới Loại')
mnu_loai.add_separator()
mnu_loai.add_command(label='Exit',command=root.destroy)

menu_bar.add_cascade(label="Quản lý loại",menu=mnu_loai)

mnu_tool = Menu(menu_bar, tearoff=0)
mnu_tool.add_command(label="Danh sách")
mnu_tool.add_command(label="Thêm mới hàng hóa")
menu_bar.add_cascade(label="Hàng hóa",menu=mnu_tool)
###############/End Thêm menu item + xử lý*************

# Nhúng (add) menubnar vào màn hình chính
root.config(menu=menu_bar)

root.mainloop()