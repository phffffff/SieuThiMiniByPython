from DataAccess.AccountDal import AccountDAL


class AccountBiz:
    def __init__(self):
        self.dal = AccountDAL()

    def get_all_account(self):
        result = self.dal.get_all()
        # if result == None:
        # return về ErrorResponse cho giao diện bắt
        return result

    def add_account(self, student):
        # kiểm tra tài khoản có tồn tại hay chưa
        # viết thêm phương thức findWithCond trong dal
        # if tồn tài:
        #     return về ErrorResponse cho giao diện bắt
        result = self.dal.add(student)
        # if result == -1:
        #     return về ErrorResponse cho giao diện bắt
        # return về SuccessResponse cho giao diện bắt

    def update_account(self, student):
        result = self.dal.update(student)
        # if result == -1:
        #     return về ErrorResponse cho giao diện bắt
        # return về SuccessResponse cho giao diện bắt

    def delete_account(self, id):
        result = self.dal.delete(id)
        # if result == -1:
        #     return về ErrorResponse cho giao diện bắt
        # return về SuccessResponse cho giao diện bắt

    def login(self, username, password):
         #cond = "is_active = 1 and username = '{}' and password = {}".format(username, password)
         #result = self.dal.findDataWithCond(cond=cond)
         result = self.dal.find_data_with_cond(conditions={"username": username, "password": password})
         if result:
            return result
         return None
