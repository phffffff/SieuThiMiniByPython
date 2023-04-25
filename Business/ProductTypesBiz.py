from DataAccess.ProductTypesDal  import ProductTypesDal


class ProductTypesBiz:
    def __init__(self):
        self.dal = ProductTypesDal()

    def get_all_prodcut_types(self):
        cond = 'is_active = 1'
        result = self.dal.findDataWithCond(cond=cond)
        if result:
            return result
        return None
    def get_id(self,id):
        cond = 'id ={}'.format(id)
        result = self.dal.findDataWithCond(cond=cond)
        if result:
            return result
        return None

    def get_name(self,name):
        cond = 'name ={}'.format(name)
        result = self.dal.listDataWithCond1(cond=cond)
        if result:
            return result
        return None
    def add_product_types(self, products_types):
        result = self.dal.create(products_types)
        if result == -1:
            return -1
        return result

    def update_product_types(self, prodcuts_types,cond):
        result = self.dal.update(prodcuts_types,cond)
        if result == -1:
            return -1
        return  result


    def delete_product_types(self, data,cond):
        result = self.dal.delete(data,cond)
        if result == -1:
            return -1
        return  result


