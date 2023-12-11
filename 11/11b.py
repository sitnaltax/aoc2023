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

GAP_SIZE = 1000 * 1000 - 1
def shortest_distance(coords1, coords2):
    base_distance = abs(coords1.x - coords2.x) + abs(coords1.y - coords2.y)
    gap_distance = 0
    for column in gap_columns:
        if (column > coords1.x and column < coords2.x) or (column < coords1.x and column > coords2.x):
            gap_distance += GAP_SIZE
    for row in gap_rows:
        if (row > coords1.y and row < coords2.y) or (row < coords1.y and row > coords2.y):
            gap_distance += GAP_SIZE            
    return base_distance + gap_distance

gap_rows = []
gap_columns = []

fstream = open("input.txt", 'r')
lines = []
line = fstream.readline()
line_index = 0
while line:
    lines.append(list(line))
    if "#" not in line:
        gap_rows.append(line_index)
    line = fstream.readline()
    line_index += 1
# now the lines are expanded

gap_columns = []
for i in range(len(lines[0]) - 1):
    found_galaxy = False
    for line in lines:
        if line[i] == "#":
            found_galaxy = True
            break
    if not found_galaxy:
        gap_columns.append(i)
#now the columns are expanded too

galaxies = []
for i in range(len(lines[0]) - 1):
    for (j, line) in enumerate(lines):
        if line[i] == "#":
            galaxies.append(Coords(i, j))

running_total = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        running_total += shortest_distance(galaxies[i], galaxies[j])

print(running_total)
