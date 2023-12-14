fstream = open("/home/rob/aoc2023/14/input.txt", 'r')
lines = []
line = fstream.readline()
running_total = 0
field = []
while line:
    field.append(list(line))
    line = fstream.readline()

# TODO this can definitely be better
for repeat in range(100):
    for (i, row) in enumerate(field):
        if i == 0:
            continue
        for (j, column) in enumerate(row):
            if field[i][j] == "O":
                if field[i - 1][j] == ".":
                    field[i - 1][j] = "O"
                    field[i][j] = "."

running_total = 0
for (i, row) in enumerate(field):
    for (j, column) in enumerate(row):
        if field[i][j] == "O":
            running_total += len(field) - i

print(running_total)
