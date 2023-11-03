""" Contoh penggunaa module Account """

import os
from Account import * 
from getpass import getpass
from enum import Enum

""" Path ke parent/main.py"""
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))


""" Tipe - tipe akun """
class AccountType(Enum):
    USER = '1'
    ADMIN = '2'


user_selection = input("Masuk sebagai: ")

if user_selection == AccountType.USER.value:
    account = User()
    account.email = input("Masukkan email: ")
    account.password = getpass("Masukkan password: ")
    print("status login:", account.login())

elif user_selection == AccountType.ADMIN.value:
    account = Admin()
    account.email = input("Masukkan email: ")
    account.password = getpass("Masukkan password: ")
    print("status login:", account.login())

else:
    print("pilihan tidak ditemukan")
