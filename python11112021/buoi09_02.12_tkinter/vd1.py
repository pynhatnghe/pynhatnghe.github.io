import tkinter as tk

# Primary GUI
root = tk.Tk()

# Label: xuất hiện thông báo
greeting = tk.Label(
    text="Hello Py Nhất Nghệ",
    foreground="yellow",
    background="blue",
    font="Arial 14 italic",
    height=3, width=20
)
greeting.pack()

# Entry: Ô nhập liệu 1 dòng
entry = tk.Entry()
entry.pack()

# Text: Ô nhập nhiều dòng
text_box = tk.Text()
text_box.pack()

# Run
root.mainloop()
