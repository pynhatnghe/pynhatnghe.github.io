"""Bài 7: Tính BMI
Yêu cầu: Nhập chiều cao (m), cân nặng (kg)
Xuất ra: Chỉ số BMI = cân nặng chia bình phương chiều cao
    Theo WHO:
        < 18.5: gầy
        18.5 <= BMI < 25: Bình thường
        25 <= BMI < 30: Thừa cân độ 1
        30 <= BMI < 40: Thừa cần độ 2
        BMI >= 40: Thừa cân độ 3
"""
try:
    chieu_cao = float(input("Chiều cao"))
    can_nang = int(input('Cân nặng'))
    
    bmi = can_nang / (chieu_cao * chieu_cao)
    print(f"Cao {chieu_cao} m, nặng {can_nang}kg. BMI: {bmi}")
    print(f"Tính thử 5 + 9 = {5+9}")
    
    if bmi >= 40:
        print("Thừa cân độ 3")
    elif bmi >= 30: # 30 <= BMI < 40: Thừa cần độ 2
        print("Thừa cân độ 2")
    elif bmi >= 25:
        print("Thừa cân độ 1")
    elif bmi >= 18.5:
        print("Sức khỏe bình thường")
    else:
        print("Gầy")
except Exception as e:
    print("Lỗi", e)
