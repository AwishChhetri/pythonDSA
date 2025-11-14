

class TreeNode:
    def __init__(self, data):
        self.data=data
        self.childern=[]
def print_tree(root):
    print(root.data)
    for i in root.childern:
        print_tree(i)


root=TreeNode(1)

child1=TreeNode(2)
child2=TreeNode(3)

root.childern.append(child1)
root.childern.append(child2)

child3=TreeNode(4)
child4=TreeNode(5)

child1.childern.append(child3)
child1.childern.append(child4)

print_tree(root)