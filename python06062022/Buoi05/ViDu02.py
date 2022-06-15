'''
Ví dụ về tham số mật định
Viết hàm tính toán và trả vể (return) giá trị
cỏ 3 tham số mà 2 tham số mặc định
** Tham số mặc định phải liền sát nhau tính từ cuối tính lên
'''
def tinh_toan(a: float, b : float = 5.5, c: float = 9):
    print("a=",a,"b=",b, "c=",c)
    return a ** b / c

# Gọi hàm
gia_tri = tinh_toan(1,2,3)
gia_tri = tinh_toan(1.2, 2.2)
gia_tri = tinh_toan(11.1)
gia_tri = tinh_toan(11.1, c=2.2)
gia_tri = tinh_toan(b=11.1, c=2.2, a=3.3)
gia_tri = tinh_toan(c=2.2, a=3.3)
# gia_tri = tinh_toan() # Lỗi vì thiếu 1 tham sô bắt buộc
print(tinh_toan(1.3))
print(12 * tinh_toan(1,3,5))