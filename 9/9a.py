class ReadingHistory:
    def __init__(self, input_string):
        self.initial_readings = [int(val) for val in input_string.split()]

    def interpolate_next_value(self):
        history_calculation_lines = [self.initial_readings]
        while any(value != 0 for value in history_calculation_lines[-1]):
            next_history_calculation_line = []
            for index in range(len(history_calculation_lines[-1]) - 1):
                next_history_calculation_line.append(history_calculation_lines[-1][index + 1] - history_calculation_lines[-1][index])
            history_calculation_lines.append(next_history_calculation_line)
        # OK, history_calculation_lines is now complete
        history_calculation_lines[-1].append(0)
        for line_index in reversed(range(len(history_calculation_lines) - 1)):
            history_calculation_lines[line_index].append(history_calculation_lines[line_index][-1] + history_calculation_lines[line_index + 1][-1])
        return history_calculation_lines [0][-1]
                
        
fstream = open("input.txt", 'r')
histories = []
line = fstream.readline()
while line:
    histories.append(ReadingHistory(line))
    line = fstream.readline()

running_total = 0
for history in histories:
    running_total += history.interpolate_next_value()

print(running_total)
