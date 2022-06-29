from tkinter import *

root = Tk()

# Khai báo menu bar
menu_bar = Menu(root)

###############Thêm menu item + xử lý*************
file_menu = Menu(menu_bar)
file_menu.add_command(label='Open')
file_menu.add_command(label='Save')
file_menu.add_command(label='Exit',command=root.destroy)

menu_bar.add_cascade(label="File",menu=file_menu)
###############/End Thêm menu item + xử lý*************

# Nhúng (add) menubnar vào màn hình chính
root.config(menu=menu_bar)

root.mainloop()