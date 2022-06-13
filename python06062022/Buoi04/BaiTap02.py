'''
Nhập vào 1 đoạn văn bản
In ra các từ đơn phân biệt (set) trong văn bản
'''
chuoi = input("Nhập vào chuỗi: ")
mang = chuoi.split() # điều kiện tách là khoảng trắng
print(mang)
print(len(mang))
tap_hop = set(mang)
print(tap_hop)
print(len(tap_hop))