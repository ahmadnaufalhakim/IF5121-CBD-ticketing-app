from abc import ABC, abstractmethod
from enum import Enum
from .payment_service import PaymentService

class CardProvider(Enum) :
    MASTERCARD = 0
    VISA = 1

class CreditCard(PaymentService, ABC) :
    def __init__(self, invoice_number, card_provider) :
        super().__init__(invoice_number)
        self.set_card_provider(card_provider)

    # Getter(s)
    def get_card_provider(self) :
        return self.card_provider
    # Setter(s)
    def set_card_provider(self, card_provider) :
        self.card_provider = CardProvider[card_provider]

    @abstractmethod
    def validate_payment(self):
        pass

    def __str__(self) -> str:
        return f"Credit Card ({self.get_card_provider().name})"