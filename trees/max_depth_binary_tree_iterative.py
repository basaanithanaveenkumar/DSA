class Solution(object):
    
    
    
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)

        return 1+max(left,right)

        #time complexity = O(N) # we visit every node
        # space complexity is with the call stack