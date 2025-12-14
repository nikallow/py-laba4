import pytest
from src.goose import Goose
from src.goose_income import GooseIncome


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
