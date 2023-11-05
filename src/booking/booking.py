from booking.interfaces.IBooking import IBooking
from account.Account import User
from item.fnb import FnB
from item.ticket import Ticket
from typing import List, Literal

class Booking(IBooking):
    def __init__(self, user: User, fnbs: List[FnB], tickets: List[Ticket]) -> None:
        super().__init__()
        self.set_user(user)
        self.set_fnbs(fnbs)
        self.set_tickets(tickets)
        self.set_status("open") # open, waiting for payment, canceled, paid
    
    def set_user(self, user: User):
        self.user = user
    
    def get_user(self) -> User:
        return self.user
    
    def set_status(self, status: Literal['open', 'waitng for payment', 'canceled', 'paid']):
        self.status = status
    
    def get_status(self) -> str:
        return self.status
    
    def set_tickets(self, tickets: List[Ticket]):
        self.tickets = tickets
    
    def get_tickets(self) -> List[Ticket]:
        return self.tickets

    def set_fnbs(self, fnbs: List[FnB]):
        self.fnbs = fnbs
    
    def get_fnbs(self) -> List[FnB]:
        return self.fnbs
    
    def checkout(self, payment_type: str) -> None:
        # kurangi stock FnB yang dibeli
        for f in self.fnbs:
            f.book()
            self.total_price += f.price
        
        for t in self.tickets:
            t.book()
            self.total_price += t.get_price()
        
        self.status = "waiting for payment"
    
    def cancel(self):
        for f in self.fnbs:
            f.cancel()

        for t in self.tickets:
            t.cancel()
        
        self.status = "canceled"