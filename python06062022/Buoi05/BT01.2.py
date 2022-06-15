'''Ví dụ về tham số *'''
# Số lượng tham số ko hạn chế cách nhau bởi dấu ,
def plus(*tham_so):
    print(tham_so)
    return sum(tham_so)

# Gọi hàm
print(plus(1,2,3,4))
# print(plus([1,2,3,4])) # Sai vì list cũng chỉ là 1 tham số


