# Ví dụ về List
'''
Nhập vào số phần tử (N)
Nhập giá trị từng phần tử của mảng
In ra số lượng, số nhỏ nhất, số lớn nhất, tổng
'''
N = 0
while N == 0:
    try:
        temp = int(input("Nhập số phần tử: "))
        if temp > 0:
            N = temp
            break
        else:
            print(("Số lượng phần tử phải dương. Nhập lại."))
    except Exception as ex:
        print("Lỗi: ", ex)

mang = []
while len(mang) < N:
    try:
        temp = float(input(f"Nhập số thực thứ {len(mang)}: "))
        mang.append(temp)
    except Exception as ex:
        print("Không phải số thực, ", ex)
print("Mảng: ", mang)
print("Nhỏ nhất: ", min(mang))
print("Lớn nhất: ", max(mang))
print("Tổng: ", sum(mang))
mang.sort() # Sắp tăng
print(mang)
mang.reverse()
print(mang)