total = 0
for line in open("input/puzzle_input.txt").readlines():
    numbers = [c for c in line if ord(c) >= 48 and ord(c) <= 57]
    total += int(numbers[0] + numbers[-1])
print(total)