import functools
from dataclasses import dataclass
from typing import Dict


@dataclass
class Config:
    constants: Dict[str, int]
    numerical_variables: Dict[str, int]
    sentential_variables: Dict[str, int]
    predicate_variables: Dict[str, int]

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
                "*": 12,
            },
            numerical_variables={
                "x": 13,
                "y": 17,
                "z": 19,
            },
            sentential_variables={
                "p": 13**2,
                "q": 17**2,
                "r": 19**2,
            },
            predicate_variables={
                "P": 13**3,
                "Q": 17**3,
                "R": 19**3,
            },
        )

    @functools.cached_property
    def characters(self) -> Dict[str, int]:
        return {
            **self.constants,
            **self.numerical_variables,
            **self.sentential_variables,
            **self.predicate_variables,
        }

    @functools.cached_property
    def godel_numbers(self) -> Dict[int, str]:
        return {v: k for k, v in self.characters.items()}
