class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def dfs_iterative(root):
    """
    Perform iterative depth-first search on a binary tree.
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        List of nodes in DFS order
    """
    if not root:
        return []
    
    visited = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        visited.append(node.value)
        
        # Push right child first (so left is processed first)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return visited


"""    Order of Pushing Children:

        We push the right child first, then the left child

        This ensures when we pop from the stack, we get the left child first (LIFO principle)

    Traversal Order:

        This implements a pre-order traversal (Root, Left, Right)

        The node is processed when it's popped from the stack

    Modifying Traversal Type:

        For in-order (Left, Root, Right) or post-order (Left, Right, Root), we need a more complex approach with state tracking"""