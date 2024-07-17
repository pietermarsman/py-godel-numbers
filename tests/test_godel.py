import pytest

from py_godel_numbers import godelize


def test_godelize_type() -> None:
    assert isinstance(godelize("0"), int)


@pytest.mark.parametrize(
    ("godel_number", "constant"),
    enumerate(["~", "V", "⊃", "∃", "=", "0", "s", "(", ")", ",", "+", "x"], 1),
)
def test_godelize_constants(godel_number: int, constant: str) -> None:
    assert godelize(constant) == godel_number
