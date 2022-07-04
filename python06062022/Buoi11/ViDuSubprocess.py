import subprocess

# Vd1: Không quan tâm kết quả
# subprocess.call(["ping", "google.com"])

# VD2: Gọi và lấy kết quả để xử lý
result = subprocess.getoutput('ping google.com')
print(result)
lines = result.split('\n')
print(lines)