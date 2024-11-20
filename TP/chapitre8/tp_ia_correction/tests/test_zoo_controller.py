import pytest
from datetime import datetime
from src.controllers.zoo_controller import ZooController
from src.models.client_visiteur import ClientVisiteur
from src.strategies.tarif_strategy import (
    TarifAdulteStrategy,
    TarifEnfantStrategy,
    TarifReduitStrategy
)

@pytest.fixture
def zoo():
    return ZooController()

@pytest.fixture
def visiteur_adulte():
    return ClientVisiteur("Jean Test", TarifAdulteStrategy())

@pytest.fixture
def visiteur_enfant():
    return ClientVisiteur("Pierre Test", TarifEnfantStrategy())

def test_ouvrir_zoo(zoo: ZooController):
    # Test ouverture initiale
    resultat = zoo.ouvrir_zoo()
    assert "Le zoo est maintenant ouvert" in resultat
    assert zoo.est_ouvert == True
    assert zoo.recette_jour == 0.0
    assert len(zoo.visiteurs) == 0

    # Test double ouverture
    resultat = zoo.ouvrir_zoo()
    assert resultat == "Le zoo est déjà ouvert"

def test_fermer_zoo(zoo: ZooController):
    # Test fermeture zoo fermé
    resultat = zoo.fermer_zoo()
    assert resultat == "Le zoo est déjà fermé"

    # Test fermeture normale
    zoo.ouvrir_zoo()
    zoo.accueillir_visiteur(ClientVisiteur("Test", TarifAdulteStrategy()))
    resultat = zoo.fermer_zoo()
    assert "=== Rapport de fermeture du" in resultat
    assert "Nombre total de visiteurs: 1" in resultat
    assert zoo.est_ouvert == False
    assert len(zoo.visiteurs) == 0

def test_accueillir_visiteur(zoo: ZooController, visiteur_adulte: ClientVisiteur, visiteur_enfant: ClientVisiteur):
    # Test accueil zoo fermé
    resultat = zoo.accueillir_visiteur(visiteur_adulte)
    assert resultat == "Impossible d'accueillir des visiteurs, le zoo est fermé"
    assert len(zoo.visiteurs) == 0

    # Test accueil visiteurs
    zoo.ouvrir_zoo()
    
    # Test visiteur adulte (tarif plein)
    resultat = zoo.accueillir_visiteur(visiteur_adulte)
    assert f"Bienvenue {visiteur_adulte.nom}!" in resultat
    assert "Prix du billet: 20.0€" in resultat
    assert zoo.recette_jour == 20.0
    
    # Test visiteur enfant (tarif réduit)
    resultat = zoo.accueillir_visiteur(visiteur_enfant)
    assert f"Bienvenue {visiteur_enfant.nom}!" in resultat
    assert "Prix du billet: 10.0€" in resultat
    assert zoo.recette_jour == 30.0

def test_ajouter_animal(zoo: ZooController):
    # Test ajout lion
    resultat = zoo.ajouter_animal("lion", "Simba")
    assert resultat == "Nouvel animal ajouté: lion nommé Simba"
    assert len(zoo.animaux) == 1
    
    # Test ajout type invalide
    with pytest.raises(ValueError):
        zoo.ajouter_animal("licorne", "Invalid")

def test_nourrir_animaux(zoo: ZooController):
    # Test sans animaux
    resultat = zoo.nourrir_animaux()
    assert resultat == "Aucun animal à nourrir"

    # Test avec animaux
    zoo.ajouter_animal("lion", "Simba")
    zoo.ajouter_animal("singe", "Kong")
    resultat = zoo.nourrir_animaux()
    assert "=== Nourrissage des animaux ===" in resultat

def test_soigner_animaux(zoo: ZooController):
    # Test sans animaux
    resultat = zoo.soigner_animaux()
    assert resultat == "Aucun animal à soigner"

    # Test avec animaux
    zoo.ajouter_animal("pingouin", "Tux")
    resultat = zoo.soigner_animaux()
    assert "=== Soin des animaux ===" in resultat

def test_rapport_journalier(zoo: ZooController, visiteur_adulte: ClientVisiteur):
    zoo.ouvrir_zoo()
    zoo.ajouter_animal("lion", "Simba")
    zoo.accueillir_visiteur(visiteur_adulte)
    
    rapport = zoo.fermer_zoo()
    
    assert "=== Rapport de fermeture du" in rapport
    assert "Nombre total de visiteurs: 1" in rapport
    assert "Recette totale: 20.0€" in rapport
    assert "Nombre d'animaux: 1" in rapport 