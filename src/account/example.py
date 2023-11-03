""" Contoh penggunaa module Account """

import os
from Account import * 
from getpass import getpass
from enum import Enum

from Membership import Membership

""" Path ke parent/main.py"""
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))


""" Tipe - tipe akun """
class SelectionType(Enum):
    USER = '1'
    ADMIN = '2'
    USER_RESET_PASSWORD = '3'
    ADMIN_RESET_PASSWORD = '4'


user_selection = None
dictionary_database = DictDatabase()
user_account =  User()
admin_account = Admin()

user_account.database = dictionary_database
admin_account.database = dictionary_database

# Login

print("Opsi: ")
print("\t1. Masuk sebagai User\n\t2. Masuk sebagai admin\n\t3. Reset password user\n\t4. Reset password admin")
user_selection = input("Pilih opsi :")

if user_selection == SelectionType.USER.value:
    user_account.email = input("Masukkan email: ")
    user_account.password = getpass("Masukkan password: ")
    active_account = user_account.login()
    print("status login:", active_account)

elif user_selection == SelectionType.ADMIN.value:
    admin_account.email = input("Masukkan email: ")
    admin_account.password = getpass("Masukkan password: ")
    active_account = admin_account.login()
    print("status login:", active_account)

elif user_selection == SelectionType.USER_RESET_PASSWORD.value:
    email = input("Masukkan email: ")
    password = getpass("Masukkan password baru: ")
    status = user_account.reset_password(email, password)
    print(status)

elif user_selection == SelectionType.ADMIN_RESET_PASSWORD.value:
    email = input("Masukkan email: ")
    password = getpass("Masukkan password baru: ")
    status = admin_account.reset_password(email, password)
    print(status)

else:
    print("pilihan tidak ditemukan")



# Purchase a membership
member_1 = Membership()
member_1.user_info = active_account
member_1.create_membership_bill(12)