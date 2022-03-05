from abc import ABC, abstractmethod


class ChristmasTree(ABC):
    @abstractmethod
    def execute(self):
        pass


class Tree(ChristmasTree):

    def execute(self):
        print('Tree')


class BaseDecorator(ChristmasTree):

    def __init__(self, christmas_tree: ChristmasTree):
        self._wrappee = christmas_tree

    def execute(self):
        self._wrappee.execute()


class ChristmasLightsDecorator(BaseDecorator):

    def _extra(self):
        # some operation
        print('Christmas Lights')

    def execute(self):
        self._extra()
        super().execute()


class ChristmasBombsDecorator(BaseDecorator):

    def _extra(self):
        # some another operation
        print('Christmas Bombs')

    def execute(self):
        self._extra()
        super().execute()


class ChristmasStarDecorator(BaseDecorator):

    def _extra(self):
        # some another operation
        print('Christmas Star')

    def execute(self):
        self._extra()
        super().execute()


if __name__ == '__main__':
    tree = Tree()
    christmas_lights_decorated = ChristmasLightsDecorator(tree)
    christmas_bombs_decorated = ChristmasBombsDecorator(christmas_lights_decorated)
    christmas_bombs_decorated = ChristmasBombsDecorator(christmas_bombs_decorated)
    christmas_bombs_decorated = ChristmasBombsDecorator(christmas_bombs_decorated)
    christmas_star_decorated = ChristmasStarDecorator(christmas_bombs_decorated)
    christmas_star_decorated.execute()

    # Christmas Star -> Christmas Bombs -> Christmas Bombs -> Christmas Bombs -> Christmas Lights -> Tree
