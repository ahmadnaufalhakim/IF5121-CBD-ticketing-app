from abc import ABC, abstractmethod

class IBooking(ABC):

    @abstractmethod
    def checkout(self) -> None:
        pass

    @abstractmethod
    def cancel(self) -> None:
        pass