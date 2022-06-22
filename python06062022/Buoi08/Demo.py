from DatabaseUtils import DB_FILE, SqliteUtil

# print(DB_FILE)
# DB_FILE = "ABC.db"
# print(DB_FILE)
# print(SqliteUtil.create_connection())

def insert_loai(ma_loai, ten_loai):
    sql_insert_loai = f'''
    INSERT INTO Loai(MaLoai, TenLoai)
    VALUES('{ma_loai}', '{ten_loai}')
    '''
    if SqliteUtil.execute(sql_insert_loai):
        print('Thêm loại thành công')

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

    # Thêm loại
    insert_loai(1, 'Bánh mì')
    insert_loai(2, 'Bánh canh')

