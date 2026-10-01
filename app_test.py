from app import additionner


def test_addition_entiers():
    assert additionner(2, 3) == 5


def test_addition_nombres_negatifs():
    assert additionner(-2, -3) == -5




