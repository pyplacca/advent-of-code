almanac = open("puzzle.txt").read()

# Part 1
seeds, *maps = almanac.split("\n\n")
numbers = list(map(int, seeds.removeprefix("seeds: ").split(" ")))

for category in maps:
    index = 0

    while index < len(numbers):
        n = numbers[index]
        category_lists = category.split("\n")[1:]

        for entry in category_lists:
            *list_starts, list_range = map(int, entry.split(" "))
            [destination_start, _], [source_start, source_end] = map(
                lambda s: [s, s + list_range - 1], list_starts
            )

            if source_start <= n <= source_end:
                numbers[index] = destination_start + n - source_start
                break

            numbers[index] = n

        index += 1

# print(numbers)
print(f"Day 5, Part 1: {min(numbers)}")
