from tkinter import *

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

root.mainloop()