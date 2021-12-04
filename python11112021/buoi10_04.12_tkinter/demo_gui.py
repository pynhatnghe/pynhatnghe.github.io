from tkinter import *
from tkinter import ttk
from calendar import month_name
from datetime import datetime
from tkinter import messagebox

root = Tk()

# Config
root.geometry("300x200")
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

# Set event select month changed


def action_month_change(event):
    messagebox.showinfo(
        title='Result', message=f"Choose: {selected_month.get()}"
    )


cbo_month.bind('<<ComboboxSelected>>', action_month_change)

# Run
root.mainloop()
