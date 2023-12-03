import re

def is_symbol(input):
    return input != '.' and not input.isdigit()

def symbol_exists_in_range(input):
    return any(map(lambda x: is_symbol(x), input))

def symbol_adjoins_number(lines, row_index, start_column_index, length):
    print((row_index, start_column_index, length))
    start_search_column_index = max(start_column_index - 1, 0)
    end_search_column_index = min(start_column_index + length + 1, len(lines[0])- 1)
    symbol_found = False
    if row_index > 0:
        if symbol_exists_in_range(lines[row_index - 1][start_search_column_index:end_search_column_index]):
            symbol_found = True
    if symbol_exists_in_range(lines[row_index][start_search_column_index:end_search_column_index]):
        symbol_found = True
    if row_index < len(lines) - 1:
        if symbol_exists_in_range(lines[row_index + 1][start_search_column_index:end_search_column_index]):
            symbol_found = True
    return symbol_found

fstream = open("input.txt", 'r')
running_total = 0
line = fstream.readline()
lines = []
while line:
    lines.append(line)
    line = fstream.readline()

for row_index, line in enumerate(lines):
    numbers = re.findall("[0-9]+", line)
    start_search = 0
    for number in numbers:
        start_index = line.find(number, start_search)
        end_index = start_index + len(number)
        start_search = end_index + 1

        if symbol_adjoins_number(lines, row_index, start_index, len(number)):
            running_total += int(number)

print(running_total)