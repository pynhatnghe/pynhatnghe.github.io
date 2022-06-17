my_file = open("my_info.txt", "r", encoding="utf-8")
lines = my_file.readlines()
print(lines)
my_file.close()
