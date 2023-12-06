input_lines = open("input/puzzle_input.txt").read().split("\n\n")
seeds = list(map(lambda x: int(x), input_lines[0].split(":")[1].split()))
rules_map = {}
for map_string in input_lines[1:]:
    lines = map_string.split("\n")
    map_key = lines[0].split()[0].split("-")
    rules_map[(map_key[0], map_key[2])] = [
        tuple(map(lambda x: int(x), line.split())) for line in lines[1:]
    ]


def find_location(current_item, value):
    key = list(filter(lambda x: x[0] == current_item, rules_map.keys()))[0]
    new_value = value
    for destination_start, source_start, range_size in rules_map[key]:
        if value >= source_start and value <= source_start + range_size:
            new_value = destination_start + (value - source_start)
    if key[1] == "location":
        return new_value
    else:
        return find_location(key[1], new_value)


print(min([find_location("seed", s) for s in seeds]))
