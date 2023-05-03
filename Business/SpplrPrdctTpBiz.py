

from DataAccess.SpplrPrdctTpDal import SpplrPrdctTpDal


class SpplrPrdctTpBiz:
    def __init__(self):
        self.dal = SpplrPrdctTpDal()

    def get_all_spplrPrdctTp(self, cond=None):
        result = self.dal.listDataWithJson(where=cond, order_by="supplier_id ASC")
        if result:
            return result
        return []

    def find_spplrPrdctTp_with_cond(self, key, value):
        # mặc định nó sẽ tìm 1 row vì t để fetch_one, còn key
        result = self.dal.findDataWithJson(where={"{}".format(key): value})
        if result:
            return result
        return []

    def add_spplrPrdctTp(self, data):
        result = self.dal.insert(data)
        if result == -1:
            return -1
        return result

    def update_spplrPrdctTp(self, data, cond):
        result = self.dal.update(update_data=data, where_data=cond)
        if result == -1:
            return -1
        return result

    def delete_spplrPrdctTp(self, id_supplier, id_prdctTp):
        result = self.dal.update(update_data={"is_active": 0}, where_data={"supplier_id": id_supplier, "product_type_id":id_prdctTp})
        if result == -1:
            return -1
        return result
