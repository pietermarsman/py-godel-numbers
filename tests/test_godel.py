from py_godel_numbers import godelize


def test_godelize_type() -> None:
    assert isinstance(godelize("0"), int)


def test_godelize_not() -> None:
    assert godelize("~") == 1
