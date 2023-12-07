class MapEntry:
    def __init__(self, source, destination, count):
        self.source = source
        self.destination = destination
        self.count = count

class Range:
    def __init__(self, source, count):
        self.source = source
        self.count = count

def read_next_map():
    line = fstream.readline()
    while not line.find("map:") > -1:
        line = fstream.readline()

    map_to_return = []
    line = fstream.readline()

    while len(line.strip()) > 0:
        entries = line.split()
        map_to_return.append(MapEntry(int(entries[1]), int(entries[0]), int(entries[2])))
        line = fstream.readline()
    map_to_return.sort(key=lambda entry: entry.source)
    return map_to_return

# Given a number and a list of MapEntries, determines the output number
def find_mapping(input_number, input_map):
    for possible_entry in input_map:
        difference = input_number - possible_entry.source
        if difference >= 0 and difference < possible_entry.count:
            return possible_entry.destination + difference
    return input_number

# Given a number and a list of MapEntries, determines the possible input for which the given number was an output
def find_reverse_mapping(output_number, input_map):
    possible_inputs = []
    for possible_entry in input_map:
        difference = output_number - possible_entry.destination
        if difference >= 0 and difference < possible_entry.count:
            possible_inputs.append(possible_entry.source + difference)
    if find_mapping(output_number, input_map) == output_number:
        possible_inputs.append(output_number)
    return possible_inputs
    

fstream = open("input.txt", 'r')
seed_ranges = []
line = fstream.readline()
(junk, payload) = line.split(':')
seeds_strings = payload.split()
for i in range(0, len(seeds_strings), 2):
    seed_ranges.append(Range(int(seeds_strings[i]), int(seeds_strings[i + 1])))

def ranges_contain_value(target_num, ranges):
    for possible_range in ranges:
        difference = target_num - possible_range.source
        if difference >= 0 and difference < possible_range.count:
            print(target_num, possible_range.source, possible_range.count)
            return True
    return False

maps = []

for i in range(7):
    maps.append(read_next_map())

reversed_maps = list(reversed(maps))

for possible_output in range(79400000, 999999999):
    values_list = [possible_output]
    for map in reversed_maps:
        next_generation_values = []
        for value in values_list:
            next_generation_values += find_reverse_mapping(value, map)
        values_list = next_generation_values
    for value in values_list:
        if ranges_contain_value(value, seed_ranges):
            print(possible_output)
            exit()
    if possible_output % 100000 == 0:
        print(possible_output)

# seeds = [3947715238]
# for seed in seeds:
#    value = seed
#    for map in maps:
#        value = find_mapping(value, map)
#        print(value)