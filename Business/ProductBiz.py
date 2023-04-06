from DataAccess.ProductDal import ProductDal


class ProductBiz:
    def __init__(self):
        self.dal = ProductDal()

    def get_all_prodcut(self):
        # result = self.dal.get_all()
        pass
        # if result == None:
        # return về ErrorResponse cho giao diện bắt
        # return result

    def add_product(self, products):
        # kiểm tra tài khoản có tồn tại hay chưa
        # viết thêm phương thức findWithCond trong dal
        # if tồn tài:
        #     return về ErrorResponse cho giao diện bắt
        result = self.dal.add(products)
        # if result == -1:
        #     return về ErrorResponse cho giao diện bắt
        # return về SuccessResponse cho giao diện bắt

    def update_product(self, prodcuts,cond):
        result = self.dal.update(prodcuts,cond)

        if result == -1:
            return -1
        return  result
        # if result == -1:
        #     return về ErrorResponse cho giao diện bắt
        # return về SuccessResponse cho giao diện bắt

    def delete_product(self, data,cond):
        result = self.dal.delete(data,cond)
        # return result




        if result == -1:
            return -1
        return  result
        # về SuccessResponse cho giao diện bắt


