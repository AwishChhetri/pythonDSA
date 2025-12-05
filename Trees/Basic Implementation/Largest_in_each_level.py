
def largest_values_in_rows(root):
    """
    Find the largest value in each row of an N-ary tree.

    Parameters:
    root (Node): The root of the N-ary tree.

    Returns:
    List[int]: A list of integers where each integer is the largest value in that level of the tree.
    """
    # Implement the function
    result=[]
    queue = deque([root])
    
    while len(queue) != 0:
        queue_size=len(queue)
        max_val = float('-inf')
        
        for i in range(queue_size):
            node = queue.popleft()
            max_val=max(max_val,node.val)
            
            for child in node.childern:
                queue.append(child)
        result.append(max_val)
        
    
        