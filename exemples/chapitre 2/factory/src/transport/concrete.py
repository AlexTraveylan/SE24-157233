


from src.transport.abstract import Transport


class Truck(Transport):

    def go_to(self, destination: str):
        print(f"Truck is going to {destination}")


class Ship(Transport):

    def go_to(self, destination: str):
        print(f"Ship is going to {destination}")

class Plane(Transport):

    def go_to(self, destination: str):
        print(f"Plane is going to {destination}")

