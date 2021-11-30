import sqlite3

connection = sqlite3.connect("MyDatabase.db")

cursor = connection.cursor()

# Lấy data ra
cursor.execute("""
SELECT MaLop, Tenlop, SoGio, HocPhi FROM LopHoc 
ORDER BY HocPhi ASC, SoGio DESC
""")

rows = cursor.fetchall()
print(rows)
print(f"Tổng cộng {len(rows)} dòng")
for item in rows:
    print(item[0], item[1], item[2], item[3])

connection.close()
