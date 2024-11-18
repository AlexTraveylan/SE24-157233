from src.transport.abstract import Transport
from src.transport.concrete import Ship
from src.transport.creator.abstract import Creator


class ShipFactory(Creator):

    def create_product(self) -> Transport:
        return Ship()


