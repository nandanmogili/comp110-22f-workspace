"""Testing my Utility Functions!"""
__author__: str = "730573354"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import concat
from exercises.ex05.utils import sub


def test_only_evens_use1() -> None:
    """Test with 6 numbers."""
    a: list[int] = [1, 2, 4, 5, 8, 9]
    assert only_evens(a) == [2, 4, 8]


def test_only_evens_use2() -> None:
    """Test with random numbers with some repeating."""
    a: list[int] = [3, 3, 3, 4, 15, 16, 20, 40, 80]
    assert only_evens(a) == [4, 16, 20, 40, 80]


def test_only_evens_edge_all_odd() -> None:
    """Test with no even numbers."""
    a: list[int] = [1, 3, 5, 7]
    assert only_evens(a) == []


def test_concat_use1() -> None:
    """Test with sequential numbers, should combine lists."""
    a: list[int] = [1, 2, 3, 4]
    b: list[int] = [5, 6, 7, 8]
    assert concat(a, b) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_concat_use2() -> None:
    """Test with two values in each list, should combine lists."""
    a: list[int] = [3, 4]
    b: list[int] = [1, 2]
    assert concat(a, b) == [3, 4, 1, 2]


def test_concat_edge_empty_list() -> None:
    """Test with no value in second list, should combine still."""
    a: list[int] = [5, 6]
    b: list[int] = []
    assert concat(a, b) == [5, 6]


def test_sub_use1() -> None:
    """Tests with a list and indexes of 2 and 4."""
    a: list[int] = [1, 2, 3, 4, 5, 6, 7]
    start: int = 2
    end: int = 4
    assert sub(a, start, end) == [3, 4]


def test_sub_use2() -> None:
    """Tests with a list and indexes of 1 and 4."""
    a: list[int] = [5, 6, 7, 8, 9]
    start: int = 1
    end: int = 4
    assert sub(a, start, end) == [6, 7, 8]


def test_sub_edge_invalid_parameters() -> None:
    """Tests with a list, with a negative starting index and an ending index that is greater than length."""
    a: list[int] = [2, 3, 5, 6, 7, 9]
    start: int = -2
    end: int = 7
    assert sub(a, start, end) == [2, 3, 5, 6, 7, 9]