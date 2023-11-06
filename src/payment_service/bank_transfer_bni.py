import random
from .bank_transfer import BankTransfer

class BankTransferBNI(BankTransfer) :
    def __init__(self, invoice_number) :
        super().__init__(invoice_number, "BNI")

    # Dummy bank transfer BNI payment validation function
    def validate_payment(self):
        return random.choice([False, True])