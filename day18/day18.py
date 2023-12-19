import math
import shapely
import matplotlib.pyplot as plt

lines = open("input/puzzle_input.txt").readlines()
coords = list()
current_coordinates = (0, 0)
directions = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}
directions_int = {"3": (-1, 0), "1": (1, 0), "0": (0, 1), "2": (0, -1)}


def add_tuples(a, b):
    return tuple(sum(x) for x in zip(a, b))


def multiply_tuples(a, b):
    return tuple(math.prod(x) for x in zip(a, b))


def find_area(coords):
    _, ax = plt.subplots()
    polygon = shapely.buffer(shapely.Polygon(coords), 0.5, join_style=2)
    area = int(polygon.area)
    x, y = polygon.exterior.xy
    ax.plot(x, y)
    # plt.show()
    return area


# part 1
for line in lines:
    direction, num, _ = line.split()
    current_coordinates = add_tuples(
        current_coordinates,
        multiply_tuples(directions[direction], (int(num), int(num))),
    )
    coords.append(current_coordinates)

area = find_area(coords)

# part 2
coords = list()
for line in lines:
    _, _, color = line.split()
    num_hex, dir_int = color[2:7], color[7]
    num = int(f"0x{num_hex}", 0)
    direction = directions_int[dir_int]

    current_coordinates = add_tuples(
        current_coordinates,
        multiply_tuples(direction, (num, num)),
    )
    coords.append(current_coordinates)

area = find_area(coords)
