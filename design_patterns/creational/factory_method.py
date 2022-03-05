from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def deliver(self):
        pass


class Truck(Product):
    def deliver(self):
        print(f'Truck delivering...')


class Boat(Product):
    def deliver(self):
        print(f'Boat delivering...')


class Factory(ABC):

    def make_and_deliver(self):
        product = self.create_product()
        product.deliver()
        return product

    @abstractmethod
    def create_product(self) -> Product:
        pass


class TruckFactory(Factory):

    def create_product(self):
        return Truck()


class BoatFactory(Factory):

    def create_product(self):
        return Boat()


if __name__ == '__main__':
    truck_factory = TruckFactory()
    truck = truck_factory.make_and_deliver()

    boat_factory = BoatFactory()
    boat = boat_factory.make_and_deliver()
