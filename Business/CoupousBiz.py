from builtins import bool
import datetime

from DataAccess.CoupousDal import CoupouDal

class CoupousBiz:
    def __init__(self):
        self.dal = CoupouDal()

    def get_info_coupou(self, cond=None, fields="*"):
        result = self.dal.listDataWithJson(where=cond,fields=fields,order_by="id ASC")
        if result:
            count_active = 0
            count_no_active  = 0
            count_sudung = 0
            count_no_sudung  = 0
            for item in result:
                if item[6] == 1:
                    count_active += 1
                if item[6] == 0:
                    count_no_active += 1
                if item[5] == 1:
                    count_sudung += 1
                if item[5] == 0:
                    count_no_sudung += 1
            return {
                "hoatdong": count_active,
                "kohoatdong":count_no_active,
                "sudung": count_sudung,
                "chuasudung": count_no_sudung,
            }
        return 0

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
    def get_A_from_B(self, A, nameB, valueB):
        result = self.dal.findDataWithJson(fields=A, where={"{}".format(nameB):valueB}, limit=1)
        if result:
            return result[0]
        return "null"

