from abc import ABC, abstractmethod
from typing import Type


class Vehicle(ABC):
    def __init__(self, model: str, brand: str):
        self.model = model
        self.brand = brand

    @abstractmethod
    def is_dirty(self) -> bool:
        pass

    @abstractmethod
    def drive(self) -> bool:
        pass


class Car(Vehicle):
    def __init__(self, model: str, brand: str, number_of_seats: int):
        super().__init__(model, brand)
        self.number_of_seats = number_of_seats

    def is_dirty(self) -> bool:
        pass

    def drive(self) -> bool:
        pass

    def drive_on_holidays(self) -> None:
        pass


class Truck(Vehicle):
    def __init__(self, model: str, brand: str, load: float):
        super().__init__(model, brand)
        self._load = load

    def is_dirty(self) -> bool:
        pass

    def drive(self) -> bool:
        pass

    def deliver_cargo(self) -> None:
        pass


class CarWash:
    def __init__(self, price_list: str):
        self.price_list = price_list

    def wash_vehicle(self, vehicle: Vehicle):
        pass

    def is_out_of_order(self) -> bool:
        pass


class Owner:
    def __init__(self, vehicle: Vehicle):
        self._vehicle = vehicle

    def go_to_car_wash(self, car_wash: CarWash):
        pass

    # def buy_new_vehicle(self, vehicle_type: Type[Vehicle]):  BARDZO ZLE ROZWIAZANIE
    #     if vehicle_type is Truck:
    #         self._vehicle = vehicle_type(
    #             model='123',
    #             brand='Volvo',
    #             load=50000,
    #         )
    #     elif vehicle_type is Car:
    #         self._vehicle = vehicle_type(
    #             model='xc90',
    #             brand='Volvo',
    #             number_of_seats=5,
    #         )

    def buy_new_vehicle(self, vehicle: Vehicle):
        self._vehicle = vehicle


if __name__ == '__main__':
    car_wash = CarWash(price_list='ala ma kota')

    car = Car(
        model='xc90',
        brand='Volvo',
        number_of_seats=5,
    )
    truck = Truck(
        model='123',
        brand='Volvo',
        load=50000,
    )

    owner = Owner(vehicle=truck)
    owner.go_to_car_wash(car_wash=car_wash)
    owner.buy_new_vehicle(vehicle_type=Truck)
    owner.buy_new_vehicle(vehicle=truck)




