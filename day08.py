from itertools import cycle
from math import lcm

map_dir: dict = {}

with open("day08.txt") as infile:
    lines = infile.readlines()
    lines = [line.strip() for line in lines]
    # print(lines)
    sequence = lines[0]
    sequence = sequence.replace("L", "0").replace("R", "1")
    sequence = cycle([int(x) for x in sequence])
    mapping = lines[2:]
    for line in mapping:
        start_point = line[:3]
        left_dest = line[7:10]
        right_dest = line [12:15]
        map_dir[start_point] = (left_dest, right_dest)

# print(map_dir)
# print(sequence)

# starting = map_dir["AAA"]
# print(starting)
# part_1_steps = 0
#
# for step in sequence:
#     next_dest = starting[step]
#     # print(f"{next_dest=}")
#     starting = map_dir[next_dest]
#     part_1_steps+=1
#     # print(f"New Starting: {starting}")
#     if next_dest == "ZZZ":
#         break
#
# print(f"{part_1_steps}=")

starting_nodes = [node for node in map_dir if node[-1]=="A"]
print(starting_nodes)
def take_step(starting_nodes: list, direction: int):
    ending_nodes = []
    for node in starting_nodes:
        ending_nodes.append(map_dir[node][direction])
    return ending_nodes

part2 = []
for node in starting_nodes:
    steps = 0
    for dir in sequence:
        next_dest = map_dir[node][dir]
        # print(f"{next_dest=}")
        steps += 1
        node = next_dest
        if node[-1]=="Z":
            part2.append(steps)
            break
        # starting = map_dir[next_dest]
        # part_1_steps+=1
        # # print(f"New Starting: {starting}")
        # if next_dest == "ZZZ":
        #     break

print(f"{part2=}")
print(lcm(*part2))