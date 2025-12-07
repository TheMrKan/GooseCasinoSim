from src.list_collections import PlayerCollection, GooseCollection
from src.dict_collections import BalanceCollection
from src.entities.actor import Actor
from src.entities.goose import Goose
from src.entities.player import Player
from src.entities.chips import Chips


class Casino:
    players: PlayerCollection
    gooses: GooseCollection
    balances: BalanceCollection

    def __init__(self):
        self.players = PlayerCollection()
        self.gooses = GooseCollection()
        self.balances = BalanceCollection()

    def register_actor(self, actor: Actor, balance: Chips):
        if isinstance(actor, Player):
            self.players.add(actor)
        elif isinstance(actor, Goose):
            self.gooses.add(actor)

        actor.balance_source = self.balances
        actor.goose_source = self.gooses
        actor.player_source = self.players

        self.balances[actor.actor_id] = balance

        raise ValueError(f"Unsupported actor type: {type(actor)}")
