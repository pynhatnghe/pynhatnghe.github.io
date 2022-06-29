from tkinter import *

# Cửa sổ chính
root = Tk()

# Gắn các control lên cửa số chính
Label(root,
    text= "Python Nhất Nghệ",
    bg="yellow green",    # bg: Màu nền
    fg = "red",           # fg: màu chữ
    font="Arial 14"
).pack()
Label(root, text= "Khai giảng: 06/06/2022").pack()

# Chú ý file dạng PNG/GIF
# img = PhotoImage(file="Python-Logo.png")
img = PhotoImage(file="python_gif.gif")
Label(root, image=img).pack()

from tkinter import messagebox
def say_hello():
    messagebox.showinfo("Hello",
        "Hello Sir/Madam!\nGood evening")

# Thêm nút nhấn
Button(root, text="Say Hello", command=say_hello).pack()

# Hiện cửa sổ chính
root.mainloop()