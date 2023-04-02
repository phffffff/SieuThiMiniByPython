import logging

from Connection.conn import Conn
from Entity.AccountEntity import Account

class AccountDAL:
    def __init__(self):
        self.conn = Conn()
    def get_all(self):
        try:
            query = "SELECT * FROM accounts"
            result = self.conn.execute_query(query)
            accounts = []
            for row in result:
                taikhoan = Account(row[0], row[1], row[2], row[3], row[4], row[5])
                accounts.append(taikhoan)
                self.conn.close()
            return accounts
        except ValueError as e:
            logging.error(e)
            self.conn.close()
            return -1

    def add(self, account):
        try:
            sql = "INSERT INTO accounts (id, username, password, role_id, status, is_active)" \
                  " VALUES (%d, %s, %s, %d, %d, %d)"
            val = (account.id, account.username, account.password, account.roleId, account.status, account.isActive)
            result = self.conn.execute_query(sql,val)
            self.conn.close()
            return result #trả về none
        except ValueError as e:
            self.conn.close()
            logging.error(e)
            return -1

    def update(self, account):
        try:
            sql = "UPDATE accounts SET username = %s, password = %s, role_id = %d, status = %d, is_active = %d" \
                  " WHERE id = %d"
            val = (account.username, account.password, account.roleId, account.status, account.isActive, account.id)
            result = self.conn.execute_query(sql, val)
            self.conn.close()
            return result
        except ValueError as e:
            logging.error(e)
            self.conn.close()
            return -1
    def delete(self, id):
        try:
            sql = "DELETE FROM accounts WHERE id = %d"
            val = (id,)
            result = self.conn.execute_query(sql, val)
            self.conn.close()
            return result
        except ValueError as e:
            logging.error(e)
            self.conn.close()
            return -1
    def find(self, username, password):
        try:
            sql = "SELECT * FROM accounts WHERE username = %s AND password = %s AND is_active = 1"
            val = (username, password)
            result = self.conn.execute_query(sql,val)
            self.conn.close()
            if result:
                return result
            return None
        except ValueError as e:
            logging.error(e)
            self.conn.close()
            return None

