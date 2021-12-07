# Demo subprocess
# Quan tâm đến kết quả trả về
import subprocess
result = subprocess.getoutput("ping google.com")
# print(result)
# Xu ly tung dong kết quả trả về
lines = result.split("\n")
for line in lines:
    print(line)

# Xử lý lấy thời gian phản hồi time=
filter = "time="
for line in lines:
    if filter in line:  # Dòng đang xét có chứa filter
        index = line.index(filter) + len(filter)
        data_needed = line[index:]
        print(data_needed)
