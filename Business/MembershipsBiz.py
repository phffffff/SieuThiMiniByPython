from builtins import bool

from DataAccess.MembershipsDal import MembershipsDal

class MembershipsBiz:
    def __init__(self):
        self.dal = MembershipsDal()

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
    def get_name(self,name):
        cond = 'name'
        like = '{}'.format(name)
        result = self.dal.listDataWithCond1(cond=cond,like=like)
        if result:
            return result
        return None
    def get_bir(self,birthday):
        cond = 'birthday'
        like = '{}'.format(birthday)
        result = self.dal.listDataWithCond1(cond=cond, like=like)
        if result:
            return result
        return None
    def get_phone(self,phone):
        cond = 'phone'
        like = '{}'.format(phone)
        result = self.dal.listDataWithCond1(cond=cond, like=like)
        if result:
            return result
        return None
    def get_point(self,point):
        cond = 'point = {}'.format(point)
        result = self.dal.listDataWithCond(cond=cond)
        if result:
            return result
        return None
    def get_mail(self,mail):
        cond = 'mail AND is_active'
        like = '{}'.format(mail)
        result = self.dal.listDataWithCond(cond=cond, like=like)
        if result:
            return result
        return None


    def add(self, member):
        result = self.dal.create(member)
        if result == -1:
            return -1
        return result

    def update(self, member,cond):
        result = self.dal.update(member,cond)
        if result == -1:
            return -1
        return result
        # if result == -1:
        #     return về ErrorResponse cho giao diện bắt
        # return về SuccessResponse cho giao diện bắt

