from src.strategies.tarif_strategy import TarifStrategy

class ClientVisiteur:
    def __init__(self, nom: str, strategie_tarif: TarifStrategy):
        self.nom = nom
        self.strategie_tarif = strategie_tarif
        
    def calculer_prix_billet(self, prix_base: float) -> float:
        return self.strategie_tarif.calculer_prix(prix_base)
    
    def changer_strategie_tarif(self, nouvelle_strategie: TarifStrategy) -> None:
        self.strategie_tarif = nouvelle_strategie 