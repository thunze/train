from train.math import add


def test_add() -> None:
    """Positive and negative tests for the add function."""
    assert add(1, 2) == 3
    assert add(5, -3) == 2
