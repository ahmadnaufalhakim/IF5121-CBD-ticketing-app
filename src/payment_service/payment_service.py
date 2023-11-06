from payment_service.interfaces import IPaymentService
from abc import ABC, abstractmethod

class PaymentService(IPaymentService, ABC) :
    def __init__(self, invoice_number) :
        self.set_invoice_number(invoice_number)

    # Getter(s)
    def get_invoice_number(self) :
        return self.invoice_number
    # Setter(s)
    def set_invoice_number(self, invoice_number) :
        self.invoice_number = invoice_number

    @abstractmethod
    def validate_payment(self) :
        pass