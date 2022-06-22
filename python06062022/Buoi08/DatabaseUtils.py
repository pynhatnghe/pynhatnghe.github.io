import sqlite3

DB_FILE = "MySqlite3.db"
class SqliteUtil:
    @staticmethod
    def create_connection():
        try:
            return sqlite3.connect(DB_FILE)
        except Exception as ex:
            print(ex)
            return None

    @staticmethod
    def execute(sql_command):
        conn = SqliteUtil.create_connection()
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
        conn = SqliteUtil.create_connection()
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