chuoi = "Python Nhất Nghệ học đủ thứ"

print(chuoi[5 : 8])
print(chuoi[5:])
print(chuoi[:5])

# Xóa chuỗi từ vị trí thứ 6 đến hết: chuoi[:6]

#In chuỗi Đảo ngược chuỗi
index = 0
do_dai = len(chuoi)
# Mảng động list
mang_1 = []
mang_2 = []
while index < do_dai:
    mang_1.append(chuoi[do_dai - index - 1])
    mang_2.append(chuoi[ - index - 1])
    index += 1
    
print("".join(mang_1))    
print("".join(mang_2))

#Cách 2:
mang_3 = []
for chi_so in range(do_dai - 1, -1, -1):
    mang_3.append(chuoi[chi_so])

print("".join(mang_3))