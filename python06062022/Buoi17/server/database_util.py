import pymysql

class MySqlUtil:
    @staticmethod
    def create_connection():
        try:
            return pymysql.connect(host='localhost',
                user='root',
                password='',
                database='pythonnn',
                cursorclass=pymysql.cursors.DictCursor
            )
        except Exception as ex:
            print(ex)
            return None

    @staticmethod
    def execute(sql_command):
        conn = MySqlUtil.create_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute(sql_command)
                conn.commit()
                conn.close()
                return True
            except Exception as ex:
                print(ex)
                return False
        else:
            return False

    @staticmethod
    def query(sql_query_command):
        conn = MySqlUtil.create_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute(sql_query_command)
                data = cur.fetchall()
                conn.close()
                return data
            except Exception as ex:
                print(ex)
                return None
        else:
            return None

    @staticmethod
    def insert_and_get_lasted_id(sql_statetement):
        conn = MySqlUtil.create_connection()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute(sql_statetement)
                conn.commit()
                lastid = cur.lastrowid
                conn.close()
                return lastid
            except Exception as ex:
                print(ex)
                return None
        else:
            return None
