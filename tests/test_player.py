from src.player import Player


def test_initial_state():
    p = Player("Игрок1", 100)

    assert p.name == "Игрок1"
    assert p.balance == 100
    assert p.panic_level == 0
    assert p.is_dead is False


def test_adjust_panic_increase():
    p = Player("Игрок1", 100)

    p.adjust_panic(5)
    assert p.panic_level == 5


def test_adjust_panic_lower_bound():
    p = Player("Игрок1", 100)

    p.adjust_panic(-10)
    assert p.panic_level == 0


def test_adjust_panic_upper_bound():
    p = Player("Игрок1", 100)

    p.adjust_panic(100)
    assert p.panic_level == 20


def test_take_money_partial():
    p = Player("Игрок1", 100)

    taken = p.take_money(30)

    assert taken == 30
    assert p.balance == 70
    assert p.is_dead is False


def test_take_money_all_and_die():
    p = Player("Игрок1", 50)

    taken = p.take_money(100)

    assert taken == 50
    assert p.balance == 0
    assert p.is_dead is True


def test_lose_chance_depends_on_panic():
    p = Player("Игрок1", 100)

    assert p.lose_chance() == 0.6

    p.adjust_panic(10)
    assert p.lose_chance() == 0.6 + 10 * 0.02


def test_repr_contains_state():
    p = Player("Игрок1", 100)

    text = repr(p)

    assert "Игрок1" in text
    assert "balance=100" in text
    assert "panic=0" in text
    assert "dead=False" in text
