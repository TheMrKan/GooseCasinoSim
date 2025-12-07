import random

from src.entities.actor import Actor


class Player(Actor):

    panic: int
    health: int

    def __init__(self, actor_id: str):
        super().__init__(actor_id)
        self.panic = 0
        self.health = 100

    def play(self):
        if self.balance < 10 or self.panic >= 100:
            amount = int(self.balance)
        else:
            amount = random.randint(int(int(self.balance) / 2), int(self.balance))
            amount = min(int(amount * (1 + self.panic / 100)), int(self.balance))

        chance = 0.5 - self.panic / 100
        if random.random() < chance:
            self._logger.debug("Player %s has won %s!", self.actor_id, amount)
            self.balance += amount
        else:
            self._logger.debug("Player %s has lost %s (((", self.actor_id, amount)
            self.balance -= amount

        if int(self.balance) <= 0:
            self.damage(self.health)

    def damage(self, amount):
        self.health -= amount
        self._logger.debug("Player %s damaged %s! (new HP: %s)", self.actor_id, amount, self.health)
        if self.health <= 0:
            self._logger.info("Player %s is dead now", self.actor_id)
            if not self.player_source:
                raise RuntimeError("Failed to kill a player: player source is not specified")
            self.player_source.remove(self)
