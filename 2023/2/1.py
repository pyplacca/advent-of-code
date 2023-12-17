record = open("puzzle.txt", "r").read().splitlines()

target = {"red": 12, "green": 13, "blue": 14}
game_ids = []

for game in record:
    [id, game_set] = game.split(":")
    id = int(id.replace("Game ", ""))
    possible = True

    for game_round in game_set.split(";"):
        for s in game_round.split(","):
            [count, color] = s.strip().split(" ")
            if target[color] < int(count):
                possible = False
                break

    if possible:
        game_ids.append(id)

print(f"Day 2, Part 1: total={sum(game_ids)}")
