# import sys
# import os
# path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../.."))
# sys.path.insert(0, path)
# from src.item.item import Item

class Ticket():
    def __init__(self,schedule, date, seat_row, seat_col):
        self.schedule = schedule
        self.date = date
        self.seat_row = seat_row
        self.seat_col = seat_col
        self.schedule.take_seat(seat_row, seat_col)
    def get_schedule(self):
        return self.schedule
    def get_date(self):
        return self.date
    def set_schedule(self, schedule):
        self.schedule = schedule
    def set_date(self,date):
        self.date = date
