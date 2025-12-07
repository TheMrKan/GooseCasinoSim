from typing import Self


class NotEnoughChipsError(Exception):
    pass


class Chips:
    amount: int

    def __init__(self, amount):
        if amount < 0:
            raise NotEnoughChipsError

        self.amount = amount

    @classmethod
    def __amount(cls, obj: Self | int) -> int:
        if isinstance(obj, Chips):
            return cls.amount
        return obj

    def __add__(self, other: Self | int):
        return Chips(self.amount + self.__amount(other))

    def __iadd__(self, other: Self | int):
        return Chips(self.amount + self.__amount(other))

    def __sub__(self, other: Self | int):
        return Chips(self.amount - self.__amount(other))

    def __isub__(self, other: Self | int):
        return Chips(self.amount - self.__amount(other))
