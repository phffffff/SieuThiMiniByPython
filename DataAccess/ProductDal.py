from Connection.conn import Conn
from Common.CRUD import Crud_Dal
# import mysql.connector.errors
# import logging


class ProductDal(Crud_Dal):
    def __init__(self):
        self.conn = Conn()
        Crud_Dal.__init__(self, tableName="products", conn=self.conn)

    def find_data_with_cond(self, select="*", cond=None, key_order_by=None, limit=None):
        return super().findDataWithJson(fields=select, where=cond, order_by=key_order_by, limit=limit)

    def list_data_with_cond(self, select="*", cond=None, key_order_by=None, limit=None):
        return super().listDataWithJson(fields=select, where=cond, order_by=key_order_by, limit=limit)

    def create_data(self, data):
        return super().insert(data)

    def update_data(self, data, cond):
        return super().update(update_data=data, where_data=cond)

    def delete_data(self,data,cond):
        return super().update(update_data=data,where_data=cond)

    # def get_all(self):
    #     try:
    #         query = "SELECT * FROM products"
    #         result = self.conn.execute_all(query)
    #         self.conn.commit()
    #         products = []
    #         for row in result:
    #             sanpham = products(row[0], row[1], row[2], row[3], row[4], row[5],row[6])
    #             products.append(sanpham)
    #             self.conn.close()
    #         return products
    #     except mysql.connector.Error as e:
    #         logging.error("Error: {}".format(e))
    #         self.conn.rollback()
    #         return -1

    # def add(self, product):
    #     try:
    #         sql = "INSERT INTO accounts (id, name, count, price, discount,product_type_id, is_active)" \
    #               " VALUES (%d, %s, %s, %d, %d, %d, %d)"
    #         val = (product.id, product.name, product.count, product.price, product.discount,product.product_type_id, product.ís_active)
    #         result = self.conn.execute(sql,val)
    #         self.conn.commit()
    #         self.conn.close()
    #         return result #số bản ghi bị ảnh hưởng (thường thì >= 0)
    #     except mysql.connector.Error as e:
    #         logging.error("Error: {}".format(e))
    #         self.conn.rollback()
    #         return -1

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
