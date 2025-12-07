from src.entities.chips import Chips


class BalanceCollection:
    __balances: dict[str, Chips]

    default_balance: Chips

    def __init__(self, default_balance: Chips):
        self.__balances = {}
        self.default_balance = default_balance

    def __getitem__(self, item: str):
        if item not in self:
            return self.default_balance
        return self.__balances[item]

    def __setitem__(self, key: str, value: Chips):
        self.__balances[key] = value

    def __contains__(self, item: str):
        return item in self.__balances.keys()

    def __len__(self):
        return len(self.__balances)

    def __iter__(self):
        return iter(self.__balances.items())
