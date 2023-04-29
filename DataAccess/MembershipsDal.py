import logging
import mysql
from Connection.conn import Conn
from Common.CRUD import Crud_Dal

class MembershipsDal(Crud_Dal):
    def __init__(self):
        self.conn = Conn()
        Crud_Dal.__init__(self, tableName="memberships", conn=self.conn)