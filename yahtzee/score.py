def score_ones(dice: list[int]) -> int:
    """Scores the ones in the list of dice."""

    return sum(1 for n in dice if n == 1)


def score_twos(dice: list[int]) -> int:
    """Scores the twos in the list of dice."""

    return sum(2 for n in dice if n == 2)


def score_threes(dice: list[int]) -> int:
    """Scores the threes in the list of dice."""

    return sum(3 for n in dice if n == 3)


def score_fours(dice: list[int]) -> int:
    """Scores the fours in the list of dice."""

    return sum(4 for n in dice if n == 4)


def score_fives(dice: list[int]) -> int:
    """Scores the fives in the list of dice."""

    return sum(5 for n in dice if n == 5)


def score_sixes(dice: list[int]) -> int:
    """Scores the sixes in the list of dice."""

    return sum(6 for n in dice if n == 6)
