from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{Phone.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, num):
        if num > 0 and isinstance(num, int):
            self.__number_of_sim = num
        else:
            print("ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.")

class Puf:
    def __init__(self, quantity):
        self.quantity = quantity
