

from DataAccess.MembershipsDal import MembershipsDal

class MembershipsBiz:
    def __init__(self):
        self.dal = MembershipsDal()

    def get_info_mem(self, cond=None, fields="*"):
        result = self.dal.listDataWithJson(where=cond,fields=fields,order_by="id ASC")
        if result:
            count_active = 0
            count_no_active  = 0
            for item in result:
                if item[7] == 1:
                    count_active += 1
                if item[7] == 0:
                    count_no_active += 1
            return {
                "hoatdong": count_active,
                "kohoatdong":count_no_active,
            }
        return 0

    def get_all_memberships(self, cond=None):
        result = self.dal.listDataWithJson(where=cond, order_by="id ASC")
        if result:
            return result
        return []

    def find_memberships_with_cond(self, key, value):
        # mặc định nó sẽ tìm 1 row vì t để fetch_one, còn key
        result = self.dal.findDataWithJson(where={"{}".format(key): value})
        if result:
            return result
        return None

    def add_memberships(self, memberships):
        result = self.dal.insert(memberships)
        if result == -1:
            return -1
        return result

    def update_memberships(self, memberships, cond):
        result = self.dal.update(update_data=memberships, where_data=cond)
        if result == -1:
            return -1
        return result

    def delete_memberships(self, id):
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
        return "MB01"

    def to_str_id(self, id):
        return "MB0{}".format(id) if id < 10 else "SP{}".format(id)

    def check_membership(self, id):
        result = self.dal.findDataWithJson(where={"is_active":1, "id": id})
        if result:
            return result
        return []

    def get_A_from_B(self, A, nameB, valueB):
        result = self.dal.findDataWithJson(fields=A, where={"{}".format(nameB):valueB}, limit=1)
        if result:
            return result[0]
        return "null"
    
    