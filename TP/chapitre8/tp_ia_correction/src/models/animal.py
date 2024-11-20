from abc import ABC, abstractmethod

from src.visitors.animal_visitor import AnimalVisitor

class Animal(ABC):
    def __init__(self, nom: str):
        self.nom = nom
        self.sante = 100  # santé maximale
        self.faim = 100   # pas faim
    
    @abstractmethod
    def faire_son(self) -> str:
        pass
    
    @abstractmethod
    def manger(self) -> str:
        pass
    
    @abstractmethod
    def dormir(self) -> str:
        pass
    
    @abstractmethod
    def accept(self, visitor: AnimalVisitor) -> None:
        pass 