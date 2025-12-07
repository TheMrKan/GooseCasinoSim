from typing import Optional

from src.entities.actor import Actor


class Goose(Actor):
    name: str
    __group: Optional["GooseGroup"] = None

    def __init__(self, actor_id: str, name: str):
        super().__init__(actor_id)
        self.name = name

    @property
    def group(self) -> "GooseGroup":
        return self.__group

    @group.setter
    def group(self, value: Optional["GooseGroup"]):
        if self.__group == value:
            return

        if self.__group:
            self.__group.remove(self)
        if value:
            value.add(self)
        self.__group = value

    def use_ability(self, propagate: bool = True):
        if propagate and self.group:
            for goose in self.group:
                goose.use_ability(propagate=False)

        self._ability()

    def _ability(self):
        pass


class GooseGroup:
    __gooses: set[Goose]

    def __init__(self):
        self.__gooses = set()

    def add(self, goose: Goose):
        self.__gooses.add(goose)

    def remove(self, goose: Goose):
        self.__gooses.remove(goose)

    def __iter__(self):
        return iter(self.__gooses)

    def __contains__(self, goose: Goose) -> bool:
        return goose in self.__gooses

    def __len__(self) -> int:
        return len(self.__gooses)


class WarGoose(Goose):

    def _ability(self):
        pass


class HonkGoose(Goose):
    honk_volume: int

    def __init__(self, actor_id: str, name: str, honk_volume: int):
        super().__init__(actor_id, name)
        self.honk_volume = honk_volume

    def _ability(self):
        pass
