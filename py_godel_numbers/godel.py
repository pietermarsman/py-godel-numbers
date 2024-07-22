from itertools import repeat
from typing import Optional

from py_godel_numbers import Config
from py_godel_numbers.arithmetic import power
from py_godel_numbers.primes import primes


class GodelizeException(ValueError):
    pass


def godelize(s: str, config: Optional[Config] = None) -> int:
    if config is None:
        config = Config.default()

    if len(s) == 0:
        raise GodelizeException("Cannot Gödelize empty statement")

    if len(s) == 1:
        return config.characters.get(s[0], 0)

    exponents = list(map(godelize, iter(s), repeat(config)))
    powers = list(map(power, primes(), exponents))
    n = sum(powers)
    return n


def degodelize(n: int, config: Optional[Config] = None) -> str:
    if config is None:
        config = Config.default()

    if n in config.godel_numbers:
        return config.godel_numbers[n]

    return ""
