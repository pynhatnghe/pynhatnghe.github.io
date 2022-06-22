import sqlite3

conn = sqlite3.connect("MyDB.db")
cur = conn.cursor()
cur.execute('''CREATE TABLE HocVien
(
    MaHV text PRIMARY KEY,
    HoTen text,
    DienThoai text,
    NgaySinh date,
    Email text
)
''')
conn.commit()
conn.close()