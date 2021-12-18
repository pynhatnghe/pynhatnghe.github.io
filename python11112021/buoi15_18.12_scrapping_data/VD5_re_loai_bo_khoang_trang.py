'''Loại bỏ khoảng trắng ở giữa chuỗi'''
import re
mystring = '''abc  def 12
def 123 \n ghj 233'''

pattern = '\s+'

replace = ''

new_string = re.sub(pattern, replace, mystring)

print(new_string)

gia = "1,234,000"
print(re.sub(",", "", gia))
'''
TÓM TẮT CÁC TỪ KHÓA THÔNG DỤNG CỦA REGULAR EXPRESSION
- Ký tự đại diện:
    []: lấy 1 trong các kí tự trong tập hợp (móc vuông)
        vd: [abc] nghĩa là hoặc a, hoặc b, hoặc c
    \: thường dùng với các kí tự đại diện, hoặc ký tự đặc biệt.
        vd: muốn có dấu \ trong mẫu kiểm tra thì dùng \\
            \d: số nguyên từ 0 --> 9
    .   : đại diện 1 ký tự bất kỳ
    \w  : đại diện 1 ký tự chữ cái (a-z, 0-9 và _)
    \d  : đại diện 1 ký tự chữ số (0 --> 9)
    \s  : đại diện cho 1 khoảng trắng
    \t  : tab
    ^   : đánh dấu bắt đầu
    $   : đánh dấu kết thúc
    *   : 0 hoặc 1 hoặc nhiều
    +   : 1 hoặc nhiều
    ?   : 0 hoặc 1
    {n} : chính xác n lần
    () kết hợp | để biễu diễn hoặc: VD: abc hoặc def ==> (abc|def)
'''
