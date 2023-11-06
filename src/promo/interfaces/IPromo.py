from abc import ABC, abstractmethod

class IPromo(ABC) :
    @abstractmethod
    def is_valid(self, amount) -> bool :
        pass