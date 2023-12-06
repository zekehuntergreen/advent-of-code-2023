from math import sqrt, floor, ceil

time, record_distance = map(
    lambda x: int("".join(x.split()[1:])),
    open("input/puzzle_input.txt").read().split("\n"),
)
first_intersection = time / 2 - (sqrt(time**2 - 4 * record_distance)) / 2
second_intersection = time / 2 + (sqrt(time**2 - 4 * record_distance)) / 2
print(floor(second_intersection) - ceil(first_intersection) + 1)
