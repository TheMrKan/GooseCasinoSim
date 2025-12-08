from src.dict_collections import BalanceCollection
from src.entities.chips import Chips


class TestBalanceCollection:
    def test_add(self):
        collection = BalanceCollection()
        collection["player1"] = Chips(100)

        assert "player1" in collection
        assert collection["player1"] == Chips(100)

    def test_update(self):
        collection = BalanceCollection()
        collection["player1"] = Chips(100)
        collection["player1"] = Chips(150)

        assert collection["player1"] == Chips(150)

    def test_contains(self):
        collection = BalanceCollection()
        collection["player1"] = Chips(100)

        assert "player1" in collection
        assert "player2" not in collection

    def test_len(self):
        collection = BalanceCollection()
        assert len(collection) == 0

        collection["player1"] = Chips(100)
        assert len(collection) == 1

        collection["player2"] = Chips(200)
        assert len(collection) == 2

    def test_iteration(self):
        collection = BalanceCollection()
        collection["player1"] = Chips(100)
        collection["player2"] = Chips(200)

        items = list(collection)
        assert ("player1", Chips(100)) in items
        assert ("player2", Chips(200)) in items
        assert len(items) == 2
