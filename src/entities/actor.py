from src.entities.chips import Chips
from src.dict_collections import BalanceCollection

from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from src.list_collections import PlayerCollection, GooseCollection


class Actor:

    actor_id: str
    balance_source: BalanceCollection | None
    player_source: Optional["PlayerCollection"]
    goose_source: Optional["GooseCollection"]

    def __init__(self, actor_id: str):
        self.actor_id = actor_id

    @property
    def balance(self) -> Chips:
        if not self.balance_source:
            raise RuntimeError("Balance source is not configured")

        return self.balance_source[self.actor_id]

    @balance.setter
    def balance(self, value: Chips):
        if not self.balance_source:
            raise RuntimeError("Balance source is not configured")

        self.balance_source[self.actor_id] = value

    def __str__(self):
        return f"<{self.__class__.__name__}({self.actor_id}): {self.balance}>"

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(self.actor_id)
