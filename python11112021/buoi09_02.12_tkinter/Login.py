from tkinter import *
from functools import partial


def xu_ly_login(username, password):
    print("Username", username.get())
    print("Password", password.get())


root = Tk()

root.title("Login form")
root.geometry("250x100")

lblTitle = Label(root, text="LOGIN",
                 font="Arial 12 bold").grid(row=0, column=1)
lblUser = Label(root, text="Username: ").grid(row=1, column=0)
lblPass = Label(root, text="Password: ").grid(row=2, column=0)
username = StringVar()
password = StringVar()
txtUser = Entry(root, textvariable=username, width=27).grid(row=1, column=1)
txtPass = Entry(root, textvariable=password, width=27).grid(row=2, column=1)

process_login = partial(xu_ly_login, username, password)
btnLogin = Button(root, text="Login",
                  command=process_login).grid(row=3, column=1)

# Run
root.mainloop()
