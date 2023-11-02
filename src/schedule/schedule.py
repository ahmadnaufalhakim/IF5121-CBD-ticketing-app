class Schedule(object):
    def __init__(self, film, studio, time, date_start, date_end):
        self.film = film
        self.studio = studio
        self.time = time
        self.date_start = date_start
        self.date_end = date_end
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