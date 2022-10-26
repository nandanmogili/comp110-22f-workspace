"""Functions that change the values in a Dictionary."""
__author__: str = "730573354"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts the values and keys in a dictionary."""
    result: dict[str, str] = {}
    for key in a:
        if a[key] in result:
            raise KeyError("Key Error!!")
        result[a[key]] = key
    return result


def favorite_color(colors: dict[str, str]) -> str:
    """Returns most frequent color in a dictionary."""
    all_colors: list[str] = []
    
    curr: int = 0 
    stored: int = 0
    #  Each color and the result
    color: str = ""
    result: str = ""

    for key in colors:
        all_colors.append(colors[key])
    a: int = 0
    b: int = 0
    while b < len(all_colors):
        color = all_colors[b]

        while a < len(all_colors):
            if (all_colors[a] == color):
                curr += 1

            if (curr > stored):
                stored = curr
                result = all_colors[b]

            a += 1
        curr = 0
        a = 0
        b += 1
    return result


def count(input_list: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in a list."""
    result: dict[str, int] = {}
    a: int = 0
    b: int = 0
    counter: int = 0
    value: str = ""

    while (b < len(result)):
        value = input_list[b]
        while a < len(input_list):
            if (input_list[a] == value):
                counter += 1
            a += 1
        result[input_list[b]] = counter
        counter = 0
        a = 0
        b += 1
    return result