class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

root = TreeNode(1)

child1=TreeNode(2)
child2=TreeNode(3)

root.children.append(child1)
root.children.append(child2)
def print_tree(root):
    if(root == None):
        return
    print(root.data,end=":")
    for i in root.children:
        print(i.data,end=",")
    print()
    for i in root.children:
        print_tree(i)
print_tree(root)

