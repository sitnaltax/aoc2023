fstream = open("input.txt", 'r')
times = []
distances = []
line = fstream.readline()
(junk, payload) = line.split(':')
for time in payload.split():
    times.append(int(time))
line = fstream.readline()
(junk, payload) = line.split(':')
for distance in payload.split():
    distances.append(int(distance))

running_total = 1
for i in range(len(times)):
    time = times[i]
    record_distance = distances[i]
    ways_to_beat = 0
    for i in range(time):
        if i * (time - i) > record_distance:
            ways_to_beat += 1
    running_total *= ways_to_beat

print(running_total)