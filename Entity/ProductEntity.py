class ProductEntity:
    def __init__(self,id,name,count,price,discount,product_type_id,is_active):
        self._id=id
        self._name=name
        self._count=count
        self._price=price
        self._discount=discount
        self._product_type_id=product_type_id
        self._is_active=is_active    

    def get_id(self):
        return self._id
    def set_id(self, id):
        self._id = id

    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name

    def get_count(self):
        return self._count
    def set_count(self, count):
        self._count = count

    def get_price(self):
        return self._price
    def set_price(self, price):
        self._price = price

    def get_discount(self):
        return self._discount
    def set_discount(self, discount):
        self._discount = discount

    def get_product_type_id(self):
        return self._product_type_id
    def set_product_type_id(self, product_type_id):
        self._product_type_id = product_type_id

    def get_is_active(self):
        return self._is_active
    def set_is_active(self, is_active):
        self._is_active = is_active