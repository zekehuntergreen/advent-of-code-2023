import itertools
parts = {}
for i, line in enumerate(open("input/sample_input.txt").readlines()):
    j = 0
    while j < len(line.strip()):
        k = 1
        if line[j].isdigit():
            while line[j + k].isdigit():
                k += 1
            parts[(i, j)] = line[j:j + k]
        elif line[j] != ".":
            parts[(i, j)] = line[j]
        j += k

# part 1
total = 0
for (i, j), string in parts.items():
    if string.isdigit():
        for x, y in itertools.product((i - 1, i, i + 1), range(j - 1, j + len(string) + 1)):
            if (x, y) in parts and not parts[(x, y)].isdigit():
                total += int(string)
                break
print("part 1: ", total)

# part 2
total = 0
for (i, j), string in parts.items():
    if string == "*":
        adjacent = list()
        for x, y in itertools.product((i - 1, i, i + 1), range(j - 3, j + len(string) + 1)):
            if (x, y) in parts and parts[(x, y)].isdigit() and y + len(parts[(x, y)]) >= j:
                adjacent.append(int(parts[(x, y)]))
        if len(adjacent) == 2:
            total += adjacent[0] * adjacent[1]
print("part 2: ", total)