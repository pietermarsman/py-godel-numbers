import pytest

from py_godel_numbers import godelize, degodelize


def test_godelize_type() -> None:
    assert isinstance(godelize("0"), int)


@pytest.mark.parametrize(
    ("godel_number", "constant"),
    enumerate(["~", "V", "⊃", "∃", "=", "0", "s", "(", ")", ",", "+", "*"], 1),
)
def test_godelize_constants(godel_number: int, constant: str) -> None:
    assert godelize(constant) == godel_number


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
    assert godelize(variable) == godel_number


@pytest.mark.parametrize(
    ("godel_number", "statement"), [(243000000, "0=0"), (18296772480000000, "x=s0")]
)
def test_godelize_theorem(godel_number: int, statement: str) -> None:
    assert godelize(statement) == godel_number


@pytest.mark.parametrize(
    ("godel_number", "constant"),
    enumerate(["~", "V", "⊃", "∃", "=", "0", "s", "(", ")", ",", "+", "*"], 1),
)
def test_degodelize_constants(godel_number: int, constant: str) -> None:
    assert degodelize(godel_number) == constant


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
def test_degodelize_variables(godel_number: int, variable: str) -> None:
    assert degodelize(godel_number) == variable


@pytest.mark.parametrize(
    ("godel_number", "statement"), [(243000000, "0=0"), (18296772480000000, "x=s0")]
)
def test_degodelize_statement(godel_number: int, statement: str) -> None:
    assert degodelize(godel_number) == statement


@pytest.mark.parametrize(
    "statement",
    [
        "~",
        "V",
        "⊃",
        "∃",
        "=",
        "0",
        "s",
        "(",
        ")",
        ",",
        "+",
        "*",
        "x",
        "y",
        "z",
        "p",
        "q",
        "r",
        "P",
        "Q",
        "R",
    ],
)
def test_degodelize_godelize(statement: str) -> None:
    assert degodelize(godelize(statement)) == statement
