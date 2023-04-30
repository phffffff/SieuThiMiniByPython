from builtins import bool
import datetime

from DataAccess.CoupousDal import CoupouDal

class CoupousBiz:
    def __init__(self):
        self.dal = CoupouDal()

    def get_all_coupous(self, cond=None):
        result = self.dal.listDataWithJson(where=cond, order_by="id ASC")
        if result:
            return result
        return []

    def find_coupous_with_cond(self, key, value):
        # mặc định nó sẽ tìm 1 row vì t để fetch_one, còn key
        result = self.dal.findDataWithJson(where={"{}".format(key): value})
        if result:
            return result
        return None

    def add_coupous(self, coupous):
        result = self.dal.insert(coupous)
        if result == -1:
            return -1
        return result

    def update_coupous(self, coupous, cond):
        result = self.dal.update(update_data=coupous, where_data=cond)
        if result == -1:
            return -1
        return result

    def delete_coupous(self, id):
        result = self.dal.update(update_data={"is_active": 0}, where_data={"id": id})
        if result == -1:
            return -1
        return result

    def get_new_id(self):
        result = self.dal.findDataWithJson(fields=['id'], order_by="id DESC", limit=1)

        if result:
            currentId = result[0]
            temp = int(currentId + 1)
            return self.to_str_id(temp)
        return "CP01"

    def to_str_id(self, id):
        return "CP0{}".format(id) if id < 10 else "SP{}".format(id)
    
    def check_coupous(self, code):
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        result = self.dal.findDataWithCond(where="is_active = 1 AND coupou_code = '{}' AND (date_from <= '{}' AND '{}'  <= date_to)".format(code, now, now))
        if result:
            return result
        return []

