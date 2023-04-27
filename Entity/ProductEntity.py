class ProductEntity:
    def __init__(self,id,name,count,price,discount,remain,product_type_id,is_active):
        self.id=id
        self.name=name
        self.count=count
        self.price=price
        self.discount=discount
        self.remain=remain
        self.product_type_id=product_type_id
        self.status=is_active    
