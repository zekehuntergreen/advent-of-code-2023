grid = open("input/puzzle_input.txt").read().split()
import shapely
import matplotlib.pyplot as plt


def find_starting_point():
    for i, line in enumerate(grid):
        for j, tile in enumerate(line):
            if tile == "S":
                return i, j


def add_tuples(a, b):
    return tuple(sum(x) for x in zip(a, b))


def find_tile_at_coordinate(x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
        return None
    return grid[x][y]


directions = {"n": (-1, 0), "s": (1, 0), "e": (0, 1), "w": (0, -1)}
opposite_direction = {"n": "s", "s": "n", "e": "w", "w": "e"}

connections = {
    ("s", "n"): "|",
    ("n", "s"): "|",
    ("e", "w"): "-",
    ("w", "e"): "-",
    ("s", "e"): "F",
    ("e", "s"): "F",
    ("w", "n"): "J",
    ("n", "w"): "J",
    ("w", "s"): "7",
    ("s", "w"): "7",
    ("e", "n"): "L",
    ("n", "e"): "L",
}

last_direction_tile_to_direction = {
    ("n", "|"): "n",
    ("s", "|"): "s",
    ("n", "F"): "e",
    ("w", "F"): "s",
    ("w", "L"): "n",
    ("s", "L"): "e",
    ("e", "7"): "s",
    ("n", "7"): "w",
    ("s", "J"): "w",
    ("e", "J"): "n",
    ("e", "-"): "e",
    ("w", "-"): "w",
}


# replace the starting tile
starting_point = find_starting_point()
valid_directions = tuple(
    filter(
        lambda d: (
            d,
            find_tile_at_coordinate(*add_tuples(starting_point, directions[d])),
        )
        in last_direction_tile_to_direction,
        ["n", "s", "e", "w"],
    )
)
replacement = connections[valid_directions]

grid[starting_point[0]] = grid[starting_point[0]].replace("S", replacement)
current_direction = opposite_direction[valid_directions[0]]


current_position = starting_point
current_tile = replacement
pipe_coordinates = list()


while current_position != starting_point or pipe_coordinates == list():
    pipe_coordinates.append(current_position)
    current_direction = last_direction_tile_to_direction[
        (current_direction, current_tile)
    ]
    diff = directions[current_direction]
    current_position = add_tuples(current_position, diff)
    current_tile = find_tile_at_coordinate(*current_position)

print("part 1", int(len(pipe_coordinates) / 2))

_, axs = plt.subplots()
polygon = shapely.Polygon(pipe_coordinates)
buffered_polygon = shapely.buffer(polygon, -0.5, join_style=2)
area = int(buffered_polygon.area)
print("part 2", area)
x, y = polygon.exterior.xy
axs.plot(x, y)

for geom in buffered_polygon.geoms:
    xs, ys = geom.exterior.xy
    axs.fill(xs, ys)

plt.show()
