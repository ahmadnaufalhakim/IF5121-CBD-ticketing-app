import sys
import os
path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.insert(0, path)

from src.film import Film
from src.studio import Studio
from src.schedule import ScheduleBoard, Schedule
from src.item import FnB, Ticket


film1 = Film("Film1",20000,"Synopsis1","Horror",120,"Poster1")
film2 = Film("Film2",20000,"Synopsis2","Horror",120,"Poster2")
studio1 = Studio("Studio1",10,12)
schedule1 = Schedule("id1",film1, studio1,"12:00","2","4")
schedule2 = Schedule("id2",film1, studio1,"11:00","2","4")
schedule3 = Schedule("id3",film2, studio1,"13:00","2","4")
schedules = ScheduleBoard()
schedules.add_schedule(schedule1)
schedules.add_schedule(schedule2)
schedules.add_schedule(schedule3)
print("Semua Jadwal")
schedules.get_schedule()
print("------------------------------------------------------ \n")
print("Jadwal berdasarkan Nama Film")
schedules.get_schedule_by_film("Film1")
print("------------------------------------------------------ \n")
makanan1 = FnB("Makanan 1", 10000, "PosterMakanan1", "Ini adalah makanan", True)
print(makanan1)
print("------------------------------------------------------ \n")
print("Test Tiketing")
print("Seat Sebelum")
before_seat = schedule1.get_available_seat()
print(before_seat)
tiket1 = Ticket(schedule1,"3",3,5)
print("Seat Sesudah")
after_seat = schedule1.get_available_seat()
print(after_seat)