"""
Yêu cầu nhập số nguyên dương N
Dùng while tính tổng S = 1 + 2 + 3 + ... + N
"""
while True:
    try:
        N = int(input("Nhập số nguyên dương N: "))
        break # DỪng vòng lặp
    except:
        print("Lỗi rồi, nhập lại đi")

tong = 0
# + 1 + 2 + 3 + ... + N
i = 1
while i <= N:
    tong = tong + i
    i = i + 1
print(f"Tổng các số nguyên từ 1 đến {N} là {tong}")
