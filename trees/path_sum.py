# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def sum_check(root,curr_sum):
            if not root:
                return False
            curr_sum+=root.val
            if not root.left and not root.right:
                if curr_sum==targetSum:
                    return True
            return sum_check(root.right,curr_sum) or sum_check(root.left,curr_sum)
        return sum_check(root,0)
        
        # time complexity O(N)
        # space complexity o(N)