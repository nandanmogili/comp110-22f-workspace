"""An Example of vectorized operations via operator overloading."""

from __future__ import annotations
from typing import Union  # TYPO CHECK YOURS


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items
    
    def __repr__(self) -> str:
        return f"StrArray({self.items})"
    
    def __add__(self, rhs: str) -> StrArray:
        result: StrArray = StrArray([])
        if isinstance(rhs, str):
            for item in self.items:
                result.items.append(item + rhs)
        else:
            assert len(self.items) == len(rhs.items)
            for i in range(len(self.items)):
                result.items.append(self.items[i] + rhs.items[i])
        return result

a: StrArray = StrArray(["Armando", "Pete", "Leaky"])
b: StrArray = StrArray(["Bacot", "Nance", "Black"])
print(a)
print(a + "!")
print(a)
print(b + ", " + a +  "!!!")