import mysql.connector.errors
import logging


class Crud_Dal:
    def __init__(self, tableName, conn):
        self.tableName = tableName
        self.conn = conn

    def findDataWithJson(self, fields='*', where=None, order_by=None, limit=None):
        try:
            query = f"SELECT {', '.join(fields) if isinstance(fields, list) else fields} FROM {self.tableName}"
            query = f"SELECT {', '.join(fields) if isinstance(fields, list) else fields} FROM {self.tableName}"

            if where:
                condition_string = " AND ".join([f"{key}=%s" for key in where.keys()])
            if where:
                condition_string = " AND ".join([f"{key}=%s" for key in where.keys()])
                query += f" WHERE {condition_string}"
            if order_by:
                query += f" ORDER BY {order_by}"

            if limit:
                query += f" LIMIT {limit}"

            params = tuple(where.values()) if where else None

            result = self.conn.execute_one(query, params)
            self.conn.commit()
            self.conn.close()
            if result:
                return result
            return None
        except mysql.connector.Error as e:
            logging.error("Error: {}".format(e))
            self.conn.rollback()
            return None

    # use:
    # intanceDal.findDataWithCond(fields=['id', 'role_id'], where='is_active = 1')
    # cond = "is_active = 1 and username = '{}' and password = {}".format(username, password)
    # result = intanceDal.findDataWithCond(cond=cond)
    def findDataWithCond(
            self,
            # table,
            fields='*',
            where=None,
            order_by=None,
            limit=None
    ):
        try:
            sql = f"SELECT {', '.join(fields) if isinstance(fields, list) else fields} FROM {self.tableName}"
            if where:
                sql += f" WHERE {where}"
                sql += f" WHERE {where}"
            if order_by:
                sql += f" ORDER BY {order_by}"
            if limit:
                sql += f" LIMIT {limit}"

            result = self.conn.execute_one(sql)
            result = self.conn.execute_one(sql)
            self.conn.commit()
            self.conn.close()
            if result:
                return result
            self.conn.close()
            if result:
                return result
            return None
        except mysql.connector.Error as e:
            logging.error("Error: {}".format(e))
            self.conn.rollback()
            return None

    # list với điều kiện
    def listDataWithCond(
            self,
            fields='*',
            where=None,
            order_by=None,
            limit=None
    ):
        try:
            sql = f"SELECT {', '.join(fields) if isinstance(fields, list) else fields} FROM {self.tableName}"
            if where:
                sql += f" WHERE {where}"
            if order_by:
                sql += f" ORDER BY {order_by}"
            if limit:
                sql += f" LIMIT {limit}"

            results = self.conn.execute_all(sql)
            self.conn.commit()
            self.conn.close()
            if results:
                return results
            return None
        except mysql.connector.Error as e:
            logging.error("Error: {}".format(e))
            self.conn.rollback()
            return None

    # vẫn là list với điều kiện (nhma điều kiện này dưới dạng json "key" - value)
    # thêm sự lựa chọn cho ai thích cond dạng key:value
    def listDataWithJson(
            self,
            fields='*',
            where=None,
            order_by=None,
            limit=None
    ):
        try:
            sql = f"SELECT {', '.join(fields) if isinstance(fields, list) else fields} FROM {self.tableName}"
            if where:
                condition_string = " AND ".join([f"{key}=%s" for key in where.keys()])
                sql += f" WHERE {condition_string}"
            if order_by:
                sql += f" ORDER BY {order_by}"
            if limit:
                sql += f" LIMIT {limit}"
            params = tuple(where.values()) if where else None

            results = self.conn.execute_all(sql, params)
            results = self.conn.execute_all(sql, params)
            self.conn.commit()
            self.conn.close()
            if results:
                return results
            self.conn.close()
            if results:
                return results
            return None
        except mysql.connector.Error as e:
            logging.error("Error: {}".format(e))
            self.conn.rollback()
            return None

    def insert(
            self,
            data
    ):
        try:
            placeholders = ', '.join(['%s'] * len(data))
            columns = ', '.join(data.keys())
            values = tuple(data.values())
            sql = f"INSERT INTO {self.tableName} ({columns}) VALUES ({placeholders})"
            result = self.conn.execute(sql, values)
            self.conn.commit()
            self.conn.close()
            return result
        except mysql.connector.Error as e:
            logging.error("Error: {}".format(e))
            self.conn.rollback()
            return -1

    """
    use:    
    use:    
        update_data = {"name": "John", "age": 30}
        where_data = {"id": 1}
        instanceDal.update("tên bảng", update_data, where_data)
    """

    def update(
            self,
            update_data,
            where_data
    ):
        try:
            set_clause = ", ".join([f"{col}=%s" for col in update_data])
            where_clause = " AND ".join([f"{col}=%s" for col in where_data])
            sql = f"UPDATE {self.tableName} SET {set_clause} WHERE {where_clause}"
            values = list(update_data.values()) + list(where_data.values())
            result = self.conn.execute(sql, values)
            self.conn.commit()
            self.conn.close()
            return result
        except mysql.connector.Error as e:
            logging.error("Error: {}".format(e))
            self.conn.rollback()
            return -1