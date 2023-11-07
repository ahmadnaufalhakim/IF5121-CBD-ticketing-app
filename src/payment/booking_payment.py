from promo import Promo
from payment_service import PaymentService
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