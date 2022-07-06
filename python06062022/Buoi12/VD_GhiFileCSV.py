import csv

with open("demo1.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=",")

    writer.writerow(["STT", "Tên", "Điện thoại"])
    writer.writerow([1, "Tèo Trần", "0123456789"])
    writer.writerow([3, "Lê Trần", "0123456789"])
