import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

class Membership:

    def __init__(self) -> None:
        self._number = None
        self._expiry = None 
        self._user_info :dict = None
        self._status =  None
        self._payment = None 

    @property
    def user_info(self):
        return self._user_info
    
    @user_info.setter
    def user_info(self, usr_info:dict):
        self._user_info = usr_info
    
    def create_membership_bill(self, months):
        print(f"Anda membeli membership selama {months} bulan")
        return self._user_info.update({'membership_month':months})

    """ NOTE: Masih bingung untuk mekanisme ini"""
    def check_status(self, payment_status):
        
        self._status = payment_status
        return self._status