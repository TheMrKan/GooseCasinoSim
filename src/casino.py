from typing import Callable
from dataclasses import dataclass
import random
import logging

from src.list_collections import PlayerCollection, GooseCollection
from src.dict_collections import BalanceCollection
from src.entities.actor import Actor
from src.entities.goose import Goose
from src.entities.player import Player
from src.entities.chips import Chips

logger = logging.getLogger(__name__)


@dataclass
class CasinoEvent:
    weight: int
    action: Callable[[], None]


class Casino:
    players: PlayerCollection
    gooses: GooseCollection
    balances: BalanceCollection

    __events: list[CasinoEvent]
    __events_weight_sum: int
    __sim_step: int

    def __init__(self):
        self.players = PlayerCollection()
        self.gooses = GooseCollection()
        self.balances = BalanceCollection()

        self.__events = [
            CasinoEvent(10, self.__event_global_play),
            CasinoEvent(7, self.__event_goose_steal),
            CasinoEvent(5, self.__event_goose_run),
            CasinoEvent(4, self.__event_goose_ability)
        ]
        self.__events.sort(key=lambda x: x.weight, reverse=True)
        self.__events_weight_sum = sum((e.weight for e in self.__events))
        self.__sim_step = 0

    def print_state(self):
        logger.info(f"########  CASINO STATE (STEP: {self.__sim_step})  #########")
        logger.info("")
        logger.info(f"PLAYERS: {self.players}")
        logger.info(f"GOOSES: {self.gooses}")
        logger.info("")
        logger.info("###########################################")

    def register_actor(self, actor: Actor, balance: Chips):
        if isinstance(actor, Player):
            self.players.add(actor)
        elif isinstance(actor, Goose):
            self.gooses.add(actor)
        else:
            raise ValueError(f"Unsupported actor type: {type(actor)}")

        actor.balance_source = self.balances
        actor.goose_source = self.gooses
        actor.player_source = self.players

        self.balances[actor.actor_id] = balance

        logger.debug(f"Registered actor {actor} with balance {balance}")

    def simulation_step(self):
        self.__sim_step += 1
        event = self.__select_random_event()
        event.action()

    def __select_random_event(self) -> CasinoEvent:
        value = random.randint(1, self.__events_weight_sum)

        for event in self.__events:
            if event.weight >= value:
                return event
            value -= event.weight
        raise RuntimeError(f"Failed to select random event. Value left: {value}")

    def __event_global_play(self):
        logger.info("EVENT: GLOBAL PLAY")
        for player in tuple(self.players):
            player.play()

    def __event_goose_run(self):
        logger.info("EVENT: GLOBAL GOOSE RUN")
        for goose in self.gooses:
            goose.random_run()

    def __event_goose_ability(self):
        logger.info("EVENT: RANDOM GOOSE USE THE ABILITY")
        goose = self.gooses.random_one()
        goose.use_ability()

    def __event_goose_steal(self):
        logger.info("EVENT: RANDOM GOOSE STEAL FROM A RANDOM PLAYER")
        goose = self.gooses.random_one()
        goose.steal()
