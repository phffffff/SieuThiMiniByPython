from Connection.conn import Conn
from Common.CRUD import Crud_Dal
import logging
import mysql.connector


class ProductDal(Crud_Dal):
    def __init__(self):
        self.conn = Conn()
        Crud_Dal.__init__(self, tableName="products", conn=self.conn)

    def update_decrease(self, count, where):
        try:
            where_clause = " AND ".join([f"{col}=%s" for col in where])
            sql = f"UPDATE {self.tableName} SET count = count - {count} WHERE {where_clause}"

            params = tuple(where.values())
            result = self.conn.execute(sql,params)
            self.conn.commit()
            self.conn.close()
            if result:
                return result
            return None
        except mysql.connector.Error as e:
            logging.error("Error: {}".format(e))
            self.conn.rollback()
            return None