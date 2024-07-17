import functools
from dataclasses import dataclass
from typing import Dict


@dataclass
class Config:
    constants: Dict[str, int]

    @classmethod
    def default(cls) -> "Config":
        return cls(
            constants={
                "~": 1,
                "V": 2,
                "⊃": 3,
                "∃": 4,
                "=": 5,
                "0": 6,
                "s": 7,
                "(": 8,
                ")": 9,
                ",": 10,
                "+": 11,
                "x": 12,
            }
        )

    @functools.cached_property
    def max_constant(self) -> int:
        return max(self.constants.values())

    @functools.cached_property
    def reverse_constants(self) -> Dict[int, str]:
        return {v: k for k, v in self.constants.items()}
