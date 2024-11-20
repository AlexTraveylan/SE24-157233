from __future__ import annotations

from src.models.animal import Animal
from src.visitors.animal_visitor import AnimalVisitor

class Singe(Animal):
    def __init__(self, nom: str):
        super().__init__(nom)
        self.agilite = 90
    
    def faire_son(self) -> str:
        return f"Le singe {self.nom} crie : Ouh ouh ah ah!"
    
    def manger(self) -> str:
        return f"Le singe {self.nom} mange des bananes"
    
    def dormir(self) -> str:
        return f"Le singe {self.nom} dort dans les arbres"
    
    def accept(self, visitor: AnimalVisitor) -> None:
        visitor.visiter_singe(self) 