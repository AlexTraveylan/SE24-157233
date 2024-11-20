from abc import ABC, abstractmethod

class TarifStrategy(ABC):
    @abstractmethod
    def calculer_prix(self, prix_base: float) -> float:
        pass

class TarifAdulteStrategy(TarifStrategy):
    def calculer_prix(self, prix_base: float) -> float:
        return prix_base

class TarifEnfantStrategy(TarifStrategy):
    def calculer_prix(self, prix_base: float) -> float:
        return prix_base * 0.5  # 50% de réduction pour les enfants

class TarifReduitStrategy(TarifStrategy):
    def calculer_prix(self, prix_base: float) -> float:
        return prix_base * 0.7  # 30% de réduction pour le tarif réduit 