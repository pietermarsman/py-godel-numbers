from itertools import repeat
from math import prod
from typing import Optional, Sequence

from py_godel_numbers import Config
from py_godel_numbers.arithmetic import power, factorize
from py_godel_numbers.primes import primes


class GodelizeException(ValueError):
    pass


class DegodelizeException(ValueError):
    pass


def godelize(s: str, config: Optional[Config] = None) -> int:
    if config is None:
        config = Config.default()

    if len(s) == 0:
        raise GodelizeException("Cannot Gödelize empty statement")

    if len(s) == 1:
        return config.characters.get(s[0], 0)

    def godelize_sequence(s: Sequence[str], config: Config) -> int:
        exponents = list(map(godelize, s, repeat(config)))
        powers = list(map(power, primes(), exponents))
        n = prod(powers)
        return n

    if "\n" in s:
        return godelize_sequence(s.split("\n"), config)

    return godelize_sequence(list(s), config)


def degodelize(n: int, config: Optional[Config] = None) -> str:
    if config is None:
        config = Config.default()

    if n < config.min_godel_number:
        raise DegodelizeException(f"Cannot de-Gödelize {n}")

    if n in config.godel_numbers:
        return config.godel_numbers[n]

    prime_counts = [c for _, c in sorted(factorize(n).items())]

    ss = list(map(degodelize, prime_counts, repeat(config)))
    if any(len(s) > 1 for s in ss):
        return "\n".join(ss)

    return "".join(ss)
