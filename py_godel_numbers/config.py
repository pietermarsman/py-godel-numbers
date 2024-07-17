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
