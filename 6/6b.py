times = [53897698]
distances = [313109012141201]

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