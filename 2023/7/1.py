from utils import CamelCard

# Part 1
camel_cards = list(map(lambda l: l.split(" "), open("puzzle.txt").read().splitlines()))

camel_cards.sort(key=lambda entry: CamelCard(entry[0]))

winnings = 0
rank = 1
for _, bid in camel_cards:
    winnings += int(bid) * rank
    rank += 1

print(f"Day 7, Part 1: {winnings=}")
