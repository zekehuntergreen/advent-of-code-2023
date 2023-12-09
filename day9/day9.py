def find_next(l, prev=False):
    if set(l) == {0}:
        return 0
    diff = [l[i + 1] - l[i] for i in range(len(l) - 1)]
    return l[0] - find_next(diff, prev) if prev else l[-1] + find_next(diff)


part1, part2 = 0, 0
for line in open("input/puzzle_input.txt").readlines():
    line = list(map(lambda x: int(x), line.split()))
    part1 += find_next(line)
    part2 += find_next(line, True)
print(f"part 1: {part1} \t part 2: {part2}")
