import pytest

from src.entities.chips import Chips, NotEnoughChipsError


class TestChips:
    def test_basic(self):
        chips = Chips(100)
        assert chips.amount == 100

    def test_eq(self):
        assert Chips(1) == Chips(1)

    def test_negative(self):
        with pytest.raises(NotEnoughChipsError):
            Chips(-1)

    def test_sum(self):
        a = Chips(100)
        b = Chips(50)
        result = a + b
        assert result == Chips(150)

    def test_sum_int(self):
        a = Chips(100)
        result = a + 50
        assert result == Chips(150)

    def test_sub(self):
        a = Chips(100)
        b = Chips(30)
        result = a - b
        assert result == Chips(70)

    def test_sub_int(self):
        a = Chips(100)
        result = a - 40
        assert result == Chips(60)

    def test_sub_negative(self):
        a = Chips(50)
        with pytest.raises(NotEnoughChipsError):
            a - 60

    def test_less(self):
        a = Chips(50)
        b = Chips(100)
        assert a < b

    def test_greater(self):
        a = Chips(100)
        b = Chips(50)
        assert a > b

    def test_str(self):
        chips = Chips(42)
        assert str(chips) == "42"
        assert repr(chips) == "42"
