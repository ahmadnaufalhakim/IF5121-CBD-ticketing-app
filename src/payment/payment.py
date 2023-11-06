from enum import Enum
from payment_service import PaymentService

class PaymentStatus(Enum) :
    PENDING = 0
    COMPLETED = 1
    FAILED = 2

class Payment :
    valid_statuses = [e.value for e in PaymentStatus]
    def __init__(self, invoice_number, total_price, payment_service:PaymentService, status=None) :
        self.set_invoice_number(invoice_number)
        self.set_total_price(total_price)
        self.set_payment_service(payment_service)
        self.set_status(status)

    # Getter(s)
    def get_invoice_number(self) :
        return self.invoice_number
    def get_total_price(self) :
        return self.total_price
    def get_payment_service(self) :
        return self.payment_service
    def get_status(self) :
        return self.status
    # Setter(s)
    def set_invoice_number(self, invoice_number) :
        self.invoice_number = invoice_number
    def set_total_price(self, total_price) :
        self.total_price = total_price
    def set_payment_service(self, payment_service:PaymentService) :
        self.payment_service = payment_service
    def set_status(self, status) :
        if status is None :
            self.status = PaymentStatus.PENDING
        elif isinstance(status, str) :
            self.status = PaymentStatus[status]
        elif isinstance(status, int) :
            self.status = PaymentStatus(status)

    def pay(self) -> bool :
        print("Validating payment..")
        payment_validation = self.payment_service.validate_payment()
        print(f"Payment validation: {payment_validation}")
        if payment_validation :
            self.set_status("COMPLETED")
            print(f"Payment with invoice number {self.get_invoice_number()} is completed!")
        else :
            self.set_status("FAILED")
            print(f"Payment with invoice number {self.get_invoice_number()} is failed.")
        return payment_validation