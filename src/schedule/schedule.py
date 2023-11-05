class Schedule(object):
    def __init__(self, id, film, studio, time, date_start, date_end):
        self.id = id
        self.film = film
        self.studio = studio
        self.time = time
        self.date_start = date_start
        self.date_end = date_end
        self.mat_seat = [[True for x in range (self.studio.num_cols)] for y in range (self.studio.num_rows)]
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
    def take_seat(self, row, col):
        if not self.mat_seat[row][col]:
            raise Exception("Seat is currently unavailable")
        self.mat_seat[row][col] = False

    def untake_seat(self, row, col):
        self.mat_seat[row][col] = True