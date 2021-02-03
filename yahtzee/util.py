from random import randint


def roll(num_sides: int = 6) -> int:
    """Returns the result of rolling a fair die with a given number of sides."""

    return randint(1, num_sides)
