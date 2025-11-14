class TreeNode:
    def __init__(self,data):
        self.data=data
        self.childern=[]

root=TreeNode(0)

child1=TreeNode(1)
child2=TreeNode(2)
child3=TreeNode(3)

#connect 1,2 to root i.e 0 --> 1,2

root.childern.append(child1)
root.childern.append(child2)

# connect 3 to 1 i.e 1-->3

child1.childern.append(child3)

def print_tree_detail(root):
    if(root==None):
        return
    print(root.data,end=":")

    for i in root.childern:
        print(i.data,end=",")

    print()
    for i in root.childern:
        print_tree_detail(i)
print_tree_detail(root)