from abc import ABC

from src.item import Item


class MixLang(ABC):
    def __init__(self):
        self.__lang = "EN"

    def change_lang(self):
        if self.__lang == "EN":
            self.__lang = "RU"
        else:
            self.__lang = "EN"
        return self

    @property
    def language(self):
        return self.__lang


class Keyboard(Item, MixLang):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

    def __str__(self):
        return self.name
