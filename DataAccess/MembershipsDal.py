import logging
import mysql
from SieuThiMiniByPython.Connection.conn import Conn
from SieuThiMiniByPython.Common.CRUD import Crud_Dal

class MembershipsDal(Crud_Dal):
    def __init__(self):
        self.conn = Conn()
        Crud_Dal.__init__(self, tableName="memberships", conn=self.conn)