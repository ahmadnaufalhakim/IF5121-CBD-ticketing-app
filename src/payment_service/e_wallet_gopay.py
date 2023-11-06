import random
from .e_wallet import EWallet

class EWalletGoPay(EWallet) :
    def __init__(self, invoice_number) :
        super().__init__(invoice_number, "GOPAY")

    # Dummy e-wallet GoPay payment validation function
    def validate_payment(self):
        return random.choice([False, True])