a = {"hang_1": "MU", "hang_2": "LIV"}
b = {"hang_2": "ABC", "hang_3": "CHE"}
print(a)
print(b)

a.update(b)
print(a)

b["hang_2"] = "NEW"
b["hang_4"] = "EVE"
print(b)

list_c = [item for item in range(9) if item % 3 != 0] #1,2,4,5,7,8
print(list_c)
print(list_c[3]) #In phần tử vị trí số 3

dict_d = {key:key**3 for key in range(1,10)}
print(dict_d)
print(dict_d[5])
print(dict_d.get(11))

