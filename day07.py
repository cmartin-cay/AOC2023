from dataclasses import dataclass, field
from collections import Counter


@dataclass
class Hand:
    cards: list[int]
    orig_cards: str
    bid: int
    hand_strength: int = field(init=False)
    joker_cards: list[int] = field(init=False)
    rank: int = 0

    def __post_init__(self):
        self.joker_cards = self.make_joker_cards()
        self.hand_strength = self.calc_hand_strength()

    def calc_hand_strength(self) -> int:
        # self.count: Counter = Counter(self.joker_cards)
        # if len(self.count) == 1:
        #     return 6
        # elif self.count.most_common()[0][1] == 4:
        #     return 5
        # elif len(self.count) == 2 and self.count.most_common()[1][1] == 2:
        #     return 4
        # elif len(self.count) == 3 and self.count.most_common()[0][1] == 3:
        #     return 3
        # elif len(self.count) == 3 and self.count.most_common()[0][1] == 2:
        #     return 2
        # elif len(self.count) == 4:
        #     return 1
        # else:
        #     return 0
        return sum(map(self.joker_cards.count, self.joker_cards))

    def winning_score(self) -> int:
        return self.rank * self.bid

    def make_joker_cards(self):
        j_count = Counter(self.orig_cards)
        num_jokers = self.orig_cards.count("J")
        if num_jokers == 5:
            return [convert[x] for x in self.orig_cards]
        if num_jokers == 0:
            return [convert[x] for x in self.orig_cards]
        else:
            del j_count["J"]
            most_common = j_count.most_common()[0][0]
            temp_cards = self.orig_cards.replace("J", most_common)
            return [convert[x] for x in temp_cards]

    def __eq__(self, other):
        return self.cards == other.cards

    def __gt__(self, other):
        if self.hand_strength == other.hand_strength:
            zipped = zip(self.cards, other.cards)
            for elem in zipped:
                if elem[0] > elem[1]:
                    return True
                if elem[0] < elem[1]:
                    return False
        return self.hand_strength > other.hand_strength


convert = {"2": 2,
           "3": 3,
           "4": 4,
           "5": 5,
           "6": 6,
           "7": 7,
           "8": 8,
           "9": 9,
           "T": 10,
           "J": 1,
           "Q": 12,
           "K": 13,
           "A": 14}

hands: list[Hand] = []

with open("day07.txt") as infile:
    lines = infile.readlines()
    lines = [line.strip().split() for line in lines]
    # print(lines)
    for line in lines:
        cards, bid = line
        new_cards = [convert[x] for x in cards]
        hands.append(Hand(new_cards, cards, int(bid)))

hands = sorted(hands)
for idx, hand in enumerate(hands, start=1):
    hand.rank = idx

part1 = 0
for hand in hands:
    part1 += hand.winning_score()

print(part1)
