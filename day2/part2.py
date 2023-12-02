total = 0
for line in open("input/puzzle_input.txt").readlines():
    cubes = line.split(": ")[1]
    max_counts = {"blue": 0, "green": 0, "red": 0}
    for draw in cubes.split("; "):
        for count in draw.split(", "):
            number, color = count.split(" ")
            max_counts[color.strip()] = max(int(number), max_counts[color.strip()])
    total += max_counts["blue"] * max_counts["green"] * max_counts["red"]
print(total)