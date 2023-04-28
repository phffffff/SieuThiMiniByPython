import logging
import mysql
from Connection.conn import Conn
from Common.CRUD import Crud_Dal

class CoupouDal(Crud_Dal):
    def __init__(self):
        self.conn = Conn()
        Crud_Dal.__init__(self, tableName="coupous", conn=self.conn)