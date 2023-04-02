import mysql.connector
import os

class Conn:
    def __init__(self):
        self.conn = mysql.connector.Connect(
            host = os.environ.get("HOST"),
            user = os.environ.get("USER"),
            password = os.environ.get("PASSWORD"),
            database = os.environ.get("DATABASE"),
            port=os.environ.get("PORT")
        )
    def getCursor(self):
        return self.conn.cursor()
    def execute_query(self, query, values=None):
        cursor = self.getCursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        self.conn.commit()
        return cursor.fetchall()
    def close(self):
        self.getCursor().close()
        self.conn.close()