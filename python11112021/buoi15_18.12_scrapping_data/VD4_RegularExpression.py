import re

chuoi_du_lieu = "Nhất Nghệ học Python, học dễ, nhiều kiến thức python bổ ích"

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

result = re.split("học", chuoi_du_lieu)
print(result)
x = re.findall("học", chuoi_du_lieu)
print(x)

# ==============
manv = "NV001.KT.001"
pattern = "^NV[0-9]{3}.\w{2}.\d{3}$"
result = re.match(pattern, manv)
if result:
    print("Match")
else:
    print("Not match")
