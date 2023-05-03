from DataAccess.SuppliersDal import SuppliersDal


class SuppliersBiz:
    def __init__(self):
        self.dal = SuppliersDal()

    def get_info_spplr(self, cond=None, fields="*"):
        result = self.dal.listDataWithJson(where=cond,fields=fields,order_by="id ASC")
        if result:
            count_active = 0
            count_no_active  = 0
            for item in result:
                if item[3] == 1:
                    count_active += 1
                if item[3] == 0:
                    count_no_active += 1
            return {
                "hoatdong": count_active,
                "kohoatdong":count_no_active,
            }
        return 0

    def get_all_suppliers(self, cond=None, fields="*"):
        result = self.dal.listDataWithJson(where=cond, fields=fields, order_by="id DESC")
        if result:
            return result
        return []
    
    def add_supplier(self, data):
        result = self.dal.insert(data=data)
        if result == -1:
            return -1
        return result
        
    def update_supplier(self, data, cond):
        result = self.dal.update(update_data=data, where_data=cond)
        if result == -1:
            return -1
        return result

    def delete_supplier(self, id):
        result = self.dal.update(update_data={"is_active":0}, where_data={"id":id})
        if result == -1:
            return -1
        return result
    
    def find_supplier_with_cond(self, key, value):
        result = self.dal.findDataWithJson(where={"{}".format(key):value})
        if result:
            return result
        return []
    
    def get_new_id(self):
        result = self.dal.findDataWithJson(fields=['id'],order_by="id DESC", limit=1)

        if result:
            currentId = result[0]
            temp = int(currentId +1)
            return self.to_str_id(temp)
        return "SP01"

    def to_str_id(self, id):
        return "SP0{}".format(id) if id < 10 else "SP{}".format(id)

    def get_A_from_B(self, A, nameB, valueB):
        result = self.dal.findDataWithJson(fields=A, where={"{}".format(nameB):valueB}, limit=1)
        
        return result[0]
            

