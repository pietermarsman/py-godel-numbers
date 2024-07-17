import pytest

from py_godel_numbers import godelize, degodelize


def test_godelize_type() -> None:
    assert isinstance(godelize("0"), int)


@pytest.mark.parametrize(
    ("godel_number", "constant"),
    enumerate(["~", "V", "⊃", "∃", "=", "0", "s", "(", ")", ",", "+", "*"], 1),
)
def test_godelize_constants(godel_number: int, constant: str) -> None:
    assert godel_number == godelize(constant)


@pytest.mark.parametrize(
    ("godel_number", "variable"),
    [
        (13, "x"),
        (17, "y"),
        (19, "z"),
        (13**2, "p"),
        (17**2, "q"),
        (19**2, "r"),
        (13**3, "P"),
        (17**3, "Q"),
        (19**3, "R"),
    ],
)
def test_godelize_variables(godel_number: int, variable: str) -> None:
    assert godel_number == godelize(variable)


@pytest.mark.parametrize(
    ("godel_number", "constant"),
    enumerate(["~", "V", "⊃", "∃", "=", "0", "s", "(", ")", ",", "+", "*"], 1),
)
def test_degodelize_constants(godel_number: int, constant: str) -> None:
    assert constant == degodelize(godel_number)
