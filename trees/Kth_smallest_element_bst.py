# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        count=[k]
        ans=[0]
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            if count[0]==1:
                ans[0]=node.val
            count[0]=count[0]-1
            if count[0]>1:
                dfs(node.right)
        dfs(root)
        return ans[0]

        