from typing import Generator


def primes() -> Generator[int, None, None]:
    p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    yield from p

    i = 31
    while True:
        if any(i % p == 0 for p in p):
            i += 2
        else:
            yield i
            p.append(i)
