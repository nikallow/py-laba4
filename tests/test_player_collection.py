import pytest
from src.player import Player
from src.player_collection import PlayerCollection


def test_add_player():
    pc = PlayerCollection()
    p = Player("Ваня", 100)

    pc.add(p)

    assert len(pc) == 1
    assert pc[0] is p


def test_add_duplicate_player_raises():
    pc = PlayerCollection()
    p = Player("Ваня", 100)

    pc.add(p)

    with pytest.raises(ValueError):
        pc.add(p)


def test_iteration():
    pc = PlayerCollection()
    players = [
        Player("Ваня", 100),
        Player("Петя", 50),
        Player("Игорь", 30),
    ]

    for p in players:
        pc.add(p)

    assert list(pc) == players


def test_indexing_and_slicing():
    pc = PlayerCollection()
    players = [Player(str(i), 100) for i in range(5)]

    for p in players:
        pc.add(p)

    assert pc[0] is players[0]
    assert pc[1:4] == players[1:4]


def test_alive_filters_dead_players():
    pc = PlayerCollection()
    p1 = Player("Ваня", 100)
    p2 = Player("Петя", 0)
    p3 = Player("Игорьб", 50)

    p2.is_dead = True

    pc.add(p1)
    pc.add(p3)

    assert pc.alive() == [p1, p3]


def test_getitem_out_of_range():
    pc = PlayerCollection()

    with pytest.raises(IndexError):
        _ = pc[0]
