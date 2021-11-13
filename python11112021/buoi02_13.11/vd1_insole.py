#In các số lẻ mà chia hết cho 3 từ nhỏ hơn 21

so = 2

while so < 21:
    if so % 2 == 1 and so % 3 == 0:
        print(so)
    so += 1 # so = so + 1