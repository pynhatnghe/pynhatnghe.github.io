'''
Nhập họ tên.
Nhập năm sinh
In ra chào bạn ? tuổi
'''
try:
    ho_ten = input("Nhập họ tên của bạn:")
    print(type(ho_ten))
    nam_sinh = int(input("Nhập năm sinh:"))
    print(type(nam_sinh))
    print(f"Chào bạn {ho_ten}, {2022 - nam_sinh} tuổi.")
except Exception as e:
    print("Lỗi: ", e)