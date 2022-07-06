import csv

with open("hang_mua.csv", "r", encoding="utf-8") as file:
    # data = csv.reader(file)
    #
    # for item in data:
    #     print(item)

    # T.h khác
    my_data = csv.DictReader(file)
    for item in my_data:
        print(item)