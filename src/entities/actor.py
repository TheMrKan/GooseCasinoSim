from src.entities.chips import Chips
from src.dict_collections import BalanceCollection


class Actor:

    actor_id: str
    __balance_source: BalanceCollection

    def __init__(self, actor_id: str, balance_source: BalanceCollection):
        self.actor_id = actor_id
        self.__balance_source = balance_source

    @property
    def balance(self) -> Chips:
        return self.__balance_source[self.actor_id]

    @balance.setter
    def balance(self, value: Chips):
        self.__balance_source[self.actor_id] = value
