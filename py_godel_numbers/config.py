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
            }
        )
