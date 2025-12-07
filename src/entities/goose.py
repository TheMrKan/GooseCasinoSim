from abc import ABC, abstractmethod

from src.entities.actor import Actor


class Goose(Actor):
    name: str

    def __init__(self, actor_id: int, name: str):
        super().__init__(actor_id)
        self.name = name


class IHasAbility(ABC):

    @abstractmethod
    def use_ability(self):
        pass


class WarGoose(Goose, IHasAbility):

    def use_ability(self):
        pass


class HonkGoose(Goose, IHasAbility):
    honk_volume: int

    def __init__(self, actor_id: int, name: str, honk_volume: int):
        super().__init__(actor_id, name)
        self.honk_volume = honk_volume

    def use_ability(self):
        pass
