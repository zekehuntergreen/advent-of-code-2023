import copy
import re

workflows_str, part_ratings_str = open("input/puzzle_input.txt").read().split("\n\n")

workflows = {}
for w in workflows_str.split():
    m = re.match(r"^([\w]+)\{(.*)\}$", w)
    workflow_name, rules_str = m.groups()
    workflows[workflow_name] = rules_str.split(",")

parts = []
for p in part_ratings_str.split():
    part = {}
    for attribute_rating in p.replace("{", "").replace("}", "").split(","):
        attribute, rating = attribute_rating.split("=")
        part[attribute] = int(rating)
    parts.append(part)


def evaluate_part(part, current_workflow="in"):
    if current_workflow == "A":
        return True
    if current_workflow == "R":
        return False
    workflow = workflows[current_workflow]
    for rule in workflow:
        if ":" in rule:
            criteria, next_workflow = rule.split(":")
            locals().update(part)
            if eval(criteria):
                return evaluate_part(part, next_workflow)
        else:
            return evaluate_part(part, rule)


total = 0
for part in parts:
    if evaluate_part(part):
        total += sum(list(part.values()))
print(f"part 1 {total}")

accepted_ranges = []
minimum, maximum = 1, 4001


def create_tree(workflow, ranges, visited):
    visited.append(workflow)
    if workflow == "A":
        accepted_ranges.append((visited, ranges))
        return
    elif workflow == "R":
        return
    workflow_rules = workflows[workflow]
    for rule in workflow_rules:
        if ":" in rule:
            criteria, next_workflow = rule.split(":")
            var, ineq, num = criteria[0], criteria[1], int(criteria[2:])
            ranges_copy_accepted = copy.deepcopy(ranges)
            if ineq == "<":
                ranges_copy_accepted[var] -= set(range(num, maximum))
                ranges[var] -= set(range(minimum, num))
            elif ineq == ">":
                ranges_copy_accepted[var] -= set(range(minimum, num + 1))
                ranges[var] -= set(range(num + 1, maximum))

            create_tree(next_workflow, ranges_copy_accepted, copy.deepcopy(visited))
        else:
            create_tree(rule, ranges, visited)


starting_ranges = {k: set(range(minimum, maximum)) for k in ["x", "m", "a", "s"]}
create_tree("in", starting_ranges, [])

total_combinations = 0
for visited, accepted_range in accepted_ranges:
    combinations = 1
    for k, v in accepted_range.items():
        combinations *= len(v)
    total_combinations += combinations
print(f"part 2 {total_combinations}")
