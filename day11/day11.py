from itertools import combinations

grid = list(
    map(lambda x: [c for c in x], open("input/puzzle_input.txt").read().split("\n"))
)
print(grid)
galaxies = list()
empty_rows = set(
    filter(
        lambda x: x is not None,
        map(lambda r: r[0] if set(r[1]) == {"."} else None, enumerate(grid)),
    )
)
empty_columns = set(
    filter(
        lambda x: x is not None,
        map(
            lambda r: r[0] if set(r[1]) == {"."} else None,
            enumerate([c for c in zip(*grid)]),
        ),
    )
)

print(f"empty_rows {empty_rows}")
print(f"empty_columns {empty_columns}")

for i, line in enumerate(grid):
    for j, item in enumerate(line):
        if item == "#":
            galaxies.append((i, j))

print(galaxies)
total = 0
multiplier = 1_000_000
for a, b in combinations(galaxies, 2):
    empty_rows_in_range = len(
        list(
            filter(
                lambda r: (r > a[0] and r < b[0]) or (r > b[0] and r < a[0]), empty_rows
            )
        )
    )
    empty_columns_in_range = len(
        list(
            filter(
                lambda r: (r > a[1] and r < b[1]) or (r > b[1] and r < a[1]),
                empty_columns,
            )
        )
    )
    distance = (
        abs(a[0] - b[0])
        + (
            empty_rows_in_range * multiplier - empty_rows_in_range
            if empty_rows_in_range
            else 0
        )
        + abs((a[1] - b[1]))
        + (
            empty_columns_in_range * multiplier - empty_columns_in_range
            if empty_columns_in_range
            else 0
        )
    )
    print(a, b, empty_rows_in_range, empty_columns_in_range, distance)
    total += distance
print(total)
