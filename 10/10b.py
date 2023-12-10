class ReadingHistory:
    def __init__(self, input_string):
        self.initial_readings = [int(val) for val in input_string.split()]

    def interpolate_next_value(self):
        history_calculation_lines = [self.initial_readings]
        while any(value != 0 for value in history_calculation_lines[-1]):
            next_history_calculation_line = []
            for index in range(len(history_calculation_lines[-1]) - 1):
                next_history_calculation_line.append(history_calculation_lines[-1][index + 1] - history_calculation_lines[-1][index])
            history_calculation_lines.append(next_history_calculation_line)
        # OK, history_calculation_lines is now complete
        history_calculation_lines[-1].append(0)
        for line_index in reversed(range(len(history_calculation_lines) - 1)):
            history_calculation_lines[line_index].append(history_calculation_lines[line_index][-1] + history_calculation_lines[line_index + 1][-1])
        return history_calculation_lines [0][-1]

# x is across, increasing to the right
# y is down, increasing down
class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))
    def __eq__(self, rhs):
        return self.x == rhs.x and self.y == rhs.y

    def get_new_coords(self):
        match lines[self.y][self.x]:
            case "|":
                return [Coords(self.x, self.y - 1), Coords(self.x, self.y + 1)]
            case "-":
                return [Coords(self.x - 1, self.y), Coords(self.x + 1, self.y)]
            case "L":
                return [Coords(self.x + 1, self.y), Coords(self.x, self.y - 1)]
            case "J":
                return [Coords(self.x - 1, self.y), Coords(self.x, self.y - 1)]
            case "7":
                return [Coords(self.x - 1, self.y), Coords(self.x, self.y + 1)]
            case "F":
                return [Coords(self.x + 1, self.y), Coords(self.x, self.y + 1)]
            case ".":
                return []
            case "S":
                return []
            case _:
                print("Unknown character")

fstream = open("input.txt", 'r')
lines = []
line = fstream.readline()
while line:
    lines.append(line)
    line = fstream.readline()

known_tiles = {}
known_tiles[Coords(103, 20)] = 0 # the initial S
initial_connections = [Coords(102, 20), Coords(103, 21)]
connections_to_check = []
for tile in initial_connections:
    known_tiles[tile] = 1
    connections_to_check.append(tile)

while len(connections_to_check) > 0:
    current_connection = connections_to_check.pop()
    for possible_new_connection in current_connection.get_new_coords():
        if possible_new_connection not in known_tiles or known_tiles[possible_new_connection] > known_tiles[current_connection] + 1:
            known_tiles[possible_new_connection] = known_tiles[current_connection] + 1
            connections_to_check.append(possible_new_connection)

print(max(known_tiles.values()))

lines[20] = lines[2].replace("S", "7") #replace the S with a 7
tiles_within_loop = 0
for (y, line) in enumerate(lines):
    for x in range(len(line)):
        if (Coords(x, y)) in known_tiles:
            continue
        # for each tile, go straight UP. We are in the loop if we cross an odd number of pipes.
        # we cross a pipe if we hit a - or a matched 7/L or a matched F/J
        tiles_touched = {"-": 0, "|": 0, "7": 0, "J": 0, "F": 0, "L": 0, ".": 0}
        for test_y in range(y):
            if Coords(x, test_y) in known_tiles:
                tiles_touched[lines[test_y][x]] += 1
        pipes_crossed = tiles_touched["-"] + max(tiles_touched["7"], tiles_touched["L"]) + max(tiles_touched["F"], tiles_touched["J"])
        if pipes_crossed % 2 == 1:
            tiles_within_loop += 1
print(tiles_within_loop)

         