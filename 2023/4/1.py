import re

scratch_cards = open("puzzle.txt").read().splitlines()

# Part 1
total = 0
for card in scratch_cards:
    [winning, staked] = map(
        lambda l: re.findall(r"\d+", l), str.split(card, ":")[1].split(" | ")
    )
    winning = set(winning)
    # print(winning, staked)
    won = 0
    for number in staked:
        if not number in winning:
            continue
        else:
            won = won + 1 if not won else won * 2
    print(f"{card} => {won}")
    total += won

print(f"Day 4, Part 1: {total=}")
