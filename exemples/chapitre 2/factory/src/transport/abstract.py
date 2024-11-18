from abc import ABC, abstractmethod

class Transport(ABC):

    @abstractmethod
    def go_to(self, destination: str):
        pass
