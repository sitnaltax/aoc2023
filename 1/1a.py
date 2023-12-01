def is_digit(input):
    return input.isdigit()

fstream = open("input.txt", 'r')
runningTotal = 0
line = fstream.readline()
while line:
    filtered = list(filter(is_digit, line))
    runningTotal += (int(filtered[0]) * 10 + int(filtered[-1]))
    line = fstream.readline()

print(runningTotal)