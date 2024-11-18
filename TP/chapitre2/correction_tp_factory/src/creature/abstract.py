
from abc import ABC, abstractmethod

class Creature(ABC):

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def get_description(self) -> str:
        raise NotImplementedError("get_description must be implemented")
