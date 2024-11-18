




from typing import Literal, Type
from src.transport.abstract import Transport
from src.transport.concrete import Plane, Ship, Truck


TransportType = Literal["truck", "ship"]


class TransportFactory:

    _transport_types: dict[TransportType, Type[Transport]] = {
        "truck": Truck,
        "ship": Ship,
        "plane": Plane,
    }

    def create_transport(self, transport_type: TransportType) -> Transport:
        match transport_type:
            case "truck":
                return Truck()
            case "ship":
                return Ship()
            case "plane":
                return Plane()
            case _:
                raise ValueError(f"Invalid transport type: {transport_type}")
        
    def display_transport_possibilities(self):
        for transport_type in self._transport_types:
            print(f"- {transport_type}")

