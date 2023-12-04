total = 0
for line in open("input/puzzle_input.txt").readlines():
    winning_numbers, my_numbers = map(
        lambda x: set([int(n) for n in x.strip().split()]),
        line.split(":")[1].split(" | "),
    )
    num_intersecting = len(winning_numbers.intersection(my_numbers))
    total += 2 ** (num_intersecting - 1) if num_intersecting > 0 else 0
print(total)
