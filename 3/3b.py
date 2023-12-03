import re

def gear_adjoins_number(gear, row_index, start_column_index, length):
    if abs(gear[0] - row_index) > 1:
        return False
    if start_column_index - gear[1] > 1:
        return False
    if gear[1] - (start_column_index + length - 1) > 1:
        return False 
    print (gear, row_index, start_column_index, length)
    return True

fstream = open("input.txt", 'r')
running_total = 0
line = fstream.readline()
lines = []
# gear = dict from (row, col) to (list of adjacent numbers)
gears = {}
while line:
    lines.append(line)
    line = fstream.readline()

for row_index, line in enumerate(lines):
    start_search = 0
    column_index = line.find("*", 0)
    while column_index >= 0:
        gears[(row_index, column_index)] = []
        column_index = line.find("*", column_index + 1)
print(gears)

for row_index, line in enumerate(lines):
    numbers = re.findall("[0-9]+", line)
    start_search = 0
    for number in numbers:
        start_index = line.find(number, start_search)
        end_index = start_index + len(number)
        start_search = end_index + 1

        for gear in gears:
            if gear_adjoins_number(gear, row_index, start_index, len(number)):
                gears[gear].append(int(number))

print(gears)
for gear in gears:
    if len(gears[gear]) == 2:
        running_total += gears[gear][0] * gears[gear][1]

print(running_total)