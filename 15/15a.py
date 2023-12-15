def HASH(sequence):
    current_value = 0
    for char in sequence:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    print(f"({sequence}, {current_value})")
    return current_value

fstream = open("/home/rob/aoc2023/15/input.txt", 'r')
line = fstream.readline()
sequences = line.split(",")

running_total = 0
for sequence in sequences:
    running_total += HASH(sequence)

print(running_total)
