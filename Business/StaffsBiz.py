

from DataAccess.StaffsDal import StaffsDal


class StaffsBiz:
    def __init__(self):
        self.dal = StaffsDal()

    def get_info_staff(self, cond=None, fields="*"):
        result = self.dal.listDataWithJson(where=cond,fields=fields,order_by="id ASC")
        if result:
            count_active = 0
            count_no_active  = 0
            for item in result:
                if item[6] == 1:
                    count_active += 1
                if item[6] == 0:
                    count_no_active += 1
            return {
                "hoatdong": count_active,
                "kohoatdong":count_no_active,
            }
        return 0

    def get_all_staffs(self, cond=None):
        result = self.dal.listDataWithJson(where=cond, order_by="id ASC")
        if result:
            return result
        return []

    def find_staffs_with_cond(self, key, value):
        # mặc định nó sẽ tìm 1 row vì t để fetch_one, còn key
        result = self.dal.findDataWithJson(where={"{}".format(key): value})
        if result:
            return result
        return []

    def add_staffs(self, staffs):
        result = self.dal.insert(staffs)
        if result == -1:
            return -1
        return result

    def update_staffs(self, staffs, cond):
        result = self.dal.update(update_data=staffs, where_data=cond)
        if result == -1:
            return -1
        return result

    def delete_staffs(self, id):
        result = self.dal.update(update_data={"is_active": 0}, where_data={"id": id})
        if result == -1:
            return -1
        return result

    def get_new_id(seft):
        result = seft.dal.findDataWithJson(fields=['id'], order_by="id DESC", limit=1)

        if result:
            currentId = result[0]
            temp = int(currentId + 1)
            return seft.to_str_id(temp)
        return "MB01"

    def to_str_id(seft, id):
        return "MB0{}".format(id) if id < 10 else "SP{}".format(id)
