input_lines = open("input/puzzle_input.txt").read().split("\n\n")
seeds = list(map(lambda x: int(x), input_lines[0].split(":")[1].split()))
seed_ranges = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

rules_map = {}
for map_string in input_lines[1:]:
    lines = map_string.split("\n")
    map_key = lines[0].split()[0].split("-")
    rules_map[(map_key[0], map_key[2])] = [
        tuple(map(lambda x: int(x), line.split())) for line in lines[1:]
    ]


def find_location(current_item, value, range):
    key = list(filter(lambda x: x[0] == current_item, rules_map.keys()))[0]
    i = 0
    ranges = []
    while i < range:
        current_value = i + value
        # is i covered by any rules?
        relevant_rule = None
        for destination_start, source_start, range_size in rules_map[key]:
            if (
                source_start <= current_value
                and current_value < source_start + range_size
            ):
                relevant_rule = destination_start, source_start, range_size
        if relevant_rule:
            destination_start, source_start, range_size = relevant_rule
            left_in_rule_range = range - i
            left_in_loop_range = source_start + range_size - (current_value)
            new_range = min([left_in_loop_range, left_in_rule_range])
            new_val = destination_start + (current_value - source_start)
            ranges.append((new_val, new_range))
            i += new_range
        else:
            all_sources = [r[1] for r in rules_map[key]]
            all_sources.append(value + range)
            next_source_start = min(
                list(
                    filter(
                        lambda x: x > current_value,
                        all_sources,
                    )
                )
            )
            ranges.append((current_value, next_source_start - current_value))
            i += next_source_start - current_value
    if key[1] == "location":
        return min([p[0] for p in ranges])
    return min([find_location(key[1], p[0], p[1]) for p in ranges])


print(min([find_location("seed", s, r) for s, r in seed_ranges]))
