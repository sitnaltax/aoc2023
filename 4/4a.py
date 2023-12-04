fstream = open("input.txt", 'r')
line = fstream.readline()
lines = []
while line:
    lines.append(line)
    line = fstream.readline()

running_total = 0

for line in lines:
    (junk, payload) = line.split(':')
    (winning_numbers_string, chosen_numbers_string) = payload.split('|')
    winning_numbers = []
    for winning_number in winning_numbers_string.strip().split():
        winning_numbers.append(int(winning_number))
    chosen_numbers = []
    for chosen_number in chosen_numbers_string.strip().split():
        chosen_numbers.append(int(chosen_number))
    value = 0
    for chosen_number in chosen_numbers:
        if chosen_number in winning_numbers:
            if value == 0:
                value = 1
            else:
                value *= 2
    running_total += value

print(running_total)