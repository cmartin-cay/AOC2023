from collections import defaultdict
import math

with open('day02.txt') as f:
    lines = f.readlines()
    lines = [line.strip().split(': ') for line in lines]
    print(lines[0])

red = 12
green = 13
blue = 14

total_games = sum(range(len(lines) +1))
print(f"{total_games=}")
invalid_games: int = 0
power_cubes = 0

for line in lines:
    game_number = int(line[0].split(" ")[-1])
    game_results = line[1].split("; ")
    scores = defaultdict(int)
    for one_grab in game_results:
        one_grab = one_grab.split(", ")
        for elem in one_grab:
            val, color = int(elem.split()[0]), elem.split()[1]
            if scores.get(color, 0) < val:
                scores[color] = val
    if scores.get("blue", 0) > blue or scores.get("green", 0) > green or scores.get("red", 0) > red:
        invalid_games += game_number
    num_cubes = math.prod(scores.values())
    power_cubes += num_cubes


print(f"{total_games - invalid_games=}")
print(f"{power_cubes=}")

