from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("LOGIN - Authenticate user")
root.geometry("230x100")
root.resizable(0, 0) # cấm resize

ttk.Label(root, text="Username")\
    .grid(column=0, row=0, padx=5, pady=5)
ttk.Label(root, text="Password")\
    .grid(column=0, row=1, padx=5, pady=5)

# Đặt 2 biến để giữ giá trị 2 entry
username = StringVar(value="user")
password = StringVar()
ttk.Entry(root, textvariable=username)\
    .grid(column=1, row=0)
ttk.Entry(root, textvariable=password, show="*")\
    .grid(column=1, row=1)

def handle_login(title_bar):
    messagebox.showinfo(title_bar,
    f"Bạn nhập:\nUsername:{username.get()}"
    + f"\nPassword: {password.get()}")

from functools import partial
process_login = partial(
    handle_login,
    title_bar="PYTHON ABC"
)
ttk.Button(root, text="LOGIN", command=process_login)\
    .grid(column=1, row=2, sticky=E)

root.mainloop()