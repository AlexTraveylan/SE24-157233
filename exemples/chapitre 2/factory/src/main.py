from src.transport.creator.abstract import Creator
from src.transport.creator.ship_factory import ShipFactory
from src.transport.creator.truck_factory import TruckFactory
from src.transport.factory import TransportFactory


def main():
    factory = TransportFactory()

    print("=== Bienvenue sur le programme de gestion des transports ===")
    print("Voici les types de transports disponibles:")
    factory.display_transport_possibilities()
    type_transport = input("Quel type de transport souhaitez-vous créer ? ")

    transport = factory.create_transport(type_transport)
    
    destination = input("Où souhaitez-vous aller ? ")
    transport.go_to(destination)

def main_creator():

    print("=== Bienvenue sur le programme de gestion des transports ===")
    print("Voici les types de transports disponibles:")
    print("- truck")
    print("- ship")
    type_transport = input("Quel type de transport souhaitez-vous créer ? ")
    
    if type_transport == "truck":
        creator : Creator = TruckFactory()
    elif type_transport == "ship":
        creator : Creator = ShipFactory()
    else:
        raise ValueError(f"Invalid transport type: {type_transport}")
    
    transport = creator.create_product()
    destination = input("Où souhaitez-vous aller ? ")
    transport.go_to(destination)




if __name__ == "__main__":
    main()
    # main_creator()
