"""Example of writing a test subject."""

def sum(xs: list[float]) -> float:
    """Computes the sum of a list"""
    # if len(xs) == 0.0:
    #     return 0.0
    # else:
    #     return xs[0]
    total: float = 0.0
    i: int = 0
    while i < len(xs):
        total += xs[i]
        i += 1
    return total
