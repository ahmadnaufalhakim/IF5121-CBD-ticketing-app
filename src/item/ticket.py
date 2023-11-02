from item import Item

class Ticket(Item):
    def __init__(self, name, price, schedule, date, seat):
        Item.__init__(self,name, price)
        self.schedule = schedule
        self.date = date
        self.seat = seat
    def get_schedule(self):
        return self.schedule
    def get_date(self):
        return self.date
    def get_seat(self):
        return self.seat
    def set_schedule(self, schedule):
        self.schedule = schedule
    def set_date(self,date):
        self.date = date
    def set_seat(self, seat):
        self.seat = seat