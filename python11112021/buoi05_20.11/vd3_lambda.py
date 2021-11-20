# Hàm lambda
# lambda arguments: expression

my_func = lambda x, y: x**y


def my_func2(x, y):
    return x ** y


print(my_func(2, 8))

print(my_func2(2, 8))


# Lambda dùng chung với filter dùng để lọc phần tử thỏa điều kiện
my_list = [1, 8, 3, 2, 10, 46, 79]
mang_so_chan = list(filter(lambda x: x % 2 == 0, my_list))
print(mang_so_chan)


# Lambda dùng chung với map dùng để định nghĩa mảng mới (cùng số lượng phần tử)
my_list = [1, 8, 3, 2, 10, 46, 79]
mang_lap_phuong = list(map(lambda x: x**3, my_list))
print(mang_lap_phuong)
