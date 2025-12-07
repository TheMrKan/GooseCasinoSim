from typing import Iterable, TypeVar
import random

from src.entities.actor import Actor
from src.entities.goose import Goose
from src.entities.player import Player


T = TypeVar('T', bound=Actor)


class GenericActorCollection[T]:
    __list: list[T]

    def __init__(self, iterable: Iterable[T] | None = None):
        self.__list = list(iterable or [])

    def add(self, actor: T):
        self.__list.append(actor)

    def remove(self, actor: T):
        self.__list.remove(actor)

    def random_one(self):
        if not self:
            raise ValueError("The collection is empty")

        index = random.randint(0, len(self) - 1)
        return self[index]

    def __getitem__(self, item: int | slice) -> T | list[T]:
        return self.__list[item]

    def __iter__(self):
        return iter(self.__list)

    def __bool__(self):
        return bool(self.__list)

    def __len__(self):
        return len(self.__list)

    def __repr__(self):
        return repr(self.__list)


class GooseCollection(GenericActorCollection[Goose]):

    def __str__(self):
        checked_gooses = set()
        groups = []
        for goose in self:
            if goose in checked_gooses:
                continue

            if goose.group:
                gp = list(goose.group)
                checked_gooses.union(gp)
            else:
                gp = [goose]

            groups.append(gp)

        groups.sort(key=len)
        sep = ', '
        return f"[{sep.join(f'{{{sep.join(str(g) for g in group)}}}' for group in groups)}]"


class PlayerCollection(GenericActorCollection[Player]):
    pass
