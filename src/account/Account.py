import os
from abc import abstractmethod, ABC

abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

class Account:
    """ Account """
    """ user credentials"""
    user_credentials = {
        'sian@gmail.com' : 'admin123',
        'adit@zetta.sg' : '123456'
        }
    
    def __init__(self) -> None:
        self._email = None 
        self._password = None
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, user_email):
        self._email = user_email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, user_password):
        self._password = user_password

    def login(self):
        if self._email in self.user_credentials and \
            self._password == self.user_credentials[self._email]:
            return self._email
        else:
            return False

    def reset_password(self, email, new_password) -> bool:
        if email in self.user_credentials:
            self.user_credentials[email] = new_password
            return True
        else:
            return False


class User(Account):

    def __init__(self):
        super().__init__()
        self._membership_status = None

    def register_membership(self):
        pass 

    def is_member(self) -> bool:
        pass 


class Admin(Account):

    def __init__(self):
        super().__init__()
        self._admin_number = None 
    
    @property
    def admin_number(self):
        return self._admin_number
    
    @admin_number.setter
    def admin_number(self, adm_number):
        self._admin_number = adm_number


class Database(ABC):
    @abstractmethod
    def get_user_credentials(self):
        pass

class PickleDatabase()