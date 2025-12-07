from typing import Optional, Self
import random

from src.entities.actor import Actor


class Goose(Actor):
    name: str
    run_crush_chance: float
    __group: Optional["GooseGroup"] = None

    def __init__(self, actor_id: str, name: str, run_crush_chance: float):
        super().__init__(actor_id)
        self.name = name
        self.run_crush_chance = run_crush_chance

    @property
    def group(self) -> Optional["GooseGroup"]:
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

    def random_run(self):
        for goose in self.goose_source:
            if random.random() < self.run_crush_chance:
                self += goose
                break

    def __iadd__(self, other: Self):
        if self.group and other.group:
            if self.group == other.group:
                self.group = None
            else:
                self.group += other.group

        elif self.group and not other.group:
            other.group = self.group

        elif not self.group and other.group:
            self.group = other.group

        else:
            self.group = GooseGroup()
            other.group = self.group


class GooseGroup:
    __gooses: set[Goose]

    def __init__(self):
        self.__gooses = set()

    def add(self, goose: Goose):
        self.__gooses.add(goose)

    def remove(self, goose: Goose):
        self.__gooses.remove(goose)

    def join(self, other: Self):
        if other == self:
            return

        for goose in other.__gooses:
            goose.group = self

    def __iter__(self):
        return iter(self.__gooses)

    def __contains__(self, goose: Goose) -> bool:
        return goose in self.__gooses

    def __len__(self) -> int:
        return len(self.__gooses)

    def __iadd__(self, other: Self | Goose):
        if isinstance(other, GooseGroup):
            self.join(other)
            return

        self.add(other)

    def __isub__(self, other: Goose):
        self.remove(other)


class WarGoose(Goose):
    damage: int

    def __init__(self, actor_id: str, name: str, run_crush_chance: float, damage: int):
        super().__init__(actor_id, name, run_crush_chance)
        self.damage = damage

    def _ability(self):
        if not self.player_source:
            raise RuntimeError("No player source specified")

        player = self.player_source.random_one()
        player.damage(self.damage)


class HonkGoose(Goose):
    honk_volume: int

    def __init__(self, actor_id: str, name: str, run_crush_chance: float, honk_volume: int):
        super().__init__(actor_id, name, run_crush_chance)
        self.honk_volume = honk_volume

    def _ability(self):
        if not self.player_source:
            raise RuntimeError("No player source specified")

        player = self.player_source.random_one()
        player.panic += self.honk_volume
