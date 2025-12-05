from common import print_binary_tree
from collections import deque
class BinaryTreeNode:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

def input_data():
    data=int(input("Enter the data for the Node:"))
    if data == -1:
        return None
    node=BinaryTreeNode(data)
    
    queue=deque([node])
    while queue:
        curr_node=queue.popleft()
        left_data=int(input(f"Enter the left data of {curr_node.data}:"))
        if left_data != -1:
            left_node=BinaryTreeNode(left_data)
            curr_node.left=left_node
            queue.append(left_node)

        right_data=int(input(f"Enter the right data of {curr_node.data}:"))
        if right_data != -1:
            right_node=BinaryTreeNode(right_data)
            node.right=right_node
            queue.append(right_node)

    
    return node

node=input_data()
print_binary_tree(node)
