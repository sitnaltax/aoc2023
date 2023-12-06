class Range:
    def __init__(self, start, count):
        self.start = start
        self.count = count

class MapEntry:
    def __init__(self, source, destination, count):
        self.source = source
        self.destination = destination
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

# Given a range and a list of MapEntries, determines a list of output ranges
def find_mapping(input_range, input_map):
    output_ranges = []
    relevant_entries = []
    for entry in input_map:
        if (entry.source + entry.count < input_range.start) and (entry.source <= input_range.start + input_range.count):
            relevant_entries.append(entry)
    # Now every entry in relevant_entries, plus every gap in the input range not covered by a mapping, needs an output range
    #  
    for possible_entry in input_map:
        difference = input_number - possible_entry.source
        if difference >= 0 and difference < possible_entry.count:
            return possible_entry.destination + difference
    return output_ranges

fstream = open("input.txt", 'r')
seeds = []
line = fstream.readline()
(junk, payload) = line.split(':')
for seed in payload.split():
    seeds.append(int(seed))
print(seeds)

maps = []

for i in range(7):
    maps.append(read_next_map())

values = []
for seed in seeds:
    value = seed
    for map in maps:
        value = find_mapping(value, map)
    values.append(value)

print(min(values))

#lines = []
#while line:
#    lines.append(line)
#    line = fstream.readline()
