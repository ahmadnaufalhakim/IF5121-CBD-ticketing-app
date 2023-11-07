from datetime import date
from src.film import Film
from src.schedule import Schedule, ScheduleBoard
from src.studio import Studio
from src.item import FnB
from src.booking import Booking
from src.payment import Payment, BookingPayment, MembershipPayment
from src.payment_service import *
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

        self.ongoing_payment = {}
        self.payment_history = {}

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
            print("2. Lihat pembelian yang sedang berlangsung")
            print("3. Lihat riwayat pembelian")
            print("4. Logout")
            c = input("Masukan pilihan Anda: ")

            if c == "1":
                valid = True
                self.schedule_screen()
            elif c == "2":
                valid = True
                self.ongoing_payment_screen()
            elif c == "3":
                valid = True
                self.payment_history_screen()
            elif c == "4":
                valid = True
                self.active_account = None
                self.login_screen()
            else:
                print("Masukan tidak valid.")
    
    def schedule_screen(self):
        valid = False
        while not valid:
            print("Silahkan pilih jadwal untuk melakukan booking:")
            for i, s in enumerate(self.schedules.get_schedules()) :
                print(f'[{i+1}] {s.get_date_start()} s.d. {s.get_date_end()}, pukul {s.get_time()}\n{s}\n')
            print("99. Kembali ke menu utama")
            c = input("Masukan pilihan Anda: ")

            if not c.isnumeric() :
                print("Masukan tidak valid.")
            elif int(c) != 99 and (int(c) <= 0 or int(c) > len(self.schedules.get_schedules())) :
                print("Masukan tidak valid.")
            elif c == "99" :
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
            tickets = []
            fnbs = []

            valid_date = False
            date = input(f"Silahkan pilih tanggal antara {schedule.get_date_start()} s.d. {schedule.get_date_end()} (format %Y-%m-%D): ")
            while not valid_date :
                try :
                    schedule.show_seats(date)
                    valid_date = True
                except KeyError as e :
                    date = input(f"Tanggal tidak tersedia.\nTolong masukkan pilihan tanggal yang valid antara {schedule.get_date_start()} s.d. {schedule.get_date_end()} (format %Y-%m-%D): ")
            chosen_seats = input("Silahkan pilih seats (pisahkan dengan koma bila lebih dari satu): ").replace(' ', '').split(",")
            for seat in convert_seat_to_index(chosen_seats) :
                tickets.append(schedule.take_seat(date, seat[0], seat[1]))

            print("FnB Menu:")              
            for i, s in enumerate(self.fnbs) :
                print(f'[{i+1}] {s}\n')

            print("Silakan pilih FnB yang ingin dipesan (pisahkan dengan koma jika memesan lebih dari satu)")
            print("Tekan <enter> jika tidak ingin memesan FnB apapun")
            chosen_fnb_str = input("Masukkan pilihan Anda: ")
            if chosen_fnb_str :
                chosen_fnb_idx = [int(f) for f in chosen_fnb_str.replace(' ', '').split(",")]
                for f in chosen_fnb_idx:
                    fnbs.append(self.fnbs[f-1])

            self.booking.set_fnbs(fnbs)
            self.booking.set_tickets(tickets)
            self.booking.checkout()
            print(f"Booking success with reference number: {self.booking.get_booking_number()}")
            valid = True
        self.select_payment_service_screen(self.booking)

    def select_payment_service_screen(self, booking: Booking) :
        valid = False
        while not valid :
            print(f"Silakan pilih salah satu metode pembayaran di bawah ini untuk kode booking {booking.get_booking_number()}:")
            print("1. QRIS")
            print("2. Credit Card (Mastercard)")
            print("3. Credit Card (VISA)")
            print("4. Bank Transfer (BCA)")
            print("5. Bank Transfer (BNI)")
            print("6. Bank Transfer (BRI)")
            print("7. E-Wallet (GoPay)")
            print("8. E-Wallet (OVO)")
            payment_service_option = input("Masukkan pilihan Anda: ")
            if payment_service_option == '1' :
                valid = True
                payment_method = QRIS(booking.get_booking_number())
            elif payment_service_option == '2' :
                valid = True
                payment_method = CreditCardMastercard(booking.get_booking_number())
            elif payment_service_option == '3' :
                valid = True
                payment_method = CreditCardVISA(booking.get_booking_number())
            elif payment_service_option == '4' :
                valid = True
                payment_method = BankTransferBCA(booking.get_booking_number())
            elif payment_service_option == '5' :
                valid = True
                payment_method = BankTransferBNI(booking.get_booking_number())
            elif payment_service_option == '6' :
                valid = True
                payment_method = BankTransferBRI(booking.get_booking_number())
            elif payment_service_option == '7' :
                valid = True
                payment_method = EWalletGoPay(booking.get_booking_number())
            elif payment_service_option == '8' :
                valid = True
                payment_method = EWalletOVO(booking.get_booking_number())
            else :
                print("Masukan tidak valid.")
        self.booking_payment = BookingPayment(
            booking.get_booking_number(),
            booking.get_total_price(),
            payment_method,
            booking
        )

        if self.active_account.email not in self.ongoing_payment:
            self.ongoing_payment[self.active_account.email] = []
        self.ongoing_payment[self.active_account.email].append(self.booking_payment)
        self.main_screen()

    def ongoing_payment_screen(self):
        if self.active_account.email not in self.ongoing_payment:
            print("\nAnda belum memiliki riwayat pembelian")
        else:
            print("\n#########################################")
            print("### Pembelian yang Sedang Berlangsung ###")
            print("#########################################")
            for i, s in enumerate(self.ongoing_payment[self.active_account.email]):
                print(f'[{i+1}] {s}')

            valid = False
            while not valid :
                print("Silahkan pilih pembelian yang ingin diproses")
                print("Atau masukkan 99 untuk kembali ke menu utama")
                c = input("Masukkan pilihan Anda: ")

                if not c.isnumeric() :
                    print("Masukan tidak valid.")
                elif int(c) != 99 and (int(c) <= 0 or int(c) > len(self.ongoing_payment[self.active_account.email])) :
                    print("Masukan tidak valid.")
                elif c == "99" :
                    valid = True
                    self.main_screen()
                else:
                    valid = True
                    self.process_payment(self.ongoing_payment[self.active_account.email][int(c)-1], int(c)-1)

    def process_payment(self, payment: Payment, ongoing_payment_idx) :
        valid = False
        while not valid :
            print(f"Silakan pilih aksi untuk pembelian dengan invoice number {payment.get_invoice_number()}:")
            print("1. Tambahkan promo")
            print("2. Hapus promo")
            print("3. Lakukan pembayaran")
            c = input("Masukkan pilihan Anda: ")
            if c == '1' :
                valid = True
                self.main_screen()
            elif c == '2' :
                valid = True
                self.main_screen()
            elif c == '3' :
                payment.pay()
                del self.ongoing_payment[self.active_account.email][ongoing_payment_idx]
                if self.active_account.email not in self.payment_history:
                    self.payment_history[self.active_account.email] = []
                self.payment_history[self.active_account.email].append(payment)
                valid = True
                self.main_screen()
            else :
                print("Masukan tidak valid.")

    def payment_history_screen(self):
        if self.active_account.email not in self.payment_history:
            print("\nAnda belum memiliki riwayat pembelian")
        else:
            print("\n#########################")
            print("### Riwayat Pembelian ###")
            print("#########################")
            for i, s in enumerate(self.payment_history[self.active_account.email]):
                print(f'[{i+1}] {s}\n')
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
                print("Masukan tidak valid.")