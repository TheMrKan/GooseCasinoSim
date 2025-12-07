from typing import Self
from dataclasses import dataclass
from functools import total_ordering


class NotEnoughChipsError(Exception):
    pass


@total_ordering
@dataclass(frozen=True)
class Chips:
    amount: int

    def __post_init__(self):
        if self.amount < 0:
            raise NotEnoughChipsError

    @classmethod
    def __amount(cls, obj: Self | int) -> int:
        if isinstance(obj, Chips):
            return obj.amount
        return obj

    def __add__(self, other: Self | int):
        return Chips(self.amount + self.__amount(other))

    def __sub__(self, other: Self | int):
        return Chips(self.amount - self.__amount(other))

    def __eq__(self, other: Self | int) -> bool:
        return self.amount == self.__amount(other)

    def __lt__(self, other: Self | int) -> bool:
        return self.amount < self.__amount(other)

    def __int__(self):
        return self.amount
