from enum import Enum

class Direction(Enum):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3

class Tile:
    def __init__(self, char):
        self.char = char
        self.energized = False
        self.already_split = False

class Beam:
    def __init__(self, column, row, direction):
        self.column = column
        self.row = row
        self.direction = direction
        self.dead = False

    def process(self):
        in_bounds = True
        while in_bounds:
            rows[self.row][self.column].energized = True
            self.handle_terrain()
            self.move()
            if (self.column < 0) or (self.column >= len(rows[0])) or (self.row < 0) or (self.row >= len(rows) or self.dead):
                in_bounds = False

    def handle_terrain(self):
        match rows[self.row][self.column].char:
            case ".":
                pass
            case "/":
                match self.direction:
                    case Direction.EAST:
                        self.direction = Direction.NORTH
                    case Direction.SOUTH:
                        self.direction = Direction.WEST
                    case Direction.WEST:
                        self.direction = Direction.SOUTH
                    case Direction.NORTH:
                        self.direction = Direction.EAST
            case "\\":
                match self.direction:
                    case Direction.EAST:
                        self.direction = Direction.SOUTH
                    case Direction.SOUTH:
                        self.direction = Direction.EAST
                    case Direction.WEST:
                        self.direction = Direction.NORTH
                    case Direction.NORTH:
                        self.direction = Direction.WEST
            case "-":
                match self.direction:
                    case Direction.EAST:
                        pass
                    case Direction.SOUTH:
                        if not rows[self.row][self.column].already_split:
                            rows[self.row][self.column].already_split = True
                            self.direction = Direction.EAST
                            all_beams.append(Beam(self.column, self.row, Direction.WEST))
                        else:
                            self.dead = True
                    case Direction.WEST:
                        pass
                    case Direction.NORTH:
                        if not rows[self.row][self.column].already_split:
                            rows[self.row][self.column].already_split = True
                            self.direction = Direction.EAST
                            all_beams.append(Beam(self.column, self.row, Direction.WEST))
                        else:
                            self.dead = True
            case "|":
                match self.direction:
                    case Direction.EAST:
                        if not rows[self.row][self.column].already_split:
                            rows[self.row][self.column].already_split = True
                            self.direction = Direction.NORTH
                            all_beams.append(Beam(self.column, self.row, Direction.SOUTH))
                        else:
                            self.dead = True
                    case Direction.SOUTH:
                        pass
                    case Direction.WEST:
                        if not rows[self.row][self.column].already_split:
                            rows[self.row][self.column].already_split = True
                            self.direction = Direction.NORTH
                            all_beams.append(Beam(self.column, self.row, Direction.SOUTH))
                        else:
                            self.dead = True
                    case Direction.NORTH:
                        pass

    def move(self):
        match self.direction:
            case Direction.EAST:
                self.column += 1
            case Direction.SOUTH:
                self.row += 1
            case Direction.WEST:
                self.column -= 1
            case Direction.NORTH:
                self.row -= 1

fstream = open("/home/rob/aoc2023/16/input.txt", 'r')
line = fstream.readline().strip()
rows = []
while line:
    row = []
    for char in line:
        row.append(Tile(char))
    rows.append(row)
    line = fstream.readline()

all_beams = []
all_beams.append(Beam(0, 0, Direction.EAST))

while len(all_beams) > 0:
    all_beams.pop().process()

running_total = 0
for (row_index, row) in enumerate(rows):
    for (column_index, tile) in enumerate(row):
        if tile.energized:
            print(f"{column_index}, {row_index}")
            running_total += 1

print(running_total)
