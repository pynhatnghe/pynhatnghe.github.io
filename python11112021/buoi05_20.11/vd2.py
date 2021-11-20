"""Tham số hàm:
- Default params
- *args
- **kargs
"""


def tinh_toan(a=10, b=5, c=7):
    print("a =", a, "b =", b, "c =", c)
    return (a + c)**b


print(tinh_toan())  # a = 10, b = 5, c = 7
print(tinh_toan(19))  # a = 19, b = 5, c = 7
print(tinh_toan(13, 7))  # a = 13, b = 7, c = 7
# Gọi hàm không theo thứ tự thì phải chỉ định tên
print(tinh_toan(c=4, a=78, b=1))


# Tham số dạng *args: số lượng tham số biến động (list: có thể lấy ra theo chỉ số)
def xuat(*items):
    # print(items[3])
    for item in items:
        print("Xin chào", item)


#xuat(["Cam", "Đào", 'Mận', 'Ổi'])
#xuat(('Quýt', 'Bưởi'))

xuat("Cam", "Đào", 'Mận', 'Ổi')
xuat('Quýt', 'Bưởi')


def demo_sao_co_sao(tham_so, *args):
    print(tham_so, args)
    print(f"Có tổng cộng {1 + len(args)} tham số.")


demo_sao_co_sao("Python")
demo_sao_co_sao("Hello", 1, 4)
demo_sao_co_sao("Hello", 1, 4, 9, 11)


# Tham số có 2 dấu *: mỗi tham số truyền vào (số lượng ko cố định) dạng key=value ==> **kwargs: giống dictionary
def my_func(**kid):
    print("Ten: ", kid["ten"])


my_func(tuoi=19, ten="Lê Thành Tùng")


def new_my_func(**args):
    for key, value in args.items():
        print("key=", key, "value=", value)


new_my_func(ten="Tèo", phone="333999", tuoi=19)
