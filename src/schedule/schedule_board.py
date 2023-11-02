class ScheduleBoard(object):
    def __init__(self):
        self.schedules = []
    def add_schedule(self, schedule):
        self.schedules.append(schedule)
    def remove_schedule(self, id):
        for index, item in enumerate(self.schedules):
            if item.id == id:
                self.schedules.pop(index)
                break
    def get_schedule_by_film(self, nama_film):
        for item in self.schedules:
            if item.film.name == nama_film:
                print(item)
                print()
    def get_schedule(self):
        for item in self.schedules:
            print(item)
            print()