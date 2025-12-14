import pytest
from src.goose import Goose, HonkGoose, WarGoose
from src.goose_collections import (
    GooseCollection,
    GooseIncome,
    HonkGooseCollection,
    WarGooseCollection,
)


def test_goose_collection_add_and_len():
    c = GooseCollection()
    g1 = Goose("A")
    g2 = Goose("B")

    c.add(g1)
    c.add(g2)

    assert len(c) == 2


def test_goose_collection_add_wrong_type_raises():
    c = GooseCollection()

    with pytest.raises(TypeError):
        c.add("not a goose")


def test_goose_collection_remove():
    c = GooseCollection()
    g = Goose("A")

    c.add(g)
    c.remove(g)

    assert len(c) == 0


def test_goose_collection_remove_missing_raises():
    c = GooseCollection()
    g = Goose("A")

    with pytest.raises(ValueError):
        c.remove(g)


def test_goose_collection_iteration():
    c = GooseCollection()
    geese = [Goose("A"), Goose("B"), Goose("C")]

    for g in geese:
        c.add(g)

    assert list(iter(c)) == geese


def test_goose_collection_indexing_and_slicing():
    c = GooseCollection()
    geese = [Goose(str(i)) for i in range(5)]

    for g in geese:
        c.add(g)

    assert c[0] is geese[0]
    assert c[1:4] == geese[1:4]
    assert isinstance(c[1:4], list)


def test_goose_collection_add_operator():
    c1 = GooseCollection()
    c2 = GooseCollection()

    g1 = Goose("A")
    g2 = Goose("B")

    c1.add(g1)
    c2.add(g2)

    c3 = c1 + c2

    assert isinstance(c3, GooseCollection)
    assert list(c3) == [g1, g2]


def test_goose_collection_add_operator_wrong_type():
    c = GooseCollection()

    assert c.__add__(123) is NotImplemented


def test_war_goose_collection_add_and_total_strength():
    c = WarGooseCollection()
    g1 = WarGoose("A", 10)
    g2 = WarGoose("B", 5)

    c.add(g1)
    c.add(g2)

    assert len(c) == 2
    assert c.total_strength == 15


def test_war_goose_collection_add_wrong_type_raises():
    c = WarGooseCollection()

    with pytest.raises(TypeError):
        c.add(Goose("weak"))


def test_war_goose_collection_remove_updates_strength():
    c = WarGooseCollection()
    g = WarGoose("A", 10)

    c.add(g)
    c.remove(g)

    assert len(c) == 0
    assert c.total_strength == 0


def test_honk_goose_collection_add_and_total_volume():
    c = HonkGooseCollection()
    g1 = HonkGoose("A", 3)
    g2 = HonkGoose("B", 7)

    c.add(g1)
    c.add(g2)

    assert len(c) == 2
    assert c.total_honk_volume == 10


def test_honk_goose_collection_add_wrong_type_raises():
    c = HonkGooseCollection()

    with pytest.raises(TypeError):
        c.add(Goose("silent"))


def test_honk_goose_collection_remove_updates_volume():
    c = HonkGooseCollection()
    g = HonkGoose("A", 4)

    c.add(g)
    c.remove(g)

    assert len(c) == 0
    assert c.total_honk_volume == 0


def test_goose_income_set_get_and_overwrite():
    income = GooseIncome()
    g = Goose("A")

    income[g] = 100
    income[g] = 150

    assert income[g] == 150


def test_goose_income_add():
    income = GooseIncome()
    g = Goose("A")

    income.add(g, 50)
    income.add(g, 25)

    assert income[g] == 75


def test_goose_income_get_unknown_raises():
    income = GooseIncome()
    g = Goose("A")

    with pytest.raises(KeyError):
        _ = income[g]


def test_goose_income_pop_existing_and_missing():
    income = GooseIncome()
    g = Goose("A")

    income[g] = 42

    assert income.pop(g) == 42
    assert income.pop(g) == 0


def test_goose_income_len_and_iteration():
    income = GooseIncome()
    g1 = Goose("A")
    g2 = Goose("B")

    income[g1] = 10
    income[g2] = 20

    assert len(income._income) == 2
    assert set(income._income.keys()) == {g1, g2}
