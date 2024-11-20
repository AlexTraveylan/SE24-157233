from __future__ import annotations

from src.visitors.animal_visitor import AnimalVisitor
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.animals.lion import Lion
    from src.models.animals.singe import Singe
    from src.models.animals.pingouin import Pingouin

class NourrisseurVisitor(AnimalVisitor):
    def visiter_lion(self, lion: Lion) -> None:
        lion.faim += 30
        print(f"Le nourrisseur donne de la viande au lion {lion.nom}. Niveau de satiété: {lion.faim}")
    
    def visiter_singe(self, singe: Singe) -> None:
        singe.faim += 20
        print(f"Le nourrisseur donne des fruits au singe {singe.nom}. Niveau de satiété: {singe.faim}")
    
    def visiter_pingouin(self, pingouin: Pingouin) -> None:
        pingouin.faim += 25
        print(f"Le nourrisseur donne du poisson au pingouin {pingouin.nom}. Niveau de satiété: {pingouin.faim}") 