from tkinter import *
from tkinter import messagebox
from functools import partial


def xu_ly_login(username, password, remember_me):
    print("Username", username.get())
    print("Password", password.get())
    messagebox.showinfo("Login", "Username: " + username.get() +
                        "\nPassword: " + password.get() +
                        "\nRemember: " + str(remember_me.get()))


root = Tk()

root.title("Login form")
root.geometry("250x123")

lblTitle = Label(root, text="LOGIN",
                 font="Arial 12 bold").grid(row=0, column=1)
lblUser = Label(root, text="Username: ").grid(row=1, column=0)
lblPass = Label(root, text="Password: ").grid(row=2, column=0)
username = StringVar()
password = StringVar()
txtUser = Entry(root, textvariable=username, width=27).grid(row=1, column=1)
txtPass = Entry(root, textvariable=password, width=27).grid(row=2, column=1)

remember_me = IntVar()
Checkbutton(root, text="Ghi nhớ", variable=remember_me).grid(row=4, sticky=W)
process_login = partial(xu_ly_login, username, password, remember_me)
btnLogin = Button(root, text="Login",
                  command=process_login).grid(row=3, column=1)


# Run
root.mainloop()
