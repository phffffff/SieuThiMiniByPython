from Connection.conn import Conn
from Common.CRUD import Crud_Dal
# import mysql.connector.errors
# import logging


class ProductDal(Crud_Dal):
    def __init__(self):
        self.conn = Conn()
        Crud_Dal.__init__(self, tableName="products", conn=self.conn)

