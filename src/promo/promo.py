from promo.interfaces import IPromo

class Promo(IPromo) :
    # Class-level attribute to keep track all promos that are created
    promos = []

    def __init__(self, name:str, discount:float, max_discount:int, info:str='', min_purchase:int=0) :
        self.set_name(name)
        self.set_info(info)
        self.set_min_purchase(min_purchase)
        self.set_discount(discount)
        self.set_max_discount(max_discount)
        # Add created promo object to class-level promos attribute
        Promo.promos.append(self)

    # Getter(s)
    def get_name(self) :
        return self.name
    def get_info(self) :
        return self.info
    def get_min_purchase(self) :
        return self.min_purchase
    def get_discount(self) :
        return self.discount
    def get_max_discount(self) :
        return self.max_discount
    # Setter(s)
    def set_name(self, name) :
        self.name = name
    def set_info(self, info) :
        self.info = info
    def set_min_purchase(self, min_purchase) :
        self.min_purchase = min_purchase
    def set_discount(self, discount) :
        self.discount = discount
    def set_max_discount(self, max_discount) :
        self.max_discount = max_discount

    def delete_promo(self) :
        if self in Promo.promos :
            Promo.promos.remove(self)
        del self
    def is_valid(self, amount) :
        return amount >= self.min_purchase