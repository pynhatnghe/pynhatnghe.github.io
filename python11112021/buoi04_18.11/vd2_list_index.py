# Demo index & sắp xếp
a = [ 2, 3, 5, 2, 6, 2, 2, 7 ] 
print(a.index(2))
print(a.index(2, 2)) # Tìm 2 từ vị trí thứ 2 trở đi
print(a.index(2, 4))
print(a.index(2, 6))

# Sắp xếp
a.sort() # Sắp tăng
print(a)
a.sort(reverse=True) #Sắp giảm
print(a)


a = [ 2, 3, 4, 3, 24, 3 ]
print(a)
print(a[2:])
print(a[:2] + [5] + a[2:])

a.append(7)
a.remove(3) #Xóa phần tử có giá trị là 3
print(a)
item = a.pop(4) #Xóa phần tử tại vị trí thứ 4
print('Sau khi xoa', a)
del a # Xoa bien
print(a)