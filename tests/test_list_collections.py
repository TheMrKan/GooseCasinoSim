import pytest

from src.entities.actor import Actor
from src.list_collections import GooseCollection, PlayerCollection, GenericActorCollection
from src.entities.goose import Goose
from src.entities.player import Player
from src.exceptions import SimulationException


class TestGenericCollection:
    def setup_method(self):
        self.player_a = Player("A")
        self.player_b = Player("B")
        self.empty = GenericActorCollection()
        self.players = GenericActorCollection([self.player_a, self.player_b])

    def test_len(self):
        assert len(self.empty) == 0
        assert len(self.players) == 2

    def test_bool(self):
        assert not self.empty
        assert self.players

    def test_add(self):
        self.empty.add(Player("X"))
        assert len(self.empty) == 1
        assert self.empty[0].actor_id == "X"

    def test_remove(self):
        self.players.remove(self.player_b)
        assert len(self.players) == 1

    def test_getitem(self):
        assert self.players[0] == self.player_a
        assert self.players[1] == self.player_b

    def test_iter(self):
        assert list(self.players) == [self.player_a, self.player_b]

    def test_random_one(self):
        p = self.players.random_one()
        assert p in self.players

    def test_random_empty(self):
        with pytest.raises(ValueError, match="empty"):
            self.empty.random_one()


class TestGooseCollection:

    def setup_method(self):
        Actor.__str__ = lambda a: a.actor_id
        self.goose_a = Goose("A", "Name", 1)
        self.goose_b = Goose("B", "Name", 1)
        self.goose_c = Goose("C", "Name", 1)

    def test_str_single(self):
        col = GooseCollection([self.goose_a])
        assert str(col) == f"[{{{self.goose_a}}}]"

    def test_str_group(self):
        self.goose_a += self.goose_b
        col = GooseCollection([self.goose_a, self.goose_b])
        assert str(col) == f"[{{{self.goose_a}, {self.goose_b}}}]"

    def test_str_mixed(self):
        self.goose_a += self.goose_b
        col = GooseCollection([self.goose_a, self.goose_b, self.goose_c])
        assert str(col) in (f"[{{{self.goose_a}, {self.goose_b}}}, {{{self.goose_c}}}]",
                            f"[{{{self.goose_b}, {self.goose_a}}}, {{{self.goose_c}}}]")


class TestPlayerCollection:
    def test_remove_last(self):
        player = Player("A")
        col = PlayerCollection([player])
        with pytest.raises(SimulationException):
            col.remove(player)

    def test_remove_ok(self):
        col = PlayerCollection([Player("A"), Player("B")])
        col.remove(col[0])
        assert len(col) == 1
