from functools import reduce

test = False
file_name_prefix = "sample" if test else "puzzle"
file_name = f"input/{file_name_prefix}_input.txt"
lines = open(file_name).read().split(",")


def hash_function(line):
    return reduce(lambda x, y: ((x + ord(y)) * 17) % 256, line, 0)


part_1 = sum(map(lambda x: hash_function(x), lines))
print(f"part 1 {part_1}")


class Box:
    def __init__(self):
        self.lense_lengths = []
        self.lense_labels = []

    def set_lense(self, i, label, flength):
        if i is not None:
            self.lense_lengths[i] = flength
            self.lense_labels[i] = label
        else:
            self.lense_lengths.append(flength)
            self.lense_labels.append(label)

    def get_label_index(self, label):
        if label in self.lense_labels:
            return self.lense_labels.index(label)

    def remove_lense(self, i):
        del self.lense_labels[i]
        del self.lense_lengths[i]


boxes = {}
for line in lines:
    if "=" in line:
        label, flength = line.split("=")
        op = "="
    elif "-" in line:
        label = line[:-1]
        op = "-"

    box_index = hash_function(label)
    if box_index in boxes:
        box = boxes[box_index]
    else:
        box = Box()
        boxes[box_index] = box

    label_index = box.get_label_index(label)
    if op == "=":
        box.set_lense(label_index, label, flength)
    elif op == "-" and label_index is not None:
        box.remove_lense(label_index)


part_2 = 0
for box_index, b in boxes.items():
    for lense_index, flength in enumerate(b.lense_lengths):
        part_2 += (box_index + 1) * (lense_index + 1) * int(flength)
print(f"part 2 {part_2}")
