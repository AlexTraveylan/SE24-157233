from typing import Literal
from src.creature.implementation import Dragon, Phoenix, Griffin
from src.creature.abstract import Creature  


type CreatureType = Literal["dragon", "phoenix", "griffin"]


class CreatureFactory:

    _creatures: dict[CreatureType, type[Creature]] = {
        "dragon": Dragon,
        "phoenix": Phoenix,
        "griffin": Griffin
    }

    @staticmethod
    def create_creature(creature_type: CreatureType) -> Creature:

        if creature_type not in CreatureFactory._creatures:
            raise ValueError(f"Invalid creature type: {creature_type}")

        return CreatureFactory._creatures[creature_type]()
    
    @staticmethod
    def display_creatures() -> None:
        print("\nAvailable creatures:")
        print('==============')
        for creature_type in CreatureFactory._creatures:
            print(f" - {creature_type.capitalize()}")
        print('==============\n')
