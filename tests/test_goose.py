from src.goose import Goose, HonkGoose, WarGoose
from src.player import Player


def test_goose_hash_and_eq():
    g1 = Goose("Гена")
    g2 = Goose("Гена")
    g3 = Goose("Вася")

    assert g1 == g2
    assert g1 != g3
    assert hash(g1) == hash(g2)


def test_goose_repr_returns_name():
    g = Goose("Гусь")

    assert repr(g) == "Гусь"


def test_goose_ocg_default_none():
    g = Goose("Гусь")

    assert g.ocg is None


def test_honk_goose_inherits_goose():
    g = HonkGoose("Крик", honk_volume=5)

    assert isinstance(g, Goose)
    assert g.honk_volume == 5


def test_honk_goose_honk_increases_panic():
    player = Player("Игрок", balance=100)
    goose = HonkGoose("Honk", honk_volume=3)

    goose.honk(player)

    assert player.panic_level == 3


def test_honk_goose_multiple_honks_stack():
    player = Player("Игрок", balance=100)
    goose = HonkGoose("Honk", honk_volume=2)

    goose.honk(player)
    goose.honk(player)

    assert player.panic_level == 4


def test_war_goose_inherits_goose():
    g = WarGoose("War", strength=4)

    assert isinstance(g, Goose)
    assert g.strength == 4


def test_war_goose_attack_reduces_balance():
    player = Player("Игрок", balance=100)
    goose = WarGoose("War", strength=5)

    stolen = goose.attack(player)

    assert stolen > 0
    assert player.balance == 100 - stolen


def test_war_goose_attack_returns_taken_amount():
    player = Player("Игрок", balance=200)
    goose = WarGoose("War", strength=1)

    stolen = goose.attack(player)

    assert isinstance(stolen, int)
    assert stolen >= 0


def test_war_goose_attack_with_high_panic():
    player = Player("Игрок", balance=100)
    player.adjust_panic(20)
    goose = WarGoose("War", strength=10)

    stolen = goose.attack(player)

    assert stolen == 90
    assert player.balance == 10
