class InvoicesSearch:
    def __init__(self, id,staff_name,membership_name):
        self.id = id
        self.staff_name = staff_name
        self.membership_name=membership_name

class InvoicesValue:
    def __init__(self,total_price,discount,remain_price,point):
        self.total_price = total_price
        self.discount = discount
        self.remain_price=remain_price
        self.point=point