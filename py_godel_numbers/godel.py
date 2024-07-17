from typing import Optional

from py_godel_numbers import Config


def godelize(s: str, config: Optional[Config] = None) -> int:
    if config is None:
        config = Config.default()

    if len(s) == 0:
        return 0

    n = config.constants.get(s[0], 0)

    return n + godelize(s[1:])


def degodelize(n: int, config: Optional[Config] = None) -> str:
    if config is None:
        config = Config.default()

    if n <= config.max_constant:
        return config.reverse_constants[n]

    return ""
