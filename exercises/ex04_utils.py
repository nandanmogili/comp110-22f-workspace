"""Exercise 04 'list' utility functions."""
__author__: str = "730573354"


def all(a: list[int], b: int) -> bool:
    """Checks if a number is at every index of a list."""
    i: int = 0
    if len(a) == 0:  # if the length is 0, returns false
        return False
    status: bool = True  # the list starts as right and if a single value is wrong it changes
    while len(a) > i:
        if a[i] != b:  # if even one index doesnt match the integer the status is false
            status = False
        i += 1
    return status


def max(input: list[int]) -> int:
    """Finds the maximum value in a list of integers."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    top_value: int = input[0]  # makes the first value to starting top value
    i: int = 0
    while i < len(input):  # iterates through the list
        if input[i] > top_value:  # if the value is larger than the current top value, it becomes the top value
            top_value = input[i]
        i += 1
    return top_value  # returns the largest value


def is_equal(a: list[int], b: list[int]) -> bool:
    """Checks if every value in two lists are the same regardless of length."""
    if len(a) != len(b):  # if the length differs, returns false 
        return False
    counter = 0
    while counter < len(a):  # loops based on the number of values in the list
        if a[counter] == b[counter]:
            counter += 1
        else:
            return False  # if a single term doesnt match its respective term then it should return false
    return True