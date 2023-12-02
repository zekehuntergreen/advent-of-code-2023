actual_cube_counts = {"red": 12, "green": 13, "blue": 14}
total = 0
for line in open("input/puzzle_input.txt").readlines():
    possible = True
    game_number, cubes = line.split(": ")
    for draw in cubes.split("; "):
        for count in draw.split(", "):
            number, color = count.split(" ")
            if actual_cube_counts[color.strip()] < int(number):
                possible = False
    if possible:
        total += int(game_number.split()[1])
print(total)
