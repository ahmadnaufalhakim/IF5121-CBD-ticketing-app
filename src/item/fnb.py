import sys
import os
path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../.."))
sys.path.insert(0, path)
from src.item.item import Item

class FnB(Item):
    def __init__(self, name, price, poster, detail_info, available_stock, is_available=True):
        Item.__init__(self,name, price)
        self.poster = poster
        self.detail_info = detail_info
        self.is_available = is_available
        self.available_stock = available_stock
    def __str__(self):
        return f'Nama Makanan / Minuman : {self.name}\nDetail Info : {self.detail_info}\nKetersediaan : {self.available_stock}'
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
    def set_available(self, is_available):
        self.is_available= is_available