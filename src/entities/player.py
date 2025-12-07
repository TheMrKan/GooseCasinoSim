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
        amount = random.randint(1, int(self.balance))
        chance = 0.5 - self.panic / 100
        if random.random() < chance:
            self.balance += amount
        else:
            self.balance -= amount

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            if not self.player_source:
                raise RuntimeError("Failed to kill a player: player source is not specified")
            self.player_source.remove(self)
