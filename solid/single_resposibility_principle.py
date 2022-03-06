from abc import ABC


class Product(ABC):
    pass


class Computer(Product):

    def __init__(self):
        self._brand = None
        self._model = None

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value


class Inventory:

    def search(self, product: Product) -> dict:
        pass


if __name__ == '__main__':
    inventory = Inventory()
    computer = Computer()

    inventory.search(product=computer)
