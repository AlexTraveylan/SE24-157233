
from abc import ABC, abstractmethod
from src.transport.abstract import Transport


class Creator(ABC):

    @abstractmethod
    def create_product(self) -> Transport:
        pass

