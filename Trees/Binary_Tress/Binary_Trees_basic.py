class BinaryTreeroot:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

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
   
root=BinaryTreeroot(2)
child1=BinaryTreeroot(1)
child2=BinaryTreeroot(2)
root.left=child1
root.right=child2

child3=BinaryTreeroot(3)
child4=BinaryTreeroot(4)

child1.left=child3
child1.right=child4





print_binary_tree(root)
