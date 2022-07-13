'''
Loại bỏ khoảng trắng thừa bên trong chuỗi
'''''
import re

chuoi_van_ban='''Văn     bản Python   đã   update   2 date
PyNhat   Nghe 02   02   202                            0
'''

pattern = "\s{3}"
result = re.sub(pattern, '', chuoi_van_ban)
print(result)