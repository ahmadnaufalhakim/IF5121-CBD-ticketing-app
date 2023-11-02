import item

class FnB(object):
    def __init__(self, name, price, poster, detail_info, available_stock):
        item.__init__(self, name, price)
        self.poster = poster
        self.detail_info = detail_info
        self.available_stock = available_stock
    def get_poster(self):
        return self.poster
    def get_detail_info(self):
        return self.detail_info
    def get_available_stock(self):
        return self.available_stock
    def set_poster(self, poster):
        self.poster = poster
    def set_detail_info(self, detail_info):
        self.detail_info = detail_info
    def set_stock(self, available_stock):
        self.available_stock = available_stock
    