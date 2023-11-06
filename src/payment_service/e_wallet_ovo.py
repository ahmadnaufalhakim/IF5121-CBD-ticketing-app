import random
from .e_wallet import EWallet

class EWalletOVO(EWallet) :
    def __init__(self, invoice_number) :
        super().__init__(invoice_number, "OVO")

    # Dummy e-wallet OVO payment validation function
    def validate_payment(self):
        return random.choice([False, True])