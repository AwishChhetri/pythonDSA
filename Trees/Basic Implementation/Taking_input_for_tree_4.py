class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]

def print_tree(root):

    if(root==None):
        return
    
    print(root.data,end=":")
    for i in root.children:
        print(i.data,end=",")
    print()

    for i in root.children:
        print_tree(i)

def take_input():
    data=int(input("Enter the node:"))
    node=TreeNode(data)
    num_child=int(input(f"Enter the number of childern for {data}:"))

    for _ in range(num_child):
        child=take_input()
        node.children.append(child)

    return node

root=take_input()
print_tree(root)