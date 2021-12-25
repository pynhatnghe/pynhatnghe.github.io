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
    with connection.cursor() as cursor:
        myemail = 'admin@nn.com'
        cursor.execute("CALL FindUser(%s)", (myemail, ))
        print(cursor.fetchall())
