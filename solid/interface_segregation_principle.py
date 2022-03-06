from abc import ABC, abstractmethod


class ProductActionsInterface(ABC):

    @abstractmethod
    def show_reviews(self):
        pass


class OfflineProductActionsInterface(ProductActionsInterface, ABC):

    @abstractmethod
    def find_in_outlet(self):
        pass


class OnlineProductActionsInterface(ProductActionsInterface, ABC):

    @abstractmethod
    def try_for_seven_days(self):
        pass


class ComputerActionsUI(OfflineProductActionsInterface):
    def find_in_outlet(self):
        pass

    def show_reviews(self):
        pass


class SoftwareActionsUI(OnlineProductActionsInterface):
    def try_for_seven_days(self):
        pass

    def show_reviews(self):
        pass
