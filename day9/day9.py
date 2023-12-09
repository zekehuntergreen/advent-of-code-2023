def find_next(l):
    if set(l) == {0}:
        return 0, 0
    prev, next = find_next([l[i + 1] - l[i] for i in range(len(l) - 1)])
    return l[0] - prev, l[-1] + next


part1, part2 = 0, 0
for line in open("input/puzzle_input.txt").readlines():
    prev, next = find_next(list(map(lambda x: int(x), line.split())))
    part1 += next
    part2 += prev
print(f"part 1: {part1} \t part 2: {part2}")
