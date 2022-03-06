from abc import abstractmethod, ABC


class Discount(ABC):
    @abstractmethod
    def get_discount(self):
        pass


class EasterDiscount(Discount):
    _EASTER_DISCOUNT = '30%'

    def get_discount(self):
        return f'{self._EASTER_DISCOUNT} on Easter'


class BlackFridayDiscount(Discount):
    _BLACK_FRIDAY_DISCOUNT = '50%'

    def get_discount(self):
        return f'{self._BLACK_FRIDAY_DISCOUNT} on Black Friday'


class WomenDayDiscount(Discount):
    _WOMEN_DAY_DISCOUNT = '25%'

    def get_discount(self):
        return f'{self._WOMEN_DAY_DISCOUNT} on Women Day'


class DiscountManager:
    def process_discount(self, discount: Discount):
        discount.get_discount()


if __name__ == '__main__':
    women_day_discount = WomenDayDiscount()
    black_friday_discount = BlackFridayDiscount()

    discount_manager = DiscountManager()
    discount_manager.process_discount(discount=women_day_discount)
    discount_manager.process_discount(discount=black_friday_discount)


class Building:
    pass


class Flat:
    pass
