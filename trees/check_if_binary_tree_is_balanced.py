# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        balanced=[0]
        def check_height(root):
            if not root:
                return 0
            left=check_height(root.left)
            if balanced[0] is False:
                return 0
            right=check_height(root.right)
            if abs(left-right)>1:
                balanced[0]=False
            return 1+max(left,right)
        check_height(root)
        return balanced[0]

        # this is a partial solution 1 test case passed
        # time complexity = O(N)