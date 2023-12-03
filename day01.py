with open("day01.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


def get_numbers(text: str):
    a = first_number(text)
    b = first_number(text[::-1])
    return int(f"{a}{b}")


def first_number(text: str):
    for char in text:
        if char.isdigit():
            return char


res = 0
for line in lines:
    res += get_numbers(line)

print(f"Part One: {res}")

digits = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine",
}

sample = "eightwothree"

part2 = 0

for line in lines:
    for key, val in digits.items():
        line = line.replace(key, val)
    part2+=get_numbers(line)

print(f"Part Two: {part2}")
