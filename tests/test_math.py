from train.math import add


def test_add() -> None:
    assert add(1, 2) == 3
    assert add(5, -3) == 2
