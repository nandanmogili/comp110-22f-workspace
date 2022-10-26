"""Unit Tests for Dictionary Functions."""
__author__: str = "730573354"
from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count


def test_invert_use1() -> None:
    """Test with different values, should switch key and value."""
    a: dict[str, str] = {"hi": "bye", "hola": "ciao"}
    assert invert(a) == {"bye": "hi", "ciao": "hola"}


def test_invert_use2() -> None:
    """Test with different values, should switch key and value."""
    a: dict[str, str] = {"Nandan": "Mogili", "Kris": "Jordan", "Krish": "Singhvi"}
    assert invert(a) == {"Mogili": "Nandan", "Jordan": "Kris", "Singhvi": "Krish"}


def test_invert_empty() -> None:
    """Test with empty input."""
    a: dict[str, str] = {"Nandan": "Mogili"}
    assert invert(a) == {"Mogili": "Nandan"}


def test_favorite_color_use1() -> None:
    """Test with 3 keys and 3 values."""
    a: dict[str, str] = {"Nandan": "Blue", "Kris": "Black", "Krish": "Blue"}
    assert favorite_color(a) == ("Blue")


def test_favorite_color_use2() -> None:
    """Test with 5 keys and 5 values."""
    a: dict[str, str] = {"Nandan": "Yellow", "Kris": "Yellow", "Krish": "Red", "Josh": "Red", "Christopher": "Blue"}
    assert favorite_color(a) == ("Yellow")


def test_favorite_color_empty() -> None:
    """Test with empty input."""
    a: dict[str, str] = {}
    assert favorite_color(a) == ("")


def test_count_empty() -> None:
    """Test with no values."""
    a = []
    assert count(a) == {}


def test_count_use1() -> None:
    """Test the count function with 3 different colors."""
    a: list[str] = ["a", "b", "c"]
    assert count(a) == {"a": 1, "b": 1, "c": 1}


def test_count_use2() -> None:
    """Test the count function."""
    a: list[str] = ["w"]
    assert count(a) == {"w": 1}