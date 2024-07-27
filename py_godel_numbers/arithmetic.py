from collections import Counter
from typing import Dict

from py_godel_numbers.primes import primes


class FactorizeException(ValueError):
    pass


def power(base: int, exponent: int) -> int:
    return int(pow(base, exponent))


def factorize(n: int) -> Dict[int, int]:
    if n < 0:
        raise FactorizeException(f"Cannot factorize negative number {n}")

    factors: Counter[int] = Counter[int]()
    while True:
        for factor in primes():
            if n % factor == 0:
                factors[factor] += 1
                n //= factor
                break

        if n == 1:
            return factors
