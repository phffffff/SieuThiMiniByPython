import logging
import mysql
from Connection.conn import Conn
from Common.CRUD import Crud_Dal
class Promotion_Dal(Crud_Dal):
    def __init__(self):
        self.conn = Conn()
        Crud_Dal.__init__(self, tableName="promotions", conn=self.conn)
    def listDataWithCond(self, select="*", cond=None, key_order_by=None, limit=None):
        return super().listDataWithCond(fields=select, where=cond, order_by=key_order_by, limit=limit)
    def listDataWithCond1(self, select="*", cond=None, key_order_by=None, limit=None, like=None):
        return super().listDataWithCond1(fields=select, where=cond, order_by=key_order_by, limit=limit, like=like)

    def findDataWithJson(self, conditions=None, key_order_by=None, limit=None):
        return super().findDataWithJson(conditions=conditions, order_by=key_order_by, limit=limit)

    def create(self, data):
        return super().insert(data)

    def update(self, data, cond):
        return super().update(update_data=data, where_data=cond)