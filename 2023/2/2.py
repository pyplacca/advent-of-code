import functools
import operator


record = open("puzzle.txt", "r").read().splitlines()

powers = 0

for game in record:
    [_, game_set] = game.split(":")
    cubes = {}

    for game_round in game_set.split(";"):
        for s in game_round.split(","):
            [count, color] = s.strip().split(" ")
            cubes[color] = max(cubes.get(color, int(count)), int(count))

    # print(_, cubes)
    powers += functools.reduce(operator.mul, cubes.values(), 1)

print(f"Day 2, Part 2: {powers=}")
