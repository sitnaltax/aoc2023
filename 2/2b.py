from functools import reduce

def is_digit(input):
    return input.isdigit()

fstream = open("input.txt", 'r')
running_total = 0
line = fstream.readline()
while line:
    possible = True
    (game, results) = line.split(":")
    game_id = game.split(" ")[1]
    line = fstream.readline()
    min_by_color = {"red": 0, "green": 0, "blue": 0}
    for result in results.split(";"):
        for cubes in result.split(","):
            (count, color) = cubes.strip().split(" ")
            min_by_color[color] = max(min_by_color[color], int(count))
    running_total += reduce(lambda x, y: x*y, min_by_color.values())

print(running_total)