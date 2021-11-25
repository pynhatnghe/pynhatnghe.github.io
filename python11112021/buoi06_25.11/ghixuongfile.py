import os
file_bcc = "data\\bangcuuchuong.txt"

# Ghi xuong file bang cuu chuong
myfile = open(file_bcc, "w")
for idx in range(1, 11):
    myfile.write(f"11 x {idx} = {11 * idx}\n")
myfile.close()

# Doc noi dung file
with open(file_bcc) as my_file:
    print(my_file.read())


# Xoa file
if os.path.exists(file_bcc):
    os.remove(file_bcc)
