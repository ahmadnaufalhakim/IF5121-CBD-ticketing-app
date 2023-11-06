from abc import ABC, abstractmethod

class IPaymentService(ABC) :
    @abstractmethod
    def validate_payment(self) -> bool :
        pass