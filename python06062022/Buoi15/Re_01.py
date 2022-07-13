import re

txt = "The rain in Spain"
txt1 = "The Spain"
txt2 = "The spain"

x = re.search("^The.*Spain$", txt)
print(x)
# Phương thúc .search() trả MatchObject nếu khớp,
#   trả về None nếu không khớp
#

# Phương thức .split() tách chuỗi thành mảng chuỗi con
result = re.split("a", txt)
print(result)

# Kiểm đúng định dạng số điện thoại
vn_phone_pattern = "^0[98765][0-9]{8}$"
vn_phone_pattern = "^0[5-9]\d{8}$"

so_phone = "0989366999s"
check_result = re.match(vn_phone_pattern, so_phone)
check_result2 = re.search(vn_phone_pattern, so_phone)
if check_result:
    print("Đúng định dạng")
else:
    print("Sai định dạng")

'''
Kí hiệu:
    ^   đánh dấu bắt đầu bởi
    $   đánh dấu kết thúc
    *       đại diện cho từ 0 hoặc nhiều kí tự
    +       đại diện cho từ 1 hoặc nhiều kí tự
    ?       0 hoặc 1
    {x,y}   xuất hiện/lặp từ x đến y lần
    .   đại diện cho 1 kí tự tùy ý (trừ dấu xuống dòng)
    []  chọn 1 trong nhóm
    \   dùng cho kí tự đặc biệt, vd: \s khoảng trắng,
            \n xuống dòng, \t tab,
    [^arn]  không bắt đầu bởi hoặc a/hoặc r/hoặc n
'''