import random
from .bank_transfer import BankTransfer

class BankTransferBRI(BankTransfer) :
    def __init__(self, invoice_number) :
        super().__init__(invoice_number, "BRI")

    # Dummy bank transfer BRI payment validation function
    def validate_payment(self):
        return random.choice([False, True])