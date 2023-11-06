from item.ticket import Ticket
from film.film import Film
from studio.studio import Studio
from datetime import date, timedelta
class Schedule(object):
    def __init__(self, id: str, film: Film, studio: Studio, time: str, date_start: date, date_end: date):
        self.id = id
        self.film = film
        self.studio = studio
        self.time = time
        self.date_start = date_start
        self.date_end = date_end
        self.mat_seat = {}

        delta = timedelta(days=1)
        while date_start <= date_end:
            self.mat_seat[date_start.strftime("%Y-%m-%d")] = [[True for x in range (self.studio.num_cols)] for y in range (self.studio.num_rows)]
            date_start += delta

    def __str__(self) -> str:
        return f'{self.film.__str__()}'
    def get_id(self):
        return self.id
    def get_film(self):
        return self.film
    def get_studio(self):
        return self.studio
    def get_time(self):
        return self.time
    def get_date_start(self):
        return self.date_start
    def get_date_end(self):
        return self.date_end
    def set_film(self, film):
        self.film = film
    def set_studio(self, studio):
        self.studio = studio
    def set_time(self, time):
        self.time = time
    def set_date_start(self, date_start):
        self.date_start = date_start
    def set_date_end(self, date_end):
        self.date_end = date_end
    def get_available_seat(self):
        return self.mat_seat
    def take_seat(self, date, row, col) -> Ticket:
        if not self.mat_seat[date][row][col]:
            raise Exception("Seat is currently unavailable")
        self.mat_seat[row][col] = False
        return Ticket(self, date, row, col)

    def untake_seat(self, date, row, col):
        self.mat_seat[date][row][col] = True