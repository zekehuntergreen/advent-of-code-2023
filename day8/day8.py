import functools
import math

instructions, graph_lines  = open("input/puzzle_input.txt").read().split("\n\n")
nodes = {}

def get_or_create_node(value):
    if value not in nodes:
        nodes[value] = {"value": value}
    return nodes[value]

# construct graph
for line in graph_lines.split("\n"):
    this_value, destinations = line.split(" = ")
    left, right = destinations[1:-1].split(", ")
    node = get_or_create_node(this_value)
    node["L"] = left
    node["R"] = right

def find_number_of_steps(start, suffix):
    current_node = nodes[start]
    i, num_instructions = 0, len(instructions)
    while not current_node["value"].endswith(suffix):
        current_instruction = instructions[i % num_instructions]
        current_node = nodes[current_node[current_instruction]]
        i += 1
    return i

print("part 1 ", find_number_of_steps("AAA", "ZZZ"))

path_lengths = map(lambda sn: find_number_of_steps(sn, "Z"), filter(lambda n: n.endswith("A") , nodes))
print("part 2 ", int(functools.reduce(math.lcm, path_lengths)))
