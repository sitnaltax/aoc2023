class Puzzle:
    def __init__(self):
        self.column_summaries = []
        self.row_summaries = []

    def set_lines(self, lines):
        self.lines = lines

    def calculate_summary_numbers(self):
        if len(self.lines) <= 1:
            return 0
        # rows first
        for line in self.lines:
            summary_total = 0
            if len(line) == 1:
                continue
            for (index, char) in enumerate(line):
                if char == "#":
                    summary_total += pow(2, index)
            self.row_summaries.append(summary_total)
        
        # now columns
        for column_index in range(len(self.lines[0]) - 1):
            summary_total = 0
            for (index, line) in enumerate(self.lines):
                if len(line) == 1:
                    continue
                if line[column_index] == "#":
                    summary_total += pow(2, index)
            self.column_summaries.append(summary_total)

    def find_reflection(self, reflection_value_to_skip=0):
        if len(self.lines) <= 1:
            return 0
        
        print(f"Analyzing the puzzle that starts: {self.lines[0]}")

        total_to_return = 0
        # let's look for column reflections first
        halfway_mark = len(self.column_summaries) // 2
        for i in range(1, halfway_mark + 1):
            list_forward = self.column_summaries[:i]
            list_backward = list(reversed(self.column_summaries[i:2*i]))
            if list_forward == list_backward and i != reflection_value_to_skip:
                print (f"Found reflection: column {i}")
                total_to_return += i

        for i in range(1, halfway_mark + 1):
            list_forward = self.column_summaries[0-i:]
            list_backward = list(reversed(self.column_summaries[0 - 2*i:0 - i]))
            if list_forward == list_backward and len(self.column_summaries) - i != reflection_value_to_skip:
                print (f"Found reflection (going backwards): column {len(self.column_summaries) - i}")
                total_to_return += len(self.column_summaries) - i
            
        # OK, let's do rows
            
        halfway_mark = len(self.row_summaries) // 2
        for i in range(1, halfway_mark + 1):
            list_forward = self.row_summaries[:i]
            list_backward = list(reversed(self.row_summaries[i:2*i]))
            if list_forward == list_backward and i * 100 != reflection_value_to_skip:
                print (f"Found reflection: row {i}")
                total_to_return += i * 100

        for i in range(1, halfway_mark + 1):
            list_forward = self.row_summaries[0-i:]
            list_backward = list(reversed(self.row_summaries[0 - 2*i:0 - i]))
            if list_forward == list_backward and (len(self.row_summaries) - i) * 100 != reflection_value_to_skip:
                print (f"Found reflection (going backwards): row {len(self.row_summaries) - i}")
                total_to_return += (len(self.row_summaries) - i) * 100

        if total_to_return == 0:
            return -1
        return total_to_return
    
    def find_smudged_variant(self):
        old_reflection = self.find_reflection()
        print("old reflection: ")
        for (row_index, line) in enumerate(self.lines):
            for column_index in range(len(line)):
                replacement_character = "#" if line[column_index] == "." else "."
                new_line = line[:column_index] + replacement_character + line[column_index + 1:]
                potential_puzzle = Puzzle()
                potential_puzzle.set_lines(self.lines)
                potential_puzzle.lines[row_index] = new_line
                potential_puzzle.calculate_summary_numbers()
                print (potential_puzzle.column_summaries)
                print (potential_puzzle.row_summaries)
                output = potential_puzzle.find_reflection(old_reflection)
                if output > 0:
                    return output
        print("Couldn't find any smudged variant")

# don't forget off-by-one for the final metric

def read_puzzle(stream):
    lines = []
    line = stream.readline()
    while len(line) > 1:
        lines.append(line)
        line = stream.readline()
    puzzle = Puzzle()
    puzzle.set_lines(lines)
    return puzzle

fstream = open("/home/rob/aoc2023/13/input.txt", 'r')
puzzles = []
puzzles.append(read_puzzle(fstream))

while len(puzzles[-1].lines) > 0:
    puzzles.append(read_puzzle(fstream))

smudged_puzzles = []
for puzzle in puzzles:
    puzzle.calculate_summary_numbers()
    smudged_puzzles.append(puzzle.find_smudged_variant())

running_total = 0
    
#for (index, puzzle) in enumerate(smudged_puzzles):
#    print(f"working on puzzle {index}")
#    puzzle.calculate_summary_numbers()
#    running_total += puzzle.find_reflection()

print(sum([puzzle for puzzle in smudged_puzzles if puzzle != None]))
