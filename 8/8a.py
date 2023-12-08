class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

fstream = open("input.txt", 'r')
instructions = fstream.readline()
fstream.readline()
line = fstream.readline()

nodes_dict = {}
while line:
    (node_name, garbage, left, right) = line.split()
    nodes_dict[node_name] = Node(node_name, left[1:4], right[0:3])
    line = fstream.readline()

current_node = "AAA"
steps = 0
while current_node != "ZZZ":
    for char in instructions.strip():
        if current_node == "ZZZ":
            continue
        steps += 1
        if char == "L":
            current_node = nodes_dict[current_node].left
        elif char == "R":
            current_node = nodes_dict[current_node].right
        else:
            print("Unknown instruction!")

print(steps)