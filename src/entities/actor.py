from src.entities.chips import Chips


class Actor:

    actor_id: str

    def __init__(self, actor_id: str):
        self.actor_id = actor_id

    @property
    def balance(self) -> Chips:
        raise NotImplementedError

    @balance.setter
    def balance(self, value: Chips):
        raise NotImplementedError
