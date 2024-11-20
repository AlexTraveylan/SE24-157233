from src.controllers.zoo_controller import ZooController
from src.strategies.tarif_strategy import TarifAdulteStrategy, TarifEnfantStrategy, TarifReduitStrategy
from src.models.client_visiteur import ClientVisiteur

if __name__ == "__main__":
    # Création du contrôleur
    zoo = ZooController()
    
    # Ouverture du zoo
    print(zoo.ouvrir_zoo())
    
    # Ajout des animaux
    print(zoo.ajouter_animal("lion", "Simba"))
    print(zoo.ajouter_animal("singe", "Kong"))
    print(zoo.ajouter_animal("pingouin", "Tux"))
    
    # Accueil des visiteurs
    visiteur1 = ClientVisiteur("Jean Dupont", TarifAdulteStrategy())
    visiteur2 = ClientVisiteur("Pierre Dupont", TarifEnfantStrategy())
    visiteur3 = ClientVisiteur("Marie Martin", TarifReduitStrategy())
    
    print(zoo.accueillir_visiteur(visiteur1))
    print(zoo.accueillir_visiteur(visiteur2))
    print(zoo.accueillir_visiteur(visiteur3))
    
    # Soins et nourrissage des animaux
    print(zoo.nourrir_animaux())
    print(zoo.soigner_animaux())
    
    # Fermeture du zoo et rapport
    print(zoo.fermer_zoo())
