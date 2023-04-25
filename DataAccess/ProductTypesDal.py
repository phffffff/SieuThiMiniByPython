from Connection.conn import Conn
from Common.CRUD import Crud_Dal
import logging
import mysql.connector.errors
class ProductTypesDal(Crud_Dal):
    def __init__(self):
        self.conn = Conn()
        Crud_Dal.__init__(self, tableName="product_types", conn=self.conn)


    # def list(self,):

    def findDataWithCond(self, select="*", cond=None, key_order_by=None, limit=None):
        return super().findDataWithCond(fields=select, where=cond, order_by=key_order_by, limit=limit)

    def findDataWithJson(self, conditions=None, key_order_by=None, limit=None):
        return super().findDataWithJson(conditions=conditions, order_by=key_order_by, limit=limit)

    def listDataWithCond1(self, select="*", cond=None, key_order_by=None, limit=None, like=None):
        return super().listDataWithCond1(fields=select, where=cond, order_by=key_order_by, limit=limit, like=like)

    def create(self, data):
        return super().insert(data)

    def update(self, data, cond):
        return super().update(update_data=data, where_data=cond)
    def delete(self,data,cond):
        return super().update(update_data=data,where_data=cond)

    def get_all(self):
        try:
            query = "SELECT * FROM product_types"
            result = self.conn.execute_all(query)
            self.conn.commit()
            product_types = []
            for row in result:
                loaisanpham = product_types(row[0], row[1], row[2])
                product_types.append(loaisanpham)
                self.conn.close()
            return product_types
        except mysql.connector.Error as e:
            logging.error("Error: {}".format(e))
            self.conn.rollback()
            return -1

    def add(self, producttypes):
        try:
            sql = "INSERT INTO product_types (id, name, is_active)" \
                  " VALUES (%d, %s, %d)"
            val = (producttypes.id, producttypes.name, producttypes.is_active)
            result = self.conn.execute(sql,val)
            self.conn.commit()
            self.conn.close()
            return result #số bản ghi bị ảnh hưởng (thường thì >= 0)
        except mysql.connector.Error as e:
            logging.error("Error: {}".format(e))
            self.conn.rollback()
            return -1

    # def update(self, account):
    #     try:
    #         sql = "UPDATE accounts SET username = %s, password = %s, role_id = %d, status = %d, is_active = %d" \
    #               " WHERE id = %d"
    #         val = (account.username, account.password, account.roleId, account.status, account.isActive, account.id)
    #         result = self.conn.execute(sql, val)
    #         self.conn.commit()
    #         self.conn.close()
    #         return result
    #     except mysql.connector.Error as e:
    #         logging.error("Error: {}".format(e))
    #         self.conn.rollback()
    #         return -1
    #
    # # delete để cho dui chứu hông sài nha, Khi xóa thì sài update cập nhật lại is_active
    # def delete(self, id):
    #     try:
    #         sql = "DELETE FROM accounts WHERE id = %d"
    #         val = (id,)
    #         result = self.conn.execute(sql, val)
    #         self.conn.commit()
    #         self.conn.close()
    #         return result
    #     except mysql.connector.Error as e:
    #         logging.error("Error: {}".format(e))
    #         self.conn.rollback()
    #         return -1
    # def findDataWithCond(self, ojb):
    #     try:
    #         sql = "SELECT * FROM accounts WHERE " {}\
    #               "is_active = 1 AND username = %s AND password = %s"
    #         val = (account.username, account.password)
    #         result = self.conn.execute_one(sql,val)
    #         self.conn.commit()
    #         self.conn.close()
    #         if result:
    #             return result
    #         return None
    #     except mysql.connector.Error as e:
    #         logging.error("Error: {}".format(e))
    #         self.conn.rollback()
    #         return None
