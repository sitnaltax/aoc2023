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

def shortest_distance(coords1, coords2):
    return abs(coords1.x - coords2.x) + abs(coords1.y - coords2.y)

fstream = open("input.txt", 'r')
lines = []
line = fstream.readline()
while line:
    lines.append(list(line))
    if "#" not in line:
        lines.append(list(line))
    line = fstream.readline()
# now the lines are expanded

columns_to_expand = []
for i in range(len(lines[0]) - 1):
    found_galaxy = False
    for line in lines:
        #print("line:" + "".join(line) + " length " + str(len(line)) + " and i = " + str(i))
        if line[i] == "#":
            found_galaxy = True
            break
    if not found_galaxy:
        columns_to_expand.append(i)
#now the columns are expanded too

for i in reversed(columns_to_expand):
    for line in lines:
        line.insert(i, ".")

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
