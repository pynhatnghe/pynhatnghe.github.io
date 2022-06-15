# Định nghĩa hàm
# Hàm my_function có 1 tham số, ko kiểu trả về
def my_function(name):
    print("Hello", name)

def say_hello(name: str = "Nhất Nghệ"):
    print("Hello" + name)

# Gọi hàm
# Lời gọi hàm nằm ở từng dòng riêng biệt
my_function("Teo")
my_function("Mr . Bean")
my_function(1234)
my_function([1,2,3,4])
say_hello()
say_hello("Mr David")
say_hello(124)
say_hello({124})
say_hello([1,2])
