import random
from .credit_card import CreditCard

class CreditCardMastercard(CreditCard) :
    def __init__(self, invoice_number) :
        super().__init__(invoice_number, "MASTERCARD")

    # Dummy credit card Mastercard payment validation function
    def validate_payment(self):
        return random.choice([False, True])