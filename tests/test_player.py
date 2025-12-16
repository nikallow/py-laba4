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


def test_steal_money_partial():
    p = Player("Игрок1", 100)

    stolen = p.steal_money(30)

    assert stolen == 30
    assert p.balance == 70
    assert p.is_dead is False


def test_steal_money_all_and_die():
    p = Player("Игрок1", 50)

    stolen = p.steal_money(100)

    assert stolen == 50
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


def test_pay_does_not_kill():
    p = Player("Игрок1", 50)

    paid = p.pay(100)

    assert paid == 50
    assert p.balance == 0
    assert p.is_dead is False


def test_receive_money():
    p = Player("Игрок1", 50)

    p.receive_money(30)

    assert p.balance == 80
    assert p.is_dead is False
