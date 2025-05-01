"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):


    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        old_to_new_hashmap={}
        def dfs(node):
            if node in old_to_new_hashmap:
                return old_to_new_hashmap[node]
            copy=Node(node.val)
            old_to_new_hashmap[node]=copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)
