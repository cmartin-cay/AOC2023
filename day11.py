from dataclasses import dataclass
from bisect import bisect_left
from itertools import combinations

with open("day11.txt") as infile:
    lines = infile.readlines()
    lines = [line.strip() for line in lines]
    # print(lines)

@dataclass
class Galaxy:
    x_pos: int
    y_pos: int

    
    def expand_y(self):
        expansion = bisect_left(empty_col, self.y_pos)
        self.y_pos += expansion *  (1000000-1)
        # print(self.y_pos)

    def expand_x(self):
        expansion = bisect_left(empty_row, self.x_pos)
        self.x_pos += expansion * (1000000-1)

galaxies = []
empty_row = []
empty_col = []

for x_idx, row in enumerate(lines):
    if all(x=="." for x in row):
        empty_row.append(x_idx)
    for y_idx, col in enumerate(row):
        if lines[x_idx][y_idx] == "#":
            galaxy = Galaxy(x_pos=x_idx, y_pos=y_idx)
            galaxies.append(galaxy)

transpose = zip(*lines)
for x_idx, row in enumerate(transpose):
    if all(x=="." for x in row):
        empty_col.append(x_idx)    

# print(f"{galaxies=}")
# print(f"{empty_row=}")
# print(f"{empty_col=}")


for galaxy in galaxies:
    galaxy: Galaxy
    galaxy.expand_x()
    galaxy.expand_y()


#taxicab distance function
def manhattan_dist(gal1: Galaxy, gal2: Galaxy) -> int:
    return abs(gal2.x_pos - gal1.x_pos) + abs(gal2.y_pos - gal1.y_pos)

#pair up al galaxies
paired_galaxies = combinations(galaxies, 2)


total_dist = 0

for pair in paired_galaxies:
    total_dist += manhattan_dist(pair[0], pair[1])

# print(galaxies[0])
print(f"{total_dist=}")