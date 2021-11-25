myfile = open("nhatnghedata.txt", "r")

# Cách 1: Đọc từng dòng
#print(myfile.readline())
#print(myfile.readline())
#print(myfile.readline())

# cách 2: Đọc tất cả dòng,
#lines = myfile.readlines() # trả về mảng chuỗi các dòng đọc được
#for line in lines:
#    print(line)

# Cách 3: Đọc theo số lượng kí tự
data = myfile.read(19)
print(data)
myfile.close()