class InvoiceDetail:
    def __init__(self, invoice_id, product_id, product_name, count, price, total, is_active):
        self.invoice_id = invoice_id
        self.product_id = product_id
        self.product_name=product_name
        self.count=count
        self.price=price
        self.total=total
        self.status=is_active