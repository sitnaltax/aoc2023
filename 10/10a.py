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
    print(f"from: {current_connection.x}, {current_connection.y}, symbol of {lines[current_connection.y][current_connection.x]}")
    for possible_new_connection in current_connection.get_new_coords():
        if possible_new_connection not in known_tiles or known_tiles[possible_new_connection] > known_tiles[current_connection] + 1:
            known_tiles[possible_new_connection] = known_tiles[current_connection] + 1
            connections_to_check.append(possible_new_connection)
            print(f"adding coords: {possible_new_connection.x}, {possible_new_connection.y}")

print(max(known_tiles.values()))
