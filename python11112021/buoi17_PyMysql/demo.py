import pymysql

# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='demopysql',
    cursorclass=pymysql.cursors.DictCursor
)


with connection:
    print("Begin working with database")

    # Chèn mới 1 user vào trong database, bảng user
    with connection.cursor() as cursor:
        try:
            sql1 = "INSERT INTO users(email, password) VALUES('admin@nn.com', '123')"
            cursor.execute(sql1)

            sql2 = "INSERT INTO users(email, password) VALUES(%s, %s)"
            cursor.execute(sql2, ('test@nn.com', '123456'))

            connection.commit()
        except Exception as ex:
            print(ex)

    with connection.cursor() as cursor:
        sql = "SELECT id, email FROM users"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
