import sys
import os
path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../.."))
sys.path.insert(0, path)

from src.item import Item
class Film(Item):
    def __init__(self,name, price, synopsis, genre, duration, poster):
        Item.__init__(self, name, price)
        self.synopsis = synopsis
        self.genre = genre
        self.duration = duration
        self.poster = poster
    def __str__(self) -> str:
        return f"Film : {self.name}\nHarga: {self.price}\nGenre : {self.genre}\nDurasi: {self.duration} menit\nSinopsis: {self.synopsis}"
    def get_synopsis(self):
        return self.synopsis
    def get_genre(self):
        return self.genre
    def get_duration(self):
        return self.duration
    def get_poster(self):
        return self.poster
    def set_synopsis(self, synopsis):
        self.synopsis = synopsis
    def set_genre(self, genre):
        self.genre = genre
    def set_duration(self, duration):
        self.duration = duration
    def set_poster(self, poster):
        self.poster = poster