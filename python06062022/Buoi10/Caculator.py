from tkinter import *

root = Tk()
WIDTH = 300
HEIGHT = 325
ITEM_HEIGHT = 50

root.title("CALCULATOR")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)

# Tạo frame (vùng) để nhập liệu & hiển thị
input_frame = Frame(root, width=WIDTH, height=ITEM_HEIGHT,
    highlightbackground="black", highlightcolor="black",
    highlightthickness=2)
input_frame.pack()

# Thêm thẻ input bên trong khung
input_text = StringVar()
input_field = Entry(
    input_frame, font="Arial 18 bold",
    textvariable=input_text,
    width=50, background="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10, ipadx=5) # internal padding y

# Tạo frame bao chứa các button bên dưới
button_frame = Frame(root, width=WIDTH, height=275, bd=0,
    highlightbackground="black", highlightcolor="black",
    highlightthickness=2)
button_frame.pack(side=TOP)

root.mainloop()