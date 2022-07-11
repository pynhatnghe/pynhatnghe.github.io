import matplotlib.pyplot as plt

# plt.figure(figsize=(15, 5))
plt.plot([1,2,3,4], [1,4,9,16], "m*-")
plt.title("Biểu đồ giá xăng")
plt.xlabel("lít")
plt.ylabel("$ USD")
plt.show()

''''
format: xyz
    x: màu, giá trị r,g,b
    y: đánh dấu tọa độ điểm:
        *: sao
        ^: tam gác
        o: tròn đen
    z: có hoặc không (-: đường nối các đỉnh)
'''