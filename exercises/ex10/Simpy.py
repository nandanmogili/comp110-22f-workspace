"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730573354"


class Simpy:
    """Class Constructor with all its methods."""
    values: list[float]
    # TODO: Your constructor and methods will go here.

    def __init__(self, values: list[float]):
        """Constructor for the Simpy Class."""
        self.values = values

    def __repr__(self) -> str:
        """Produces a Str Representation of the Simpy Class."""
        return f"Simpy({self.values})"
    
    def fill(self, input: float, multiple: int) -> None:
        """Fills Simpy's values with a value a number of times."""
        result: list[float] = []
        index: int = 0
        while index < multiple:
            result.append(input)
            index += 1
        self.values = result
    
    def arange(self, start: int, stop: int, step: float = 1.0) -> None:
        """Method that arranges values in the values of a Simpy Class."""
        result = list[float] = [start]
        before: float = start
        if step == 0.0:
            raise IndexError("Error: Invalid Step Value")
        elif step != 0.0:
            while stop != before + step:
                result.append(before + step)
                before += step
        self.values = result
    
    def sum(self) -> float:
        """Overloads itself in order to find the sum of Simpy's values."""
        total: float = sum(self.values)
        return total
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds all the float values by overloading the addition operator."""
        result = list[float] = []
        index: int = 0
        if isinstance(rhs, float):
            for i in self.values:
                result.append(i + rhs)
        elif len(self.values) == len(rhs.values):
            while index < len(self.values):
                result.append(self.values[index] + rhs.values[index])
                index += 1
        else:
            raise IndexError
        return Simpy(result)
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Puts all the values of a Simpy to a power by overloading the power operator."""
        result = list[float] = []
        index: int = 0
        if isinstance(rhs, float):
            for i in self.values:
                result.append(i ** rhs)
        elif len(self.values) == len(rhs.values):
            while index < len(self.values):
                result.append(self.values[index] ** rhs.values[index])
                index += 1
        else:
            raise IndexError
        return Simpy(result)
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Method that overloads the equals sign operator."""
        result: list[bool] = []
        index: int = 0
        if isinstance(rhs, Simpy):
            for i in self.values:
                result.append(i == rhs)
        elif len(self.values) == len(rhs.values):

            while index < len(self.values):

                result.append(self.values[index] == rhs.values[index])
                index += 1
        else:
            raise IndexError
        return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Method that overloads the greater than operator."""
        result: list[bool] = []
        index: int = 0
        if isinstance(rhs, float):
            for i in self.values:
                result.append(i > rhs)

        elif len(self.values) == len(rhs.values):
            while index < len(self.values):
                result.append(self.values(index) > rhs.values[index])
                index += 1

        else:
            raise IndexError
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Method that overloads both operators together."""
        if isinstance(rhs, int):
            return self.values[rhs]

        else:
            result: list[float] = []
            index: int = 0
            while index < len(rhs):
                if rhs[index]:
                    result.append(self.values[index])
                index += 1
            return Simpy(result)