# Tao mang số nguyên từ 3 đến 11
# range(start, stop, step=1):
# sinh mảng chạy từ start --> stop -1 (không bằng stop)
# mỗi phần tử cách nhau step
mang = range(3, 12, 2)
print(mang)
print(list(mang))
for item in range(3, 11):
    print(item)

#================
#Ví dụ: cho mảng và xuất từng phần từ trong mảng
mang_so = [1.2, 3, -9, 234, 111]
for item in mang_so:
    print(item)
# In mảng với chỉ số
for idx in range(0, len(mang_so)):
    print(idx, " : ", mang_so[idx])