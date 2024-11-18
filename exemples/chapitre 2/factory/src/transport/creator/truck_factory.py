



from src.transport.abstract import Transport
from src.transport.concrete import Truck
from src.transport.creator.abstract import Creator


class TruckFactory(Creator):

    def create_product(self) -> Transport:
        return Truck()

