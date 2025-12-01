class BinaryTreeNode:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def input_data():
    data=int(input("Enter the data for the Node:"))
    node=BinaryTreeNode(data)

    left_data=int(input(f"Enter the left data of {node.data}"))
    left_node=BinaryTreeNode(left_data)
    node.left=left_node

    right_data=int(input(f"Enter the right data of {node.data}"))
    right_node=BinaryTreeNode(right_node)
    node.right=right_node


def print_binary_tree(root):
    if(root == None):
        return None
    print(f"{root.data}",end=": ")
    if(root.left!=None):
        print(f"L-->{root.left.data}",end=",")
  
    else:
        print("L-->None",end=",")
    if(root.right!=None):
        print(f"R-->{root.right.data}",end="")
    else:
        print("R-->None",end=",")
    print()
    print_binary_tree(root.left)
    print_binary_tree(root.right)



