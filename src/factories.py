import random

from src.casino import Casino
from src.entities.player import Player
from src.entities.chips import Chips
from src.entities.goose import Goose, HonkGoose, WarGoose


def generate_players(add_to: Casino, count: int, balance_min: int, balance_max: int):
    for i in range(count):
        player = Player(f"P_{i}")
        balance = random.randint(balance_min, balance_max)
        add_to.register_actor(player, Chips(balance))


__GOOSE_NAME_FIRST = first = [
    "Байтовый", "Флопповый", "Шустрый", "Криптовый", "Ломанный", "Багнутый", "Опытный", "Хитрый",
    "Шифровый", "Кэшовый", "Рандомный", "Жирный", "Турбо", "Сольный", "Сетевой", "Слепой", "Гладкий", "Честный", "Глючный", "Ставочный"
]

__GOOSE_NAME_SECOND = [
    "Гусь", "Алгоритм", "Коммит", "Кряк", "Сниппет", "Слот", "Фрейм", "Токен", "Крякодром", "Пакет", "Джекпот",
    "Спин", "Крякбит", "Селектор", "Рендер", "Крякдилер", "Лут", "Кряктабель", "Контекст", "Логгер"
]


def generate_gooses(add_to: Casino,
                    count: int,
                    balance_range: tuple[int, int],
                    honk_chance: float,
                    war_chance: float,
                    honk_volume_range: tuple[int, int],
                    damage_range: tuple[int, int],
                    run_crush_chance: float):
    for i in range(count):
        actor_id = f"G_{i}"
        name = random.choice(__GOOSE_NAME_FIRST) + " " + random.choice(__GOOSE_NAME_SECOND)

        goose: Goose

        if random.random() < honk_chance:
            volume = random.randint(*honk_volume_range)
            goose = HonkGoose(actor_id, name, run_crush_chance, volume)

        elif random.random() < war_chance:
            damage = random.randint(*damage_range)
            goose = WarGoose(actor_id, name, run_crush_chance, damage)

        else:
            goose = Goose(actor_id, name, run_crush_chance)

        balance = random.randint(*balance_range)
        add_to.register_actor(goose, Chips(balance))
