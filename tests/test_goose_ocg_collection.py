import pytest
from src.goose_ocg import GooseOCG
from src.goose_ocg_collection import GooseOCGCollection


def test_add_ocg_and_len():
    c = GooseOCGCollection()
    ocg1 = GooseOCG()
    ocg2 = GooseOCG()

    c.add(ocg1)
    c.add(ocg2)

    assert len(c) == 2


def test_add_wrong_type_raises():
    c = GooseOCGCollection()

    with pytest.raises(TypeError):
        c.add("not an ocg")


def test_remove_ocg():
    c = GooseOCGCollection()
    ocg = GooseOCG()

    c.add(ocg)
    c.remove(ocg)

    assert len(c) == 0


def test_remove_wrong_type_raises():
    c = GooseOCGCollection()

    with pytest.raises(TypeError):
        c.remove("not an ocg")


def test_remove_missing_ocg_raises_value_error():
    c = GooseOCGCollection()
    ocg = GooseOCG()

    with pytest.raises(ValueError):
        c.remove(ocg)


def test_iteration():
    c = GooseOCGCollection()
    ocgs = [GooseOCG() for _ in range(5)]

    for ocg in ocgs:
        c.add(ocg)

    assert list(c) == ocgs


def test_indexing_and_slicing():
    c = GooseOCGCollection()
    ocgs = [GooseOCG() for _ in range(5)]

    for ocg in ocgs:
        c.add(ocg)

    assert c[0] is ocgs[0]
    assert c[1:4] == ocgs[1:4]
    assert isinstance(c[1:4], list)


def test_getitem_out_of_range():
    c = GooseOCGCollection()

    with pytest.raises(IndexError):
        _ = c[0]
