import pytest
from src.goose import Goose, HonkGoose, WarGoose
from src.goose_ocg import GooseOCG


def test_unite_creates_new_ocg_for_two_single_geese():
    g1 = Goose("A")
    g2 = Goose("B")

    ocg = GooseOCG.unite(g1, g2)

    assert isinstance(ocg, GooseOCG)
    assert g1.ocg is ocg
    assert g2.ocg is ocg


def test_unite_adds_second_goose_to_existing_ocg():
    g1 = Goose("A")
    g2 = Goose("B")
    g3 = Goose("C")

    ocg = GooseOCG.unite(g1, g2)
    same_ocg = GooseOCG.unite(g1, g3)

    assert ocg is same_ocg
    assert g3.ocg is ocg


def test_unite_same_goose_raises():
    g = Goose("A")

    with pytest.raises(ValueError):
        GooseOCG.unite(g, g)


def test_unite_second_goose_already_in_ocg_raises():
    g1 = Goose("A")
    g2 = Goose("B")
    g3 = Goose("C")

    GooseOCG.unite(g1, g2)

    with pytest.raises(ValueError):
        GooseOCG.unite(g3, g2)


def test_add_goose_sets_ocg():
    ocg = GooseOCG()
    g = Goose("A")

    ocg.add_goose(g)

    assert g.ocg is ocg


def test_add_goose_twice_raises():
    ocg = GooseOCG()
    g = Goose("A")

    ocg.add_goose(g)

    with pytest.raises(ValueError):
        ocg.add_goose(g)


def test_add_war_goose_updates_collections_and_strongest():
    ocg = GooseOCG()
    g1 = WarGoose("A", 5)
    g2 = WarGoose("B", 10)

    ocg.add_goose(g1)
    ocg.add_goose(g2)

    assert ocg.war_geese.total_strength == 15
    assert ocg.strongest_war is g2


def test_add_honk_goose_updates_collections_and_loudest():
    ocg = GooseOCG()
    g1 = HonkGoose("A", 3)
    g2 = HonkGoose("B", 7)

    ocg.add_goose(g1)
    ocg.add_goose(g2)

    assert ocg.honk_geese.total_honk_volume == 10
    assert ocg.loudest_honk is g2
