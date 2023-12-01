def is_digit(input):
    return input.isdigit()

def replace_words(input):
    replacements_dict = {"one": "one1one", "two": "two2two", "three": "three3three", "four": "four4four", "five": "five5five", "six": "six6six", "seven": "seven7seven", "eight": "eight8eight", "nine": "nine9nine"}
    work_string = input
    for key in replacements_dict:
        work_string = work_string.replace(key, replacements_dict[key])
    return work_string

fstream = open("input.txt", 'r')
running_total = 0
line = fstream.readline()
while line:
    line = replace_words(line)
    filtered = list(filter(is_digit, line))
    running_total += (int(filtered[0]) * 10 + int(filtered[-1]))
    line = fstream.readline()

print(running_total)