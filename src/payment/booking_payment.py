from src.promo import Promo
from src.payment_service import PaymentService
from .payment import Payment

class BookingPayment(Payment) :
    def __init__(self, invoice_number, total_price, payment_service: PaymentService, booking, promo:Promo=None, status=None):
        super().__init__(invoice_number, total_price, payment_service, status)
        self.set_booking(booking)
        self.set_promo(promo)

    # Getter(s)
    def get_booking(self) :
        return self.booking
    def get_promo(self) :
        return self.promo
    # Setter(s)
    def set_booking(self, booking) :
        self.booking = booking
    def set_promo(self, promo:Promo) :
        if promo is not None and promo.is_valid(self.total_price) :
            discounted_total_price = min(self.booking.total_price * (1-promo.get_discount()), promo.get_max_discount())
            self.total_price = discounted_total_price
            self.promo = promo

    def remove_promo(self) :
        if self.promo is not None :
            self.total_price = self.booking.total_price
        self.promo = None

    def pay(self) -> bool :
        if super().pay() :
            self.booking.set_status("paid")
            return True
        else :
            self.booking.cancel()
            return False

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"Booking info:\n"
            f"\tFilm: {self.get_booking().get_tickets()[0].get_schedule().get_film().get_name()}\n"
            f"\tStudio: {self.get_booking().get_tickets()[0].get_schedule().get_studio().get_name()}\n"
            f"\tSeats: {', '.join([ticket.get_seat() for ticket in self.booking.get_tickets()])}\n"
            f"\tFnBs: {', '.join([str(fnb.get_name()) for fnb in self.booking.get_fnbs()]) if len(self.booking.get_fnbs())>0 else 'No FnBs'}\n"
            f"\tTotal price: {self.booking.get_total_price()}\n"
            f"Final price (net): {self.get_total_price()}\n"
            f"Payment status: {self.get_status().name}\n"
        )