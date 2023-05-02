from DataAccess.PromotionDetailsDal import PromotionDetailsDal

class PromotionDetailsBiz:
    def __init__(self):
        self.dal = PromotionDetailsDal()

    def get_all_promotion_details(self, cond=None, fields="*"):
        result = self.dal.listDataWithJson(where=cond, fields=fields, order_by="promotion_id DESC")
        if result:
            return result
        return []


    def find_promotion_details_with_cond(self, key, value):
        # mặc định nó sẽ tìm 1 row vì t để fetch_one, còn key
        result = self.dal.findDataWithJson(where={"{}".format(key): value})
        if result:
            return result
        return None


    def add_promotion_details(self, promotions):
        result = self.dal.insert(promotions)
        if result == -1:
            return -1
        return result


    def update_promotion_detais(self, promotion, cond):
        result = self.dal.update(update_data=promotion, where_data=cond)
        if result == -1:
            return -1
        return result


    def delete_promotion(self, id , product_id):
        result = self.dal.update(update_data={"is_active": 0}, where_data={"promotion_id": id , "product_id": product_id})
        if result == -1:
            return -1
        return result


    def get_new_id(seft):
        result = seft.dal.findDataWithJson(fields=['id'], order_by="id DESC", limit=1)

        if result:
            currentId = result[0]
            temp = int(currentId + 1)
            return seft.to_str_id(temp)
        return "SP01"


    def to_str_id(seft, id):
        return "KM0{}".format(id) if id < 10 else "KM{}".format(id)
