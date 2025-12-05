from collections import deque
def height(node):
    count=1

def diameter_tree(root):
    if(root is None):
        return None
    #left hegiht
    left_height = height(root.left)
    #right right
    right_height = height(root.right)
    #left subtree
    left_subtree_height = left_subtree_height()
    #right subtree
    right_subtree_height = right_subtree_height()

    #  max (height̐left subtress, right subtree, left+right height)
    max_height = max(left_subtree_height,right_subtree_height,left_height+right_height)