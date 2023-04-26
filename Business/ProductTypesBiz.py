from DataAccess.ProductTypesDal  import ProductTypesDal


class ProductTypesBiz:
    def __init__(self):
        self.dal = ProductTypesDal()

    def get_all_prodcut_types(self, cond=None):
        result = self.dal.listDataWithJson(where=cond, order_by="id DESC")
        if result:
            return result
        return []
    
    def add_product_type(self, data):
        result = self.dal.insert(data=data)
        if result == -1:
            return -1
        return result
        
    def update_product_type(self, data, cond):
        result = self.dal.update(update_data=data, where_data=cond)
        if result == -1:
            return -1
        return result

    def delete_product_type(self, id):
        result = self.dal.update(update_data={"is_active":0}, where_data={"id":id})
        if result == -1:
            return -1
        return result
    
    def find_product_types_with_cond(self, cond, data):
        result = self.dal.findDataWithJson(where={"{}".format(cond):data})
        if result:
            return result
        return []
    
    def get_new_id(seft):
        result = seft.dal.findDataWithJson(fields=['id'],order_by="id DESC", limit=1)

        if result:
            currentId = result[0]
            temp = int(currentId +1)
            return seft.to_str_id(temp)
        return "LM01"

    def to_str_id(seft, id):
        return "LM0{}".format(id) if id < 10 else "LM{}".format(id)

