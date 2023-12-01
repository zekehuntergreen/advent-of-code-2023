replacements = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

lengths = set([len(k) for k in replacements.keys()])

def find_first_number(line, start, end, reverse = 1):
    for i in range(start, end, reverse):
        if ord(line[i]) >= 48 and ord(line[i]) <= 57:
            return line[i]
        for l in lengths:
            num = line[i:i+l] if reverse == 1 else line[i - l:i]
            if num in replacements:
                return replacements[num]

total = 0
for line in open("input/puzzle_input.txt").readlines():
    total += int(find_first_number(line, 0, len(line)) + find_first_number(line, len(line) - 1, -1, -1))
print(total)