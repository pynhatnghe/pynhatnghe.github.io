from tkinter import *
from tkinter import ttk
from calendar import month_name
from datetime import datetime
from tkinter import messagebox

root = Tk()

# Config
root.geometry("300x300")
root.resizable(False, False)
root.title("DEMO Combo")

# Label
label = Label(text="Please choose month:")
label.pack(fill=X, padx=5, pady=5)

# Combobox / Dropdown
selected_month = StringVar()
cbo_month = ttk.Combobox(root, textvariable=selected_month)
cbo_month["values"] = [month_name[mo][0:3] for mo in range(1, 13)]
cbo_month.pack(fill=X, pady=5, padx=5)

# set current month
current_month = datetime.now().strftime("%b")
cbo_month.set(current_month)


def action_month_change(event):
    messagebox.showinfo(
        title='Result', message=f"Choose: {selected_month.get()}"
    )


cbo_month.bind('<<ComboboxSelected>>', action_month_change)

# DEMO Radio Button
selected_size = StringVar()
sizes = (
    ('Small', 'S'),
    ("Medium", "M"),
    ("Large", "L"),
    ("Extra Large", "XL"),
    ("Extra Extra Large", "XXL")
)
Label(text="Please choose t'shirt size?").pack(fill=X, pady=5, padx=5)
for size in sizes:
    ttk.Radiobutton(root, text=size[0], value=size[1], variable=selected_size)\
        .pack(fill=X, pady=5, padx=5)

# set default
selected_size.set('L')


def show_selected_size():
    messagebox.showinfo(
        title='Size', message=f"Đang chọn {selected_size.get()}"
    )


Button(root, text="show selected size",
       command=show_selected_size).pack(fill=X, pady=5, padx=5)

# Run
root.mainloop()
