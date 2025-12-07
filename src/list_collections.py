from typing import Iterable, TypeVar

from src.entities.actor import Actor
from src.entities.goose import Goose
from src.entities.player import Player


T = TypeVar('T', bound=Actor)


class GenericActorCollection[T]:
    __list: list[T]

    def __init__(self, iterable: Iterable[T] | None = None):
        self.__list = list(iterable or [])

    def __getitem__(self, item: int | slice) -> T:
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
    pass


class PlayerCollection(GenericActorCollection[Player]):
    pass
