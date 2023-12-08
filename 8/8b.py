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

current_nodes_list = [node for node in nodes_dict.keys() if node[2] == "A"]
print(current_nodes_list)
steps = 0
while any(node[2] != "Z" for node in current_nodes_list):
    for char in instructions.strip():
        if all(node[2] == "Z" for node in current_nodes_list):
            continue
        steps += 1
        next_nodes_list = []
        if char == "L":
            for node in current_nodes_list:
                next_nodes_list.append(nodes_dict[node].left)
        elif char == "R":
            for node in current_nodes_list:
                next_nodes_list.append(nodes_dict[node].right)
        else:
            print("Unknown instruction!")
        current_nodes_list = next_nodes_list
        if (steps % 100000) == 0:
            print(steps)

print(steps)