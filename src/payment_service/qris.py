import random
from .payment_service import PaymentService

class QRIS(PaymentService) :
    def __init__(self, invoice_number) :
        super().__init__(invoice_number)

    # Dummy QRIS payment validation function
    def validate_payment(self):
        return random.choice([False, True])

    def __str__(self) -> str:
        return "QRIS"