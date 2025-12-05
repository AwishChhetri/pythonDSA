class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children =[]

def take_input():
    data = int(input("Enter the detail:"))
    node = TreeNode(data)

    num_of_childern = int(input(f"Enter the number of childer for {node.data}:"))

    for i in range(num_of_childern):
        child=take_input()
        child.childern.append(child)
        
    return node 

def print_tree(node):
    if(node == None):
        return 
    print(node.data,end=":")

    for i in node.children:
        print(i.data, end=",")
    print()
    for i in node.children:
        print_tree(i)

node=take_input()
print_tree(node)