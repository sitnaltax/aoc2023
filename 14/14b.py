fstream = open("/home/rob/aoc2023/14/input.txt", 'r')
lines = []
line = fstream.readline()
running_total = 0
field = []
while line:
    field.append(list(line))
    line = fstream.readline()

# TODO this can definitely be better
def roll_north():
    for repeat in range(100):
        for (i, row) in enumerate(field):
            if i == 0:
                continue
            for (j, column) in enumerate(row):
                if field[i][j] == "O":
                    if field[i - 1][j] == ".":
                        field[i - 1][j] = "O"
                        field[i][j] = "."

def roll_south():
    for repeat in range(100):
        for (i, row) in enumerate(field):
            if i == len(field) - 1:
                continue
            for (j, column) in enumerate(row):
                if field[i][j] == "O":
                    if field[i + 1][j] == ".":
                        field[i + 1][j] = "O"
                        field[i][j] = "."

def roll_west():
    for repeat in range(100):
        for (i, row) in enumerate(field):
            for (j, column) in enumerate(row):
                if j == 0:
                    continue
                if field[i][j] == "O":
                    if field[i][j - 1] == ".":
                        field[i][j - 1] = "O"
                        field[i][j] = "."

def roll_east():
    for repeat in range(100):
        for (i, row) in enumerate(field):
            for (j, column) in enumerate(row):
                if j == len(row) - 1:
                    continue
                if field[i][j] == "O":
                    if field[i][j + 1] == ".":
                        field[i][j + 1] = "O"
                        field[i][j] = "."

def find_score():
    running_total = 0
    for (i, row) in enumerate(field):
        for (j, column) in enumerate(row):
            if field[i][j] == "O":
                running_total += len(field) - i
    return running_total

scores = []
for total_iteration in range(1000):
    roll_north()
    roll_west()
    roll_south()
    roll_east()
    scores.append(find_score())
    if total_iteration % 100 == 0:
        print(total_iteration)
        print(scores)


print(scores)
