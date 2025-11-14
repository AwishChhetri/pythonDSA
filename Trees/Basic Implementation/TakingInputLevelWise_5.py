from collections import deque
class TreeNode:
    def __init__(self, data):
        self.data=data
        self.childern =[]

def print_tree(node):
    if(node == None):
        return 
    
    print(node.data,end=":")

    for i in node.childern:
        print(i.data,end=",")
    
    print()

    for i in node.childern:
        print_tree(i)

def take_input_level_wise():
    data= int(input("Enter the node:"))
    root=TreeNode(data)
    queue=deque([root])

    while len(queue) != 0:
        curr_node=queue.popleft()
        num_child=int(input(f"Enter the number of child for {curr_node.data}:"))

        for i in range(num_child):
            child_data=int(input(f"Enter the data for {i+1} child node of {curr_node.data}:"))
            child_node=TreeNode(child_data)
            curr_node.childern.append(child_node)
            queue.append(child_node)
    return root

node=take_input_level_wise()
print_tree(node)