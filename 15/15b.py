def HASH(sequence):
    current_value = 0
    for char in sequence:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    print(f"({sequence}, {current_value})")
    return current_value

class Lens:
    def __init__(self, label, focal_length):
        self.label = label
        self.focal_length = focal_length

class Box:
    def __init__(self):
        self.contents = []

    def remove_lens_if_able(self, label):
        for lens in self.contents:
            if lens.label == label:
                self.contents.remove(lens)

    def add_lens(self, lens):
        found_existing_lens = False
        for existing_lens in self.contents:
            if existing_lens.label == lens.label:
                existing_lens.focal_length = lens.focal_length
                found_existing_lens = True
        if not found_existing_lens:
            self.contents.append(lens)

fstream = open("/home/rob/aoc2023/15/input.txt", 'r')
line = fstream.readline()
sequences = line.split(",")

boxes = {}
for i in range(256):
    boxes[i] = Box()

for sequence in sequences:
    if sequence.find("-") > -1:
        (label, junk) = sequence.split("-")
        target_box = HASH(label)
        boxes[target_box].remove_lens_if_able(label)
    else:
        (label, focal_length) = sequence.split("=")
        target_box = HASH(label)
        boxes[target_box].add_lens(Lens(label, int(focal_length)))

running_total = 0
for i in range(256):
    target_box = boxes[i]
    for (slot, lens) in enumerate(target_box.contents):
        running_total += (i + 1) * (slot + 1) * lens.focal_length

print(running_total)
