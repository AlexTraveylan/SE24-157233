from typing import Literal
from src.models.animal import Animal
from src.models.animals.lion import Lion
from src.models.animals.singe import Singe
from src.models.animals.pingouin import Pingouin

TypeAnimal = Literal["lion", "singe", "pingouin"]

class AnimalFactory:
    @staticmethod
    def creer_animal(type_animal: TypeAnimal, nom: str) -> Animal:
        animaux: dict[TypeAnimal, type[Animal]] = {
            "lion": Lion,
            "singe": Singe,
            "pingouin": Pingouin
        }
        
        if type_animal.lower() not in animaux:
            raise ValueError(f"Type d'animal non supporté: {type_animal}")
            
        return animaux[type_animal.lower()](nom) 