import os

# Mở chương trình NotePad, MS Paint
# Gõ = lệnh ở command line/Terminal
# os.system("notepad.exe")
# os.system("mspaint")
os.system("ping google.com")


# Lấy thông tin hệ điều hành
print(os.name)
print("Thư mục hiện tại:", os.getcwd())

list_items_in_directory = os.listdir()
print(os.listdir())
list_items_in_python_folder = os.listdir(r"E:\pynhatnghe.github.io")
print(list_items_in_python_folder)
for item in list_items_in_python_folder:
    if os.path.isdir(os.path.join(r"E:\pynhatnghe.github.io", item)):
        print(f"{item} is directory")
    elif os.path.isfile(os.path.join(r"E:\pynhatnghe.github.io", item)):
        print(f"{item} is file")
