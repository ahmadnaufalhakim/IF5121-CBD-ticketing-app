import random
from .bank_transfer import BankTransfer

class BankTransferBCA(BankTransfer) :
    def __init__(self, invoice_number) :
        super().__init__(invoice_number, "BCA")

    # Dummy bank transfer BCA payment validation function
    def validate_payment(self):
        return random.choice([False, True])