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