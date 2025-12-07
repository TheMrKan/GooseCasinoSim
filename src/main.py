from src.casino import Casino
from src.entities.goose import Goose, WarGoose, HonkGoose
from src.entities.player import Player
from src.entities.chips import Chips


def main() -> None:
    casino = Casino()

    casino.register_actor(Player("P_0"), Chips(100))
    casino.register_actor(Player("P_1"), Chips(50))
    casino.register_actor(Player("P_2"), Chips(10))

    casino.register_actor(Goose("G_0", "Goose 0", 0.3), Chips(0))
    casino.register_actor(Goose("G_1", "Goose 1", 0.3), Chips(0))
    casino.register_actor(Goose("G_2", "Goose 2", 0.3), Chips(0))

    casino.register_actor(HonkGoose("G_3", "Goose 3", 0.3, 30), Chips(0))
    casino.register_actor(WarGoose("G_4", "Goose 4", 0.3, 50), Chips(0))

    casino.print_state()
    for _ in range(5):
        casino.simulation_step()
        casino.print_state()


if __name__ == "__main__":
    main()
