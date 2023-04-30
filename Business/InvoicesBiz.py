from DataAccess.InvoicesDal  import InvoicessDal


class InvoicesBiz:
    def __init__(self):
        self.dal = InvoicessDal()

    def get_all_invoices(self, cond=None, fields="*"):
        result = self.dal.listDataWithJson(where=cond, fields=fields, order_by="id DESC")
        if result:
            return result
        return []
    
    def add_invoices(self, data):
        result = self.dal.insert(data=data)
        if result == -1:
            return -1
        return result
        
    def update_invoices(self, data, cond):
        result = self.dal.update(update_data=data, where_data=cond)
        if result == -1:
            return -1
        return result

    def delete_invoices(self, id):
        result = self.dal.update(update_data={"is_active":0}, where_data={"id":id})
        if result == -1:
            return -1
        return result
    
    def find_invoices_with_cond(self, key, value):
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
        return "IV01"

    def to_str_id(self, id):
        return "IV0{}".format(id) if id < 10 else "IV{}".format(id)

    def get_A_from_B(self, A, nameB, valueB):
        result = self.dal.findDataWithJson(fields=A, where={"{}".format(nameB):valueB}, limit=1)
        
        return result[0]
            

