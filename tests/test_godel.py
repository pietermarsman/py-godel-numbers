from py_godel_numbers import godelize


def test_godelize_type() -> None:
    assert isinstance(godelize("0"), int)
