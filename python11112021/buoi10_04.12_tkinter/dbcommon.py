import sqlite3


class MyDatabase:
    @staticmethod
    def sql_connection():
        try:
            return sqlite3.connect("MyDatabase.db")
        except Exception as ex:
            print(ex)
            return None

    @staticmethod
    def run_statement(connection, sql_statetement):
        try:
            cursor = connection.cursor()
            cursor.execute(sql_statetement)
            connection.commit()
        except Exception as ex:
            print(ex)

    @staticmethod
    def insert_and_get_lasted_id(connection, sql_statetement):
        try:
            cursor = connection.cursor()
            cursor.execute(sql_statetement)
            connection.commit()
            return cursor.lastrowid
        except Exception as ex:
            print(ex)
            return None

    @staticmethod
    def query_data(connection, sql_statetement):
        try:
            cursor = connection.cursor()
            cursor.execute(sql_statetement)
            return cursor.fetchall()
        except Exception as ex:
            print(ex)
            return None
