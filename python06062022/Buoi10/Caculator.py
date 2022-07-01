from tkinter import *

root = Tk()
WIDTH = 300
HEIGHT = 345
ITEM_HEIGHT = 50

root.title("CALCULATOR")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)

expression = "0"
############# Định nghĩa hám xử lý$$$$$$$$$$
def click_number(item):
    global expression
    if expression == "0":
        if item > 0:
            expression = str(item)
    else:
        expression += str(item)
    input_text.set(expression)

def click_clear():
    global expression
    expression = "0"
    input_text.set(expression)

def click_back():
    global expression
    # expression = expression[:-1]
    # if expression == "":
    #     expression = "0"
    expression = expression[:-1] if len(expression) > 1 else "0"
    input_text.set(expression)


#############$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# Tạo frame (vùng) để nhập liệu & hiển thị
input_frame = Frame(root, width=WIDTH, height=ITEM_HEIGHT,
    highlightbackground="black", highlightcolor="black",
    highlightthickness=2)
input_frame.pack()

# Thêm thẻ input bên trong khung
input_text = StringVar(value=expression)
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

# Dòng 0: Nút CLEAR, BACK
clear = Button(
    button_frame, text="Clear", height=3, width=20,
    command=click_clear
).grid(row=0, column=0, columnspan=2, padx=1, pady=1)
back = Button(
    button_frame, text="<--", height=3, width=20,
    command=click_back
).grid(row=0, column=2, columnspan=2, padx=1, pady=1)

# Row 1: 7,8,9, /
so7 = Button(
    button_frame, text="7", width=9, height=3,
    command=lambda: click_number(7)
).grid(row=1, column=0, padx=1, pady=1)
so8 = Button(
    button_frame, text="8", width=9, height=3,
    command=lambda: click_number(8)
).grid(row=1, column=1, padx=1, pady=1)
so9 = Button(
    button_frame, text="9", width=9, height=3,
    command=lambda: click_number(9)
).grid(row=1, column=2, padx=1, pady=1)
chia = Button(button_frame, text="/", width=9, height=3).grid(
 row=1, column=3, padx=1, pady=1)

# Row 2: 4, 5, 6, *
so4 = Button(
    button_frame, text="4", width=9, height=3,
    command=lambda: click_number(4)
).grid(row=2, column=0, padx=1, pady=1)
so5 = Button(
    button_frame, text="5", width=9, height=3,
    command=lambda: click_number(5)
).grid(row=2, column=1, padx=1, pady=1)
so6 = Button(
    button_frame, text="6", width=9, height=3,
    command=lambda: click_number(6)
).grid(row=2, column=2, padx=1, pady=1)
nhan = Button(button_frame, text="*", width=9, height=3).grid(
 row=2, column=3, padx=1, pady=1)

# Row 3: 1, 2, 3, -
so1 = Button(
    button_frame, text="1", width=9, height=3,
    command=lambda: click_number(1)
).grid(row=3, column=0, padx=1, pady=1)
so2 = Button(
    button_frame, text="2", width=9, height=3,
    command=lambda: click_number(2)
).grid(row=3, column=1, padx=1, pady=1)
so3 = Button(
    button_frame, text="3", width=9, height=3,
    command=lambda: click_number(3)
).grid(row=3, column=2, padx=1, pady=1)
tru = Button(button_frame, text="-", width=9, height=3).grid(
 row=3, column=3, padx=1, pady=1)

# Row 4: 0, ., =, +
so0 = Button(
    button_frame, text="0", width=9, height=3,
    command=lambda: click_number(0)
).grid(row=4, column=0, padx=1, pady=1)
cham = Button(button_frame, text=".", width=9, height=3).grid(
 row=4, column=1, padx=1, pady=1)
bang = Button(button_frame, text="=", width=9, height=3).grid(
 row=4, column=2, padx=1, pady=1)
cong = Button(button_frame, text="+", width=9, height=3).grid(
 row=4, column=3, padx=1, pady=1)

root.mainloop()