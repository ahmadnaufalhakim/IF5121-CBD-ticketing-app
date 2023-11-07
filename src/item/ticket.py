# import sys
# import os
# path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../.."))
# sys.path.insert(0, path)
from src.item.item import Item

class Ticket(Item):
    def __init__(self, schedule, date, seat_row, seat_col):
        self.schedule = schedule
        self.date = date
        self.seat_row = seat_row
        self.seat_col = seat_col
        self.set_price(schedule.get_film().get_price())

    def get_schedule(self):
        return self.schedule
    def get_date(self):
        return self.date
    def set_schedule(self, schedule):
        self.schedule = schedule
    def set_date(self,date):
        self.date = date
    def cancel(self):
        self.schedule.untake_seat(self.seat_row, self.seat_col)
    def book(self):
        self.status = "booked"
    def buy(self):
        self.status = "bought"
    def invalidate(self):
        if self.status != "bought":
            raise Exception("Only bought ticket can be invalidated")
        self.set_status("invalidated")