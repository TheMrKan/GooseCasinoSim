import logging

from src.entities.chips import Chips


logger = logging.getLogger("BalanceCollection")


class BalanceCollection:
    __balances: dict[str, Chips]

    def __init__(self):
        self.__balances = {}

    def __getitem__(self, item: str):
        return self.__balances[item]

    def __setitem__(self, key: str, value: Chips):
        old_value = self.__balances.get(key, 0)
        self.__balances[key] = value
        logger.debug("Balance %s: %s -> %s", key, old_value, value)

    def __contains__(self, item: str):
        return item in self.__balances.keys()

    def __len__(self):
        return len(self.__balances)

    def __iter__(self):
        return iter(self.__balances.items())
