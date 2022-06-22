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
