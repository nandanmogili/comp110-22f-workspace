"""Exercise 5 List Utility Functions!"""
__author__: str = "730573354"


def only_evens(a: list[int]) -> list[int]:
    """Takes all the even values in a list."""
    result: list[int] = list()
    for val in a:
        if val % 2 == 0:
            result.append(val)
    return result


def concat(a: list[int], b: list[int]) -> list[int]:
    """Takes the values in the second list and appends them to the end of the first list."""
    c: list[int] = []
    for num in a:
        c.append(num)
    for num in b:
        c.append(num)
    return c


def sub(a: list[int], start: int, end: int) -> list[int]:
    """Takes a list and the start and end index to make a new list."""
    result: list[int] = []
    if start < 0:
        start = 0
    if end > len(a):
        end = len(a)
    if len(a) == 0:
        return result
    if start > len(a):
        return result
    if end <= 0:
        return result
    i: int = start
    while i < end:
        result.append(a[i])
        i += 1
    return result