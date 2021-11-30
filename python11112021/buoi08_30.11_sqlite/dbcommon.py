import sqlite3


class MyDatabase:
    @staticmethod
    def sql_connection(self):
        try:
            return sqlite3.connect("MyDatabase.db")
        except Exception as ex:
            print(ex)
            return None

    @staticmethod
    def create_table(self, connection, sql_statetement):
        try:
            cursor = connection.cursor()
            cursor.execute(sql_statetement)
            connection.commit()
        except Exception as ex:
            print(ex)
