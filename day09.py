with open("day09.txt") as infile:
    lines = infile.readlines()
    lines = [line.strip() for line in lines]
    lines = [[int(x) for x in sublist.split()] for sublist in lines]
    # print(lines)

def find_zero_diff(seq, running_total=0):
    running_total += seq[0]
    if sum(seq) == 0:
        return running_total
    else:
        seq = [(seq[i] - seq[i+1]) for i in range(len(seq)-1)]
        return find_zero_diff(seq, running_total=running_total)

part1 = 0
for line in lines:
    line = line[::-1]
    part1 += find_zero_diff(line)

print(f"{part1=}")

def find_first_diff(seq, running_total=0, zeroth=[]):
    zeroth = [] if not zeroth else zeroth
    start_idx = 0
    running_total += seq[0]
    zeroth.append(seq[-1])
    if seq[0] - seq[start_idx + 1] == 0:
        zeroth.append(0)
        return zeroth[::-1]
    else:
        seq = [(seq[i] - seq[i + 1]) for i in range(len(seq) - 1)]
        return find_first_diff(seq, running_total=running_total, zeroth=zeroth)

def first_num(vals, rt=0):
    for i in range(len(vals) - 1):
        a = vals[i + 1]
        b = rt
        rt = a - b
    return rt

part2 = 0
for line in lines:
    line = line[::-1]
    lst = find_first_diff(line)
    part2 += first_num(lst)

print(f"{part2=}")

# x = find_first_diff(lines[1][::-1])
# print(x)
# print(first_num(x))