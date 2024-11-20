from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.animals.lion import Lion
    from src.models.animals.singe import Singe
    from src.models.animals.pingouin import Pingouin

class AnimalVisitor(ABC):
    @abstractmethod
    def visiter_lion(self, lion: Lion) -> None:
        pass
    
    @abstractmethod
    def visiter_singe(self, singe: Singe) -> None:
        pass
    
    @abstractmethod
    def visiter_pingouin(self, pingouin: Pingouin) -> None:
        pass 