def is_digit(input):
    return input.isdigit()

fstream = open("input.txt", 'r')
running_total = 0
line = fstream.readline()
max_by_color = {"red": 12, "green": 13, "blue": 14}
while line:
    possible = True
    (game, results) = line.split(":")
    game_id = game.split(" ")[1]
    line = fstream.readline()
    for result in results.split(";"):
        for cubes in result.split(","):
            (count, color) = cubes.strip().split(" ")
            if int(count) > max_by_color[color]:
                possible = False
    if possible:
        running_total += int(game_id)    

print(running_total)