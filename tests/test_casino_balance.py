import pytest
from src.casino_balance import CasinoBalance
from src.player import Player


class Chip:
    def __init__(self, value: int):
        self.value = value

    def __add__(self, other):
        if not isinstance(other, Chip):
            return NotImplemented
        return Chip(self.value + other.value)


def test_register_player():
    balance = CasinoBalance()
    p = Player("Игрок1", 100)

    balance.register_player(p)

    assert len(balance) == 1
    assert balance[p].value == 0


def test_get_unregistered_player_raises():
    balance = CasinoBalance()
    p = Player("Игрок1", 100)

    with pytest.raises(KeyError):
        _ = balance[p]


def test_add_chips():
    balance = CasinoBalance()
    p = Player("Игрок1", 100)

    balance.register_player(p)
    balance.add(p, 10)
    balance.add(p, 5)

    assert balance[p].value == 15


def test_reset_player():
    balance = CasinoBalance()
    p = Player("Игрок1", 100)

    balance.register_player(p)
    balance.add(p, 20)
    balance.reset(p)

    assert balance[p].value == 0


def test_iteration_and_len():
    balance = CasinoBalance()
    p1 = Player("Игрок1", 100)
    p2 = Player("Игрок2", 100)

    balance.register_player(p1)
    balance.register_player(p2)

    assert set(balance) == {p1, p2}
    assert len(balance) == 2
