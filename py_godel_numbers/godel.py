from typing import Optional

from py_godel_numbers import Config


def godelize(s: str, config: Optional[Config] = None) -> int:
    if config is None:
        config = Config.default()

    if len(s) == 0:
        return 0

    n = config.characters.get(s[0], 0)

    return n + godelize(s[1:], config)


def degodelize(n: int, config: Optional[Config] = None) -> str:
    if config is None:
        config = Config.default()

    if n in config.godel_numbers:
        return config.godel_numbers[n]

    return ""
