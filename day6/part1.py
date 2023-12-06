times, distances = map(
    lambda x: [int(n) for n in x],
    map(lambda y: y.split()[1:], open("input/puzzle_input.txt").read().split("\n")),
)

total = 1
for race_number, time in enumerate(times):
    record_distance = distances[race_number]
    winning_races = 0
    for x in range(time + 1):
        y = x * (time - x)
        if y > record_distance:
            winning_races += 1
    total *= winning_races
print(total)
