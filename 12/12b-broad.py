def evaluate_pattern_exactly(pattern, criteria):
    blocks = [token for token in pattern.split('.') if len(token) > 0]
    if len(blocks) != len(criteria):
        return False
    for (index, block) in enumerate(blocks):
        if len(block) != int(criteria[index]):
            return False
    return True

#evaluates only until we hit a ?
def evaluate_pattern_leniently(pattern, criteria):
    blocks = [token for token in pattern.split('.') if len(token) > 0]
    for (index, block) in enumerate(blocks):
        if block.find("?") > -1:
            return True
        if index >= len(criteria):
            return False
        if len(block) != int(criteria[index]):
            return False
    return True

# If there is no ? in the pattern, returns 1 if the pattern matches the criteria, 0 otherwise
# Otherwise, tries replacing the first ? with both a . or a # and calls itself recursively
def count_of_possible_patterns(pattern, criteria):
    if not evaluate_pattern_leniently(pattern, criteria):
        return 0
    if pattern.find("?") == -1:
        return 1 if evaluate_pattern_exactly(pattern, criteria) else 0
    else:
        total_of_children = 0
        return count_of_possible_patterns(pattern.replace("?", ".", 1), criteria) + count_of_possible_patterns(pattern.replace("?", "#", 1), criteria)    

fstream = open("/home/rob/aoc2023/12/input.txt", 'r')
lines = []
line = fstream.readline()
running_total = 0
while line:
    print (f"Evaluating line: {line}")
    (pattern, unsplit_criteria) = line.split()
    pattern = ((pattern + "?") * 4) + pattern
    criteria = unsplit_criteria.split(',')
    criteria = criteria * 5
    patterns = count_of_possible_patterns(pattern, criteria)
    print(patterns)
    running_total += patterns
    line = fstream.readline()

print(running_total)
