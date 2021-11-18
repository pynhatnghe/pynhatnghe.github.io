my_list = ["An", "Quỳnh", "Huy", "Phúc", "Yên"]
print(sorted(my_list))

def ham_sort(item):
    return len(item)
    
print(sorted(my_list,key=ham_sort))

#Demo sort dict ==> tự viết
my_dict = {
    2: 'Tèo', 0: 'Tý', 11: 'Hằng', 7: 'Huy', 8: 'Tèo'
}
dict_sorted_key = {} #dict_sorted_key = dict()
for key in sorted(my_dict.keys()):
    dict_sorted_key[key] = my_dict[key]
print(dict_sorted_key)
print(my_dict.values())
