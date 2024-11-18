
from src.creature.abstract import Creature


class Dragon(Creature):

    def __init__(self) -> None:
        super().__init__("Dragon")
        self._element = "Fire"
        self._wingspan = 30  # in meters

    def get_description(self) -> str:
        return f"A {self._element} {self.name} with a wingspan of {self._wingspan} meters."
    

class Phoenix(Creature):

    def __init__(self) -> None:
        super().__init__("Phoenix")
        self._regeneration_cycle = 500  # in years

    def get_description(self) -> str:
        return f"A {self.name} with a regeneration cycle of {self._regeneration_cycle} years."
    

class Griffin(Creature):

    def __init__(self) -> None:
        super().__init__("Griffin")
        self._head_type = "aigle"
        self._body_type = "lion"

    def get_description(self) -> str:
        return f"A {self.name} with a {self._head_type} head and a {self._body_type} body."

