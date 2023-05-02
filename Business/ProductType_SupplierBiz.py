from DataAccess.ProductType_SupplierDal  import ProductTypeSupplierDal


class ProductTypeSupplierBiz:
    def __init__(self):
        self.dal = ProductTypeSupplierDal()

    def get_all_product_type_supplier(self, cond=None, fields="*"):
        result = self.dal.listDataWithJson(where=cond, fields=fields)
        if result:
            return result
        return []
    
    def add_product_type_supplier(self, data):
        result = self.dal.insert(data=data)
        if result == -1:
            return -1
        return result
        
    def update_product_type_supplier(self, data, cond):
        result = self.dal.update(update_data=data, where_data=cond)
        if result == -1:
            return -1
        return result

    def delete_product_type_supplier(self, id):
        result = self.dal.update(update_data={"is_active":0}, where_data={"id":id})
        if result == -1:
            return -1
        return result
    
    def find_product_type_supplier_with_cond(self, key, value):
        result = self.dal.findDataWithJson(where={"{}".format(key):value})
        if result:
            return result
        return []
    
    def get_A_from_B(self, A, nameB, valueB):
        result = self.dal.findDataWithJson(fields=A, where={"{}".format(nameB):valueB}, limit=1)
        
        return result[0]
            

