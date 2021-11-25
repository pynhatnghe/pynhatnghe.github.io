with open("mybinary.txt", "wb") as file:
    file.write(bytes("Hello Nhất Nghệ Tinh\n", 'utf-8'))
    file.write(bytes("Nhất thân vinh\n", 'utf-8'))
    file.write(bytes("Python Sqlite MySQL PosgreSQL, MongDB\n", 'utf-8'))

with open("mybinary.txt", "r", encoding='utf-8') as file:
    print(file.read())
