import sys
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(name)s] %(message)s',
    stream=sys.stdout,
)
logger = logging.getLogger(__name__)

from src.casino import Casino    # noqa: E402
from src.factories import generate_players, generate_gooses    # noqa: E402
from src.exceptions import SimulationException     # noqa: E402


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
        logger.info("")
        logger.info("")
        logger.info("")
        logger.info("__________ THE END __________")
        logger.info("")
        logger.info("The simulation has ended with result:")
        logger.info(str(e))
        logger.info("")
        casino.print_state()
    except Exception as e:
        logger.info("__________ ERROR __________")
        logger.exception("Looks like an error has occured", exc_info=e)


if __name__ == "__main__":
    main()
