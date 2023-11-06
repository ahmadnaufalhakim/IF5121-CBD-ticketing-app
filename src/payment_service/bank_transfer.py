from abc import ABC, abstractmethod
from enum import Enum
from .payment_service import PaymentService

class Bank(Enum) :
    BCA = 0
    BNI = 1
    BRI = 2

class BankTransfer(PaymentService, ABC) :
    def __init__(self, invoice_number, bank) :
        super().__init__(invoice_number)
        self.set_bank(bank)

    # Getter(s)
    def get_bank(self) :
        return self.bank
    # Setter(s)
    def set_bank(self, bank) :
        self.bank = Bank[bank]

    @abstractmethod
    def validate_payment(self):
        pass