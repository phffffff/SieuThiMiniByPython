from DataAccess.ProductDal import ProductDal


class ProductBiz:
    def __init__(self):
        self.dal = ProductDal()

    def get_all_product(self):
        cond = "is_active = 1"
        result = self.dal.findDataWithCond(cond=cond)
        if result :
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

    def get_count(self,count):
        cond = 'count = {}'.format(count)
        result = self.dal.listDataWithCond1(cond=cond)
        if result:
            return result
        return None

    def get_price(self,price):
        cond = 'price = {}'.format(price)
        result = self.dal.listDataWithCond1(cond=cond)
        if result:
            return result
        return None

    def get_discount(self,discount):
        cond = 'discount = {}'.format(discount)
        result = self.dal.findDataWithCond(cond=cond)
        if result:
            return result
        return None

    def get_product_type_id(self,product_type_id):
        cond = ' product_type_id = {}'.format(product_type_id)
        result = self.dal.findDataWithCond(cond=cond)
        if result:
            return result
        return None


    def add(self, products):
        result = self.dal.create(products)
        if result == -1:
            return -1
        return result

    def update_product(self, prodcuts,cond):
        result = self.dal.update(prodcuts,cond)

        if result == -1:
            return -1
        return  result

    def delete_product(self, data,cond):
        result = self.dal.delete(data,cond)
        if result == -1:
            return -1
        return  result



