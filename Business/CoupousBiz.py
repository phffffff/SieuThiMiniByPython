from builtins import bool

from DataAccess.CoupousDal import CoupouDal

class CoupousBiz:
    def __init__(self):
        self.dal = CoupouDal()

    def get_all(self):
        cond = 'is_active=1'
        result = self.dal.listDataWithCond(cond=cond)
        if result:
            return result
        return None
    def get_id(self,id):
        cond = 'id = {}'.format(id)
        result = self.dal.listDataWithCond(cond=cond)
        if result:
            return result
        return None
    def get_discount(self,name):
        cond = 'discount = {}'.format(name)
        result = self.dal.listDataWithCond(cond=cond)
        if result:
            return result
        return None
    def get_date_from(self,date):
        cond = 'date_from'
        like = '{}'.format(date)
        result = self.dal.listDataWithCond1(cond=cond, like=like)
        if result:
            return result
        return None
    def get_date_to(self,date):
        cond = 'date_to'
        like = '{}'.format(date)
        result = self.dal.listDataWithCond1(cond=cond, like=like)
        if result:
            return result
        return None

    def get_status(self,status):
        cond = 'status'
        like = '{}'.format(status)
        result = self.dal.listDataWithCond1(cond=cond,like=like)
        if result:
            return result
        return None



    def add(self, coupous):
        result = self.dal.create(coupous)
        if result == -1:
            return -1
        return result

    def update(self, coupous,cond):
        result = self.dal.update(coupous,cond)
        if result == -1:
            return -1
        return result
        # if result == -1:
        #     return về ErrorResponse cho giao diện bắt
        # return về SuccessResponse cho giao diện bắt

