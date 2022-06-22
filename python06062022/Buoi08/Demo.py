from DatabaseUtils import DB_FILE, SqliteUtil

# print(DB_FILE)
# DB_FILE = "ABC.db"
# print(DB_FILE)
# print(SqliteUtil.create_connection())

if __name__ == '__main__':
    # Tạo 2 table
    sql_create_table_loai = """
         CREATE TABLE Loai(
         MaLoai integer PRIMARY KEY,
         TenLoai varchar(40)
     )
     """
    sql_create_table_hang_hoa = """
    CREATE TABLE HangHoa(
         MaHH char(6) PRIMARY KEY,
         TenHH varchar(40),
         MoTa varchar(55),
         DonGia decimal(10,2),
         SKU varchar(15) NULL,
         MaLoai interger NULL,
         FOREIGN KEY (MaLoai) REFERENCES Loai(MaLoai)
     )
     """
    SqliteUtil.execute(sql_create_table_loai)
    SqliteUtil.execute(sql_create_table_hang_hoa)