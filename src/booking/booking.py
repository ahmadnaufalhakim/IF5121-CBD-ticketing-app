from src.booking.interfaces.IBooking import IBooking
from src.account.Account import User
from src.item.fnb import FnB
from src.item.ticket import Ticket
from typing import List, Literal
import string
import random

class Booking(IBooking):
    def __init__(self, user: User, fnbs: List[FnB], tickets: List[Ticket]) -> None:
        super().__init__()
        self.set_user(user)
        self.set_fnbs(fnbs)
        self.set_tickets(tickets)
        self.set_status("open") # open, waiting for payment, canceled, paid
        self.set_total_price(0)
        self.set_booking_number(self.generate_booking_number())
    
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
    
    def set_total_price(self, total_price):
        self.total_price = total_price
    
    def get_total_price(self):
        return self.total_price
    
    def set_booking_number(self, booking_number):
        self.booking_number = booking_number
    
    def get_booking_number(self):
        return self.booking_number

    def generate_booking_number(self):
        prefix = "BK"
        random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        booking_number = prefix + random_part
        return booking_number
    
    def checkout(self, payment_type: str) -> None:
        # kurangi stock FnB yang dibeli
        for f in self.fnbs:
            f.book()
            self.total_price += f.price
        
        for t in self.tickets:
            t.book()
            self.total_price += t.get_price()
        
        self.set_status("waiting for payment")
    
    def cancel(self):
        for f in self.fnbs:
            f.cancel()

        for t in self.tickets:
            t.cancel()
        
        self.status = "canceled"
    
    def __str__(self):
        fnb_list = ', '.join([str(fnb.get_name()) for fnb in self.fnbs])
        seat_list = ', '.join([ticket.get_seat() for ticket in self.tickets])

        return (
            f"Booking Number: {self.booking_number}\n"
            f"Film Name: {self.tickets[0].get_schedule().get_film().get_name()}\n"
            f"Studio: {self.tickets[0].get_schedule().get_studio().get_name()}\n"
            f"Seats: {seat_list}\n"
            f"FnBs: {fnb_list if fnb_list else 'No FnBs'}, \n"
            f"Status: {self.status}\n"
            f"Total Price: {self.total_price}\n\n"
        )