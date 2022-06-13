# Cho danh sách các thời điểm khách hàng đến cửa hàng
# In ra các khung giờ có khách hàng
timestamps = ['06:45', '06:50', '07:05', '07:15', '08:05',
 '11:45', '11:50', '11:55', '12:15', '12:30', '13:05',
 '18:45', '18:50', '19:15', '19:30', '19:45'
 ]

khung_gio = set()
thong_ke = dict() # thong_ke = {}
for item in timestamps:
  temp = item.split(":")
  hour, minute = temp
  # print(temp,  hour, minute)

  khung_gio.add(hour)

  # Cách 1: dùng hàm get() có gán = 0 nếu ko tìm thấy
  thong_ke[hour] = thong_ke.get(hour, 0) + 1

  # Cách 2 viết rõ
  # if hour in thong_ke:
  #   thong_ke[hour] += 1
  # else:
  #   thong_ke[hour] = 1

print(khung_gio)
print(thong_ke)
print("Khung gio co nhieu lượt viếng thăm: ", end="")
so_lan_max = max(list(thong_ke.values()))
for item in thong_ke:
 if thong_ke[item] == so_lan_max:
   print(item, end=", ")