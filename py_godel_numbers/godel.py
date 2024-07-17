from typing import Optional

from py_godel_numbers import Config


def godelize(s: str, config: Optional[Config] = None) -> int:
    if config is None:
        config = Config()

    return 0


def degodelize(n: int, config: Optional[Config] = None) -> str:
    if config is None:
        config = Config()

    return ""
