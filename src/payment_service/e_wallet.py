from abc import ABC, abstractmethod
from enum import Enum
from .payment_service import PaymentService

class WalletName(Enum) :
    GOPAY = 0
    OVO = 1

class EWallet(PaymentService, ABC) :
    def __init__(self, invoice_number, wallet_name) :
        super().__init__(invoice_number)
        self.set_wallet_name(wallet_name)

    # Getter(s)
    def get_wallet_name(self) :
        return self.wallet_name
    # Setter(s)
    def set_wallet_name(self, wallet_name) :
        self.wallet_name = WalletName[wallet_name]

    @abstractmethod
    def validate_payment(self):
        pass