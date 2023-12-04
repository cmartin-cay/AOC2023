from dataclasses import dataclass, field
import time
from operator import attrgetter

@dataclass
class Ticket:
    game_number: int
    winning_numbers: set = field(default_factory=set)
    elf_numbers: set = field(default_factory=set)
    copies: int = 1

    def winning_score(self):
        result = self.winning_numbers & self.elf_numbers
        if result:
            return 2 ** (len(result) - 1)
        else:
            return 0

    def crate_copies(self):
        score = len(self.winning_numbers & self.elf_numbers)
        return score


ticket_list = []

start = time.perf_counter()

with open("day04.txt") as f:
    lines = f.readlines()
    lines = [line.strip().split(": ") for line in lines]
    for line in lines:
        game_num = int(line[0].split(" ")[-1])
        nums = line[1].split(' | ')
        winning_numbers, elf_numbers = nums[0].split(), nums[1].split()
        winning_numbers = set(winning_numbers)
        elf_numbers = set(elf_numbers)
        ticket_list.append(Ticket(game_number=game_num, winning_numbers=winning_numbers, elf_numbers=elf_numbers))

part1 = 0

for ticket in ticket_list:
    part1 += ticket.winning_score()

print(f"{part1=}")
part_1_time = time.perf_counter()

for ticket in ticket_list:
    num_copies = ticket.crate_copies()
    for _ in range(ticket.game_number + 1, ticket.game_number + num_copies + 1):
        obj = [x for x in ticket_list if x.game_number==_][0]
        # obj = next((x for x in ticket_list if x.game_number == _), None)
        obj.copies += ticket.copies

part2 = 0
for ticket in ticket_list:
    part2 += ticket.copies

print(f"{part2=}")
part_2_time = time.perf_counter()
print(f"{part_1_time-start=}")
print(f"{part_2_time-start= }")
