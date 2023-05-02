from Connection.conn import Conn
from Common.CRUD import Crud_Dal

class PurchaseOrdersDal(Crud_Dal):
    def __init__(self):
        self.conn = Conn()
        Crud_Dal.__init__(self, tableName="purchase_orders", conn=self.conn)