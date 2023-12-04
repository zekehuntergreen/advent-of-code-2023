total = 0
lines = open("input/puzzle_input.txt").readlines()
copies = [1 for _ in range(len(lines))]
for i, line in enumerate(lines):
    winning_numbers, my_numbers = map(
        lambda x: set([int(n) for n in x.strip().split()]),
        line.split(":")[1].split(" | "),
    )
    num_intersecting = len(winning_numbers.intersection(my_numbers))
    for j in range(1, num_intersecting + 1):
        copies[i + j] += copies[i]
    total += copies[i]
print(total)
