# Step 1a - Identify numbers and indexes
# Step 1b - Identify symbols and position
from dataclasses import dataclass, field
from string import punctuation
import math

punctuation = punctuation.replace(".", "")
print(punctuation)


@dataclass
class Nums:
    number: int
    row: int
    col_start: int
    col_end: int
    is_touching: bool = False


@dataclass
class Gears:
    row: int
    col: int
    vals: set[int] = field(default_factory=set)
    num_touching: int = 0


def gen_neighbors(x, y):
    neighbors = [
        (x - 1, y),
        (x - 1, y - 1),
        (x - 1, y + 1),
        (x + 1, y),
        (x + 1, y + 1),
        (x + 1, y - 1),
        (x, y - 1),
        (x, y + 1),
        (x, y),
    ]
    return neighbors


all_nums = []
all_symbols = []
all_gears = {}

with open("day03.txt") as infile:
    infile = infile.readlines()
    infile = [line.strip() for line in infile]

limit = len(infile[0]) - 1

for r_idx, row in enumerate(infile):
    temp_num = []
    start_idx = None
    end_idx = 0
    for c_idx, col in enumerate(row):
        if infile[r_idx][c_idx].isnumeric():
            if not start_idx and not start_idx == 0:
                start_idx = c_idx
            temp_num.extend(infile[r_idx][c_idx])
            end_idx = c_idx
            if c_idx == limit and temp_num:
                val: Nums = Nums(
                    number=int("".join(temp_num)),
                    row=r_idx,
                    col_start=start_idx,
                    col_end=end_idx,
                )
                all_nums.append(val)
        else:
            if temp_num:
                val: Nums = Nums(
                    number=int("".join(temp_num)),
                    row=r_idx,
                    col_start=start_idx,
                    col_end=end_idx,
                )
                all_nums.append(val)
                temp_num = []
                start_idx = None
            if infile[r_idx][c_idx] in punctuation:
                all_symbols.append((r_idx, c_idx))
            if infile[r_idx][c_idx] == "*":
                all_gears[(r_idx, c_idx)] = Gears(row=r_idx, col=c_idx)

print(all_nums)
print(all_symbols)
print(all_gears)

for tester in all_nums:
    for x in range(tester.col_start, tester.col_end + 1):
        checkers = gen_neighbors(tester.row, x)
        # print(checkers)
        for elem in checkers:
            x, y = elem
            if elem in all_symbols:
                # print("TOUCHING")
                tester.is_touching = True
            try:
                if infile[x][y] == "*":
                    # print("GEAR")
                    gear = all_gears[(x, y)]
                    gear.vals.add(tester.number)
            except IndexError:
                pass

res = 0
for elem in all_nums:
    if elem.is_touching:
        res += elem.number

print(res)
# for elem in all_nums:
#     if not elem.is_touching:
#         print(elem)
# print(all_gears)
part2 = []
for gear in all_gears.values():
    gear: Gears
    if len(gear.vals) > 1:
        part2.append(math.prod(gear.vals))

print(sum(part2))
