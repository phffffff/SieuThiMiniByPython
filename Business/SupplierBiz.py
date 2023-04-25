from DataAccess.SupplierDal import SupplierDal


class SupplierBiz:
    def __init__(self):
        self.dal = SupplierDal()

    def get_all_account(self):
        cond= "is_active = 1"
        result = self.dal.findDataWithCond(cond=cond)
        if result:
            return result
        return None
    def get_id(self,id):
        cond = 'id = {}'.format(id)
        result = self.dal.findDataWithCond(cond=cond)
        if result:
            return result
        return None

    def get_name(self,name):
        cond = 'name = {}'.format(name)
        result = self.dal.listDataWithCond1(cond=cond)
        if result:
            return result
        return None
    def get_addr(self,addr):
        cond = 'addr = {}'.format(addr)
        result = self.dal.findDataWithCond(cond=cond)
        if result:
           return result
        return None
    def add_supplier(self, supplier):
        result = self.dal.create(supplier)
        if result == -1:
            return -1
        return None

    def update_supplier(self, supplier):
        result = self.dal.update(supplier)
        if result == -1:
            return -1
        return result

    def delete_supplier(self, id):
        result = self.dal.delete(id)
        if result == -1:
            return -1
        return result


