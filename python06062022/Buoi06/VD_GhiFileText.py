from datetime import datetime
my_file = open("my_info.txt", "w+", encoding="utf-8")
my_file.write("Tui tên Tèo\n")
my_file.write(datetime.now().strftime("%d-%m-%Y %I:%M:%S"))
my_file.write("\nPhone: 0909009990")
my_file.close()

if my_file.closed:
    print(f"File {my_file.name} đang đóng")
    print(my_file.mode)