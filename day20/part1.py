import math


class Module:
    def __str__(self):
        return self.name

    def __init__(self, name, destinations):
        self.destinations = destinations
        self.name = name
        self.inputs = []

    def send_pulse(self, high):
        for d in self.destinations:
            pulse_strength = "high" if high else "low"
            print(f"{self.name} -{pulse_strength}> {d}")
            stack.append((self.name, d, high))

    def add_input(self, module):
        self.inputs.append(module)


class RX(Module):
    def __init__(self, *args):
        self.on = False
        super().__init__(*args)

    def handle_pulse(self, _, high):
        if not high:
            self.on = True


class FlipFlop(Module):
    def __init__(self, *args):
        self.on = False
        super().__init__(*args)

    def handle_pulse(self, _, high):
        if high:
            return
        self.on = not self.on
        self.send_pulse(self.on)


class Conjunction(Module):
    def __init__(self, *args):
        super().__init__(*args)
        self.input_pulses = {}

    def add_input(self, module):
        super().add_input(module)
        self.input_pulses[module] = False

    def handle_pulse(self, input, high):
        self.input_pulses[input] = high
        if all(self.input_pulses.values()):
            self.send_pulse(False)
        else:
            self.send_pulse(True)


class Broadcast(Module):
    def __init__(self, *args):
        super().__init__(*args)

    def handle_pulse(self, _, high):
        self.send_pulse(high)


class Output(Module):
    def __init__(self, *args):
        super().__init__(*args)
        self.pulses = 0

    def handle_pulse(self, *args):
        self.pulses += 1


modules = {"output": Output("output", []), "rx": RX("rx", [])}

file_name = "input/puzzle_input.txt"
for line in open(file_name).read().split("\n"):
    source, destination_str = line.split(" -> ")
    destinations = destination_str.split(", ")
    if source[0] == "%":
        name = source[1:]
        modules[name] = FlipFlop(name, destinations)
    elif source[0] == "&":
        name = source[1:]
        modules[name] = Conjunction(name, destinations)
    elif source == "broadcaster":
        modules[source] = Broadcast(source, destinations)


for line in open(file_name).read().split("\n"):
    source, destination_str = line.split(" -> ")
    destinations = destination_str.split(", ")
    source = source.replace("%", "").replace("&", "")
    for d in destinations:
        if d in modules:
            modules[d].add_input(source)


def push_button():
    modules["broadcaster"].send_pulse(False)


pulses_sent = {False: 0, True: 0}
stack = []


def push_button_and_process():
    pulses_sent[False] += 1
    push_button()
    while len(stack) > 0:
        source, destination, high = stack.pop(0)
        pulses_sent[high] += 1
        if destination in modules:
            modules[destination].handle_pulse(source, high)


# part 1
for i in range(1000):
    push_button_and_process()
print(math.prod(pulses_sent.values()))
