from math import prod, sqrt, floor, ceil
race_time: int = 7
distance: int = 9

# infile = [(52, 426), (94, 1374), (75, 1279), (94, 1216)]
infile = [(52947594, 426137412791216)]
# infile = [(71530, 940200)]
def calc_record(race_time: int, distance: int):
    num_wins = 0
    for elem in range(race_time):
        charge_time = speed = elem
        remaining_time = race_time - charge_time
        if speed * remaining_time > distance:
            num_wins +=1
    return num_wins

wins = []
for race in infile:
    time, distance = race
    wins.append(calc_record(time, distance))

print(wins)