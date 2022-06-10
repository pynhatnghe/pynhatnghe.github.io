chuoi = input("Nhập chuỗi: ")
print(f"Chuỗi {chuoi} có {len(chuoi)} ký tự.")
my_enum = enumerate(chuoi) # nhiều phần tử dạng (index, value)
print(my_enum)
print(list(my_enum)) # ==> thường dùng
print(tuple(my_enum))
print(dict(my_enum))
