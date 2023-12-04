fstream = open("input.txt", 'r')
line = fstream.readline()
lines = []
while line:
    lines.append(line)
    line = fstream.readline()

running_total = 0

count_by_card = [1] * (len(lines) + 1)
count_by_card[0] = 0
for (card_number, line) in enumerate(lines, start=1):
    (junk, payload) = line.split(':')
    (winning_numbers_string, chosen_numbers_string) = payload.split('|')
    winning_numbers = []
    for winning_number in winning_numbers_string.strip().split():
        winning_numbers.append(int(winning_number))
    chosen_numbers = []
    for chosen_number in chosen_numbers_string.strip().split():
        chosen_numbers.append(int(chosen_number))
    matches = 0
    for chosen_number in chosen_numbers:
        if chosen_number in winning_numbers:
            matches += 1
    for index_increment in range(1, matches + 1):
        count_by_card[card_number + index_increment] += count_by_card[card_number]                                                                                                                                                                                       
    
print(sum(count_by_card))