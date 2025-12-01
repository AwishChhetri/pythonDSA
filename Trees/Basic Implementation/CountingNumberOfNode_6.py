from collections import deque

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children =[]

def take_input():
    data = int(input("Enter the node data:"))
    root = TreeNode(data)
    queue=deque([root])

    while len(queue) != 0:
        curr_node=queue.popleft()
        num_child=int(input(f"Enter the number of childer for {curr_node.data}: "))
        for i in range(num_child):
            child_data=int(input(f"Enter the data for {i+1} of {curr_node.data}: "))
            child_node= TreeNode(child_data)
            curr_node.children.append(child_node)
            queue.append(child_node)
    return root

def print_tree(node):
    if(node == None):
        return 
    
    print(node.data,end=":")

    for i in node.children:
        print(i.data,end=",")

    print()

    for i in node.children:
        print_tree(i)

def count_nodes(node):
    if(node == None):
        return 0
    
    num_nodes=1

    for i in node.children:
        num_nodes = num_nodes + count_nodes(i)

    return num_nodes

node=take_input()
print('This is it!')
print_tree(node)
print("count-")
print(count_nodes(node))


#Height of the tree

def height_tree(node):
    if(node == None):
        return 0
    height=1
    max_height=0

    for i in node.children:
        max_height=max(max_height,height_tree(i))

    height = height + max_height

    return height

print(height_tree(node))