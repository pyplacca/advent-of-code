import re
import operator
import functools
from utils import find_ways_to_win


# Part 1
races = list(
    zip(
        *map(
            lambda l: map(int, re.findall(r"\d+", l)),
            open("puzzle.txt").read().splitlines(),
        )
    )
)
# print(races)

margins_of_error = list(map(lambda r: find_ways_to_win(*r), races))
# print(margins_of_error)
print("Day 6, Part 1: ", functools.reduce(operator.mul, margins_of_error))
