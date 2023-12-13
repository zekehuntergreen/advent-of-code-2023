from copy import deepcopy

patterns = list(
    map(
        lambda x: list((list(l) for l in x.split())),
        open("input/puzzle_input.txt").read().split("\n\n"),
    )
)


def find_reflection_point(pattern, ignore=None):
    line_length = len(pattern[0])
    possible_reflection_indexes = set(range(line_length - 1))
    if ignore in possible_reflection_indexes:
        possible_reflection_indexes.remove(ignore)
    for line in pattern:
        new_possible_reflection_indexes = set()
        for i in possible_reflection_indexes:
            num_matching = min(i + 1, line_length - 1 - i)
            left = line[i - num_matching + 1 : i + 1][::-1]
            right = line[i + 1 : i + num_matching + 1]
            if left == right:
                new_possible_reflection_indexes.add(i)
        possible_reflection_indexes = new_possible_reflection_indexes
    if len(possible_reflection_indexes) == 1:
        return possible_reflection_indexes.pop()


part1_total, part2_total = 0, 0
for pattern in patterns:
    original_index_vertical = find_reflection_point(pattern)
    original_index_horizontal = find_reflection_point(list(zip(*pattern)))
    if original_index_vertical is not None:
        part1_total += original_index_vertical + 1
    else:
        part1_total += (original_index_horizontal + 1) * 100

    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            pattern_copy = deepcopy(pattern)
            pattern_copy[i][j] = "." if pattern_copy[i][j] == "#" else "#"
            index_vertical = find_reflection_point(
                pattern_copy, original_index_vertical
            )
            index_horizontal = find_reflection_point(
                list(zip(*pattern_copy)), original_index_horizontal
            )
            if index_vertical is not None or index_horizontal is not None:
                break
        if index_vertical is not None or index_horizontal is not None:
            break
    if index_vertical is not None:
        part2_total += index_vertical + 1
    else:
        part2_total += (index_horizontal + 1) * 100
print(part1_total, part2_total)
