'''
Lambda function - hàm vô danh - hàm ko có tên
có kiểu trả về
cần biến giữ ==> biến đó sẽ làm tên hàm tạm thời trong ngữ cảnh
'''
ham_mu = lambda  x,y : x**y
print(ham_mu(3,4))
print(ham_mu(3.3,4.9))

mang_diem = [1.2, 7.9, 3.2, 4.2, 8, 9, 10, 5.9]
# yêu cầu lọc lấy danh sách điểm >= 4
diem_dau = filter(lambda diem: diem >= 4, mang_diem)
print(diem_dau)
print(list(diem_dau))

#tăng 1.5 đ cho mỗi HS, nếu > 10 thì ghi 10
# Từ python 3.9: a = x if bthuc_dkien else y
# nếu bthuc_dkien = true ==> x, false ghi y
diem_sau_tang = list(map(
    lambda sv: 10 if sv + 1.5 > 10 else sv + 1.5,
    mang_diem
))
print(diem_sau_tang)