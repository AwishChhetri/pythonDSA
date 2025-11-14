class NodeTree:
    def __init__(self,data):
        self.data=data
        self.childern=[]

root=NodeTree(1)

child1=NodeTree(2)
child2=NodeTree(3)

root.childern.append(child1)
root.childern.append(child2)

print(root.childern[0].data)

child4=NodeTree(4)
child5=NodeTree(5)
child1.childern.append(child4)
child1.childern.append(child5)

print(child1.childern[0].data,child1.childern[1].data)
