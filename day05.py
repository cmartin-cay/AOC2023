from itertools import batched

with open("day05.txt") as infile:
    infile = infile.readlines()
    infile = [x.strip() for x in infile]
    infile = [x for x in infile if x]
    # print(infile)
    seeds = infile[0][6:].split()
    seeds = [int(x) for x in seeds]
    print(seeds)
    new_seeds = []
    batched_seeds = batched(seeds, 2)
    for elem in batched_seeds:
        a, b = elem
        new_seeds.append(range(a, a + b))

seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

key_name_dict = {
    "seed_to_soil": seed_to_soil,
    "soil_to_fertilizer": soil_to_fertilizer,
    "fertilizer_to_water": fertilizer_to_water,
    "water_to_light": water_to_light,
    "light_to_temperature": light_to_temperature,
    "temperature_to_humidity": temperature_to_humidity,
    "humidity_to_location": humidity_to_location,
}

key_name = ""


def lookup(val, target_list):
    for each in target_list:
        r, gap = each
        if val in r:
            return val + gap
    return val

def overlap(r1: range, r2: range):
    return r2.start <= r1.start < r2.stop or r1.start <= r2.start < r1.stop

def new_lookup(range_a, range_b):
    pass

for elem in infile[1:]:
    # print(key_name)
    if elem[0].isalpha():
        elem = elem.replace("-", "_")
        if elem[:5] != key_name:
            key_name = elem[:-5]
    elif elem[0].isnumeric():
        elem = [int(x) for x in elem.split()]
        correct_map = key_name_dict[key_name]
        start, finish, gap = elem[1], elem[1] + elem[2], elem[0] - elem[1]
        correct_map.append((range(start, finish), gap))

possible_loctions = []
for seed in seeds:
    soil = lookup(seed, seed_to_soil)
    fertilizer = lookup(soil, soil_to_fertilizer)
    water = lookup(fertilizer, fertilizer_to_water)
    light = lookup(water, water_to_light)
    temperature = lookup(light, light_to_temperature)
    humididty = lookup(temperature, temperature_to_humidity)
    location = lookup(humididty, humidity_to_location)
    possible_loctions.append(location)

print(min(possible_loctions))

smallest_location = 389056265

for _ in new_seeds:
    for seed in _:
        soil = lookup(seed, seed_to_soil)
        fertilizer = lookup(soil, soil_to_fertilizer)
        water = lookup(fertilizer, fertilizer_to_water)
        light = lookup(water, water_to_light)
        temperature = lookup(light, light_to_temperature)
        humididty = lookup(temperature, temperature_to_humidity)
        location = lookup(humididty, humidity_to_location)
        if location < smallest_location:
            smallest_location = location

print(f"{smallest_location=}")