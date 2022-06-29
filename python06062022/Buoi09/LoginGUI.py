from tkinter import *
from tkinter import ttk

root = Tk()
root.title("LOGIN - Authenticate user")
root.geometry("230x100")
root.resizable(0, 0) # cấm resize

ttk.Label(root, text="Username")\
    .grid(column=0, row=0, padx=5, pady=5)
ttk.Label(root, text="Password")\
    .grid(column=0, row=1, padx=5, pady=5)

ttk.Entry(root).grid(column=1, row=0)
ttk.Entry(root).grid(column=1, row=1)

ttk.Button(root, text="LOGIN").grid(column=1, row=2)

root.mainloop()