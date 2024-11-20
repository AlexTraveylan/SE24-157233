from __future__ import annotations

from src.models.animal import Animal
from src.visitors.animal_visitor import AnimalVisitor

class Lion(Animal):
    def __init__(self, nom: str):
        super().__init__(nom)
        self.force = 80
    
    def faire_son(self) -> str:
        return f"Le lion {self.nom} rugit : ROAAAR!"
    
    def manger(self) -> str:
        return f"Le lion {self.nom} mange de la viande"
    
    def dormir(self) -> str:
        return f"Le lion {self.nom} dort dans sa tanière"
    
    def accept(self, visitor: AnimalVisitor) -> None:
        visitor.visiter_lion(self) 