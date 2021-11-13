# Yêu cầu: In bảng cửu chương từ 2 --> 9
#Viết hàm in bảng cửu chương
def in_bang_cuu_chuong(N : int):
    '''Bảng cửu chương'''
    for j in range(0, 11):
        print(f"{N} x {j} = {N*j}")
        
for i in range(2, 10):
    print()
    #Bảng cửu chương i
    #for j in range(0, 11):
    #    print(f"{i} x {j} = {i*j}")
    in_bang_cuu_chuong(i)

