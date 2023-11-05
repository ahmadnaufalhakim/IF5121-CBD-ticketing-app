from promo.interfaces import IPromo

class Promo(IPromo):
    def __init__(self, name, info, min_purchase, max_discount, discount):
        self.set_name(name)
        self.set_info(info)
        self.set_min_purchase(min_purchase)
        self.set_max_discount(max_discount)
        self.set_discount(discount)
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_info(self):
        return self.info
    
    def set_info(self, info):
        self.info = info
    
    def get_min_purchase(self):
        return self.min_purchase
    
    def set_min_purchase(self, min_purchase):
        self.min_purchase = min_purchase
    
    def get_max_discount(self):
        return self.max_discount
    
    def set_max_discount(self, max_discount):
        self.max_discount = max_discount
    
    def get_discount(self):
        return self.discount
    
    def set_discount(self, discount):
        self.discount = discount
    
    def is_valid(self, amount):
        if amount < self.min_purchase:
            return False
        return True