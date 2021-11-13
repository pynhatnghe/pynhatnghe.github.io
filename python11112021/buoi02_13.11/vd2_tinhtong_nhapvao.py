"""
Nhập vào số nguyên dương N. Tính tổng các số nguyên từ 1 đến N.
"""

"""
Trong vòng lặp:
- break: thoát vòng lặp (gần nhất)
- continue: tiếp tục lần lặp mới
"""

while True:
    try:
        so_nguyen = int(input("Nhập số nguyên dương N: "))
        
        if so_nguyen < 1:
            continue #Tiếp tục lần lặp mới
        
        break #Thoát vòng lặp
    except:
        print("Nhập sai")

#Tính tổng
tong = 0
for phantu in range(1, so_nguyen + 1):
    #print(phantu)
    tong = tong + phantu
    
print(f"Tổng các số từ 1 đến {so_nguyen} là {tong}")

