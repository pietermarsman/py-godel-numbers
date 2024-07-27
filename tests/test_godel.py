import pytest
from py_godel_numbers import godelize, degodelize

TEST_CASES = [
    (1, "~"),
    (2, "V"),
    (3, "⊃"),
    (4, "∃"),
    (5, "="),
    (6, "0"),
    (7, "s"),
    (8, "("),
    (9, ")"),
    (10, ","),
    (11, "+"),
    (12, "*"),
    (13, "x"),
    (17, "y"),
    (19, "z"),
    (13**2, "p"),
    (17**2, "q"),
    (19**2, "r"),
    (13**3, "P"),
    (17**3, "Q"),
    (19**3, "R"),
    (243000000, "0=0"),
    (18296772480000000, "x=s0"),
    (
        172225505803959398742621651659678877886965404082311908389214945877004912002249920215937500000000,
        "(∃x)(x=sy)",
    ),
]


@pytest.mark.parametrize(("godel_number", "theorem"), TEST_CASES)
def test_godelize(godel_number: int, theorem: str) -> None:
    assert godelize(theorem) == godel_number


@pytest.mark.parametrize(("godel_number", "theorem"), TEST_CASES)
def test_degodelize(godel_number: int, theorem: str) -> None:
    assert degodelize(godel_number) == theorem


@pytest.mark.parametrize(("godel_number", "theorem"), TEST_CASES)
def test_degodelize_godelize(godel_number: int, theorem: str) -> None:
    assert degodelize(godelize(theorem)) == theorem
