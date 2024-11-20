from typing import List
from datetime import datetime
from src.models.client_visiteur import ClientVisiteur
from src.visitors.soigneur_visitor import SoigneurVisitor
from src.visitors.nourrisseur_visitor import NourrisseurVisitor
from src.factory.animal_factory import AnimalFactory
from src.models.animal import Animal

class ZooController:
    def __init__(self):
        self.est_ouvert = False
        self.visiteurs: List[ClientVisiteur] = []
        self.animaux: List[Animal] = []
        self.recette_jour = 0.0
        self.prix_base_billet = 20.0
        self.animal_factory = AnimalFactory()
        self.soigneur = SoigneurVisitor()
        self.nourrisseur = NourrisseurVisitor()

    def ouvrir_zoo(self) -> str:
        if self.est_ouvert:
            return "Le zoo est déjà ouvert"
        self.est_ouvert = True
        self.visiteurs.clear()
        self.recette_jour = 0.0
        return f"Le zoo est maintenant ouvert - {datetime.now().strftime('%d/%m/%Y %H:%M')}"

    def fermer_zoo(self) -> str:
        if not self.est_ouvert:
            return "Le zoo est déjà fermé"
        self.est_ouvert = False
        rapport = self._generer_rapport_journalier()
        self.visiteurs.clear()
        return rapport

    def accueillir_visiteur(self, visiteur: ClientVisiteur) -> str:
        if not self.est_ouvert:
            return "Impossible d'accueillir des visiteurs, le zoo est fermé"
        prix_billet = visiteur.calculer_prix_billet(self.prix_base_billet)
        self.recette_jour += prix_billet
        self.visiteurs.append(visiteur)
        return f"Bienvenue {visiteur.nom}! Prix du billet: {prix_billet}€"

    def ajouter_animal(self, type_animal: str, nom: str) -> str:
        nouvel_animal = self.animal_factory.creer_animal(type_animal, nom)
        self.animaux.append(nouvel_animal)
        return f"Nouvel animal ajouté: {type_animal} nommé {nom}"

    def nourrir_animaux(self) -> str:
        if not self.animaux:
            return "Aucun animal à nourrir"
        resultat = "=== Nourrissage des animaux ===\n"
        for animal in self.animaux:
            animal.accept(self.nourrisseur)
        return resultat

    def soigner_animaux(self) -> str:
        if not self.animaux:
            return "Aucun animal à soigner"
        resultat = "=== Soin des animaux ===\n"
        for animal in self.animaux:
            animal.accept(self.soigneur)
        return resultat

    def _generer_rapport_journalier(self) -> str:
        rapport = f"\n=== Rapport de fermeture du {datetime.now().strftime('%d/%m/%Y')} ===\n"
        rapport += f"Nombre total de visiteurs: {len(self.visiteurs)}\n"
        rapport += f"Recette totale: {self.recette_jour}€\n"
        rapport += f"Nombre d'animaux: {len(self.animaux)}"
        return rapport 