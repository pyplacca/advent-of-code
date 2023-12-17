import re


# Part 1
result = 0
for line in open("puzzle.txt").read().splitlines():
    digits = re.findall(r"\d", line)
    if len(digits):
        result += int(digits[0] + digits[-1])

print(f"Day 1, Part 1: {result=}")
