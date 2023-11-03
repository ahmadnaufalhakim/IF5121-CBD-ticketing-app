from Account import * 

user_selection = input("Masuk sebagai: ")

if user_selection == '1':
    account = User()
    account.email = input("Masukkan email: ")
    account.password = input("Masukkan password: ")
    print(account.login())

elif user_selection == '2':
    account = Admin()
    account.email = input("Masukkan email: ")
    account.password = input("Masukkan password: ")
    print(account.login())

elif user_selection == '3':
    account = User()
    account.reset_password("sian@gmail.com", "akuganteng")
    print(Account.user_credentials)
    exit(0)

else:
    print("pilihan tidak ditemukan")
