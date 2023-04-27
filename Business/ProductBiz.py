from DataAccess.ProductDal import ProductDal


class ProductBiz:
    def __init__(self):
        self.dal = ProductDal()

    def get_all_product(self, cond=None, fields="*"):
        result = self.dal.listDataWithJson(where=cond, fields=fields, order_by="id DESC")
        if result :
           return result
        return []
        
    def find_product_with_cond(self, key, value):
        # mặc định nó sẽ tìm 1 row vì t để fetch_one, còn key
        result = self.dal.findDataWithJson(where={"{}".format(key):value})
        if result:
            return result
        return None

    def add_product(self, products):
        result = self.dal.insert(products)
        if result == -1:
            return -1
        return result

    def update_product(self, product,cond):
        result = self.dal.update(update_data=product, where_data=cond)
        if result == -1:
            return -1
        return  result

    def delete_product(self, id):
        result = self.dal.update(update_data={"is_active":0},where_data={"id":id})
        if result == -1:
            return -1
        return result

    def get_new_id(seft):
        result = seft.dal.findDataWithJson(fields=['id'],order_by="id DESC", limit=1)

        if result:
            currentId = result[0]
            temp = int(currentId +1)
            return seft.to_str_id(temp)
        return "SP01"

    def to_str_id(seft, id):
        return "SP0{}".format(id) if id < 10 else "SP{}".format(id)



