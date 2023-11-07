from src.payment_service import PaymentService
from .payment import Payment

class MembershipPayment(Payment) :
    def __init__(self, invoice_number, total_price, payment_service: PaymentService, user, status=None):
        super().__init__(invoice_number, total_price, payment_service, status)
        self.set_user(user)

    # Getter(s)
    def get_user(self) :
        return self.user
    # Setter(s)
    def set_user(self, user) :
        self.user = user

    def pay(self) -> bool :
        print("Checking user status..")
        user_status_validation = self.user.check_status()
        print(f"User status validation: {user_status_validation}")
        if user_status_validation :
            return super().pay()
        else :
            self.set_status("FAILED")
            print(f"Payment with invoice number {self.get_invoice_number()} is failed.")
            return False

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"User info: {self.get_user()}\n"
            f"Final price (net): {self.get_total_price()}\n"
            f"Payment status: {self.get_status().name}"
        )