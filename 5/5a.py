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
    return map_to_return

# Given a number and a list of MapEntries, determines the output number
def find_mapping(input_number, input_map):
    for possible_entry in input_map:
        difference = input_number - possible_entry.source
        if difference >= 0 and difference < possible_entry.count:
            return possible_entry.destination + difference
    return input_number

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