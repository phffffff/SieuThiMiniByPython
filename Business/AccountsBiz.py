

from DataAccess.AccountsDal import AccountsDal


class AccountsBiz:
    def __init__(self):
        self.dal = AccountsDal()

    def get_info_account(self, cond=None, fields="*"):
        result = self.dal.listDataWithJson(where=cond,fields=fields,order_by="id ASC")
        if result:
            count_active = 0
            count_duoc_cap = 0
            count_no_active  = 0
            for item in result:
                if item[5] == 1:
                    count_active += 1
                if item[5] == 0:
                    count_no_active += 1
                if item[4] == 1:
                    count_duoc_cap += 1
            return {
                "cap": count_duoc_cap,
                "hoatdong": count_active,
                "kohoatdong":count_no_active,
            }
        return 0


    def get_all_accounts(self, cond=None,fields="*"):
        result = self.dal.listDataWithJson(where=cond,fields=fields, order_by="id ASC")
        if result:
            return result
        return []

    def find_accounts_with_cond(self, key, value):
        # mặc định nó sẽ tìm 1 row vì t để fetch_one, còn key
        result = self.dal.findDataWithJson(where={"{}".format(key): value})
        if result:
            return result
        return None

    def add_accounts(self, accounts):
        result = self.dal.insert(accounts)
        if result == -1:
            return -1
        return result

    def update_accounts(self, accounts, cond):
        result = self.dal.update(update_data=accounts, where_data=cond)
        if result == -1:
            return -1
        return result

    def delete_accounts(self, id):
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
        return "AC01"

    def to_str_id(seft, id):
        return "AC0{}".format(id) if id < 10 else "AC{}".format(id)
    
    def login(seft, username, password):
        result = seft.dal.findDataWithJson(where={"username":username,"password":password, "is_active":1})
        if result:
            if result[4] == 1:
                return {
                    "flag":True,
                    "data": result
                }
            return {
                "flag":False,
                "data": "Tài khoản chưa được cấp"
            }
        return {
            "flag":False,
            "data": "Username or password invalid!"
        }
