from abc import ABC, abstractmethod
from typing import List, Optional


class Component(ABC):
    @abstractmethod
    def execute(self):
        pass


class Car(Component):
    def __init__(self, color):
        self.color = color

    def execute(self):
        print(f'{self.color} Car')


class Ball(Component):
    def __init__(self, type):
        self.type = type

    def execute(self):
        print(f'{self.type} Ball')


class Bike(Component):
    def __init__(self, wheel_size):
        self.wheel_size = wheel_size

    def execute(self):
        print(f'{self.wheel_size} Bike')


class Box(Component):

    def __init__(self):
        self._children: Optional[List[Component]] = []

    def add(self, component: Component):
        self._children.append(component)

    def remove(self, component: Component):
        self._children.remove(component)

    def get_children(self):
        return self._children

    def execute(self):
        print('[')
        for child in self._children:
            child.execute()
        print(']')


if __name__ == '__main__':
    box = Box()
    box.add(Bike('26\"'))
    box.add(Bike('29\"'))
    box.add(Ball('Football'))

    parent_box = Box()
    parent_box.add(box)
    parent_box.add(Car('Burning Orange'))
    parent_box.execute()
