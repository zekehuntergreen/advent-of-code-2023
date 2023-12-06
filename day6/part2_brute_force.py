time, record_distance = map(
    lambda x: int("".join(x.split()[1:])),
    open("input/puzzle_input.txt").read().split("\n"),
)

total = 1
winning_races = 0
for x in range(time + 1):
    y = x * (time - x)
    print(f"x {x} y {y}")
    if y > record_distance:
        winning_races += 1
print(winning_races)
