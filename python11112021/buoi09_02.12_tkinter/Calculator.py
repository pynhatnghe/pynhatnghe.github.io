from tkinter import *
root = Tk()
root.title("Calculator")
root.geometry("300x325")
root.resizable(0, 0)  # Cam resize

expression = ""
input_text = StringVar()

input_frame = Frame(root, width=300, height=50, bd=0,
                    highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=TOP)

# Tạo thẻ input bên trong khung
input_field = Entry(input_frame, font="Arial 18 bold", textvariable=input_text,
                    width=50, background="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)  # internal padding y

# Tạo frame bao chứa các button bên dưới
button_frame = Frame(root, width=300, height=275, bd=0,
                     highlightbackground="black", highlightcolor="black", highlightthickness=2)
button_frame.pack(side=TOP)
clear = Button(button_frame, text="Clear", height=3, width=20).grid(
    row=0, column=0, columnspan=2, padx=1, pady=1)
back = Button(button_frame, text="<--", height=3, width=20).grid(
    row=0, column=2, columnspan=2, padx=1, pady=1)

# Row 1: 7,8,9, /
so7 = Button(button_frame, text="7", width=9, height=3).grid(
    row=1, column=0, padx=1, pady=1)
so8 = Button(button_frame, text="8", width=9, height=3).grid(
    row=1, column=1, padx=1, pady=1)
so8 = Button(button_frame, text="9", width=9, height=3).grid(
    row=1, column=2, padx=1, pady=1)
chia = Button(button_frame, text="/", width=9, height=3).grid(
    row=1, column=3, padx=1, pady=1)

# RUN
root.mainloop()
