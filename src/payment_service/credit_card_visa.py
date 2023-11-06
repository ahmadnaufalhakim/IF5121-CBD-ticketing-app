import random
from .credit_card import CreditCard

class CreditCardVISA(CreditCard) :
    def __init__(self, invoice_number) :
        super().__init__(invoice_number, "VISA")

    # Dummy credit card VISA payment validation function
    def validate_payment(self):
        return random.choice([False, True])