from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def bfs_iterative(root):
    """
    Perform iterative breadth-first search on a binary tree.
    
    Args:
        root: Root node of the binary tree
        
    Returns:
        List of nodes in BFS order (level-order traversal)
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])  # Initialize queue with root node
    
    while queue:
        current_node = queue.popleft()  # Dequeue the front node
        result.append(current_node.value)
        
        # Enqueue left child first (to process left-to-right)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    
    return result

# Example usage:
if __name__ == "__main__":
    # Build the example binary tree:
    #        A
    #       / \
    #      B   C
    #     / \   \
    #    D   E   F
    F = TreeNode('F')
    E = TreeNode('E')
    D = TreeNode('D')
    C = TreeNode('C', right=F)
    B = TreeNode('B', left=D, right=E)
    A = TreeNode('A', left=B, right=C)
    
    print("BFS (Level-order) traversal:")
    print(bfs_iterative(A))  # Output: ['A', 'B', 'C', 'D', 'E', 'F']