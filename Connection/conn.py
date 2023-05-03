import logging
import mysql.connector
import os


class Conn:
    def __init__(self):
        self.conn = mysql.connector.Connect(
            # host=os.environ.get("HOST"),
            # user=os.environ.get("USER"),
            # password=os.environ.get("PASSWORD"),
            # database=os.environ.get("DATABASE"),
            # port=os.environ.get("PORT")
        host = "localhost",
        user = "root",
        password = "",
        database = "sieu_thi_mini",
        port = 3306

        )
        self.cursor = self.conn.cursor()

    def getCursor(self):
        if not self.conn.is_closed() and self.conn.is_connected():
            return self.conn.cursor()
        logging.error("Something wrong with db")
        return None

    def execute_query(self, query, values=None):
        cursor = self.getCursor()
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        self.conn.commit()
        return cursor.fetchall()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    # transaction
    def commit(self):
        if self.conn:
            self.conn.commit()

    def rollback(self):
        if self.conn:
            self.conn.rollback()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.cursor.rowcount

    def execute_one(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.cursor.fetchone()

    def execute_all(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.cursor.fetchall()
