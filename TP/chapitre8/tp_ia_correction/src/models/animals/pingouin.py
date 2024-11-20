from __future__ import annotations

from src.models.animal import Animal
from src.visitors.animal_visitor import AnimalVisitor

class Pingouin(Animal):
    def __init__(self, nom: str):
        super().__init__(nom)
        self.resistance_froid = 95
    
    def faire_son(self) -> str:
        return f"Le pingouin {self.nom} fait : Coin coin!"
    
    def manger(self) -> str:
        return f"Le pingouin {self.nom} mange du poisson"
    
    def dormir(self) -> str:
        return f"Le pingouin {self.nom} dort en groupe"
    
    def accept(self, visitor: AnimalVisitor) -> None:
        visitor.visiter_pingouin(self) 