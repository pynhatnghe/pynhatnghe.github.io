from dbcommon import MyDatabase


def test_insert_lop(connection):
    sql = '''
    INSERT INTO HocVien(SoDienThoai, HoTen, MaLop)
        VALUES('0989333999', 'Anh Hùng', 1)
    '''
    MyDatabase.create_table(connection, sql)


if __name__ == "__main__":
    connection = MyDatabase.sql_connection()
    test_insert_lop(connection)
