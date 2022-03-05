# pylint: disable=too-few-public-methods, missing-module-docstring, missing-class-docstring, missing-function-docstring


class SamplePylint:

    def __init__(self, number):
        self._number = number

    @staticmethod
    def divide(number):
        if number == 0:
            raise ZeroDivisionError()


class Children(SamplePylint):

    def __init__(self, name, number):
        super().__init__(number)
        self._name = name

    @staticmethod
    def some_method(param):
        return param in [1, 2, 3]

    @staticmethod
    def some_method2():
        print('bad implementation')


if __name__ == '__main__':
    sample = SamplePylint(10)
    try:
        sample.divide(0)
    except ZeroDivisionError:
        pass
    sample.divide(number=10)

    Children.some_method(4)
