import traceback

from src.casino import Casino
from src.factories import generate_players, generate_gooses
from src.exceptions import SimulationException


def main() -> None:
    casino = Casino()

    generate_players(casino, 5, 10, 100)
    generate_gooses(
        casino,
        10,
        (0, 20),
        0.5,
        0.5,
        (30, 100),
        (50, 100),
        0.3
    )

    casino.print_state()
    try:
        for _ in range(15):
            casino.simulation_step()
            casino.print_state()
    except SimulationException as e:
        print()
        print()
        print()
        print("__________ THE END __________")
        print()
        print("The simulation has ended with result:")
        print(str(e))
        print()
        casino.print_state()
    except Exception as e:
        print("__________ ERROR __________")
        print("Looks like an error has occured:")
        traceback.print_exception(type(e), e)


if __name__ == "__main__":
    main()
