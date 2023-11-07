from src.film.film import Film
from src.schedule import Schedule, ScheduleBoard
from src.studio import Studio
from src.item import FnB
from src.booking import Booking
from datetime import date
from src.account.Account import Account, User, DictDatabase
from getpass import getpass
import string

class UI:
    def __init__(self):
        self.init_data()
    
    def init_data(self):
        self.film1 = Film("The Marvels",20000, "Kekuatan Captain Marvel (Brie Larson) ternyata terhubung dengan Ms. Marvel (Iman Vellani) dan Monica Rambeau (Teyonah Parris). Hal ini membuat ketiganya terus menerus bertukar tempat. Mereka akhirnya bertemu dan mencari tahu kenapa kekuatan mereka saling terkoneksi. Dengan ancaman baru yang datang, ketiganya memutuskan menjadi satu tim untuk menyelamatkan alam semesta sebagai The Marvels.","Action, Adventure, Fantasy",120,"Poster The Marvels")
        self.film2 = Film("Petualangan Sherina 2",20000,"SHERINA (Sherina Munaf) dan SADAM (Derby Romero), dua teman kecil yang lama terpisah, bertemu kembali di Kalimantan untuk pelepasliaran orang utan. Reuni manis terhenti ketika anak orang utan bernama SAYU dicuri sekelompok orang.","Drama, Musikal",120,"Poster Sherina")
        self.studio1 = Studio("Studio 1",10,12)
        self.studio2 = Studio("Studio 2",10,12)
        self.schedule1 = Schedule("id1",self.film1, self.studio1,"12:00", date(2023,11,1), date(2023,12,31))
        self.schedule2 = Schedule("id2",self.film1, self.studio1,"19:00", date(2023,11,1), date(2023,12,31))
        self.schedule3 = Schedule("id3",self.film2, self.studio2,"10:00", date(2023,11,1), date(2023,12,31))
        self.schedule4 = Schedule("id4",self.film2, self.studio2,"15:00", date(2023,11,1), date(2023,12,31))

        self.schedules = ScheduleBoard()
        self.schedules.add_schedule(self.schedule1)
        self.schedules.add_schedule(self.schedule2)
        self.schedules.add_schedule(self.schedule3)
        self.schedules.add_schedule(self.schedule4)

        french_fries = FnB("French Fries", 10000, "Poster French Fries", "French fries ukuran L", 100)
        popcorn = FnB("Salt Popcorn ", 25000, "Poster Salt Popcorn", "French fries ukuran M", 100)
        thai_tea = FnB("Iced Thai Tea ", 25000, "Poster Thai Tea", "Es Thai Teas ukuran cup L", 100)

        self.fnbs = [french_fries, popcorn, thai_tea]

        self.booking_history = {}
    
    def init_session(self, user):
        self.active_account = user

    def login_screen(self):
        valid = False
        while not valid:
            email = input("Masukan email Anda: ")
            password = getpass("Masukan password Anda: ")

            user_account = User()
            user_account.database = DictDatabase()
            user_account.email = email
            user_account.password = password
            
            active_account = user_account.login()
            
            if not active_account:
                print("Password salah!")
            else:
                valid = True
                self.init_session(user_account)
                self.main_screen()
    
    def main_screen(self):
        valid = False
        while not valid:
            print("Silahkan pilih menu dibawah ini:")
            print("1. Lihat jadwal")
            print("2. Cek status pembayaran")
            print("3. Lihat riwayat pembelian")
            print("4. Logout")
            c = input("Masukan pilihan Anda: ")

            if c == "1":
                valid = True
                self.schedule_screen()
            elif c == "2":
                valid = True
                self.payment_status_screen()
            elif c == "3":
                valid = True
                self.booking_history_screen()
            elif c == "4":
                valid = True
                self.active_account = None
                self.login_screen()
            else:
                print("Pilihan tidak valid")
    
    def schedule_screen(self):
        valid = False
        while not valid:
            print("Silahkan pilih jadwal untuk melakukan booking:")
            i = 1
            for s in self.schedules.get_schedules():
                print(f'[{i}] {s}\n')
                i += 1
            print("99. Kembali ke menu utama")
            c = input("Masukan pilihan Anda: ")

            if not c.isnumeric() or (int(c) != 99 and int(c) > len(self.schedules.get_schedules())):
                print("Pilihan tidak valid")
            if c == "99":
                valid = True
                self.main_screen()
            else:
                valid = True
                self.booking_screen(self.schedules.get_schedules()[int(c)-1])
    
    def booking_screen(self, schedule: Schedule):
        self.booking = Booking(self.active_account, [], [])

        def convert_seat_to_index(chosen_seats):
            row_dict = {letter: index for index, letter in enumerate(string.ascii_uppercase)}
            matrix_indices = []
            for seat in chosen_seats:
                row_label, col_label = seat[0], int(seat[1:])  # Extracting row label and column number
                row_index = row_dict[row_label]  # Convert row label to numeric index
                col_index = col_label - 1  # Adjusting column to 0-based index
                matrix_indices.append((row_index, col_index))
            return matrix_indices

        valid = False
        while not valid:
            # try:
            tickets = []
            fnbs = []

            date = input("Silahkan pilih tanggal: ")
            schedule.show_seats(date)
            chosen_seats = input("Silahkan pilih seats (pisahkan dengan koma bila lebih dari satu): ").split(",")
            for seat in convert_seat_to_index(chosen_seats):
                tickets.append(schedule.take_seat(date, seat[0], seat[1]))

            print("FnB Menu:")
            i = 1                
            for s in self.fnbs:
                print(f'[{i}] {s}\n')
                i += 1
            chosen_fnb_idx = [int(f) for f in input("Silahkan pilih FnB (pisahkan dengan koma bila lebih dari satu):").split(",")]
            if chosen_fnb_idx:
                for f in chosen_fnb_idx:
                    fnbs.append(self.fnbs[f-1])
            
            self.booking.set_fnbs(fnbs)
            self.booking.set_tickets(tickets)

            self.booking.checkout("")
            # store to temp db
            if self.active_account.email not in self.booking_history:
                self.booking_history[self.active_account.email] = []
            self.booking_history[self.active_account.email].append(self.booking)

            print(f"Booking success with reference number: {self.booking.get_booking_number()}")
            

            valid = True
            self.main_screen()
            # except Exception as e:

            #     print(e)


    def booking_history_screen(self):
        if self.active_account.email not in self.booking_history:
            print("Anda belum memiliki riwayat pembelian")
        else:
            for h in self.booking_history[self.active_account.email]:
                print(h)
        input("Tekan <enter> untuk kembali ke menu utama")
        self.main_screen()

    def start(self):
        print("Selamat datang di Bioskop Gadjah 21!")
        live = True
        while live:
            print("Silahkan pilih menu dibawah ini:")
            print("1. Login")
            print("2. Keluar aplikasi")
            c = input("Masukan pilihan Anda: ")

            if c == "1":
                self.login_screen()
            elif c == "2":
                print("Bye..")
                live = False
            else:
                print("Masukan tidak valid")