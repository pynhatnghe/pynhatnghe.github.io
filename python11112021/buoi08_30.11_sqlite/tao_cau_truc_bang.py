from dbcommon import MyDatabase


def create_loai(connect):
    sql = '''
    CREATE TABLE Loai(
        MaLoai integer PRIMARY KEY AUTOINCREMENT,
        TenLoai varchar(40)
    )
    '''
    MyDatabase.create_table(connect, sql)


def create_hanghoa(connect):
    sql = '''
    CREATE TABLE HangHoa(
        MaHH char(6) PRIMARY KEY,
        TenHH varchar(40),
        MoTa varchar(55),
        DonGia decimal(10,2),
        SKU varchar(15) NULL,
        MaLoai interger NULL,
        FOREIGN KEY (MaLoai) REFERENCES Loai(MaLoai)
    )
    '''
    MyDatabase.create_table(connect, sql)


def chen_loai(connection):
    try:
        categories = (
            ('Ti vi',),
            ('Máy giặt',),
            ('Điều hòa',),
            ('Máy nước nóng',)
        )
        cursor = connection.cursor()
        cursor.executemany("INSERT INTO Loai(TenLoai) VALUES(?)", categories)
        connection.commit()
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    myconnection = MyDatabase.sql_connection()
    if myconnection:
        create_loai(myconnection)
        create_hanghoa(myconnection)
        chen_loai(myconnection)
